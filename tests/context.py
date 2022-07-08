import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.parse.article import Article

# the pretty-print versions allow for easier inspection but include additional spaces that affect the tests
# the real-world use-cases use the unstructured HTML string, so that is what should be imported for tests

# corresponds to: https://en.wikipedia.org/w/index.php?title=Mike_Potts&oldid=1052159182
# disambiguation page
example_html_one = '<!DOCTYPE html>\n<html prefix="dc: http://purl.org/dc/terms/ mw: http://mediawiki.org/rdf/" about="https://en.wikipedia.org/wiki/Special:Redirect/revision/1052159182"><head prefix="mwr: https://en.wikipedia.org/wiki/Special:Redirect/"><meta property="mw:TimeUuid" content="cd159e50-bc7e-11ec-9de6-11b7fdafb6ee"/><meta charset="utf-8"/><meta property="mw:pageId" content="31967453"/><meta property="mw:pageNamespace" content="0"/><link rel="dc:replaces" resource="mwr:revision/874370476"/><meta property="mw:revisionSHA1" content="aef8e32baa25d08f9f482936208ec4533406f5b8"/><meta property="dc:modified" content="2021-10-27T18:20:34.000Z"/><meta property="mw:htmlVersion" content="2.4.0"/><meta property="mw:html:version" content="2.4.0"/><link rel="dc:isVersionOf" href="//en.wikipedia.org/wiki/Mike_Potts"/><base href="//en.wikipedia.org/wiki/"/><title>Mike Potts</title><link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=mediawiki.skinning.content.parsoid%7Cmediawiki.skinning.interface%7Csite.styles&amp;only=styles&amp;skin=vector"/><meta http-equiv="content-language" content="en"/><meta http-equiv="vary" content="Accept"/></head><body id="mwAA" lang="en" class="mw-content-ltr sitedir-ltr ltr mw-body-content parsoid-body mediawiki mw-parser-output" dir="ltr"><section data-mw-section-id="0" id="mwAQ"><p id="mwAg"><b id="mwAw">Mike</b> or <b id="mwBA">Michael Potts</b> may refer to:</p>\n<ul id="mwBQ"><li id="mwBg"><a rel="mw:WikiLink" href="./Michael_Potts_(actor)" title="Michael Potts (actor)" id="mwBw">Michael Potts (actor)</a>, American actor</li>\n<li id="mwCA"><a rel="mw:WikiLink" href="./Michael_Potts_(footballer)" title="Michael Potts (footballer)" id="mwCQ">Michael Potts (footballer)</a> (born 1991), English footballer</li>\n<li id="mwCg"><a rel="mw:WikiLink" href="./Mike_Potts_(baseball)" title="Mike Potts (baseball)" id="mwCw">Mike Potts (baseball)</a> (born 1970), former left-handed Major League Baseball relief pitcher</li>\n<li id="mwDA"><a rel="mw:WikiLink" href="./Mike_Potts_(American_football)" title="Mike Potts (American football)" id="mwDQ">Mike Potts (American football)</a> (born 1985), American football quarterback</li>\n<li id="mwDg"><a rel="mw:WikiLink" href="./Michael_Potts_(diplomat)" title="Michael Potts (diplomat)" id="mwDw">Michael Potts (diplomat)</a>, Australian diplomat</li></ul>\n\n<style data-mw-deduplicate="TemplateStyles:r1008001242" typeof="mw:Extension/templatestyles mw:Transclusion" about="#mwt1" data-mw=\'{"parts":[{"template":{"target":{"wt":"hndis","href":"./Template:Hndis"},"params":{"1":{"wt":"Potts, Mike"}},"i":0}}]}\' id="mwEA">.mw-parser-output .dmbox{display:flex;align-items:center;clear:both;margin:0.9em 1em;border-top:1px solid #ccc;border-bottom:1px solid #ccc;padding:0.25em 0.35em;font-style:italic}.mw-parser-output .dmbox>*{flex-shrink:0;margin:0 0.25em;display:inline}.mw-parser-output .dmbox-body{flex-grow:1;flex-shrink:1;padding:0.1em 0}</style><span about="#mwt1">\n</span><div role="note" id="_disambigbox" class="metadata plainlinks dmbox \ndmbox-disambig " about="#mwt1"><span typeof="mw:Image"><a href="./File:Disambig_gray.svg" class="mw-file-description"><img alt="Disambiguation icon" resource="./File:Disambig_gray.svg" src="//upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/30px-Disambig_gray.svg.png" decoding="async" data-file-width="220" data-file-height="168" data-file-type="drawing" height="23" width="30" srcset="//upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/45px-Disambig_gray.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/60px-Disambig_gray.svg.png 2x"/></a></span><div class="dmbox-body"> <div class="shortdescription nomobile noexcerpt noprint searchaux" style="display:none">Topics referred to by the same term</div><link rel="mw:PageProp/Category" href="./Category:Disambiguation_pages_with_short_descriptions"/><link rel="mw:PageProp/Category" href="./Category:Short_description_is_different_from_Wikidata"/>This <a rel="mw:WikiLink" href="./Help:Disambiguation" title="Help:Disambiguation">disambiguation</a> page lists articles about people with the same name. <br/><small>If an <a rel="mw:ExtLink" href="//en.wikipedia.org/w/index.php?title=Special:Whatlinkshere/Mike_Potts&amp;namespace=0" class="external text">internal link</a> led you here, you may wish to change the link to point directly to the intended article.</small> </div>\n</div><meta property="mw:PageProp/disambiguation" about="#mwt1"/><link rel="mw:PageProp/Category" href="./Category:All_article_disambiguation_pages" about="#mwt1"/><link rel="mw:PageProp/Category" href="./Category:All_disambiguation_pages" about="#mwt1"/><link rel="mw:PageProp/Category" href="./Category:Human_name_disambiguation_pages#Potts,%20Mike" about="#mwt1" id="mwEQ"/></section></body></html>'

