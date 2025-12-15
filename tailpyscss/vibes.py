
# The Vibe Engine Presets
# Defines the "Physics" of the UI.
# Used to inject SCSS variables globally.

VIBE_PRESETS = {
    # 1. FLAT (Default) - Clean, Modern, Minimal
    "flat": {
        "vibe-bg": "#ffffff",
        "vibe-shadow": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)",
        "vibe-border": "1px solid #e5e7eb",
        "vibe-radius": "0.5rem",
        "vibe-backdrop": "none",
        "vibe-accent-glow": "none",
        "vibe-text": "#1f2937"
    },
    
    # 2. GLASS - Frosted, Translucent, Premium
    "glass": {
        "vibe-bg": "rgba(255, 255, 255, 0.7)",
        "vibe-shadow": "0 8px 32px 0 rgba(31, 38, 135, 0.15)",
        "vibe-border": "1px solid rgba(255, 255, 255, 0.4)",
        "vibe-radius": "1rem",
        "vibe-backdrop": "blur(12px)",
        "vibe-accent-glow": "0 0 10px rgba(255, 255, 255, 0.5)",
        "vibe-text": "#1f2937"
    },
    
    # 3. NEON - Dark, Glowing, Cyberpunk
    "neon": {
        "vibe-bg": "#0f172a", # Dark Slate
        "vibe-shadow": "0 0 15px rgba(59, 130, 246, 0.5)", # Primary color glow
        "vibe-border": "2px solid #3b82f6",
        "vibe-radius": "0px", # Sharp edges
        "vibe-backdrop": "none",
        "vibe-accent-glow": "0 0 20px #3b82f6",
        "vibe-text": "#f3f4f6"
    }
}
