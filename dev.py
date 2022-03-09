"""
Dev playground
"""

from docx import Document

import sys
sys.path.append(".")

from htmldocx import HtmlToDocx

html = """
<title>Dev exploration</title>

<p>
<span class="canvasFileLink">Hello</span>
</p>

<h1 class="canvasFile">Canvas File</h1>

<p class="canvasFile">COM31 Study Guide-Week 1.pdf</p>

<p class="intenseQuote">This should be a quote.</p>

<h2>Global Lawyer: What, Why, How?</h2>
<p>We start day one with discussion about the aim of this course: establishing the meaning of the 
<em>global lawyer</em>. Why are we focusing on this? What is it? How do we 
become one?</p><p>By way of background, this slide deck introduces the what, 
why, how of this course—or 
<a href="https://griffitheduau-my.sharepoint.com/:p:/g/personal/kate_galloway_griffith_edu_au/EXKjxAHC1zRAgxKD4Zy4Q2sBNsdB69ucNebLB6LAugAqWg?e=esR1fQ" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6452059_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_95488_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fgriffitheduau-my.sharepoint.com%2F%3Ap%3A%2Fg%2Fpersonal%2Fkate_galloway_griffith_edu_au%2FEXKjxAHC1zRAgxKD4Zy4Q2sBNsdB69ucNebLB6LAugAqWg%3Fe%3DesR1fQ';" target="_blank">link to the powerpoint here</a>.</p>
<p class="embed">&lt;iframe frameborder="0" height="565px" src="https://griffitheduau-my.sharepoint.com/personal/kate_galloway_griffith_edu_au/_layouts/15/Doc.aspx?sourcedoc={01c4a372-d7c2-4034-8312-83e19cb8436b}&amp;amp;action=embedview&amp;amp;wdAr=1.7777777777777777" width="962px"&gt;This is an embedded &lt;a href="https://office.com" target="_blank"&gt;Microsoft Office&lt;/a&gt; presentation, powered by &lt;a href="https://office.com/webapps" target="_blank"&gt;Office&lt;/a&gt;.&lt;/iframe&gt;</p>
"""


fred = """

<h3>To discuss in class</h3><p>Bring to class the three biggest takeaways from the readings.</p><div class="activity"><div class="activityImage">
<img alt="Activity icon" src="https://filebucketdave.s3.amazonaws.com/banner.js/images/icons8-dancing-48.png"/>
</div>
<div class="instructions">
<p>What do they say about the contemporary nature of legal practice? How is legal practice ‘global’?</p>
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

document.save('dev.docx')