from pyscript import display, HTML, when, document
import io


def click_handler1():
    display(HTML('''<br/><h1>Example21</h1><p>python live code editor.</p>
    <h5>index.html</h5>
    <pre style="background-color:#f1f1f1;">
    <code onmousedown="return false" onselectstart="return false">
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;style&gt;
    body {
        background-color: lightslategray;
    }
&lt;/style&gt;  
&lt;head&gt;
    &lt;title&gt;Noisy Math&lt;/title&gt;

    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width,initial-scale=1.0"&gt;
    &lt;link rel="stylesheet" href="https://pyscript.net/releases/2024.5.2/core.css"&gt;
    &lt;script type="module" src="https://pyscript.net/releases/2024.5.2/core.js"&gt;&lt;/script&gt;
    &lt;link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.63.1/codemirror.min.css" crossorigin="anonymous" referrerpolicy="no-referrer"/&gt;
  &lt;script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.63.1/codemirror.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"&gt;&lt;/script&gt;
  &lt;script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.63.1/mode/javascript/javascript.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"&gt;&lt;/script&gt;
&lt;pre&gt; 
&lt;textarea id="ta"&gt;
import pandas as pd
from pyscript import display
def fun():
    print("hello")
display(fun())
display("hello World")
display("hello")
display("hello World")
    
  
    
&lt;/textarea&gt;
&lt;/pre&gt;
     &lt;p&gt;
&lt;button id="run" onclick='click_handler'&gt;Run&lt;/button&gt;
&lt;button id="clearTerm"&gt;Click to Clear&lt;/button&gt;      
         
  &lt;/p&gt;
&lt;/head&gt;
&lt;body&gt; 
    &lt;script type="py" config="./pyscript.toml"&gt;
from pyscript import when, display,document
@when("click","#clearTerm")    
def clearTerm(evt):
    print('\x1bc')        
@when("click", "#run")
def click_handler(event):
    import js
    result = js.get_textarea_value()
    exec(result)
    &lt;/script&gt;
&lt;/body&gt;
    &lt;script src='main.js'&gt;&lt;/script&gt;    

&lt;/html&gt;
</code>
</pre>
<h5>main.js</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
let cm_editor;

function initCodeMirror() {
    window.editor = CodeMirror.fromTextArea(document.getElementById('ta'), {
      mode: { name: "javascript", json: true },
      lineWrapping: true,
      smartIndent: true,
      addModeClass: true,
      autoCloseTags: true,
      autoRefresh: true,
      lineNumbers: true
    });

    // create an instance.
    cm_editor = document.querySelector('.CodeMirror').CodeMirror;  
  }

  window.addEventListener('load', function () { initCodeMirror(); })

  function get_textarea_value () {
    let val = cm_editor.getValue();		// retrieve values from the editor.
	return val; 
  }
  function input() {
      const userInput = prompt("Please enter your name:");
      return userInput;
      
  }  
</pre>
</code>
<h5>pyscript.toml</h5>
<pre style="background-color:#f1f1f1;">
<code onmousedown="return false" onselectstart="return false">
"packages" = ["textual","tabulate","html2text","ipywidgets","sqlite3","pandas","Jinja2","numpy","scikit-learn","matplotlib","scipy","requests","beautifulsoup4","seaborn","opencv-python"]
</code>
</pre>
<h5>output</h5>
<iframe src="https://nasrin1748.github.io/pythonProject24/" title="Example iframe" width="600" height="500" credentialless></iframe>
    '''), append=False)
