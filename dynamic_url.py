#building dynamic web app using flask

from flask import Flask, redirect, url_for

app= Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to flask app"


@app.route('/success/<int:score>')
def success(score):
    #return "<html><body><h1>the result is passed</h1></body></html>"
    return "the person passed with marks "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The peson has failed with marks "+str(score)
    
# @app.route('/result/<int:score>')
# def result(score):
#     result=""
#     if score>50:
#         return "pass"
#     else:
#         return "fail"
    
    # redirect is used to redirect to som other page if sucess nd fail
    # to create that url dynamically we use "url_for"
    
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks>50:
        result='success'
        return redirect(url_for(result, score=marks))
    else:
        result='fail'
        return "fail"
      
    
    
    
    
    
if __name__=='__main__':
    app.run(debug= True)