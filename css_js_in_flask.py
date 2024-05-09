# learn how to add css nd Js in flask app
# jinja2 template engine
#{%...%} for statements
#{{  }} expressions to print output
#{#....#} this for comments 
## integrate html with flask
#HHTP verb Like POST GET

from flask import Flask, redirect,request, url_for, render_template
app= Flask(__name__)

@app.route('/')
def welcome():
    return render_template('css_js.html ')


@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="fail"
    exp={ 'score':score, 'res':res }
    return render_template('results.html', result = exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The peson has failed with marks "+str(score)
    

  
  # result checker  
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks>50:
        result='success'
        return redirect(url_for(result, score=marks))
    else:
        result='fail'
        return "fail"
 # result checker submit html page    
@app.route ('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science= float(request.form['science'])
        data_science= float(request.form['data_science'])
        maths= float(request.form['maths'])
        english= float(request.form['english'])
        
        total_score=(science+maths+data_science+english)/4
    res=""
    if total_score>=50:
        res="success"
        return redirect(url_for(res, score=total_score))
    else:
        res="fail"
        return redirect(url_for(res, score=total_score))
        
    
    
if __name__=='__main__':
    app.run(debug=True)
