import os
import re
from typing import Set, List

class ContextScanner:
    """
    The 'Eye' of TailPySCSS.
    Scans the user's codebase to detect which 'ui="..."' attributes are actually used.
    This enables Tree Shaking (Demand-Driven CSS Generation).
    """
    
    # Extensions to scan
    TARGET_EXTENSIONS = {'.py', '.html', '.css', '.js', '.jsx', '.tsx', '.jinja2', '.j2'}
    
    # Regex Patterns
    # 1. Standard HTML/String: ui="card" or ui='card'
    # 2. Python Keyword (rare but good to catch): ui="card" inside function calls
    # 3. Python Class Usage: UIComponent("card")
    # 4. Shortcut Usage: Card(...), Button(...)
    PATTERNS = [
        re.compile(r'ui\s*=\s*["\']([a-zA-Z0-9_-]+)["\']'),
        re.compile(r'UIComponent\s*\(\s*["\']([a-zA-Z0-9_-]+)["\']'),
        re.compile(r'(Card|Button|Badge|Alert|Navbar|Hero|Input|Textarea|Select|Checkbox|Label|Spinner|Modal|Table|Avatar|Footer|Breadcrumb|Accordion|Tabs|Pagination|Sidebar|Dropdown|Switch|Radio|Range|File|Toast|Progress|Tooltip|Popover)\s*\('),
    ]

    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir
        self.found_contexts: Set[str] = set()

    def scan(self) -> Set[str]:
        """
        Recursively scans the project and returns a set of detected context names.
        e.g. {'card', 'navbar', 'button'}
        """
        self.found_contexts = set()
        
        # print(f"DEBUG: Scanning {self.root_dir}...")
        
        for root, dirs, files in os.walk(self.root_dir):
            
            # Exclude virtualenvs, git, and node_modules
            dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', 'venv', 'env', 'node_modules', '.gemini', 'tailpyscss'}]
            
            for file in files:
                _, ext = os.path.splitext(file)
                if ext in self.TARGET_EXTENSIONS:
                    file_path = os.path.join(root, file)
                    self.scan_file(file_path)
                    
        return self.found_contexts

    def scan_file(self, file_path: str) -> Set[str]:
        """
        Scans a single file and adds found contexts to self.found_contexts.
        Returns the set of found contexts for this file.
        """
        local_found = set()
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
                for pattern in self.PATTERNS:
                    matches = pattern.findall(content)
                    for match in matches:
                        # Normalize to lowercase (Card -> card)
                        cleaned = match.lower()
                        self.found_contexts.add(cleaned)
                        local_found.add(cleaned)
                        
        except Exception as e:
            # Silently fail on unreadable files to not break the build
            # print(f"Warning: Could not read {file_path}: {e}")
            pass
        
        return local_found

if __name__ == "__main__":
    # Quick Test
    scanner = ContextScanner(".")
    print("Found Contexts:", scanner.scan())
