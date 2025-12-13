from .base import UtilityGenerator

class LayoutGenerator(UtilityGenerator):
    def generate(self):
        spacing = self.theme.get("spacing", {})
        scss = []
        scss.append("// Layout (Flex, Grid, Sizing)")
        
        # --- Container ---
        # Basic implementation of container
        scss.append(".container { width: 100%; margin-left: auto; margin-right: auto; max-width: 1280px; }")
        
        # --- Display ---
        displays = ["block", "inline-block", "inline", "flex", "inline-flex", "hidden", "grid"]
        for d in displays:
            # .hidden maps to display: none specifically
            val = "none" if d == "hidden" else d
            scss.append(f".{d} {{ display: {val}; }}")
            
        # --- Box Sizing ---
        scss.append(".box-border { box-sizing: border-box; }")
        scss.append(".box-content { box-sizing: content-box; }")

        # --- Flexbox ---
        # Direction
        scss.append(".flex-row { flex-direction: row; }")
        scss.append(".flex-col { flex-direction: column; }")
        scss.append(".flex-row-reverse { flex-direction: row-reverse; }")
        scss.append(".flex-col-reverse { flex-direction: column-reverse; }")
        
        # Wrap
        scss.append(".flex-wrap { flex-wrap: wrap; }")
        scss.append(".flex-nowrap { flex-wrap: nowrap; }")
        
        # Grow/Shrink
        scss.append(".flex-1 { flex: 1 1 0%; }")
        scss.append(".flex-auto { flex: 1 1 auto; }")
        scss.append(".flex-none { flex: none; }")
        scss.append(".grow { flex-grow: 1; }")
        
        # Justify Content
        justify_map = {
            "start": "flex-start", "end": "flex-end", "center": "center",
            "between": "space-between", "around": "space-around", "evenly": "space-evenly"
        }
        for name, value in justify_map.items():
            scss.append(f".justify-{name} {{ justify-content: {value}; }}")
            
        # Align Items
        align_map = {
            "start": "flex-start", "end": "flex-end", "center": "center",
            "baseline": "baseline", "stretch": "stretch"
        }
        for name, value in align_map.items():
            scss.append(f".items-{name} {{ align-items: {value}; }}")

        # --- Grid ---
        # Columns 1-12
        for i in range(1, 13):
            scss.append(f".grid-cols-{i} {{ grid-template-columns: repeat({i}, minmax(0, 1fr)); }}")

        # Gap (shared with flex)
        for name, value in spacing.items():
            scss.append(f".gap-{name} {{ gap: {value}; }}")
            scss.append(f".gap-x-{name} {{ column-gap: {value}; }}")
            scss.append(f".gap-y-{name} {{ row-gap: {value}; }}")

        # --- Sizing ---
        # Width
        widths = {
            "full": "100%", "screen": "100vw", "min": "min-content", "max": "max-content", 
            "1/2": "50%", "1/3": "33.333333%", "2/3": "66.666667%", 
            "1/4": "25%", "3/4": "75%"
        }
        for name, value in widths.items():
            safe_name = name.replace("/", "\\/")
            scss.append(f".w-{safe_name} {{ width: {value}; }}")
            
        # Fixed Widths (Spacing)
        for name, value in spacing.items():
             scss.append(f".w-{name} {{ width: {value}; }}")

        # Height
        heights = {
            "full": "100%", "screen": "100vh", "min": "min-content", "max": "max-content"
        }
        for name, value in heights.items():
             scss.append(f".h-{name} {{ height: {value}; }}")
             
        # Fixed Heights (Spacing)
        for name, value in spacing.items():
             scss.append(f".h-{name} {{ height: {value}; }}")
             
        # Min/Max Height
        for name, value in heights.items():
             scss.append(f".min-h-{name} {{ min-height: {value}; }}")
             scss.append(f".max-h-{name} {{ max-height: {value}; }}")

        # --- Positioning ---
        positions = ["static", "fixed", "absolute", "relative", "sticky"]
        for pos in positions:
            scss.append(f".{pos} {{ position: {pos}; }}")
            
        # Position Offsets (top, right, bottom, left)
        offsets = ["top", "right", "bottom", "left"]
        scss.append(f".top-0 {{ top: 0px; }}")
        scss.append(f".right-0 {{ right: 0px; }}")
        scss.append(f".bottom-0 {{ bottom: 0px; }}")
        scss.append(f".left-0 {{ left: 0px; }}")
        
        # Add spacing offsets
        for name, value in spacing.items():
            for side in offsets:
                scss.append(f".{side}-{name} {{ {side}: {value}; }}")

        # Z-Index
        z_indices = [0, 10, 20, 30, 40, 50]
        for z in z_indices:
            scss.append(f".z-{z} {{ z-index: {z}; }}")

        return "\n".join(scss)
