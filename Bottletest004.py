# A very simple Bottle Hello World app for you to get started with...
from flask import Flask, Response, send_from_directory, request, render_template, url_for, redirect
import tiktoken
import os
import openai
import datetime
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# from bottle import default_app, template, get, post, request, route, run, static_file

app = Flask(__name__)
json = 'index-0416.json'

indexLoad = 0

# Bottletest004 = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


# @get('/')
# def hello_world():
#     return '''<h1>Search Jim Rutt Show ChatBot</h1>

#                <h2>warning the search may take several seconds...</h2>
#               <form method="POST" action="/">
#                 <textarea rows = "5" cols = "50" name = "prompt"></textarea>
#                 <br><br>
#                 <input type="submit" />
#               </form>'''

@app.route('/')
def hello_world():
    return render_template('index.html')


@ app.route('/', methods=['GET', 'POST'])
def response():
    myQuery = request.form['prompt']
    index = GPTSimpleVectorIndex.load_from_disk(json)
    indexLoad = 1
    response = index.query(myQuery)
    print(response)
    return (render_template('index.html', myQuery=myQuery, response=response))


if __name__ == '__main__':
    app.run(port=8000, debug=True)

    # replyObject = (str(myQuery), str(response))
    #     return redirect(url_for('prompt', response=response))
    # response = request.args.get('result')
    # return redirect('index.html', result=response)

# @ post('/')
# def response():
#     myQuery = request.forms.get('prompt')

#     # index = GPTSimpleVectorIndex.load_from_disk('/home/memetic007/mysite/index.json')
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     indexLoad = 1
#     response = index.query(myQuery)
#     replyObject = '''
#                <h1>Search Jim Rutt Show ChatBot</h1>

#                <h2>warning the search may take several seconds...</h2>
#               <form method="POST" action="/">
#                 <textarea rows = "5" cols = "50" name = "prompt"></textarea>
#                 <br><br>
#                 <input type="submit" />
#               </form>
#               <br>
#               <p1>Prompt:
#               ''' + str(myQuery) + "</p1><br><p1>Response: " + str(response) + "</p1>"
#     return replyObject('main.tpl')


# # application = default_app()
# run(host='localhost', port=8080, debug=True)
