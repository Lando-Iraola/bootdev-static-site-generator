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
    for path in os.listdir(from_path):
        markdown_path = os.path.join(from_path, path)

        if os.path.isdir(markdown_path):
            new_dst = os.path.join(dest_path, path)
            if not os.path.exists(new_dst):
                os.makedirs(new_dst)
            generate_page(markdown_path, template_path, new_dst)
        else:
            with open(markdown_path, "r") as f:
                markdown = f.read()

            with open(template_path, "r") as f:
                template = f.read()

            html = markdown_to_html_node(markdown)
            html = html.to_html()
            title = extract_title(markdown)

            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)



            dest = os.path.join(dest_path, "index.html")
            with open(dest, "w") as f:
                f.write(template)


def generate_pages_recursive(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    for path in os.listdir(from_path):
        markdown_path = os.path.join(from_path, path)

        if os.path.isdir(markdown_path):
            new_dst = os.path.join(dest_path, path)
            if not os.path.exists(new_dst):
                os.makedirs(new_dst)
            generate_page(markdown_path, template_path, new_dst)
        else:
            with open(markdown_path, "r") as f:
                markdown = f.read()

            with open(template_path, "r") as f:
                template = f.read()

            html = markdown_to_html_node(markdown)
            html = html.to_html()
            title = extract_title(markdown)

            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)



            dest = os.path.join(dest_path, "index.html")
            with open(dest, "w") as f:
                f.write(template)
