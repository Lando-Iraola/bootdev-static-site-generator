from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        del self.value

    def to_html(self, node=None):
        if self.tag is None:
            raise ValueError("Missing tag!")
        if self.children is None:
            raise ValueError("Missing children!")

        html_rep = ""
        children = None
        if node is None:
            html_rep += f"<{self.tag}>"
            children = self.children
        elif hasattr(node, "children"):
            children = node.children
        for child in children:
            html_rep += child.to_html()
        if node is None:
            html_rep += f"</{self.tag}>"
        return html_rep
