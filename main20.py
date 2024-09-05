from pyscript import display,HTML,when,document
import io
def click_handler1():
    display(HTML('''<br/><h1>Example20</h1><p>python live code editor.</p>
    <h5>index.html</h5>
    <pre style="background-color:#f1f1f1;">
    <code onmousedown="return false" onselectstart="return false">
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
  &lt;link rel="stylesheet" href="style.css"&gt;
  &lt;script src="https://pyscript.net/releases/2024.8.1/core.js"
          crossorigin="anonymous"&gt;&lt;/script&gt;
&lt;/head&gt;
 &lt;div class="container"&gt;
&lt;iframe id="ifrm" width="1500" height="200" &gt;&lt;/iframe&gt;
&lt;button id="run" onclick='fun'&gt;Run&lt;/button&gt;        
&lt;/div&gt;
&lt;script type="py" config="./pyscript.toml" terminal&gt;
from pyscript import when,document,display,HTML
from bs4 import BeautifulSoup
from lxml import etree
import textwrap    
@when("click", "#run")
def fun(event):
    x=document.getElementById('ifrm').contentWindow.document.body.innerHTML
    def etree_pretty(root, space="\t"):
        for elem in root.iterdescendants():
            if elem.text:
               depth = int(elem.xpath("count(ancestor::*)")) + 1
               temp_text = textwrap.dedent(elem.text).strip()
               exec(temp_text) 
    html_str = x
    root = etree.HTML(html_str)
    etree_pretty(root)
 &lt;/script&gt;
    
&lt;script src=./main.js id="iframeContent"&gt;   
&lt;pre contenteditable="true"&gt;    
import matplotlib.pyplot as plt

x = [87,91,97,95]

plt.hist(x)

plt.show()       
&lt;/pre&gt;
&lt;/script&gt;    
&lt;/body&gt;
&lt;/html&gt;
</code>
</pre>
<h5>main.js</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
var iframe = document.getElementById( 'ifrm' );
	var content = document.getElementById("iframeContent").innerHTML;
	var frameDoc = iframe.document;
	if (iframe.contentWindow)
		frameDoc = iframe.contentWindow.document;

	frameDoc.open();
	frameDoc.writeln(content);
	frameDoc.close();

function input() {
      const userInput = prompt("Please enter your name:");
      return userInput;
      
  }    
</pre>
</code>
<h5>pyscript.toml</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
packages = [ "beautifulsoup4", "lxml","pandas","matplotlib"]
</code>
</pre>
<h5>output</h5>
<iframe src="https://nasrin1748.github.io/pythonProject9/" title="Example iframe" width="600" height="500"></iframe>
    '''),append=False)
