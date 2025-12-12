import os
import markdown
from jinja2 import Environment, FileSystemLoader

# Configuration
CONTENT_DIR = "../docs"
OUTPUT_DIR = "../docs"
TEMPLATE_DIR = "templates"

def build():
    # 1. Setup Jinja2
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("layout.html")
    
    # 2. Find Markdown Files
    print(f"Building documentation from {CONTENT_DIR}...")
    
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(CONTENT_DIR, filename)
            
            # Read Markdown
            with open(filepath, "r", encoding="utf-8") as f:
                md_content = f.read()
            
            # Convert to HTML
            html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
            
            # Determine Title (First H1 or Filename)
            title = filename.replace(".md", "").title()
            for line in md_content.splitlines():
                if line.startswith("# "):
                    title = line.replace("# ", "").strip()
                    break
            
            # Render Template
            output_html = template.render(
                title=title,
                content=html_content,
                current_page=filename
            )
            
            # Save HTML
            output_filename = filename.replace(".md", ".html")
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output_html)
                
            print(f"✔ Generated: {output_filename}")

if __name__ == "__main__":
    build()