# corresponds to: https://en.wikipedia.org/w/index.php?title=William_Clark_(inventor)&oldid=1054288291
# full article
example_html_two = '<!DOCTYPE html>\n<html prefix="dc: http://purl.org/dc/terms/ mw: http://mediawiki.org/rdf/" about="https://en.wikipedia.org/wiki/Special:Redirect/revision/1054288291"><head prefix="mwr: https://en.wikipedia.org/wiki/Special:Redirect/"><meta property="mw:TimeUuid" content="1d7a0e80-ab04-11ec-928b-672b4cbca9d4"/><meta charset="utf-8"/><meta property="mw:pageId" content="13924699"/><meta property="mw:pageNamespace" content="0"/><link rel="dc:replaces" resource="mwr:revision/1029323736"/><meta property="mw:revisionSHA1" content="5f8419d1401a3bcb6301fcb123fc291a9a7b92f0"/><meta property="dc:modified" content="2021-11-09T04:36:27.000Z"/><meta property="mw:htmlVersion" content="2.4.0"/><meta property="mw:html:version" content="2.4.0"/><link rel="dc:isVersionOf" href="//en.wikipedia.org/wiki/William_Clark_(inventor)"/><base href="//en.wikipedia.org/wiki/"/><title>William Clark (inventor)</title><meta property="mw:moduleStyles" content="ext.cite.style|ext.cite.styles"/><link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.cite.style%7Cext.cite.styles%7Cmediawiki.skinning.content.parsoid%7Cmediawiki.skinning.interface%7Csite.styles&amp;only=styles&amp;skin=vector"/><meta http-equiv="content-language" content="en"/><meta http-equiv="vary" content="Accept"/></head><body id="mwAA" lang="en" class="mw-content-ltr sitedir-ltr ltr mw-body-content parsoid-body mediawiki mw-parser-output" dir="ltr"><section data-mw-section-id="0" id="mwAQ"><style data-mw-deduplicate="TemplateStyles:r1033289096" typeof="mw:Extension/templatestyles mw:Transclusion" about="#mwt1" data-mw=\'{"parts":[{"template":{"target":{"wt":"Other people","href":"./Template:Other_people"},"params":{"1":{"wt":"William Clark"}},"i":0}}]}\' id="mwAg">.mw-parser-output .hatnote{font-style:italic}.mw-parser-output div.hatnote{padding-left:1.6em;margin-bottom:0.5em}.mw-parser-output .hatnote i{font-style:normal}.mw-parser-output .hatnote+link+.hatnote{margin-top:-0.5em}</style><div role="note" class="hatnote navigation-not-searchable" about="#mwt1" id="mwAw">For other people named William Clark, see <a rel="mw:WikiLink" href="./William_Clark_(disambiguation)" title="William Clark (disambiguation)" class="mw-disambig">William Clark (disambiguation)</a>.</div>\n<p id="mwBA"><span typeof="mw:Nowiki mw:Transclusion" about="#mwt5" data-mw=\'{"parts":[{"template":{"target":{"wt":"Use dmy dates","href":"./Template:Use_dmy_dates"},"params":{"date":{"wt":"November 2021"}},"i":0}}]}\' id="mwBQ"></span><link rel="mw:PageProp/Category" href="./Category:Use_dmy_dates_from_November_2021" about="#mwt5" id="mwBg"/>\n<span typeof="mw:Nowiki mw:Transclusion" about="#mwt8" data-mw=\'{"parts":[{"template":{"target":{"wt":"Use British English","href":"./Template:Use_British_English"},"params":{"date":{"wt":"July 2012"}},"i":0}}]}\' id="mwBw"></span><link rel="mw:PageProp/Category" href="./Category:Use_British_English_from_July_2012" about="#mwt8" id="mwCA"/>\n<b id="mwCQ">William Clark</b> (17 March 1821 – 22 January 1880) was an <a rel="mw:WikiLink" href="./England" title="England" id="mwCg">English</a> <a rel="mw:WikiLink" href="./Civil_engineer" title="Civil engineer" id="mwCw">civil engineer</a> and <a rel="mw:WikiLink" href="./Inventor" title="Inventor" class="mw-redirect" id="mwDA">inventor</a>.</p>\n\n</section><section data-mw-section-id="1" id="mwDQ"><h2 id="Life">Life</h2>\n\n<p id="mwDg">Born at <a rel="mw:WikiLink" href="./Colchester" title="Colchester" id="mwDw">Colchester</a>, Clark attended <a rel="mw:WikiLink" href="./King\'s_College_London" title="King\'s College London" id="mwEA">King\'s College London</a> in 1842, and was made an <a rel="mw:WikiLink" href="./Associate_of_King\'s_College" title="Associate of King\'s College" class="mw-redirect" id="mwEQ">Associate of King\'s College</a> in 1845. Soon afterwards he became a pupil of, and subsequently an assistant to, J. Birkinshaw, M. Inst. C.E., under whom he was employed for three years on the works of the York and North Midland railway system. In 1850 he was connected with Sir <a rel="mw:WikiLink" href="./Goldsworthy_Gurney" title="Goldsworthy Gurney" id="mwEg">Goldsworthy Gurney</a> in the warming and ventilation of the houses of parliament. In 1851 he entered into partnership with A. W. Makinson, M. Inst. C.E., the firm devoting special attention to the warming and ventilating of public buildings. He shortly afterwards obtained the appointment of surveyor to the local board of health of <a rel="mw:WikiLink" href="./Kingston-upon-Hull" title="Kingston-upon-Hull" class="mw-redirect" id="mwEw">Kingston-upon-Hull</a>, and devised a complete system of drainage for that town.</p>\n\n<p id="mwFA">In 1854 he entered the service of the <a rel="mw:WikiLink" href="./East_Indian_Railway_Company" title="East Indian Railway Company" id="mwFQ">East Indian Railway Company</a>, and, after acting for a year as resident engineer on a portion of the East India railway, became the secretary and subsequently the engineer to the municipality of <a rel="mw:WikiLink" href="./Calcutta" title="Calcutta" class="mw-redirect" id="mwFg">Calcutta</a>. Clark devoted himself with zeal to his work, and very soon proposed a complete scheme for the drainage of the city, only imperfectly carried out owing to the expense. He also devised a system of waterworks, comprising three large pumping stations, with their filter beds and settling tanks.</p>\n\n<p id="mwFw">He returned to England in 1874, when he entered into partnership with W. F. Batho, M. Inst. C.E., and in the same year received the appointment of consulting engineer to the <a rel="mw:WikiLink" href="./Oudh_and_Rohilkund_Railway_Company" title="Oudh and Rohilkund Railway Company" class="new" id="mwGA">Oudh and Rohilkund Railway Company</a>. In December 1874 he visited <a rel="mw:WikiLink" href="./Madras" title="Madras" class="mw-redirect" id="mwGQ">Madras</a>, where he remained four months planning a system of drainage for that city. He was selected by the colonial office in 1876, in concert with the government of <a rel="mw:WikiLink" href="./New_South_Wales" title="New South Wales" id="mwGg">New South Wales</a>, to advise and report upon the water supply and drainage of <a rel="mw:WikiLink" href="./Sydney" title="Sydney" id="mwGw">Sydney</a>. During a residence of two years in the Australian colonies he prepared schemes of a like description for <a rel="mw:WikiLink" href="./Port_Adelaide,_South_Australia" title="Port Adelaide, South Australia" class="mw-redirect" id="mwHA">Port Adelaide</a>, <a rel="mw:WikiLink" href="./Newcastle,_New_South_Wales" title="Newcastle, New South Wales" id="mwHQ">Newcastle</a>, <a rel="mw:WikiLink" href="./Bathurst,_New_South_Wales" title="Bathurst, New South Wales" id="mwHg">Bathurst</a>, <a rel="mw:WikiLink" href="./Goulburn,_New_South_Wales" title="Goulburn, New South Wales" id="mwHw">Goulburn</a>, <a rel="mw:WikiLink" href="./Orange,_New_South_Wales" title="Orange, New South Wales" id="mwIA">Orange</a>, <a rel="mw:WikiLink" href="./Maitland,_New_South_Wales" title="Maitland, New South Wales" id="mwIQ">Maitland</a> (the <a rel="mw:WikiLink" href="./Walka_Water_Works" title="Walka Water Works" id="mwIg">Walka Water Works</a>), and <a rel="mw:WikiLink" href="./Brisbane" title="Brisbane" id="mwIw">Brisbane</a>, and afterwards for <a rel="mw:WikiLink" href="./Wellington" title="Wellington" id="mwJA">Wellington</a> and <a rel="mw:WikiLink" href="./Christchurch" title="Christchurch" id="mwJQ">Christchurch</a> in <a rel="mw:WikiLink" href="./New_Zealand" title="New Zealand" id="mwJg">New Zealand</a>.</p>\n\n<p id="mwJw">Among Clark\'s inventions was his tied brick arch, of which examples exist in Calcutta and in other places in <a rel="mw:WikiLink" href="./India" title="India" id="mwKA">India</a>; and he was joint patentee with <a rel="mw:WikiLink" href="./William_F._Batho" title="William F. Batho" class="new" id="mwKQ">William F. Batho</a> of the well-known steam road roller. Among his schemes was a proposal for reclaiming the salt-water lakes in the neighbourhood of Calcutta. He was elected a member of the Institution of Civil Engineers on 2 February 1864, and a member of the Institution of Mechanical Engineers in 1867.</p>\n\n<p id="mwKg">He died from liver disease, at Surbiton, on 22 January 1880. He was the writer of <i id="mwKw">The Drainage of Calcutta,</i> 1871.<sup about="#mwt12" class="mw-ref reference" id="cite_ref-1" rel="dc:references" typeof="mw:Extension/ref" data-mw=\'{"name":"ref","attrs":{},"body":{"id":"mw-reference-text-cite_note-1"}}\'><a href="./William_Clark_(inventor)#cite_note-1" style="counter-reset: mw-Ref 1;" id="mwLA"><span class="mw-reflink-text" id="mwLQ">[1]</span></a></sup></p>\n\n</section><section data-mw-section-id="2" id="mwLg"><h2 id="References">References</h2>\n<style data-mw-deduplicate="TemplateStyles:r1011085734" typeof="mw:Extension/templatestyles mw:Transclusion" about="#mwt13" data-mw=\'{"parts":[{"template":{"target":{"wt":"reflist","href":"./Template:Reflist"},"params":{},"i":0}}]}\' id="mwLw">.mw-parser-output .reflist{font-size:90%;margin-bottom:0.5em;list-style-type:decimal}.mw-parser-output .reflist .references{font-size:100%;margin-bottom:0;list-style-type:inherit}.mw-parser-output .reflist-columns-2{column-width:30em}.mw-parser-output .reflist-columns-3{column-width:25em}.mw-parser-output .reflist-columns{margin-top:0.3em}.mw-parser-output .reflist-columns ol{margin-top:0}.mw-parser-output .reflist-columns li{page-break-inside:avoid;break-inside:avoid-column}.mw-parser-output .reflist-upper-alpha{list-style-type:upper-alpha}.mw-parser-output .reflist-upper-roman{list-style-type:upper-roman}.mw-parser-output .reflist-lower-alpha{list-style-type:lower-alpha}.mw-parser-output .reflist-lower-greek{list-style-type:lower-greek}.mw-parser-output .reflist-lower-roman{list-style-type:lower-roman}</style><div class="reflist   " about="#mwt13" id="mwMA">\n<div class="mw-references-wrap" typeof="mw:Extension/references" about="#mwt19" data-mw=\'{"name":"references","attrs":{"group":"","responsive":"1"},"body":{"html":""}}\' id="mwMQ"><ol class="mw-references references" id="mwMg"><li about="#cite_note-1" id="cite_note-1"><a href="./William_Clark_(inventor)#cite_ref-1" rel="mw:referencedBy" id="mwMw"><span class="mw-linkback-text" id="mwNA">↑ </span></a> <span id="mw-reference-text-cite_note-1" class="mw-reference-text"><a rel="mw:ExtLink" href="https://books.google.com/books/about/The_drainage_of_Calcutta.html?id=oQVbAAAAQAAJ&amp;redir_esc=y" class="external text" id="mwNQ">The drainage of Calcutta</a>: a paper read at the Bengal social science congress, held at the town hall, Calcutta, on 2 February 1871 (Google eBook)</span></li></ol></div></div>\n<p id="mwNg"><span class="noviewer" typeof="mw:Transclusion mw:Image" about="#mwt20" data-mw=\'{"parts":[{"template":{"target":{"wt":"DNB","href":"./Template:DNB"},"params":{"wstitle":{"wt":"Clark, William (1821-1880)"}},"i":0}}]}\' id="mwNw"><span><img alt="" resource="./File:Wikisource-logo.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/12px-Wikisource-logo.svg.png" decoding="async" data-file-width="410" data-file-height="430" data-file-type="drawing" height="13" width="12" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/18px-Wikisource-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/24px-Wikisource-logo.svg.png 2x"/></span></span><span typeof="mw:Entity" about="#mwt20">\xa0</span><span about="#mwt20">This article incorporates text from a publication now in the </span><a rel="mw:WikiLink" href="./Public_domain" title="Public domain" about="#mwt20">public domain</a><span about="#mwt20">:</span><span typeof="mw:Entity" about="#mwt20">\xa0</span><style data-mw-deduplicate="TemplateStyles:r1067248974" typeof="mw:Extension/templatestyles" about="#mwt20" data-mw=\'{"name":"templatestyles","attrs":{"src":"Module:Citation/CS1/styles.css"},"body":{"extsrc":""}}\'>.mw-parser-output cite.citation{font-style:inherit;word-wrap:break-word}.mw-parser-output .citation q{quotes:"\\"""\\"""\'""\'"}.mw-parser-output .citation:target{background-color:rgba(0,127,255,0.133)}.mw-parser-output .id-lock-free a,.mw-parser-output .citation .cs1-lock-free a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg")right 0.1em center/9px no-repeat}.mw-parser-output .id-lock-limited a,.mw-parser-output .id-lock-registration a,.mw-parser-output .citation .cs1-lock-limited a,.mw-parser-output .citation .cs1-lock-registration a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg")right 0.1em center/9px no-repeat}.mw-parser-output .id-lock-subscription a,.mw-parser-output .citation .cs1-lock-subscription a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg")right 0.1em center/9px no-repeat}.mw-parser-output .cs1-ws-icon a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg")right 0.1em center/12px no-repeat}.mw-parser-output .cs1-code{color:inherit;background:inherit;border:none;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;color:#d33}.mw-parser-output .cs1-visible-error{color:#d33}.mw-parser-output .cs1-maint{display:none;color:#3a3;margin-left:0.3em}.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right{padding-right:0.2em}.mw-parser-output .citation .mw-selflink{font-weight:inherit}</style><cite class="citation encyclopaedia cs1" about="#mwt20">"<a rel="mw:WikiLink/Interwiki" href="https://en.wikisource.org/wiki/Dictionary%20of%20National%20Biography,%201885-1900/Clark,%20William%20(1821-1880)" title="s:Dictionary of National Biography, 1885-1900/Clark, William (1821-1880)" class="extiw">Clark, William (1821-1880)</a>". <i><a rel="mw:WikiLink" href="./Dictionary_of_National_Biography" title="Dictionary of National Biography">Dictionary of National Biography</a></i>. London: Smith, Elder &amp; Co. 1885–1900.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=bookitem&amp;rft.atitle=Clark%2C+William+%281821-1880%29&amp;rft.btitle=Dictionary+of+National+Biography&amp;rft.place=London&amp;rft.pub=Smith%2C+Elder+%26+Co&amp;rft.date=1885%2F1900&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AWilliam+Clark+%28inventor%29" class="Z3988" about="#mwt20"></span><span about="#mwt20"> </span><link rel="mw:PageProp/Category" href="./Category:Articles_incorporating_Cite_DNB_template" about="#mwt20"/><link rel="mw:PageProp/Category" href="./Category:Articles_incorporating_DNB_text_with_Wikisource_reference" about="#mwt20" id="mwOA"/></p>\n\n<link rel="mw:PageProp/Category" href="./Category:AC_with_0_elements" about="#mwt23" typeof="mw:Transclusion" data-mw=\'{"parts":[{"template":{"target":{"wt":"authority control","href":"./Template:Authority_control"},"params":{},"i":0}}]}\' id="mwOQ"/>\n\n<meta property="mw:PageProp/categorydefaultsort" content="Clark, William" id="mwOg"/>\n<link rel="mw:PageProp/Category" href="./Category:1821_births" id="mwOw"/>\n<link rel="mw:PageProp/Category" href="./Category:1880_deaths" id="mwPA"/>\n<link rel="mw:PageProp/Category" href="./Category:English_civil_engineers" id="mwPQ"/>\n<link rel="mw:PageProp/Category" href="./Category:19th-century_British_inventors" id="mwPg"/>\n<link rel="mw:PageProp/Category" href="./Category:Alumni_of_King\'s_College_London" id="mwPw"/>\n<link rel="mw:PageProp/Category" href="./Category:Associates_of_King\'s_College" id="mwQA"/></section></body></html>'

