import os
from markdown_blocks import markdown_to_html_node
def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Could not extract title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown)
    html = html.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    dest = os.path.join(dest_path, "index.html")
    with open(dest, "w") as f:
        f.write(template)