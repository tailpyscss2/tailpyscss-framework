import sass
import os
import re

def compile_scss(input_path, output_path, output_style='expanded'):
    """
    Compile SCSS to CSS using libsass with full @apply and @import support.
    Uses a manual preprocessor to recursively resolve imports and inline content.
    """
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # --- 1. Recursive Import Resolver ---
    def resolve_imports(content, base_dir):
        """
        recursively find @import and replace with file content.
        This ensures we have one giant SCSS string for @apply and @extend to work.
        """
        def import_replacer(match):
            import_path = match.group(2).strip().strip("'").strip('"')
            
            # Skip css imports (http/url)
            if import_path.startswith("http") or "url(" in import_path or import_path.endswith(".css"):
                return match.group(0)

            # Try finding the file
            candidates = [
                os.path.join(base_dir, import_path),
                os.path.join(base_dir, import_path + ".scss"),
                os.path.join(base_dir, "_" + import_path + ".scss"),
                # Handle subdirectories e.g. components/card
                os.path.join(base_dir, os.path.dirname(import_path), "_" + os.path.basename(import_path) + ".scss") 
            ]
            
            target_file = None
            for c in candidates:
                if os.path.exists(c):
                    target_file = c
                    break
            
            if target_file:
                with open(target_file, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                # print(f"DEBUG: Reading {target_file} ({len(file_content)} bytes)")
                
                # Recursively resolve imports in the new file
                return resolve_imports(file_content, os.path.dirname(target_file)) + "\n"
            else:
                # --- NEW: Fallback to Internal Assets ---
                internal_path = os.path.join(os.path.dirname(__file__), 'internal_assets', import_path)
                if not internal_path.endswith('.scss'):
                    # Try partial _filename.scss
                    parts = os.path.split(internal_path)
                    internal_candidate = os.path.join(parts[0], "_" + parts[1] + ".scss")
                else:
                    internal_candidate = internal_path

                if os.path.exists(internal_candidate):
                    # print(f"DEBUG: Found internal asset: {internal_candidate}")
                    with open(internal_candidate, 'r', encoding='utf-8') as f:
                        internal_content = f.read()
                    return resolve_imports(internal_content, os.path.dirname(internal_candidate)) + "\n"
                
                # If not found, leave it for libsass to error or handle
                return match.group(0)

        # Regex for @import "path"; or @import 'path';
        return re.sub(r'@import\s+("|\')(.*?)("|\');', import_replacer, content)

    # --- 2. The Magic Replacer (@apply) ---
    def process_apply_directives(scss_content):
        def apply_replacer(match):
            content = match.group(1).strip()
            classes = content.replace(";", "").split()
            output_parts = []
            
            arbitrary_map = {
                "w": ["width"], "h": ["height"],
                "min-w": ["min-width"], "min-h": ["min-height"],
                "max-w": ["max-width"], "max-h": ["max-height"],
                "p": ["padding"], "pt": ["padding-top"], "pr": ["padding-right"], "pb": ["padding-bottom"], "pl": ["padding-left"],
                "px": ["padding-left", "padding-right"], "py": ["padding-top", "padding-bottom"],
                "m": ["margin"], "mt": ["margin-top"], "mr": ["margin-right"], "mb": ["margin-bottom"], "ml": ["margin-left"],
                "mx": ["margin-left", "margin-right"], "my": ["margin-top", "margin-bottom"],
                "top": ["top"], "right": ["right"], "bottom": ["bottom"], "left": ["left"],
                "z": ["z-index"],
                "rounded": ["border-radius"],
            }

            for c in classes:
                jit_match = re.match(r'^([a-z-]+)-\[(.+)\]$', c)
                if jit_match:
                    prefix = jit_match.group(1)
                    value = jit_match.group(2)
                    if prefix in arbitrary_map:
                        props = arbitrary_map[prefix]
                        for prop in props:
                            final_value = value.replace("_", " ")
                            output_parts.append(f"{prop}: {final_value};")
                else:
                    safe_c = c.replace(":", "\\:")
                    output_parts.append(f"@extend .{safe_c} !optional;")
                    
            return " ".join(output_parts)

        return re.sub(r'@apply\s+(.*?);', apply_replacer, scss_content, flags=re.DOTALL)

    # --- 3. Execution ---
    with open(input_path, 'r', encoding='utf-8') as f:
        root_content = f.read()
    
    # Step A: Inline all imports (Recursive)
    unified_scss = resolve_imports(root_content, os.path.dirname(input_path))
    
    # Step B: Process @apply on the unified content
    # This ensures @extend finds the classes defined in previously imported chunks
    processed_scss = process_apply_directives(unified_scss)
    
    with open("debug_processed.scss", "w", encoding="utf-8") as f:
        f.write(processed_scss)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        css = sass.compile(
            string=processed_scss,
            include_paths=[os.path.dirname(input_path)],
            output_style=output_style
        )
        with open(output_path, "w") as f:
            f.write(css)
            
    except sass.CompileError as e:
        raise Exception(f"Sass Compilation Exception: {e}")
