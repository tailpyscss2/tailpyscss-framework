import unittest
from tailpyscss.generator import generate_utilities

class TestTailPySCSS(unittest.TestCase):
    def test_import(self):
        """Test that the framework imports without error."""
        import tailpyscss
        self.assertIsNotNone(tailpyscss)

    def test_generator(self):
        """Test that utility generation produces a string."""
        config = {
            "colors": {"primary": "#000"},
            "spacing": {"4": "1rem"}
        }
        css = generate_utilities(config)
        self.assertIsInstance(css, str)
        self.assertIn(".text-primary", css)
        self.assertIn(".p-4", css)

if __name__ == '__main__':
    unittest.main()
