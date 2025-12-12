import json
import hashlib
import os

CACHE_FILE = ".tailpy.cache"

def get_config_hash(config):
    """Generate an MD5 hash of the configuration for caching."""
    config_str = json.dumps(config, sort_keys=True)
    return hashlib.md5(config_str.encode('utf-8')).hexdigest()

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return f.read().strip()
    return None

def save_cache(hash_val):
    with open(CACHE_FILE, "w") as f:
        f.write(hash_val)
