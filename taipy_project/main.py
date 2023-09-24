from taipy import Gui
from taipy.gui import Html
from taipy.gui import Gui
from powerpoint import getInfo
from summarize.GPTSummarize import clarifai_api_call
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
info = ""
file_data = ""
# html_page = """
# <center>
# <|navbar|lov={[("page1", "This Page"), ("page2", "That Page")]}|>
# </center>
# Default page
# <|layout|columns= 1 3| 
# <|
# ###Please select a file
# <br/>
# <|{content}|file_selector|label=Select File|on_action=help_getInfo|extensions=.pdf,.pptx|>
# <br/>
# <|Button Label|button|on_action=button_file|>
# <center>
# <|{info}|>
# </center>
# |>
# <|
# Second Column
# |>
# |>
# """

# html_page = Html("""
# <h1>Page title</h1>
# <button onclick="uploadFile()">Upload File</button>
# <script src ="fileUpload.js"></script>

      
# """)
# pg2 =  """
# <center>
# <|navbar|lov={[("page1", "This Page"), ("page2", "That Page")]}|>
# </center>
# Default page
# <|layout|columns= 1 3| 
# <|
# ###Please select a file
# <br/>
# <|{content}|file_selector|label=Select File|on_action=help_getInfo|extensions=.pdf,.pptx|>
# <br/>
# <|Button Label|button|on_action=button_file|>
# <center>
# <|{info}|>
# </center>
# |>
# <|
# Second Column
# |>
# |>
# """

# # Gui(pages=html_page).run()
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     uploaded_file = request.files['file']
#     if uploaded_file:
#         # Save the uploaded file on the server
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
#         uploaded_file.save(file_path)
#         info = getInfo(file_path)
#         return file_path  # Return the server-side file path to the client
#     return "No file uploaded."

# def help_getInfo(state, id, payload):
#     #grab the file from the file_Selector
#     # file = state.file_selector
#     thing = state.context
#     state.info = thing
#     # state.file_selector = value
#     # state.info = value + " is the file you selected"

# rendering = {
#     "page1": html_page,
#     "page2": pg2
# }
context=""
md = """
<|{context}|file_selector|label=Select File|on_action=actionThing|extensions=.pdf,.pptx|>
"""


def actionThing(state, id, payload):
    print("hi" + str(state))
    print("hi" + str(state.context))
    print("The file was selected!\n")
    text = getInfo(state.context)
    clarify = "Can you clean up and summarize this for me?:"
    concatenated_string = clarify + "\n"
    for i in text:
        concatenated_string += i 
    print(concatenated_string)
    call = clarifai_api_call(concatenated_string)
    print(call)
    state.info = call

port = 5029

Gui(page=md).run(port=port) 
port +=1
# Gui(page="# Getting started with *Taipy*").run()