import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .build import build_project

def watch_project():
    print("Watching for changes... (Config: Python, Debounce: 0.1s)")
    
    # Initial build to get hash
    last_hash = build_project(watch_mode=True, last_hash=None)
    
    # We need a mutable wrapper to share state with handler
    state = {'last_hash': last_hash}

    class BuildHandler(FileSystemEventHandler):
        def __init__(self, state_ref):
            self.last_run = 0
            self.debounce_interval = 0.1 # 100ms
            self.state = state_ref
            
        def on_modified(self, event):
            if event.is_directory:
                return
            
            # Watch valid files
            if event.src_path.endswith(".scss") or \
               event.src_path.endswith("tailpy_config.py") or \
               event.src_path.endswith("tailpy.config.json"):
                
                # Debounce
                now = time.time()
                if now - self.last_run < self.debounce_interval:
                    return
                self.last_run = now
                
                print(f"Detected change in {os.path.basename(event.src_path)}...")
                # Pass previous hash to optimize utility generation
                self.state['last_hash'] = build_project(watch_mode=True, last_hash=self.state['last_hash'])

    observer = Observer()
    handler = BuildHandler(state)
    
    # Watch current directory
    observer.schedule(handler, path=".", recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
