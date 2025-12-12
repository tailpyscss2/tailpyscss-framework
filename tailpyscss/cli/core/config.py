import os
import sys
import json
import importlib.util
from .security import sanitize_css_value

def sanitize_config(config):
    """Recursively sanitize the config dictionary."""
    clean_config = {}
    for key, val in config.items():
        if isinstance(val, dict):
            clean_config[key] = sanitize_config(val)
        elif isinstance(val, str):
            clean_config[key] = sanitize_css_value(val)
        else:
            clean_config[key] = val
    return clean_config

def load_config():
    """
    Load configuration from tailpy_config.py (priority) or tailpy.config.json.
    """
    # 1. Try Python Config
    if os.path.exists("tailpy_config.py"):
        try:
            spec = importlib.util.spec_from_file_location("tailpy_config", "tailpy_config.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "config"):
                # print("Loaded configuration from tailpy_config.py") # Less verbose
                return sanitize_config(module.config)
            else:
                print("Error: tailpy_config.py must define a 'config' dictionary.")
                sys.exit(1)
        except Exception as e:
            print(f"Error loading tailpy_config.py: {e}")
            sys.exit(1)

    # 2. Try JSON Config (Legacy)
    elif os.path.exists("tailpy.config.json"):
        print("Warning: tailpy.config.json is deprecated. Please migrate to tailpy_config.py.")
        with open("tailpy.config.json", "r") as f:
            try:
                return sanitize_config(json.load(f))
            except json.JSONDecodeError:
                print("Error: Invalid JSON in tailpy.config.json")
                sys.exit(1)
    
    # 3. No config found
    else:
        print("Error: No configuration found. Run 'tailpyscss init' to create one.")
        sys.exit(1)
