
class UIComponent:
    """
    The Universal Atomic Unit of TailPySCSS.
    Renders pure HTML with the 'ui' attribute context.
    """
    def __init__(self, context: str, tag: str = "div", children=None, **attrs):
        self._context = context
        self.tag = tag
        self.children = children or []
        self.attrs = attrs

    def render(self) -> str:
        # 1. Build Attributes
        attr_str = f'ui="{self._context}"'
        for k, v in self.attrs.items():
            # Convert python_style to html-style (class_ -> class)
            key = k.rstrip("_")
            attr_str += f' {key}="{v}"'
            
        # 2. Render Children
        child_html = ""
        if isinstance(self.children, list):
            for child in self.children:
                child_html += str(child)
        else:
            child_html = str(self.children)

        # 3. Return HTML
        return f'<{self.tag} {attr_str}>{child_html}</{self.tag}>'

    def __str__(self):
        return self.render()