example_html_one_pretty = """<!DOCTYPE html>
<html about="https://en.wikipedia.org/wiki/Special:Redirect/revision/1052159182" prefix="dc: http://purl.org/dc/terms/ mw: http://mediawiki.org/rdf/">
 <head prefix="mwr: https://en.wikipedia.org/wiki/Special:Redirect/">
  <meta content="cd159e50-bc7e-11ec-9de6-11b7fdafb6ee" property="mw:TimeUuid"/>
  <meta charset="utf-8"/>
  <meta content="31967453" property="mw:pageId"/>
  <meta content="0" property="mw:pageNamespace"/>
  <link rel="dc:replaces" resource="mwr:revision/874370476"/>
  <meta content="aef8e32baa25d08f9f482936208ec4533406f5b8" property="mw:revisionSHA1"/>
  <meta content="2021-10-27T18:20:34.000Z" property="dc:modified"/>
  <meta content="2.4.0" property="mw:htmlVersion"/>
  <meta content="2.4.0" property="mw:html:version"/>
  <link href="//en.wikipedia.org/wiki/Mike_Potts" rel="dc:isVersionOf"/>
  <base href="//en.wikipedia.org/wiki/"/>
  <title>
   Mike Potts
  </title>
  <link href="/w/load.php?lang=en&amp;modules=mediawiki.skinning.content.parsoid%7Cmediawiki.skinning.interface%7Csite.styles&amp;only=styles&amp;skin=vector" rel="stylesheet"/>
  <meta content="en" http-equiv="content-language"/>
  <meta content="Accept" http-equiv="vary"/>
 </head>
 <body class="mw-content-ltr sitedir-ltr ltr mw-body-content parsoid-body mediawiki mw-parser-output" dir="ltr" id="mwAA" lang="en">
  <section data-mw-section-id="0" id="mwAQ">
   <p id="mwAg">
    <b id="mwAw">
     Mike
    </b>
    or
    <b id="mwBA">
     Michael Potts
    </b>
    may refer to:
   </p>
   <ul id="mwBQ">
    <li id="mwBg">
     <a href="./Michael_Potts_(actor)" id="mwBw" rel="mw:WikiLink" title="Michael Potts (actor)">
      Michael Potts (actor)
     </a>
     , American actor
    </li>
    <li id="mwCA">
     <a href="./Michael_Potts_(footballer)" id="mwCQ" rel="mw:WikiLink" title="Michael Potts (footballer)">
      Michael Potts (footballer)
     </a>
     (born 1991), English footballer
    </li>
    <li id="mwCg">
     <a href="./Mike_Potts_(baseball)" id="mwCw" rel="mw:WikiLink" title="Mike Potts (baseball)">
      Mike Potts (baseball)
     </a>
     (born 1970), former left-handed Major League Baseball relief pitcher
    </li>
    <li id="mwDA">
     <a href="./Mike_Potts_(American_football)" id="mwDQ" rel="mw:WikiLink" title="Mike Potts (American football)">
      Mike Potts (American football)
     </a>
     (born 1985), American football quarterback
    </li>
    <li id="mwDg">
     <a href="./Michael_Potts_(diplomat)" id="mwDw" rel="mw:WikiLink" title="Michael Potts (diplomat)">
      Michael Potts (diplomat)
     </a>
     , Australian diplomat
    </li>
   </ul>
   <style about="#mwt1" data-mw='{"parts":[{"template":{"target":{"wt":"hndis","href":"./Template:Hndis"},"params":{"1":{"wt":"Potts, Mike"}},"i":0}}]}' data-mw-deduplicate="TemplateStyles:r1008001242" id="mwEA" typeof="mw:Extension/templatestyles mw:Transclusion">
    .mw-parser-output .dmbox{display:flex;align-items:center;clear:both;margin:0.9em 1em;border-top:1px solid #ccc;border-bottom:1px solid #ccc;padding:0.25em 0.35em;font-style:italic}.mw-parser-output .dmbox>*{flex-shrink:0;margin:0 0.25em;display:inline}.mw-parser-output .dmbox-body{flex-grow:1;flex-shrink:1;padding:0.1em 0}
   </style>
   <span about="#mwt1">
   </span>
   <div about="#mwt1" class="metadata plainlinks dmbox dmbox-disambig" id="_disambigbox" role="note">
    <span typeof="mw:Image">
     <a class="mw-file-description" href="./File:Disambig_gray.svg">
      <img alt="Disambiguation icon" data-file-height="168" data-file-type="drawing" data-file-width="220" decoding="async" height="23" resource="./File:Disambig_gray.svg" src="//upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/30px-Disambig_gray.svg.png" srcset="//upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/45px-Disambig_gray.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/60px-Disambig_gray.svg.png 2x" width="30"/>
     </a>
    </span>
    <div class="dmbox-body">
     <div class="shortdescription nomobile noexcerpt noprint searchaux" style="display:none">
      Topics referred to by the same term
     </div>
     <link href="./Category:Disambiguation_pages_with_short_descriptions" rel="mw:PageProp/Category"/>
     <link href="./Category:Short_description_is_different_from_Wikidata" rel="mw:PageProp/Category"/>
     This
     <a href="./Help:Disambiguation" rel="mw:WikiLink" title="Help:Disambiguation">
      disambiguation
     </a>
     page lists articles about people with the same name.
     <br/>
     <small>
      If an
      <a class="external text" href="//en.wikipedia.org/w/index.php?title=Special:Whatlinkshere/Mike_Potts&amp;namespace=0" rel="mw:ExtLink">
       internal link
      </a>
      led you here, you may wish to change the link to point directly to the intended article.
     </small>
    </div>
   </div>
   <meta about="#mwt1" property="mw:PageProp/disambiguation"/>
   <link about="#mwt1" href="./Category:All_article_disambiguation_pages" rel="mw:PageProp/Category"/>
   <link about="#mwt1" href="./Category:All_disambiguation_pages" rel="mw:PageProp/Category"/>
   <link about="#mwt1" href="./Category:Human_name_disambiguation_pages#Potts,%20Mike" id="mwEQ" rel="mw:PageProp/Category"/>
  </section>
 </body>
</html>"""

