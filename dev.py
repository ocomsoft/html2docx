"""
Dev playground
"""

from docx import Document

import sys
sys.path.append(".")

from htmldocx import HtmlToDocx

html = """
<title>Dev exploration</title>

<h1>Link Test</h1>

<p>
<span class="canvasFileLink">Hello</span>
<br />
<span class="canvasFileLink"><a href="some link">Hello</a></span>
</p>
<p class="hide">[Attached files]</p>
<ul> 
  <li> <span class="canvasFileLink"> Valve Steams Ahead.pdf </span> </li>
</ul>



<h1>Hello Friend</h1>

<img src="https://bblearn-blaed.griffith.edu.au/bbcswebdav/pid-6470054-dt-content-rid-121375576_1/xid-121375576_1" />

<p>This is a paragraph.</p>

<img src="https://www.diga.me.uk/lena.bmp" />

<h1 class="canvasFile">Canvas File</h1>

<p class="canvasFile">COM31 Study Guide-Week 1.pdf</p>

<p class="intenseQuote">This should be a quote.</p>

<h1>Testing spaces</h1> 

<div class="details">
<div class="vtbegenerated">

<a href="https://augustlovesmay.com/wp-content/uploads/2011/07/2011-07-18-How-to-decide-if-you-need-a-flowchart1.jpg" target="_blank"><p>Image <a href="https://bblearn-blaed.griffith.edu.au/bbcswebdav/pid-6470054-dt-content-rid-121375576_1/xid-121375576_1">https://bblearn-blaed.griffith.edu.au/bbcswebdav/pid-6470054-dt-content-rid-121375576_1/xid-121375576_1</a></p></a>

<input id="121375576_1_fileReadWritePermAvl" name="121375576_1_fileReadWritePermAvl" type="hidden" value="true"/>




</div>
</div>


"""

#-- attempt to use a reverse Mammoth style map
# https://github.com/mwilliamson/mammoth.js#writing-style-maps
# - But I don't have the time to do the full parser
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

#-- do the work with html2docx
document = Document('C:\\Users\\s2986288\\code\\Example.docx')

new_parser = HtmlToDocx()
new_parser.style_map = STYLE_MAP

new_parser.add_html_to_document(html,document)

document.save('dev.docx')