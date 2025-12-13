from .base import UtilityGenerator

class TypographyGenerator(UtilityGenerator):
    def generate(self):
        font_params = self.theme.get("fontParams", {})
        scss = []
        scss.append("// Typography")
        
        # Base HTML font size for rem calculation ease
        scss.append("html { font-size: 62.5%; }")
        scss.append("body { font-family: sans-serif; font-size: 1.6rem; }")

        # Font Family
        if "sans" in font_params:
            scss.append(f".font-sans {{ font-family: {font_params['sans']}; }}")
        if "serif" in font_params:
            scss.append(f".font-serif {{ font-family: {font_params['serif']}; }}")
        if "mono" in font_params:
            scss.append(f".font-mono {{ font-family: {font_params['mono']}; }}")

        # Font Size
        font_sizes = {
            "xs": "0.75rem", "sm": "0.875rem", "base": "1rem", 
            "lg": "1.125rem", "xl": "1.25rem", "2xl": "1.5rem",
            "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem"
        }
        for name, value in font_sizes.items():
            scss.append(f".text-{name} {{ font-size: {value}; }}")
        
        # Font Weight
        font_weights = {
            "thin": "100", "light": "300", "normal": "400",
            "medium": "500", "semibold": "600", "bold": "700",
            "bolder": "900", "black": "900"
        }
        for name, value in font_weights.items():
            scss.append(f".font-{name} {{ font-weight: {value}; }}")
        
        # Text Align
        scss.append(".text-left { text-align: left; }")
        scss.append(".text-center { text-align: center; }")
        scss.append(".text-right { text-align: right; }")
        scss.append(".text-justify { text-align: justify; }")

        # Line Height (Leading)
        line_heights = {
            "none": "1",
            "tight": "1.25",
            "snug": "1.375",
            "normal": "1.5",
            "relaxed": "1.625",
            "loose": "2"
        }
        for name, value in line_heights.items():
            scss.append(f".leading-{name} {{ line-height: {value}; }}")
        
        return "\n".join(scss)
