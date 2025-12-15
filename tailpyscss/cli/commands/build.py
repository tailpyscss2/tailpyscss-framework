import sys
import os
from tailpyscss.generator import generate_utilities
from tailpyscss.builder import compile_scss
from tailpyscss.cli.core.config import load_config
from tailpyscss.cli.core.cache import get_config_hash, load_cache, save_cache
from tailpyscss.cli.core.bridge import generate_theme_bridge
from tailpyscss.scanner import ContextScanner

def build_project(watch_mode=False, last_hash=None):
    try:
        config = load_config()
        
        # 1. Smart Caching
        current_hash = get_config_hash(config)
        
        if watch_mode:
            cached_hash = last_hash
        else:
            cached_hash = load_cache()

        # 2. Context Scanning (New in v2)
        # We always scan because code usage might change even if config doesn't.
        # Ideally we should hash the code too, but for now we just scan fast.
        scanner = ContextScanner(".")
        active_contexts = scanner.scan()
        
        if not watch_mode and active_contexts:
            print(f"Tree Shaking Active: Found {len(active_contexts)} contexts: {', '.join(active_contexts)}")

        # Force regeneration if contexts found, to ensure imports are added
        # (Optimization: We could include contexts in the hash to only rebuild on change)
        
        if cached_hash != current_hash or not os.path.exists("styles/_utilities.scss") or active_contexts:
            if watch_mode and cached_hash is not None and cached_hash != current_hash:
                print("Config changed. Regenerating utilities...")

            utilities_css = generate_utilities(config, active_contexts=active_contexts)
            with open("styles/_utilities.scss", "w") as f:
                f.write(utilities_css)
            
            generate_theme_bridge(config)
            save_cache(current_hash)
            
            if watch_mode:
                 print("Updated tailpyscss_theme.py")
        else:
            if not watch_mode:
                print("Config unchanged. Using cached utilities.")
        
        # 3. Always compile SCSS (libsass is fast enough)
        # The `compile_scss` function from `tailpyscss.builder` is expected to handle `output_style`.
        compile_scss("styles/main.scss", "static/css/styles.css", output_style='compressed')
        if not watch_mode:
            print(f"Build complete. Output: static/css/styles.css")
        
        return current_hash
        
    except Exception as e:
        print(f"Build Error: {e}")
        if not watch_mode:
            sys.exit(1)
        return last_hash
