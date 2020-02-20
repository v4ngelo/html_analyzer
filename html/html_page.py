
import lxml.html

from html.html_helper import HtmlHelper


class HtmlPage:

    def __init__(self, html_file):
        try:
            with open(html_file) as fp:
                file = fp.read()
                self.html_page = lxml.html.document_fromstring(file)
        except FileNotFoundError:
            print('Caution: the file %s does not exist ' % html_file)
            raise

    # This returns all the elements in the file with the same ID - either 1 or 0
    def get_elements_with_id(self, element_id):
        return self.html_page.xpath("//*[@id='%s']" % element_id)

    def get_elements_with_href(self, element_href):
        return self.html_page.xpath("//*[@href='%s']" % element_href)

    def get_elements_with_text(self, element_text):
        return self.html_page.xpath("//*[contains(text(),'%s')]" % element_text)

    def get_elements_with_class(self, element_class):
        return self.html_page.xpath("//*[@class='%s']" % element_class)

    def get_elements_with_title(self, element_title):
        return self.html_page.xpath("//*[@title='%s']" % element_title)

    def get_most_similar_element(self, original_element):
        html_helper = HtmlHelper(original_element, self)
        matching_element = None
        similarities = -1

        for element in html_helper.matching_elements:
            element_coincidences = html_helper.get_quantity_of_matches(original_element)

            if element_coincidences > similarities:
                similarities = element_coincidences
                matching_element = element

        return matching_element
