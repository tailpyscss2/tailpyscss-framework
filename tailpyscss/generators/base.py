from abc import ABC, abstractmethod

class UtilityGenerator(ABC):
    def __init__(self, config):
        self.config = config
        # Support both nested 'theme' and flat structure
        self.theme = config.get("theme", config)
    
    @abstractmethod
    def generate(self):
        """Generate SCSS string for this utility category."""
        pass
