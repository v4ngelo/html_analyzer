#### HTML Analyzer


This programs allows you to find the most similar element in an HTML file, given 
the properties of the element.

#####Parameters:
- The *path* to the HTML file containing the HTML element used as a base for the search.
- The *path* to the HTML file where the application need to search for the element.
- The 'id' of the original element the application needs to use to match properties (From the original file)

#####Requirements
 Python 3
 
#####Steps
1. After cloning the project, create a virtual environment in the home folder and 
 execute `python3 -m venv <name_of_virtualenv>`
2. Execute `source venv/bin/activate`
3. Run `pip install -r requirements.txt`

#####Usage:
In the home folder, execute in the terminal:
``` python
python html_analyzer.py <origin_file_path> <diff_file_path> <html_element_id>
