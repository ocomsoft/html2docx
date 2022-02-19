"""
Dev playground
"""

from docx import Document

import sys
sys.path.append(".")

from htmldocx import HtmlToDocx

print(f"Name: {__name__}")
print(f"Package: {__package__}")

html = """
<title>Dev exploration</title>

<h1>Hello Friend</h1>

<p>This is a paragraph.</p>

<h1 class="canvasFile">Canvas File</h1>

<p class="canvasFile">COM31 Study Guide-Week 1.pdf</p>

<p class="intenseQuote">This should be a quote.</p>
"""

#-- attempt to use a reverse Mammoth style map
# https://github.com/mwilliamson/mammoth.js#writing-style-maps
# - But I don't have the time to do the full parser
STYLE_MAP = {
	# Mammoth "p[style-name='Canvas File'] => h1.canvasFile",
	"h1" : {
		"canvasFile" : 'Canvas File',
		"canvasSubHeader" : 'Canvas SubHeader',
		"canvasDiscussion" : 'Canvas Discussion',
		"canvasQuiz" : 'Canvas Quiz'
	}, 
	"p" : {
		"intenseQuote" : "Quote"
	}
}

document = Document('C:\\Users\\s2986288\\code\\Example.docx')

new_parser = HtmlToDocx()
new_parser.style_map = STYLE_MAP

new_parser.add_html_to_document(html,document)

document.save('dev.docx')