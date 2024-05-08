# simple flask app
from flask import Flask
#WSGI Application

app= Flask(__name__)



@app.route('/')
def welcome():
    return "Welcome to my flask basic code page"


@app.route('/name')
def name():
    return "I Am Ravinder Kumar"

if __name__=='__main__':
    app.run(debug=True)
    #debug =True krne se server restart ho jata hai automatically 