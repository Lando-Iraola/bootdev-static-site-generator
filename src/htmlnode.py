class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        children = ""
        if self.children:
            for child in children:
                children += f"\n{child}"
        props = ""
        if self.props:
            for key, value in self.props.items():
                props += f"\n{key}:{value}"

        return f"""tag={self.tag}
value={self.value}
children={children}
props={props}"""

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        texts = []
        for key, value in self.props.items():
            texts.append(f' {key}="{value}"')
        return "".join(texts)
