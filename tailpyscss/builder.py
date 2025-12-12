import sass
import os
import re

def compile_scss(input_path, output_path):
    """Compile SCSS to CSS using libsass with @apply support."""
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, 'r') as f:
        scss_content = f.read()

    # Preprocess @apply
    # Transforms "@apply text-xl font-bold;" to "@extend .text-xl; @extend .font-bold;"
    def apply_replacer(match):
        # Remove semicolons and extra spaces, then split
        content = match.group(1).strip()
        classes = content.replace(";", "").split()
        # Create @extend directives or inline styles for arbitrary values
        output_parts = []
        
        # Mapping for arbitrary values
        # e.g. min-h-[80rem] -> min-height: 80rem;
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
            # Check for arbitrary value syntax: prefix-[value]
            # Regex: ^([a-z-]+)-\[(.+)\]$
            jit_match = re.match(r'^([a-z-]+)-\[(.+)\]$', c)
            
            if jit_match:
                prefix = jit_match.group(1)
                value = jit_match.group(2)
                
                # If valid prefix, generate inline CSS
                if prefix in arbitrary_map:
                    props = arbitrary_map[prefix]
                    for prop in props:
                        # Convert underscores to spaces in value (common Tailwind convention for spaces)
                        final_value = value.replace("_", " ")
                        output_parts.append(f"{prop}: {final_value};")
                else:
                    # Unknown prefix, maybe just normal CSS?
                    pass
            else:
                # Standard utility -> @extend
                # Escape colons for SASS (e.g. hover:bg-black -> hover\:bg-black)
                safe_c = c.replace(":", "\\:")
                output_parts.append(f"@extend .{safe_c};")
                
        return " ".join(output_parts)

    # Regex to capture content inside @apply ... ;
    # We use non-greedy matches for safety
    scss_content = re.sub(r'@apply\s+(.*?);', apply_replacer, scss_content, flags=re.DOTALL)

    # Output directory must exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Compile
    # include_paths is needed to resolve imports relative to the input file
    include_paths = [os.path.dirname(input_path)]
    
    try:
        css = sass.compile(string=scss_content, include_paths=include_paths, output_style='expanded')
        with open(output_path, "w") as f:
            f.write(css)
    except sass.CompileError as e:
        # Rethrow with a cleaner message or let it bubble up
        raise Exception(f"Sass Compilation Exception: {e}")