example_html_two_pretty = """<!DOCTYPE html>
<html about="https://en.wikipedia.org/wiki/Special:Redirect/revision/1054288291" prefix="dc: http://purl.org/dc/terms/ mw: http://mediawiki.org/rdf/">
 <head prefix="mwr: https://en.wikipedia.org/wiki/Special:Redirect/">
  <meta content="1d7a0e80-ab04-11ec-928b-672b4cbca9d4" property="mw:TimeUuid"/>
  <meta charset="utf-8"/>
  <meta content="13924699" property="mw:pageId"/>
  <meta content="0" property="mw:pageNamespace"/>
  <link rel="dc:replaces" resource="mwr:revision/1029323736"/>
  <meta content="5f8419d1401a3bcb6301fcb123fc291a9a7b92f0" property="mw:revisionSHA1"/>
  <meta content="2021-11-09T04:36:27.000Z" property="dc:modified"/>
  <meta content="2.4.0" property="mw:htmlVersion"/>
  <meta content="2.4.0" property="mw:html:version"/>
  <link href="//en.wikipedia.org/wiki/William_Clark_(inventor)" rel="dc:isVersionOf"/>
  <base href="//en.wikipedia.org/wiki/"/>
  <title>
   William Clark (inventor)
  </title>
  <meta content="ext.cite.style|ext.cite.styles" property="mw:moduleStyles"/>
  <link href="/w/load.php?lang=en&amp;modules=ext.cite.style%7Cext.cite.styles%7Cmediawiki.skinning.content.parsoid%7Cmediawiki.skinning.interface%7Csite.styles&amp;only=styles&amp;skin=vector" rel="stylesheet"/>
  <meta content="en" http-equiv="content-language"/>
  <meta content="Accept" http-equiv="vary"/>
 </head>
 <body class="mw-content-ltr sitedir-ltr ltr mw-body-content parsoid-body mediawiki mw-parser-output" dir="ltr" id="mwAA" lang="en">
  <section data-mw-section-id="0" id="mwAQ">
   <style about="#mwt1" data-mw='{"parts":[{"template":{"target":{"wt":"Other people","href":"./Template:Other_people"},"params":{"1":{"wt":"William Clark"}},"i":0}}]}' data-mw-deduplicate="TemplateStyles:r1033289096" id="mwAg" typeof="mw:Extension/templatestyles mw:Transclusion">
    .mw-parser-output .hatnote{font-style:italic}.mw-parser-output div.hatnote{padding-left:1.6em;margin-bottom:0.5em}.mw-parser-output .hatnote i{font-style:normal}.mw-parser-output .hatnote+link+.hatnote{margin-top:-0.5em}
   </style>
   <div about="#mwt1" class="hatnote navigation-not-searchable" id="mwAw" role="note">
    For other people named William Clark, see
    <a class="mw-disambig" href="./William_Clark_(disambiguation)" rel="mw:WikiLink" title="William Clark (disambiguation)">
     William Clark (disambiguation)
    </a>
    .
   </div>
   <p id="mwBA">
    <span about="#mwt5" data-mw='{"parts":[{"template":{"target":{"wt":"Use dmy dates","href":"./Template:Use_dmy_dates"},"params":{"date":{"wt":"November 2021"}},"i":0}}]}' id="mwBQ" typeof="mw:Nowiki mw:Transclusion">
    </span>
    <link about="#mwt5" href="./Category:Use_dmy_dates_from_November_2021" id="mwBg" rel="mw:PageProp/Category"/>
    <span about="#mwt8" data-mw='{"parts":[{"template":{"target":{"wt":"Use British English","href":"./Template:Use_British_English"},"params":{"date":{"wt":"July 2012"}},"i":0}}]}' id="mwBw" typeof="mw:Nowiki mw:Transclusion">
    </span>
    <link about="#mwt8" href="./Category:Use_British_English_from_July_2012" id="mwCA" rel="mw:PageProp/Category"/>
    <b id="mwCQ">
     William Clark
    </b>
    (17 March 1821 – 22 January 1880) was an
    <a href="./England" id="mwCg" rel="mw:WikiLink" title="England">
     English
    </a>
    <a href="./Civil_engineer" id="mwCw" rel="mw:WikiLink" title="Civil engineer">
     civil engineer
    </a>
    and
    <a class="mw-redirect" href="./Inventor" id="mwDA" rel="mw:WikiLink" title="Inventor">
     inventor
    </a>
    .
   </p>
  </section>
  <section data-mw-section-id="1" id="mwDQ">
   <h2 id="Life">
    Life
   </h2>
   <p id="mwDg">
    Born at
    <a href="./Colchester" id="mwDw" rel="mw:WikiLink" title="Colchester">
     Colchester
    </a>
    , Clark attended
    <a href="./King's_College_London" id="mwEA" rel="mw:WikiLink" title="King's College London">
     King's College London
    </a>
    in 1842, and was made an
    <a class="mw-redirect" href="./Associate_of_King's_College" id="mwEQ" rel="mw:WikiLink" title="Associate of King's College">
     Associate of King's College
    </a>
    in 1845. Soon afterwards he became a pupil of, and subsequently an assistant to, J. Birkinshaw, M. Inst. C.E., under whom he was employed for three years on the works of the York and North Midland railway system. In 1850 he was connected with Sir
    <a href="./Goldsworthy_Gurney" id="mwEg" rel="mw:WikiLink" title="Goldsworthy Gurney">
     Goldsworthy Gurney
    </a>
    in the warming and ventilation of the houses of parliament. In 1851 he entered into partnership with A. W. Makinson, M. Inst. C.E., the firm devoting special attention to the warming and ventilating of public buildings. He shortly afterwards obtained the appointment of surveyor to the local board of health of
    <a class="mw-redirect" href="./Kingston-upon-Hull" id="mwEw" rel="mw:WikiLink" title="Kingston-upon-Hull">
     Kingston-upon-Hull
    </a>
    , and devised a complete system of drainage for that town.
   </p>
   <p id="mwFA">
    In 1854 he entered the service of the
    <a href="./East_Indian_Railway_Company" id="mwFQ" rel="mw:WikiLink" title="East Indian Railway Company">
     East Indian Railway Company
    </a>
    , and, after acting for a year as resident engineer on a portion of the East India railway, became the secretary and subsequently the engineer to the municipality of
    <a class="mw-redirect" href="./Calcutta" id="mwFg" rel="mw:WikiLink" title="Calcutta">
     Calcutta
    </a>
    . Clark devoted himself with zeal to his work, and very soon proposed a complete scheme for the drainage of the city, only imperfectly carried out owing to the expense. He also devised a system of waterworks, comprising three large pumping stations, with their filter beds and settling tanks.
   </p>
   <p id="mwFw">
    He returned to England in 1874, when he entered into partnership with W. F. Batho, M. Inst. C.E., and in the same year received the appointment of consulting engineer to the
    <a class="new" href="./Oudh_and_Rohilkund_Railway_Company" id="mwGA" rel="mw:WikiLink" title="Oudh and Rohilkund Railway Company">
     Oudh and Rohilkund Railway Company
    </a>
    . In December 1874 he visited
    <a class="mw-redirect" href="./Madras" id="mwGQ" rel="mw:WikiLink" title="Madras">
     Madras
    </a>
    , where he remained four months planning a system of drainage for that city. He was selected by the colonial office in 1876, in concert with the government of
    <a href="./New_South_Wales" id="mwGg" rel="mw:WikiLink" title="New South Wales">
     New South Wales
    </a>
    , to advise and report upon the water supply and drainage of
    <a href="./Sydney" id="mwGw" rel="mw:WikiLink" title="Sydney">
     Sydney
    </a>
    . During a residence of two years in the Australian colonies he prepared schemes of a like description for
    <a class="mw-redirect" href="./Port_Adelaide,_South_Australia" id="mwHA" rel="mw:WikiLink" title="Port Adelaide, South Australia">
     Port Adelaide
    </a>
    ,
    <a href="./Newcastle,_New_South_Wales" id="mwHQ" rel="mw:WikiLink" title="Newcastle, New South Wales">
     Newcastle
    </a>
    ,
    <a href="./Bathurst,_New_South_Wales" id="mwHg" rel="mw:WikiLink" title="Bathurst, New South Wales">
     Bathurst
    </a>
    ,
    <a href="./Goulburn,_New_South_Wales" id="mwHw" rel="mw:WikiLink" title="Goulburn, New South Wales">
     Goulburn
    </a>
    ,
    <a href="./Orange,_New_South_Wales" id="mwIA" rel="mw:WikiLink" title="Orange, New South Wales">
     Orange
    </a>
    ,
    <a href="./Maitland,_New_South_Wales" id="mwIQ" rel="mw:WikiLink" title="Maitland, New South Wales">
     Maitland
    </a>
    (the
    <a href="./Walka_Water_Works" id="mwIg" rel="mw:WikiLink" title="Walka Water Works">
     Walka Water Works
    </a>
    ), and
    <a href="./Brisbane" id="mwIw" rel="mw:WikiLink" title="Brisbane">
     Brisbane
    </a>
    , and afterwards for
    <a href="./Wellington" id="mwJA" rel="mw:WikiLink" title="Wellington">
     Wellington
    </a>
    and
    <a href="./Christchurch" id="mwJQ" rel="mw:WikiLink" title="Christchurch">
     Christchurch
    </a>
    in
    <a href="./New_Zealand" id="mwJg" rel="mw:WikiLink" title="New Zealand">
     New Zealand
    </a>
    .
   </p>
   <p id="mwJw">
    Among Clark's inventions was his tied brick arch, of which examples exist in Calcutta and in other places in
    <a href="./India" id="mwKA" rel="mw:WikiLink" title="India">
     India
    </a>
    ; and he was joint patentee with
    <a class="new" href="./William_F._Batho" id="mwKQ" rel="mw:WikiLink" title="William F. Batho">
     William F. Batho
    </a>
    of the well-known steam road roller. Among his schemes was a proposal for reclaiming the salt-water lakes in the neighbourhood of Calcutta. He was elected a member of the Institution of Civil Engineers on 2 February 1864, and a member of the Institution of Mechanical Engineers in 1867.
   </p>
   <p id="mwKg">
    He died from liver disease, at Surbiton, on 22 January 1880. He was the writer of
    <i id="mwKw">
     The Drainage of Calcutta,
    </i>
    1871.
    <sup about="#mwt12" class="mw-ref reference" data-mw='{"name":"ref","attrs":{},"body":{"id":"mw-reference-text-cite_note-1"}}' id="cite_ref-1" rel="dc:references" typeof="mw:Extension/ref">
     <a href="./William_Clark_(inventor)#cite_note-1" id="mwLA" style="counter-reset: mw-Ref 1;">
      <span class="mw-reflink-text" id="mwLQ">
       [1]
      </span>
     </a>
    </sup>
   </p>
  </section>
  <section data-mw-section-id="2" id="mwLg">
   <h2 id="References">
    References
   </h2>
   <style about="#mwt13" data-mw='{"parts":[{"template":{"target":{"wt":"reflist","href":"./Template:Reflist"},"params":{},"i":0}}]}' data-mw-deduplicate="TemplateStyles:r1011085734" id="mwLw" typeof="mw:Extension/templatestyles mw:Transclusion">
    .mw-parser-output .reflist{font-size:90%;margin-bottom:0.5em;list-style-type:decimal}.mw-parser-output .reflist .references{font-size:100%;margin-bottom:0;list-style-type:inherit}.mw-parser-output .reflist-columns-2{column-width:30em}.mw-parser-output .reflist-columns-3{column-width:25em}.mw-parser-output .reflist-columns{margin-top:0.3em}.mw-parser-output .reflist-columns ol{margin-top:0}.mw-parser-output .reflist-columns li{page-break-inside:avoid;break-inside:avoid-column}.mw-parser-output .reflist-upper-alpha{list-style-type:upper-alpha}.mw-parser-output .reflist-upper-roman{list-style-type:upper-roman}.mw-parser-output .reflist-lower-alpha{list-style-type:lower-alpha}.mw-parser-output .reflist-lower-greek{list-style-type:lower-greek}.mw-parser-output .reflist-lower-roman{list-style-type:lower-roman}
   </style>
   <div about="#mwt13" class="reflist" id="mwMA">
    <div about="#mwt19" class="mw-references-wrap" data-mw='{"name":"references","attrs":{"group":"","responsive":"1"},"body":{"html":""}}' id="mwMQ" typeof="mw:Extension/references">
     <ol class="mw-references references" id="mwMg">
      <li about="#cite_note-1" id="cite_note-1">
       <a href="./William_Clark_(inventor)#cite_ref-1" id="mwMw" rel="mw:referencedBy">
        <span class="mw-linkback-text" id="mwNA">
         ↑
        </span>
       </a>
       <span class="mw-reference-text" id="mw-reference-text-cite_note-1">
        <a class="external text" href="https://books.google.com/books/about/The_drainage_of_Calcutta.html?id=oQVbAAAAQAAJ&amp;redir_esc=y" id="mwNQ" rel="mw:ExtLink">
         The drainage of Calcutta
        </a>
        : a paper read at the Bengal social science congress, held at the town hall, Calcutta, on 2 February 1871 (Google eBook)
       </span>
      </li>
     </ol>
    </div>
   </div>
   <p id="mwNg">
    <span about="#mwt20" class="noviewer" data-mw='{"parts":[{"template":{"target":{"wt":"DNB","href":"./Template:DNB"},"params":{"wstitle":{"wt":"Clark, William (1821-1880)"}},"i":0}}]}' id="mwNw" typeof="mw:Transclusion mw:Image">
     <span>
      <img alt="" data-file-height="430" data-file-type="drawing" data-file-width="410" decoding="async" height="13" resource="./File:Wikisource-logo.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/12px-Wikisource-logo.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/18px-Wikisource-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/24px-Wikisource-logo.svg.png 2x" width="12"/>
     </span>
    </span>
    <span about="#mwt20" typeof="mw:Entity">
    </span>
    <span about="#mwt20">
     This article incorporates text from a publication now in the
    </span>
    <a about="#mwt20" href="./Public_domain" rel="mw:WikiLink" title="Public domain">
     public domain
    </a>
    <span about="#mwt20">
     :
    </span>
    <span about="#mwt20" typeof="mw:Entity">
    </span>
    <style about="#mwt20" data-mw='{"name":"templatestyles","attrs":{"src":"Module:Citation/CS1/styles.css"},"body":{"extsrc":""}}' data-mw-deduplicate="TemplateStyles:r1067248974" typeof="mw:Extension/templatestyles">
     .mw-parser-output cite.citation{font-style:inherit;word-wrap:break-word}.mw-parser-output .citation q{quotes:"\"""\"""'""'"}.mw-parser-output .citation:target{background-color:rgba(0,127,255,0.133)}.mw-parser-output .id-lock-free a,.mw-parser-output .citation .cs1-lock-free a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg")right 0.1em center/9px no-repeat}.mw-parser-output .id-lock-limited a,.mw-parser-output .id-lock-registration a,.mw-parser-output .citation .cs1-lock-limited a,.mw-parser-output .citation .cs1-lock-registration a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg")right 0.1em center/9px no-repeat}.mw-parser-output .id-lock-subscription a,.mw-parser-output .citation .cs1-lock-subscription a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg")right 0.1em center/9px no-repeat}.mw-parser-output .cs1-ws-icon a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg")right 0.1em center/12px no-repeat}.mw-parser-output .cs1-code{color:inherit;background:inherit;border:none;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;color:#d33}.mw-parser-output .cs1-visible-error{color:#d33}.mw-parser-output .cs1-maint{display:none;color:#3a3;margin-left:0.3em}.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right{padding-right:0.2em}.mw-parser-output .citation .mw-selflink{font-weight:inherit}
    </style>
    <cite about="#mwt20" class="citation encyclopaedia cs1">
     "
     <a class="extiw" href="https://en.wikisource.org/wiki/Dictionary%20of%20National%20Biography,%201885-1900/Clark,%20William%20(1821-1880)" rel="mw:WikiLink/Interwiki" title="s:Dictionary of National Biography, 1885-1900/Clark, William (1821-1880)">
      Clark, William (1821-1880)
     </a>
     ".
     <i>
      <a href="./Dictionary_of_National_Biography" rel="mw:WikiLink" title="Dictionary of National Biography">
       Dictionary of National Biography
      </a>
     </i>
     . London: Smith, Elder &amp; Co. 1885–1900.
    </cite>
    <span about="#mwt20" class="Z3988" title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=bookitem&amp;rft.atitle=Clark%2C+William+%281821-1880%29&amp;rft.btitle=Dictionary+of+National+Biography&amp;rft.place=London&amp;rft.pub=Smith%2C+Elder+%26+Co&amp;rft.date=1885%2F1900&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AWilliam+Clark+%28inventor%29">
    </span>
    <span about="#mwt20">
    </span>
    <link about="#mwt20" href="./Category:Articles_incorporating_Cite_DNB_template" rel="mw:PageProp/Category"/>
    <link about="#mwt20" href="./Category:Articles_incorporating_DNB_text_with_Wikisource_reference" id="mwOA" rel="mw:PageProp/Category"/>
   </p>
   <link about="#mwt23" data-mw='{"parts":[{"template":{"target":{"wt":"authority control","href":"./Template:Authority_control"},"params":{},"i":0}}]}' href="./Category:AC_with_0_elements" id="mwOQ" rel="mw:PageProp/Category" typeof="mw:Transclusion"/>
   <meta content="Clark, William" id="mwOg" property="mw:PageProp/categorydefaultsort"/>
   <link href="./Category:1821_births" id="mwOw" rel="mw:PageProp/Category"/>
   <link href="./Category:1880_deaths" id="mwPA" rel="mw:PageProp/Category"/>
   <link href="./Category:English_civil_engineers" id="mwPQ" rel="mw:PageProp/Category"/>
   <link href="./Category:19th-century_British_inventors" id="mwPg" rel="mw:PageProp/Category"/>
   <link href="./Category:Alumni_of_King's_College_London" id="mwPw" rel="mw:PageProp/Category"/>
   <link href="./Category:Associates_of_King's_College" id="mwQA" rel="mw:PageProp/Category"/>
  </section>
 </body>
</html>"""
