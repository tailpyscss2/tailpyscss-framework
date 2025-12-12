from .base import UtilityGenerator

class BordersGenerator(UtilityGenerator):
    def generate(self):
        scss = []
        scss.append("// Borders")

        # --- Border Radius ---
        radii = {
            "none": "0px",
            "sm": "0.125rem",
            "DEFAULT": "0.25rem", # .rounded
            "md": "0.375rem",
            "lg": "0.5rem",
            "xl": "0.75rem",
            "2xl": "1rem",
            "3xl": "1.5rem",
            "full": "9999px"
        }

        for name, value in radii.items():
            if name == "DEFAULT":
                scss.append(f".rounded {{ border-radius: {value}; }}")
            else:
                scss.append(f".rounded-{name} {{ border-radius: {value}; }}")

        # --- Border Width ---
        widths = {
            "DEFAULT": "1px",
            "0": "0px",
            "2": "2px",
            "4": "4px",
            "8": "8px"
        }
        
        for name, value in widths.items():
            if name == "DEFAULT":
                scss.append(f".border {{ border-width: {value}; border-style: solid; }}")
            else:
                scss.append(f".border-{name} {{ border-width: {value}; border-style: solid; }}")

        return "\n".join(scss)
