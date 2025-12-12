import sys
from tailpyscss.generator import generate_utilities
from tailpyscss.builder import compile_scss
from tailpyscss.cli.core.config import load_config
from tailpyscss.cli.core.cache import get_config_hash, load_cache, save_cache
from tailpyscss.cli.core.bridge import generate_theme_bridge

def build_project(watch_mode=False, last_hash=None):
    try:
        config = load_config()
        
        # 1. Smart Caching
        current_hash = get_config_hash(config)
        
        if watch_mode:
            cached_hash = last_hash
        else:
            cached_hash = load_cache()

        if cached_hash != current_hash:
            if watch_mode and cached_hash is not None:
                print("Config changed. Regenerating utilities...")
            # elif not watch_mode:
                # print("Configuration changed. Converting...")

            utilities_css = generate_utilities(config)
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
        compile_scss("styles/main.scss", "static/css/styles.css")
        if not watch_mode:
            print(f"Build complete. Output: static/css/styles.css")
        
        return current_hash
        
    except Exception as e:
        print(f"Build Error: {e}")
        if not watch_mode:
            sys.exit(1)
        return last_hash
