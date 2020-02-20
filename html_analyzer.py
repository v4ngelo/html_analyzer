import sys
from html.html_page import HtmlPage
from html.html_element import HtmlElement


def analyze_html(original_file, diff_file, element_id_to_find):

    try:
        original_html = HtmlPage(original_file)
        diff_html = HtmlPage(diff_file)
        original_element = HtmlElement(original_html.get_elements_with_id(element_id_to_find)[0])
    except FileNotFoundError:
        return
    except Exception:
        print('The original element could not be found in %s' % original_file)
        return

    most_similar_element = diff_html.get_most_similar_element(original_element)

    if most_similar_element is None:
        print('The element could not be found')
        return

    print(
        'Attributes: %s \n'
        'Tag: %s \n'
        'Text: %s \n' % (most_similar_element.attrib, most_similar_element.tag, most_similar_element.text.strip()))


if len(sys.argv) < 4:
    print('Missing arguments: \n '
          '<file-origin> <file-diff> <element-id> are required.')
    exit()

input_original_file = sys.argv[1]
input_diff_file = sys.argv[2]
element_id = sys.argv[3]
analyze_html(input_original_file, input_diff_file, element_id)
