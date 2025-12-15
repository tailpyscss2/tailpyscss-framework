from .core import UIComponent

class Card(UIComponent):
    """A standard Card component."""
    def __init__(self, *children, **kwargs):
        super().__init__("card", "div", children=list(children), **kwargs)

class Button(UIComponent):
    """A standard Button component."""
    def __init__(self, label, **kwargs):
        super().__init__("button", "button", children=[label], **kwargs)

class Badge(UIComponent):
    """A small label/badge."""
    def __init__(self, label, **kwargs):
        super().__init__("badge", "span", children=[label], **kwargs)

class Alert(UIComponent):
    """An alert box."""
    def __init__(self, message, **kwargs):
        super().__init__("alert", "div", children=[message], **kwargs)

class Navbar(UIComponent):
    """A navigation bar."""
    def __init__(self, *children, **kwargs):
        super().__init__("navbar", "nav", children=list(children), **kwargs)

class Hero(UIComponent):
    """A hero section."""
    def __init__(self, *children, **kwargs):
        super().__init__("hero", "section", children=list(children), **kwargs)

# --- Forms ---
class Input(UIComponent):
    """Standard text input."""
    def __init__(self, type="text", placeholder="", **kwargs):
        super().__init__("input", "input", type=type, placeholder=placeholder, **kwargs)

class Textarea(UIComponent):
    """Multi-line text input."""
    def __init__(self, placeholder="", **kwargs):
        super().__init__("textarea", "textarea", placeholder=placeholder, **kwargs)

class Select(UIComponent):
    """Dropdown menu."""
    def __init__(self, *options, **kwargs):
        super().__init__("select", "select", children=list(options), **kwargs)

class Checkbox(UIComponent):
    """Checkbox toggle."""
    def __init__(self, label, **kwargs):
        # Wrapper div for layout
        super().__init__("checkbox", "div", children=[
            UIComponent("checkbox-input", "input", type="checkbox"),
            UIComponent("checkbox-label", "span", children=[label])
        ], **kwargs)

class Label(UIComponent):
    """Field label."""
    def __init__(self, text, **kwargs):
        super().__init__("label", "label", children=[text], **kwargs)

# --- Feedback ---
class Spinner(UIComponent):
    """Loading indicator."""
    def __init__(self, **kwargs):
        super().__init__("spinner", "div", **kwargs)

class Modal(UIComponent):
    """Overlay dialog."""
    def __init__(self, *children, **kwargs):
        super().__init__("modal", "dialog", children=list(children), **kwargs)

# --- Layout & Data ---
class Table(UIComponent):
    """Data grid."""
    def __init__(self, *children, **kwargs):
        super().__init__("table", "table", children=list(children), **kwargs)

class Avatar(UIComponent):
    """User profile image."""
    def __init__(self, src, alt="User", **kwargs):
        super().__init__("avatar", "img", src=src, alt=alt, **kwargs)

class Footer(UIComponent):
    """Page footer."""
    def __init__(self, *children, **kwargs):
        super().__init__("footer", "footer", children=list(children), **kwargs)

class Breadcrumb(UIComponent):
    """Navigation path."""
    def __init__(self, *links, **kwargs):
        super().__init__("breadcrumb", "nav", children=list(links), **kwargs)

class Accordion(UIComponent):
    """Collapsible content."""
    def __init__(self, title, content, **kwargs):
        super().__init__("accordion", "details", children=[
            UIComponent("accordion-header", "summary", children=[title]),
            UIComponent("accordion-content", "div", children=[content])
        ], **kwargs)

# --- Navigation ---
class Tabs(UIComponent):
    """Tabbed content container."""
    def __init__(self, *children, **kwargs):
        super().__init__("tabs", "div", children=list(children), **kwargs)

class Pagination(UIComponent):
    """Page navigation controls."""
    def __init__(self, *children, **kwargs):
        super().__init__("pagination", "nav", children=list(children), **kwargs)

class Sidebar(UIComponent):
    """Vertical navigation drawer."""
    def __init__(self, *children, **kwargs):
        super().__init__("sidebar", "aside", children=list(children), **kwargs)

class Dropdown(UIComponent):
    """Interactive dropdown menu."""
    def __init__(self, trigger, menu, **kwargs):
        super().__init__("dropdown", "div", children=[
            UIComponent("dropdown-trigger", "div", children=[trigger]),
            UIComponent("dropdown-menu", "div", children=[menu])
        ], **kwargs)

# --- Advanced Forms ---
class Switch(UIComponent):
    """Toggle switch."""
    def __init__(self, label, **kwargs):
        super().__init__("switch", "label", children=[
            UIComponent("switch-input", "input", type="checkbox"),
            UIComponent("switch-slider", "span"),
            UIComponent("switch-label", "span", children=[label])
        ], **kwargs)

class Radio(UIComponent):
    """Radio button."""
    def __init__(self, label, name, **kwargs):
        super().__init__("radio", "label", children=[
            UIComponent("radio-input", "input", type="radio", name=name),
            UIComponent("radio-label", "span", children=[label])
        ], **kwargs)

class Range(UIComponent):
    """Range slider input."""
    def __init__(self, **kwargs):
        super().__init__("range", "input", type="range", **kwargs)

class File(UIComponent):
    """File upload input."""
    def __init__(self, **kwargs):
        super().__init__("file", "input", type="file", **kwargs)

# --- Feedback & Overlay ---
class Toast(UIComponent):
    """Non-blocking notification."""
    def __init__(self, message, **kwargs):
        super().__init__("toast", "div", children=[message], **kwargs)

class Progress(UIComponent):
    """Progress bar."""
    def __init__(self, value, max=100, **kwargs):
        super().__init__("progress", "progress", value=str(value), max=str(max), children=[f"{value}%"], **kwargs)

class Tooltip(UIComponent):
    """Hover information."""
    def __init__(self, text, children, **kwargs):
        super().__init__("tooltip", "div", children=list(children) + [
            UIComponent("tooltip-text", "span", children=[text])
        ], **kwargs)

class Popover(UIComponent):
    """Click information overlay."""
    def __init__(self, content, children, **kwargs):
        super().__init__("popover", "div", children=list(children) + [
            UIComponent("popover-content", "div", children=[content])
        ], **kwargs)
