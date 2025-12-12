from .base import UtilityGenerator

class ColorGenerator(UtilityGenerator):
    def generate(self):
        colors = self.theme.get("colors", {})
        scss = []
        scss.append("// Colors")
        
        for name, value in colors.items():
            # Standard
            scss.append(f".text-{name} {{ color: {value}; }}")
            scss.append(f".bg-{name} {{ background-color: {value}; }}")
            scss.append(f".border-{name} {{ border-color: {value}; }}")
            
            # Hover states (Fixed logic: only apply on :hover)
            # We use \\: to escape the colon in the class name for CSS
            scss.append(f".hover\\:bg-{name}:hover {{ background-color: {value}; }}")
            scss.append(f".hover\\:text-{name}:hover {{ color: {value}; }}")
            
        return "\n".join(scss)
