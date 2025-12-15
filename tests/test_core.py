import unittest
import os
import shutil
from tailpyscss.generator import generate_utilities
from tailpyscss.scanner import ContextScanner
from tailpyscss.ui import Card, Button, Navbar
from tailpyscss.ui.core import UIComponent

class TestTailPySCSS_v2(unittest.TestCase):
    
    # --- V1: Core Engine Tests ---
    def test_import(self):
        """Test that the framework imports without error."""
        import tailpyscss
        self.assertIsNotNone(tailpyscss)

    def test_generator_basics(self):
        """Test that utility generation produces a string."""
        config = {
            "colors": {"primary": "#000"},
            "spacing": {"4": "1rem"}
        }
        css = generate_utilities(config)
        self.assertIsInstance(css, str)
        self.assertIn(".text-primary", css)
        self.assertIn(".p-4", css)

    # --- V2: Python Component Tests ---
    def test_ui_component_rendering(self):
        """Test that UIComponents render correct HTML structure."""
        # 1. Basic Component
        btn = Button("Click Me", variant="primary")
        html = str(btn)
        self.assertIn('ui="button"', html)
        self.assertIn('Click Me', html)
        
        # 2. Nested Component
        card = Card(
            Button("Submit")
        )
        html = str(card)
        self.assertIn('ui="card"', html)
        self.assertIn('ui="button"', html)
        self.assertIn('Submit', html)

    def test_scanner_detection(self):
        """Test that the ContextScanner detects Python class usage."""
        # Create a temp file simulating user code
        test_file = "temp_view.py"
        with open(test_file, "w") as f:
            f.write("""
from tailpyscss.ui import Navbar, Hero
def home():
    return Navbar(Hero("Welcome"))
            """)
        
        try:
            scanner = ContextScanner(".")
            contexts = scanner.scan_file(test_file)
            
            # Should detect 'navbar' and 'hero'
            self.assertIn("navbar", contexts)
            self.assertIn("hero", contexts)
            
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
