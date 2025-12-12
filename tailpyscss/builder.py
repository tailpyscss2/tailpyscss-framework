import sass
import os
import re

def compile_scss(input_path, output_path):
    """
    Compile SCSS to CSS using libsass with @apply support.
    Uses a custom importer to recursively process @apply in all imported files.
    """
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # --- 1. The Magic Replacer (Shared Logic) ---
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
                    output_parts.append(f"@extend .{safe_c};")
                    
            return " ".join(output_parts)

        return re.sub(r'@apply\s+(.*?);', apply_replacer, scss_content, flags=re.DOTALL)

    # --- 2. Custom Importer ---
    # Intercepts @import to run the replacer on every file
    def tailpy_importer(path, prev):
        # Resolve path relative to previous file or input file
        base_dir = os.path.dirname(prev) if prev != "stdin" else os.path.dirname(input_path)
        
        # Try finding the file (handling _partial.scss convention)
        candidates = [
            os.path.join(base_dir, path),
            os.path.join(base_dir, path + ".scss"),
            os.path.join(base_dir, "_" + path + ".scss")
        ]
        
        target_file = None
        for c in candidates:
            if os.path.exists(c):
                target_file = c
                break
        
        if not target_file:
            return None # Let libsass handle error

        with open(target_file, 'r', encoding='utf-8') as f:
            raw_content = f.read()
        
        # PROCESS THE CONTENT
        processed_content = process_apply_directives(raw_content)
        
        # Return fully resolved path to help libsass track subsequent imports
        return [(target_file, processed_content)]

    # --- 3. Compile ---
    # We must read the entry file manually first
    with open(input_path, 'r') as f:
        entry_content = f.read()
    
    processed_entry = process_apply_directives(entry_content)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        css = sass.compile(
            string=processed_entry,
            importers=[(0, tailpy_importer)], # Priority 0
            include_paths=[os.path.dirname(input_path)],
            output_style='expanded'
        )
        with open(output_path, "w") as f:
            f.write(css)
            
    except sass.CompileError as e:
        raise Exception(f"Sass Compilation Exception: {e}")
