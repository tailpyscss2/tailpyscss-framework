from .base import UtilityGenerator

class SpacingGenerator(UtilityGenerator):
    def generate(self):
        spacing = self.theme.get("spacing", {})
        scss = []
        scss.append("// Spacing")
        
        for name, value in spacing.items():
            # Padding
            scss.append(f".p-{name} {{ padding: {value}; }}")
            scss.append(f".pt-{name} {{ padding-top: {value}; }}")
            scss.append(f".pr-{name} {{ padding-right: {value}; }}")
            scss.append(f".pb-{name} {{ padding-bottom: {value}; }}")
            scss.append(f".pl-{name} {{ padding-left: {value}; }}")
            scss.append(f".px-{name} {{ padding-left: {value}; padding-right: {value}; }}")
            scss.append(f".py-{name} {{ padding-top: {value}; padding-bottom: {value}; }}")
            
            # Margin
            scss.append(f".m-{name} {{ margin: {value}; }}")
            scss.append(f".mt-{name} {{ margin-top: {value}; }}")
            scss.append(f".mr-{name} {{ margin-right: {value}; }}")
            scss.append(f".mb-{name} {{ margin-bottom: {value}; }}")
            scss.append(f".ml-{name} {{ margin-left: {value}; }}")
            scss.append(f".mx-{name} {{ margin-left: {value}; margin-right: {value}; }}")
            scss.append(f".my-{name} {{ margin-top: {value}; margin-bottom: {value}; }}")

        # Auto Margins
        scss.append(".m-auto { margin: auto; }")
        scss.append(".mx-auto { margin-left: auto; margin-right: auto; }")
        scss.append(".my-auto { margin-top: auto; margin-bottom: auto; }")

            
        return "\n".join(scss)
