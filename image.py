"""
Dev playground
"""

from docx import Document

import sys
sys.path.append(".")

from htmldocx import HtmlToDocx

html = """
<title>base64 test</title>


<div style="float: left;">
<img height="106" src="https://bblearn-blaed.griffith.edu.au/bbcswebdav/courses/7700IBA_6184_OL/Images/question mark.jpg" style="float: left;" width="90"/>
</div>


"""

# Define the mapping from HTML class to Word style
# Each HTML tag has a dict keyed on HTML class where
# the value is the Word style name

STYLE_MAP = {
		"h1" : {
		"canvasFile" : 'Canvas File',
		"canvasSubHeader" : 'Canvas SubHeader',
		"canvasDiscussion" : 'Canvas Discussion',
		"canvasQuiz" : 'Canvas Quiz',
        "canvasAssignment" : 'Canvas Assignment',
        "canvasExternalTool" : 'Canvas External Tool',
        'canvasExternalUrl' : 'Canvas External Url',
	}, 
    "p" : {
        "embed": 'Embed',
        "hide" : "Hide",
        "canvasFileLink": 'Canvas File Link'
    },
    "span" : {
        "embed": 'Embed',
        "hide" : "Hide",
        "canvasFileLink": 'Canvas File Link'
    }
}

# Start with a blank Word doc that has the Word styles 
# from above defined
document = Document('C:\\Users\\s2986288\\code\\Example.docx')

# create the parser and point to the style map
new_parser = HtmlToDocx()
new_parser.style_map = STYLE_MAP

new_parser.add_html_to_document(html,document)

document.save('image.docx')