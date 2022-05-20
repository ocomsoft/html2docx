"""
Dev playground
"""

from htmldocx import HtmlToDocx
from docx import Document

import sys
sys.path.append(".")


html = """
<div class="item clearfix" id="_6463035_1">
<h1>Geography Teachers' Association Queensland</h1>
</div>
<div class="details">
<p>
<p>
<a href="http://gtaq.com.au/" rel="noreferrer noopener" target="_blank"><img class="W2C_IMAGE_LINK" height="130" src="GTAQ.jpg" width="239"/></a>
<input id="121330013_1_fileReadWritePermAvl" name="121330013_1_fileReadWritePermAvl" type="hidden" value="true"/>
</p>
</p>
</div>
<div class="moduleSample" id="_6463035_1previewModule">
</div>
"""

html = """
<title>Library researching and referencing for 1536QCA</title>
<br/><p class="hide">[<a href="https://bblearn-blaed.griffith.edu.au/webapps/blackboard/content/listContentEditable.jsp?content_id=_6732134_1&amp;course_id=_99031_1">Original Bb page</a>]</p>
<br/><h1>Welcome</h1>
<p><p>
<table border="1" style="border-collapse: collapse; width: 100%; border-style: none; height: 339px;">
<tbody>
<tr style="height: 351px;">
<td style="width: 50.0642%; border-style: none; height: 339px;"> <h4 id="anonymous_element_25">Welcome!</h4>
<p></p>
<p>
       This standalone module was developed by the Library to help you with your assessment.
     </p>
<p></p>
<p>
       This module covers the following topics:

<br/>
<br/>
</p>
<ul>
<li>Academic integrity
<br/>
<br/></li>
<li> <p>Searching techniques</p> </li>
<li> <p>Searching the Library Catalogue</p> </li>
<li> <p>Searching the Library databases</p> </li>
<li> <p>Searching using Google Scholar</p> </li>
<li> <p>Identifying and locating scholarly literature</p> </li>
<li> <p>Evaluating information</p> </li>
<li> <p>Referencing using Chicago (notes &amp; bibliography)</p> </li>
</ul> </td>
<td class="nowrapCell" style="width: 49.9358%; border-style: none; height: 339px;">
<br/>
<img alt="Stack of open magazines" class="W2C_IMAGE_LINK" height="255" src="magazine-806073_1920.jpg" style="border: 0px solid #000000;" width="384"/>

</td>
</tr>
</tbody>
</table>
<p>
<br/></p>
<p>
<br/></p>
<h5 id="anonymous_element_26">Adding to your employability skills</h5>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/employability.svg" style="width: 100px; height: auto; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<p>
<p>
     Researching and referencing uses several transferable skills that show your:
   </p>
<ul>
<li>Communication (attention to detail)</li>
<li>Ability to find, critically evaluate, and use information</li>
<li>Ability to act with ethical awareness and academic integrity</li>
<li>Problem solving skills (in literature searching, collecting and collating information).</li>
</ul>
</p>
</div>
<p style="text-shadow: none; box-sizing: inherit; border: 0px none; margin: 0pt 0in; padding: 0px; outline: currentcolor none 0px; font-family: 'Open Sans', sans-serif; font-size: small; line-height: normal; overflow: visible; color: #000000; text-align: left; text-indent: 0in; background-color: #fefefe; direction: ltr; unicode-bidi: embed; word-break: normal;">
<span style="text-shadow: none; box-sizing: inherit; border: 0px none; margin: 0px; padding: 0px; outline: currentcolor none 0px; font-weight: bold; font-family: Arial; font-size: 10pt; line-height: 18.6px; color: black; vertical-align: baseline;"><a href="https://www.griffith.edu.au/employability" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732135_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fwww.griffith.edu.au%2Femployability';" style="text-shadow: none; box-sizing: inherit; border: 0px none; margin: 0px; padding: 0px; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; color: #8c2f2f; text-decoration: underline; line-height: 18.6px;">Employability - Griffith University</a> </span>
</p>
<p style="text-shadow: none; box-sizing: inherit; border: 0px none; margin: 0pt 0in; padding: 0px; outline: currentcolor none 0px; font-family: 'Open Sans', sans-serif; font-size: small; line-height: normal; overflow: visible; color: #000000; text-align: left; text-indent: 0in; background-color: #fefefe; direction: ltr; unicode-bidi: embed; word-break: normal;">

</p>
<p style="text-shadow: none; box-sizing: inherit; border: 0px none; margin: 0pt 0in; padding: 0px; outline: currentcolor none 0px; font-family: 'Open Sans', sans-serif; font-size: small; line-height: normal; overflow: visible; color: #000000; text-align: left; text-indent: 0in; background-color: #fefefe; direction: ltr; unicode-bidi: embed; word-break: normal;">

</p>
<p style="text-shadow: none; box-sizing: inherit; border: 0px none; margin: 0pt 0in; padding: 0px; outline: currentcolor none 0px; font-family: 'Open Sans', sans-serif; font-size: small; line-height: normal; overflow: visible; color: #000000; text-align: left; text-indent: 0in; background-color: #fefefe; direction: ltr; unicode-bidi: embed; word-break: normal;">
<p>
<br/></p>

</p>
<p style="text-shadow: none; box-sizing: inherit; border: 0px none; margin: 0pt 0in; padding: 0px; outline: currentcolor none 0px; font-family: 'Open Sans', sans-serif; font-size: small; line-height: normal; overflow: visible; color: #000000; text-align: left; text-indent: 0in; background-color: #fefefe; direction: ltr; unicode-bidi: embed; word-break: normal;">
<p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/more-information.svg" style="width: 70px; height: auto; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p>
<div style="overflow: hidden;">
<p>If you are still not sure what to do after working through this tutorial, you should:</p>
<ul style="list-style-type: disc;">
<li style="list-style-type: square;">Contact a member of the teaching team if your questions are specifically about the content of your assignment</li>
<li style="list-style-type: square;"><a href="https://intranet.secure.griffith.edu.au/library/forms/help" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732135_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fintranet.secure.griffith.edu.au%2Flibrary%2Fforms%2Fhelp';">Get help from the Library</a> - a Librarian can assist with research and referencing and a Learning Adviser can assist with assignment writing</li>
<li style="list-style-type: square;">Refer to the <a href="https://www.griffith.edu.au/library/study" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732135_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fwww.griffith.edu.au%2Flibrary%2Fstudy';">Library Study pages</a></li>
<li style="list-style-type: square;">Access <a href="https://www2.griffith.edu.au/library/study/smarthinking" rel="noopener" target="_blank">Smarthinking</a>, a free online tutoring service, for help with planning, preparing or writing your assignment</li>
</ul>
</div>

</p>
</p></p>
<h1>Academic integrity</h1>
<p><p>
<h4 id="anonymous_element_28">Academic integrity</h4>
<p>Academic integrity is about being honest, respectful and fair in your academic work. An example of acting with academic integrity is to correctly reference your work, which shows you are being honest about where the information or idea came from and respectful of the author of the work you are citing.</p>
<p>To understand more about what academic integrity is, why it is important and the University's policies on academic integrity you can complete the <a href="https://www.griffith.edu.au/academic-integrity#tutorial" rel="noopener" target="_blank">Academic Integrity Student Tutorial</a>.</p>
<p>
<br/>
<a href="https://www.griffith.edu.au/academic-integrity#tutorial" rel="noopener" target="_blank"><img alt="Screenshot of Academic integrity student tutorial. " class="W2C_IMAGE_LINK" height="229" src="Academic integrity tutorial.png" style="border: 0px solid #000000;" width="546"/></a>

<br/> </p>
</p></p>
<h1>Creating a search statement</h1>
<p><p>
<h4 id="anonymous_element_30">Creating a search statement</h4>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 1em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: 400; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: small; line-height: 20.15px; position: relative; overflow: visible; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #fefefe; text-decoration-style: initial; text-decoration-color: initial;"><span style="font-size: 10pt;">A search statement is the combination of keywords that will be entered into the search box of the Library Catalogue, databases, or Google Scholar.</span></p>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 1em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: 400; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: small; line-height: 20.15px; position: relative; overflow: visible; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #fefefe; text-decoration-style: initial; text-decoration-color: initial;"><span style="font-size: 10pt;"><span style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; line-height: 20.15px;">Start by identifying the topic words in your assignment task. Check out the <a href="https://www.griffith.edu.au/library/study/prepare-assignments/understand-your-assessment" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732137_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fwww.griffith.edu.au%2Flibrary%2Fstudy%2Fprepare-assignments%2Funderstand-your-assessment';">Understand your assessment</a> information on the Library Study pages for help with identifying these. You will also need to think of any alternative words for your topic words (such as synonyms or different spellings). The topic words and alternative words will all be the keywords in your search statement. Use the techniques below to put these words together into an effective search statement.
<br/>
<br/><span style="text-shadow: none; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; line-height: 20.15px;">Some common search techniques used when creating a search statement include:</span> </span></span></p>
<h6 id="anonymous_element_31">Phrase Searching:</h6>
<p><span style="font-size: 10pt;"><strong></strong><span style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; line-height: 20.15px;">Use quotation marks around words to search for the words in that order.  Instead of searching for the word 'global' and the word 'warming' it will search for "global warming".</span></span></p>
<p><span style="font-size: 10pt;"><span style="color: #000000;"><strong><span style="margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-style: inherit; font-family: inherit; line-height: 20.15px; text-shadow: none; letter-spacing: normal;">"global warming"
<br/>
<br/>"artificial intelligence" </span></strong></span></span></p>

<p><span style="font-size: 10pt; color: #000000;"><strong><span style="margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-style: inherit; font-family: inherit; line-height: 20.15px; text-shadow: none; letter-spacing: normal;">"Mona Lisa"</span></strong></span></p>

<h6 id="anonymous_element_32"></h6>
<h6 id="anonymous_element_33">Truncation:</h6>
<p><span style="font-size: 10pt;"><strong></strong>When adding an asterisk onto the end of a word, the search will come back with the word plus any letters that can appear afterwards.  In this example, results will include design, designs, designing, designer etc.</span></p>
<p><span style="font-size: 10pt; color: #000000;"><strong>design*</strong></span></p>
<h6 id="anonymous_element_34"></h6>

<h6 id="anonymous_element_35">Boolean Operations:</h6>
<h6 id="anonymous_element_36"></h6>
<p><span style="font-size: 10pt;"><strong style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: bold; font-style: normal; font-family: 'Open Sans', sans-serif; line-height: 20.15px; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #fefefe; text-decoration-style: initial; text-decoration-color: initial;"></strong>Boolean operations are a great way to join keywords together and create a search strategy.  Click on the information symbol below to read more about Boolean operations.</span></p>
<div style="max-width: 540px;">
<p><p class="embed">&lt;iframe allowfullscreen="" data-mce-fragment="1" frameborder="0" height="360" src="https://griffith.h5p.com/content/1290721737060288219/embed" style="font-size: small;" width="540"&gt;&lt;/iframe&gt;</p></p>
<span style="font-size: 10pt;"> </span>
</div>
<div style="max-width: 540px;"></div>
<div style="max-width: 540px;"></div>
<h6 id="anonymous_element_37"></h6>
<h6 id="anonymous_element_38"><span style="font-size: 10pt;"><strong open="" sans="" sans-serif="">Example search statements:</strong></span></h6>
<p><span style="font-size: 10pt;">To search for information about the impact of artificial intelligence on design, designs or designing, the following search statement could be used:
<br/>
<br/><span style="color: #000000;"><strong>("artificial intelligence" OR AI) AND design*</strong></span>
<br/></span></p>
<p>
<br/>To search for information about sustainability and public art the following search statement could be used:
<br/>
<br/><strong>"public art" AND sustainab*</strong> </p>

<h6 id="anonymous_element_39" style="overflow: hidden;">Activity - create your search statement</h6>
<div style="overflow: hidden;">
<p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/activity.svg" style="width: 70px; height: auto; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p>
<div style="overflow: hidden;">
<p>Let's create your search statement to use in the Library catalogue, databases and Google Scholar.</p>
<p>1. Analyse your assignment question or task - what are the main topics/keywords? Are there any alternate words or spellings you could also include?</p>
<p>2. Apply the phrase searching and truncation techniques as needed.</p>
<p>3. Join your keywords and alternate words or spellings together by using the Boolean operators AND/OR. Remember to place keywords separated by OR into brackets.</p>
</div>
</div>
<p>You can now start using your search statement to find resources for your assignment. As you search you may find you need to modify your search statement by removing or adding keywords to find the most relevant results for your topic.</p>
<p>
<br/></p>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/more-information.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">
<h6 id="anonymous_element_40" style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 0.7em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: bold; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: 16.9px; line-height: 26.195px; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgba(254, 254, 254, 0.61); text-decoration-style: initial; text-decoration-color: initial;"><span style="font-size: 10pt;"><strong>Further information</strong></span></h6>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 1em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: 400; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: small; line-height: 20.15px; position: relative; overflow: visible; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgba(254, 254, 254, 0.61); text-decoration-style: initial; text-decoration-color: initial;"><span style="font-size: 10pt;"><span style="background-color: rgba(254, 254, 254, 0.61); color: #000000; font-family: 'Open Sans', sans-serif; font-style: normal; font-weight: 400;">Additional resources for this section that may be of use to you:</span></span></p>
<ul>
<li style="text-shadow: none; letter-spacing: normal; border: 0px none; outline: currentcolor none 0px; font-weight: 400; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: small; line-height: 20.15px; position: relative; overflow: visible; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgba(254, 254, 254, 0.61); text-decoration-style: initial; text-decoration-color: initial;"><a href="https://www.griffith.edu.au/library/study/prepare-assignments/prepare-to-search" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732137_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fwww.griffith.edu.au%2Flibrary%2Fstudy%2Fprepare-assignments%2Fprepare-to-search';">Prepare to search</a></li>
</ul>
</div>
</div>
</p></p>
<h1>Searching the Library catalogue</h1>
<p><p>
<h4 id="anonymous_element_42">Searching the Library catalogue</h4>
<p>Through the Library catalogue search box you will be able to find and access the majority of library resources, available either online 24/7 or physically on our shelves. Watch the video or view the transcript to find out how to use the Library catalogue effectively including how to search, use the refinements and save and email search results.</p>
<p>
<br/></p>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/video.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">

<p><span style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 10pt; line-height: 20.15px;">The following video from the Library gives you a click-by-click demonstration on how to search the Library Catalogue efficiently and effectively.</span></p>
<p>
<br/></p>
<p>
<br/></p>
</div>
<p><p class="embed">&lt;iframe allow="autoplay; fullscreen; picture-in-picture" allowfullscreen="" frameborder="0" height="360" src="https://player.vimeo.com/video/366398938" width="640"&gt;&lt;/iframe&gt;</p></p>
</div>
<div style="overflow: hidden;"></div>
<div style="overflow: hidden;">
<p><span style="color: #000000; font-family: 'Open Sans', sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-style: initial; text-decoration-color: initial; display: inline; float: none;">You can download the transcript:</span><br style="text-shadow: none; letter-spacing: normal; line-height: 20.15px; color: #000000; font-family: 'Open Sans', sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-style: initial; text-decoration-color: initial;"/>
<br/>
<span class="canvasFileLink">2022-T1_LibraryCatalogueTranscript-VisualAndCreativeArts.pdf</span>

<br/> 
<br/></p>
</div>
</p></p>
<h1>Searching the Library databases</h1>
<p><p>
<p>
<p>
<h4 id="anonymous_element_44">Searching the Library databases</h4>
</p>
</p>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/video.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p> <span style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; line-height: 20.15px;">
<br/>The following video from the Library gives you a click-by-click demonstration on how to use the Visual and creative arts library guides to locate subject specific scholarly resources. </span></span>
</div>
<div style="max-width: 400px;">
<p><p class="embed">&lt;iframe allow="autoplay; fullscreen" allowfullscreen="" data-mce-fragment="1" frameborder="0" height="360" src="https://player.vimeo.com/video/366660011" width="640"&gt;&lt;/iframe&gt;</p></p>
<span style="font-size: 10pt;"> </span>
</div>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: 400; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: 10pt; line-height: 20.15px; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial; background-color: #ffffff; float: none; display: inline;">You can download the transcript:</span></p>
<p><span style="font-size: 10pt;"><span style="color: #000000; font-family: 'Open Sans', sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-style: initial; text-decoration-color: initial; display: inline; float: none;">
<br/>
<span class="canvasFileLink">2022-T1_VisualArtsDatabasesTranscript.pdf</span>

<br/> 
<br/>
<br/></span> Reference databases contain subject specific information such as definitions, terms, timelines, and artist and works information. You may like to consider using the following reference databases : </span></p>
<ul>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; display: list-item; list-style-position: outside; list-style-type: inherit; line-height: 20.15px;"><a href="https://www-oxfordreference-com.libraryproxy.griffith.edu.au/" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732139_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fwww-oxfordreference-com.libraryproxy.griffith.edu.au%2F';"><span style="font-size: 10pt;">Oxford Reference</span></a></li>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; display: list-item; list-style-position: outside; list-style-type: inherit; line-height: 20.15px;"><span style="font-size: 10pt;"><a href="https://www-oxfordartonline-com.libraryproxy.griffith.edu.au/" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732139_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fwww-oxfordartonline-com.libraryproxy.griffith.edu.au%2F';">Oxford Art Online</a></span></li>
</ul>

<p><span style="font-size: 10pt;">You may like to consider using the following <a href="https://libraryguides.griffith.edu.au/c.php?g=540282&amp;p=6849652" rel="noopener" target="_blank">Library databases</a> to locate scholarly literature such as journal articles, conference papers, and theses:</span></p>
<ul>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; display: list-item; list-style-position: outside; list-style-type: inherit; line-height: 20.15px;"><span style="font-size: 10pt;">Art Full Text</span></li>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; display: list-item; list-style-position: outside; list-style-type: inherit; line-height: 20.15px;"><span style="font-size: 10pt;">Taylor and Francis Journals</span></li>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; display: list-item; list-style-position: outside; list-style-type: inherit; line-height: 20.15px;"><span style="font-size: 10pt;">JSTOR</span></li>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; display: list-item; list-style-position: outside; list-style-type: inherit; line-height: 20.15px;"><span style="font-size: 10pt;">ProQuest</span></li>
</ul>
</p></p>
<h1>Search using Google Scholar</h1>
<p><p>
<div style="overflow: hidden;">
<div style="overflow: hidden;">
<h4 id="anonymous_element_46">Search using Google Scholar</h4>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/video.svg" style="width: 69px; height: 60px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">
<p><span style="font-size: 10pt;">
<br/>The following video from the Library explains the value of Google Scholar and gives you a click-by-click demonstration on how to search Google Scholar and set up Fulltext@Griffith links to access content via Griffith Library suscriptions.</span></p>
</div>
</div>
</div>
</div>
<div style="max-width: 400px;">
<p><p class="embed">&lt;iframe allow="autoplay; fullscreen" allowfullscreen="" data-mce-fragment="1" frameborder="0" height="360" src="https://player.vimeo.com/video/438747401" width="640"&gt;&lt;/iframe&gt;</p></p>
</div>

<p style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="color: #000000; font-family: 'Open Sans', sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-style: initial; text-decoration-color: initial; display: inline; float: none;">You can download the video and transcript:</span><br style="text-shadow: none; letter-spacing: normal; line-height: 20.15px; color: #000000; font-family: 'Open Sans', sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-style: initial; text-decoration-color: initial;"/><span style="color: #000000; font-family: 'Open Sans', sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-style: initial; text-decoration-color: initial; display: inline; float: none;"><a href="https://vimeo.com/user82369617/download/438747401/2e9a69c40f" rel="noreferrer noopener" target="_blank" title="Search using Google Scholar">Search using Google Scholar (VIDEO)</a></span></p>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;">
<span class="canvasFileLink">Search using Google Scholar (TRANSCRIPT-pdf)</span>

</p>


<h6 id="anonymous_element_47" style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 0.7em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: bold; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: 16.9px; line-height: 26.195px; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgba(254, 254, 254, 0.61); text-decoration-style: initial; text-decoration-color: initial;"><span style="font-size: 10pt;">Further Information</span></h6>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/more-information.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">
<span style="background-color: #fefefe; font-family: 'Open Sans', sans-serif; font-size: 10pt; font-style: normal; font-weight: 400;">Additional resources for this section that may be of use to you:</span>

</div>
<ul>
<li><span style="text-decoration: underline; font-size: 10pt;"><span style="color: #993300;"><span style="letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: normal; font-style: normal; font-family: 'Open Sans', sans-serif; line-height: 20.15px; color: #993300; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; float: none; text-shadow: none; display: inline; text-decoration: underline;"><a href="https://studenthelp.secure.griffith.edu.au/app/answers/detail/a_id/3033/kw/Google%20scholar" rel="noopener" target="_blank"><span style="color: #000000; text-decoration: underline;">How do I setup Google <span>Scholar</span> to access Griffith full-text articles?</span></a></span></span></span></li>
</ul>
</div>
</p></p>
<h1>Identifying scholarly literature</h1>
<p><p>
<h4 id="anonymous_element_49">Identifying scholarly literature</h4>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 1em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: 400; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: small; line-height: 20.15px; position: relative; overflow: visible; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #fefefe; text-decoration-style: initial; text-decoration-color: initial;"><span style="font-size: 10pt;">Your assessment should contain high quality, scholarly sources of information. Scholarly literature contains in-depth research and/or analysis and is written by academics, scholars and researchers. It is mostly found in journals, books, conference papers, theses, and reports.</span></p>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/video.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">
<p style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="font-size: 10pt;">The following video from the Library explains how to identify scholarly literature.</span></p>
</div>
</div>
<div style="max-width: 400px;">
<p><p class="embed">&lt;iframe allow="autoplay; fullscreen" allowfullscreen="" data-mce-fragment="1" frameborder="0" height="360" src="https://player.vimeo.com/video/340604311?texttrack=en" style="font-size: 13px;" width="640"&gt;&lt;/iframe&gt;</p></p>
</div>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 1em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: 400; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: small; line-height: 20.15px; position: relative; overflow: visible; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #fefefe; text-decoration-style: initial; text-decoration-color: initial;">You can download the video and transcript:
<br/><a href="https://vimeo.com/user82369617/download/340604311/30028400c1" rel="noreferrer noopener" target="_blank">Scholarly and peer reviewed journal articles (VIDEO)</a>
<br/><a href="https://griffitheduau.sharepoint.com/:b:/s/LearningObjectsLibrary/EYKJm9CyQX1MtJ16FNcHKuUBuBV-zPN5xiCIa3hf_lqWSA" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732141_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fgriffitheduau.sharepoint.com%2F%3Ab%3A%2Fs%2FLearningObjectsLibrary%2FEYKJm9CyQX1MtJ16FNcHKuUBuBV-zPN5xiCIa3hf_lqWSA';">Scholarly and peer reviewed journal articles (TRANSCRIPT - PDF)</a></p>
<p><span style="font-size: 10pt;">You may like to consider using the following sources to locate scholarly literature:</span></p>
<ul>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="font-size: 10pt;">the <a href="https://www.griffith.edu.au/library" rel="noopener" target="_blank">Library Catalogue</a></span></li>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="font-size: 10pt;">library databases; primary sources; websites listed in the <a href="https://libraryguides.griffith.edu.au/arts-guides" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732141_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Flibraryguides.griffith.edu.au%2Farts-guides';">Visual and creative arts library guides</a></span></li>
<li style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="font-size: 10pt;"><a href="https://scholar.google.com.au/" rel="noopener" target="_blank">Google Scholar</a></span></li>
</ul>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="font-size: 10pt;">For further information about using these sources refer to the relevant sections of this module.</span></p>
<h6 id="anonymous_element_50" style="text-shadow: none; letter-spacing: normal; margin: 0px 0px 0.7em; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: bold; font-style: normal; font-family: 'Open Sans', sans-serif; font-size: 16.9px; line-height: 26.195px; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgba(254, 254, 254, 0.61); text-decoration-style: initial; text-decoration-color: initial;"><span style="font-size: 10pt;">Further information</span></h6>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/more-information.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<p><span style="font-size: 10pt;">Additional resources for this section that may be of use to you:</span></p>
<ul>
<li><span style="font-size: 10pt;"><a href="https://www.griffith.edu.au/library/study/prepare-assignments/evaluate-sources" rel="noopener" target="_blank">Evaluate your sources</a></span></li>
</ul>
</div>
</p></p>
<h1>Evaluating information</h1>
<p><p>
<h4 id="anonymous_element_52">Evaluating information</h4>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/reading.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<p><span style="font-size: 10pt;">You will need to use your critical thinking skills to evaluate whether a source is suitable to use. Here are five factors to consider before you include a source of information in your assignment. <span style="font-size: 13px;">Click on the + to find out more information on evaluating your sources.</span> </span></p>
</div>
<div style="max-width: 800px;">
<p><p><p class="embed">&lt;iframe allow="geolocation *; microphone *; camera *; midi *; encrypted-media *" allowfullscreen="" data-mce-fragment="1" frameborder="0" height="360" src="https://griffith.h5p.com/content/1290699402263054719/embed" style="font-size: 13px;" width="640"&gt;&lt;/iframe&gt;</p></p></p>
</div>
<p style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;">You can
<span class="canvasFileLink">download the text version.</span>

<br/> </p>
<h6 id="anonymous_element_53" style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"></h6>
<h6 id="anonymous_element_54">Further information</h6>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/more-information.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">
<p style="text-shadow: none; letter-spacing: normal; margin: 0px; padding: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit;"><span style="font-size: 10pt;">Additional resources for this section that may be of use to you:</span></p>
<ul>
<li><a href="https://www.open.ac.uk/library/help-and-support/advanced-evaluation-using-prompt" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732142_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=https%3A%2F%2Fwww.open.ac.uk%2Flibrary%2Fhelp-and-support%2Fadvanced-evaluation-using-prompt';">Evaluation using PROMPT</a></li>
<li><a href="http://blog.efpsa.org/2011/08/01/how-to-critically-evaluate-the-quality-of-a-research-article/" onclick="this.href='/webapps/blackboard/content/contentWrapper.jsp?content_id=_6732142_1&amp;displayName=Linked+File&amp;navItem=content&amp;attachment=true&amp;course_id=_99031_1&amp;tab_group=courses&amp;href=http%3A%2F%2Fblog.efpsa.org%2F2011%2F08%2F01%2Fhow-to-critically-evaluate-the-quality-of-a-research-article%2F';"><span style="font-size: 10pt;">How to critically evaluate the quality of a research article?</span></a></li>
</ul>
</div>
</div>
</p></p>
<h1>Referencing - why do we reference?</h1>
<p><p>
<h4 id="anonymous_element_8">Why do we reference?</h4>
<p>
   Referencing is a part of assessment writing. Using the research of others to build and support concepts, ideas and arguments in your assignment, provides credibility to your work. It also allows the marker of your paper to know that you have accessed experts in your field of knowledge.
 </p>
<p></p>
<p>
   Referencing allows you to clearly and consistently acknowledge all the information sources you have used in your assessment. By doing this, you also avoid plagiarism, which means to use the words or ideas of others as your own. Avoiding plagiarism maintains
  <a href="https://www.griffith.edu.au/academic-integrity" rel="noopener" target="_blank">academic integrity</a>.
 </p>
<p></p>
<p></p>
<p>
<img alt="Part of academic writing, support your work, avoid plagiarism, enables you to find those resources next time." class="W2C_IMAGE_LINK" height="255" src="Why reference(3).PNG" style="border: 0px solid #000000;" width="563"/>

<br/> 
 </p>
<p></p>
<p>
   Contact a member of the teaching team of your course for more guidance or refer to the Library 
  <a href="https://www.griffith.edu.au/library/study" rel="noopener" target="_blank">self-help resources</a>.
 </p>
</p></p>
<h1>Referencing - what do we reference?</h1>
<p><p>
<h4 id="anonymous_element_57">What do we reference?</h4>
<ul>
<li class="vtbegenerated_div">Words: e.g. direct quotes (exact copy of original text) </li>
<li class="vtbegenerated_div">Ideas: e.g. definitions, ideas, creative works, expert opinion</li>
<li class="vtbegenerated_div">Information: e.g. statistics, research results, facts that are <strong>not</strong> “common knowledge”</li>
</ul>
<p>
<strong>NOTE</strong>: 'Common knowledge' is difficult to define, as what may be common knowledge in one area of study may not in another i.e. what most people in a particular field would be expected to know, and which has the status of established fact.
 </p>

<p>
<p><span style="font-size: 10pt;">You do not need to reference:</span></p>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit; text-shadow: none;"><span style="font-size: 10pt;">Your own original ideas
<br/></span></li>
<li style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; border: 0px none; outline: currentcolor none 0px; font-weight: inherit; font-style: inherit; font-family: inherit; font-size: 13px; line-height: 20.15px; display: list-item; list-style-position: outside; list-style-type: inherit; text-shadow: none;"><span style="font-size: 10pt;">Your reflections </span></li>
</ul> </li>
</ul>
</p>
<p>
   If you haven't referenced a particular point, the implication is that you are claiming the idea as your own.
 </p>


<p>
<img alt="Do need to reference: direct quotes, paraphrasing, facts and figures. Don't need to reference: common knowledge, your own original ideas, your reflections. " class="W2C_IMAGE_LINK" height="257" src="What do we reference(3).PNG" style="border: 0px solid #000000;" width="557"/>

<br/>
<br/>
</p>
</p></p>
<h1>Referencing - how do we reference?</h1>
<p><p>
<h4 id="anonymous_element_10">How do we reference?</h4>
<p>
   As you research for your assignment you will need to collect four pieces of information:
  <strong>Who</strong>,
  <strong>When</strong>,
  <strong>What</strong> and
  <strong>Where</strong>?
 </p>
<p>
   This video explains the
  <strong>Who</strong>,
  <strong>When</strong>,
  <strong>What</strong> and
  <strong>Where</strong> of referencing.
 </p>

<p>
<p><p class="embed">&lt;iframe allow="autoplay; fullscreen" allowfullscreen="" data-mce-fragment="1" frameborder="0" height="240" src="https://player.vimeo.com/video/486627170" width="426"&gt;&lt;/iframe&gt;</p></p>
</p>
<p>
   You can download the video and transcript:
 </p>
<ul>
<li><a href="https://vimeo.com/user82369617/download/486627170/21593e3dc9" rel="noopener" target="_blank">Referencing the Four Ws (VIDEO)</a></li>
<li><a href="https://griffitheduau.sharepoint.com/sites/LearningObjectsLibrary/LearningObjects/Forms/AllItems.aspx?id=%2Fsites%2FLearningObjectsLibrary%2FLearningObjects%2FBusiness%2FBusiness%20General%2F2020%5FTranscripts%2F2020%5FReferencing%2DWho%2DWhen%2DWhat%2DWhere%281%29%2Epdf&amp;parent=%2Fsites%2FLearningObjectsLibrary%2FLearningObjects%2FBusiness%2FBusiness%20General%2F2020%5FTranscripts&amp;p=true&amp;ct=1611288991380&amp;or=OWA-NT&amp;cid=a44ff91b-3c35-90f3-4df1-2d1a71948fbf&amp;originalPath=aHR0cHM6Ly9ncmlmZml0aGVkdWF1LnNoYXJlcG9pbnQuY29tLzpiOi9zL0xlYXJuaW5nT2JqZWN0c0xpYnJhcnkvRWFuLXVJZkViRVJEai0yNFRYQXVya3dCa2ZCWHdQaENlUzJnck5GNzdHTDNndz9ydGltZT11QXpzZjR5LTJFZw" rel="noopener" target="_blank">Referencing the Four Ws (PDF 57KB)</a></li>
</ul>
<p>
<br/></p>

<p>
   Once you have gathered these four pieces of information you can create a reference. A reference consists of two parts:
 </p>
<ul>
<li>the <strong>citation (in-text)</strong> which is a shortcut to the full information in the reference list</li>
<li>the <strong>reference list</strong>.</li>
</ul>
<p>
   How you go about creating your references depends on the
  <strong>referencing style</strong> you are required to use.
 </p>
</p></p>
<h1>Referencing using Chicago 17 (Notes &amp; Bibliography)</h1>
<p><p>
<h4 id="anonymous_element_60">Referencing using Chicago 17 (Notes &amp; Bibliography)</h4>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/video.svg" style="width: 68px; height: 60px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p> </span>
<br/>
<span style="font-size: 10pt;">The following video from the Library explains how to create in-text references using Chicago 17 Notes &amp; Bibliography style. </span>
</div>
<p><p><p class="embed">&lt;iframe allow="autoplay; fullscreen" allowfullscreen="" data-mce-fragment="1" frameborder="0" height="360" src="https://player.vimeo.com/video/413798067" width="640"&gt;&lt;/iframe&gt;</p></p></p>
<p><span style="font-size: 10pt;">You can download the video: </span></p>
<p><span style="font-size: 10pt;"><a href="https://vimeo.com/user82369617/download/413798067/f761eb96db" rel="noreferrer noopener" target="_blank">Creating in-text references using the Chicago 17 Notes &amp; Bibliography referencing style (VIDEO)</a></span></p>
<p>
<br/></p>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/video.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">
<p><span style="font-size: 10pt;">
<br/>The following video from the Library explains how to create bibliography entries using Chicago 17 Notes &amp; Bibliography style.</span></p>
</div>
</div>
<p><p><p class="embed">&lt;iframe allow="autoplay; fullscreen" allowfullscreen="" data-mce-fragment="1" frameborder="0" height="360" src="https://player.vimeo.com/video/413862967" width="640"&gt;&lt;/iframe&gt;</p></p></p>
<p><span style="font-size: 10pt;">You can download the video: </span></p>
<p><span style="font-size: 10pt;"><a href="https://vimeo.com/user82369617/download/413862967/00309ed5e4" rel="noreferrer noopener" target="_blank">Creating a bibliography using the Chicago 17 Notes &amp; Bibliography referencing style (VIDEO) </a></span></p>
<p>
<br/></p>
<div style="overflow: hidden;">
<span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/web-link.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span>
<div style="overflow: hidden;">

<ul>
<li><span style="font-size: 10pt;">The <a href="https://www.griffith.edu.au/library/study/referencing" rel="noreferrer noopener" target="_blank">Referencing guides</a> on the Library website provide examples of citations and reference list/bibliography entries.</span></li>
<li><span style="font-size: 10pt;">The Chicago Manual of Style website contains <a href="https://www.chicagomanualofstyle.org/tools_citationguide.html" rel="noreferrer noopener" target="_blank">quickguides</a> with instructions and examples for creating footnotes and reference lists/bibliographies.</span></li>
<li>Learn <a href="https://support.office.com/en-us/article/Insert-footnotes-and-endnotes-61f3fb1a-4717-414c-9a8f-015a5f3ff4cb" rel="noopener" target="_blank">how to insert footnotes and endnotes in Word for Office 365, Word 2019/2016/2013/2010/2007</a>.</li>
</ul>
</div>
</div>
<p>
<br/></p>
<h6 id="anonymous_element_9">Further information</h6>
<div style="overflow: hidden;">
<p><span style="font-size: 10pt;"><p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/more-information.svg" style="width: 69px; height: 61px; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p></span></p>
<p><span style="font-size: 10pt;">Additional resources for this section that may be of use to you:</span></p>
<ul>
<li><span style="font-size: 10pt;"><a href="http://librarycatalogue.griffith.edu.au/record=b2449685" rel="noreferrer noopener" target="_blank">Print copies</a> of The Chicago Manual of Style in the Library and at the QCA Library Desk</span></li>
</ul>
</div>
<p>
<br/></p>
<p><span style="font-size: 10pt;">If you are still not sure what type of referencing style is required to satisfy your assessment question or how to use it after working through this page, you should contact a member of the teaching team of your course for more guidance, or refer to the Library <a href="https://www.griffith.edu.au/library/study" rel="noreferrer noopener" target="_blank">self-help resources</a>.</span></p>
</p></p>
<h1>Feedback</h1>
<p><p>
<h4 id="anonymous_element_62" style="overflow: hidden;">Feedback</h4>
<div style="overflow: hidden;">
<p><p class="embed">&lt;img src="https://app.secure.griffith.edu.au/gois/ultra/icons-regular/reflection-activity.svg" style="width: 70px; height: auto; float: left; margin: 0px 10px 10px 0px;"/&gt;</p></p>
<div style="overflow: hidden;">
<p>
<br/></p>
<p>Please give us your feedback by completing this <a href="https://prodsurvey.rcs.griffith.edu.au/prodls200/index.php/43245?lang=en" rel="noopener" target="_blank">short </a><a href="https://prodsurvey.rcs.griffith.edu.au/prodls200/index.php/43245?lang=en" rel="noopener" target="_blank">survey</a>.</p>
</div>
</div>
</p></p>

"""

fred =""" 
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
    "h1": {
        "canvasFile": 'Canvas File',
        "canvasSubHeader": 'Canvas SubHeader',
        "canvasDiscussion": 'Canvas Discussion',
        "canvasQuiz": 'Canvas Quiz',
        "canvasAssignment": 'Canvas Assignment',
        "canvasExternalTool": 'Canvas External Tool',
        'canvasExternalUrl': 'Canvas External Url',
    },
    "p": {
        "embed": 'Embed',
        "hide": "Hide",
        "canvasFileLink": 'Canvas File Link'
    },
    "span": {
        "embed": 'Embed',
        "hide": "Hide",
        "canvasFileLink": 'Canvas File Link'
    }
}

# Start with a blank Word doc that has the Word styles
# from above defined
document = Document('C:\\Users\\s2986288\\code\\Example.docx')

# create the parser and point to the style map
new_parser = HtmlToDocx()
new_parser.style_map = STYLE_MAP

new_parser.add_html_to_document(html, document)

document.save('dev.docx')
