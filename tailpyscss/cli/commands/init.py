import os

def init_project():
    print("Initializing TailPySCSS project...")
    
    # Python Config Template
    config_py = """
# TailPySCSS Configuration
# Defines your design system tokens.

config = {
    "colors": {
        "primary": "#3b82f6",
        "secondary": "#ec4899",
        "danger": "#ef4444",
        "dark": "#1f2937",
        "light": "#f3f4f6",
        "white": "#ffffff",
        "black": "#000000"
    },
    "screens": {
        "sm": "640px",
        "md": "768px",
        "lg": "1024px",
        "xl": "1280px"
    },
    "spacing": {
        "1": "0.25rem",
        "2": "0.5rem",
        "4": "1rem",
        "8": "2rem",
        "16": "4rem"
    },
    "typography": {
        "font-sans": "Inter, sans-serif",
        "font-serif": "Merriweather, serif"
    }
}
"""
    if not os.path.exists("tailpy_config.py"):
        with open("tailpy_config.py", "w") as f:
            f.write(config_py.strip())
        print("Created tailpy_config.py")
    else:
        print("tailpy_config.py already exists.")

    # Create directories
    os.makedirs("styles", exist_ok=True)
    
    if not os.path.exists("styles/main.scss"):
        with open("styles/main.scss", "w") as f:
            f.write('@import "utilities";\n\nbody {\n    @apply bg-dark text-light;\n}\n\n.btn-primary {\n    @apply bg-primary p-4 rounded text-white;\n}\n')
        print("Created styles/main.scss")
