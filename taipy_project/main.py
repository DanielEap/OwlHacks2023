from taipy import Gui
from taipy.gui import Html
from taipy.gui import Gui

html_page = """
<center>
<|navbar|lov={[("page1", "This Page"), ("page2", "That Page")]}|>
</center>

Default page
<|layout|columns= 1 3| 
<|
###Please select a file
<br/>
<|file_selector|label=Upload File|extensions=.ppt,.pptx,.pdf|>
|>
<|
Second Column
|>
|>
"""

# html_page = """Hello World"""

# Gui(pages=html_page).run()
Gui(page=html_page).run() 
# Gui(page="# Getting started with *Taipy*").run()