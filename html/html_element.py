class HtmlElement:
    id = None
    class_name = None
    title = None
    href = None
    text = None

    def __init__(self, html_element):
        self.id = html_element.attrib.get('id', None)
        self.class_name = html_element.attrib.get('class', None)
        self.title = html_element.attrib.get('title', None)
        self.href = html_element.attrib.get('href', None)
        self.text = html_element.text.strip()

    def get_id(self):
        return self.id

    def get_class_name(self):
        return self.class_name

    def get_title(self):
        return self.title

    def get_href(self):
        return self.href

    def get_text(self):
        return self.text