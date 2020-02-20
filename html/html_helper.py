

class HtmlHelper:
    matching_id = None
    matching_class = None
    matching_title = None
    matching_href = None
    matching_text = None
    matching_elements = None

    def __init__(self, element_to_find, html_page):
        self.matching_id = html_page.get_elements_with_id(element_to_find.get_id())
        self.matching_class = html_page.get_elements_with_class(element_to_find.get_class_name())
        self.matching_title = html_page.get_elements_with_title(element_to_find.get_title())
        self.matching_href = html_page.get_elements_with_href(element_to_find.get_href())
        self.matching_text = html_page.get_elements_with_text(element_to_find.get_text())
        self.matching_elements = list(set().union(self.matching_id, self.matching_class, self.matching_title,
                                                  self.matching_href, self.matching_text))

    def get_quantity_of_matches(self, element):
        element_matches = 0
        if element in self.matching_id:
            element_matches += 1
        if element in self.matching_class:
            element_matches += 1
        if element in self.matching_title:
            element_matches += 1
        if element in self.matching_href:
            element_matches += 1
        if element in self.matching_text:
            element_matches += 1
        return element_matches
