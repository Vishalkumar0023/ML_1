from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is home page and First Page"

@app.route("/index",methods=['GET'])
def index():
    return "This is an index page"

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=="POST":
        name=request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

# variable rule

@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res= "PASSED"
    else:
        res= "FAILED"
    return render_template('result.html',results=res)    


@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res= "PASSED"
    else:
        res= "FAILED"
    exp={'score':score,'res':res}    
    return render_template('result1.html',results=exp)   


@app.route("/successif/<int:score>")
def successif(score):
    
    return render_template('result.html',results=score)    



if __name__=="__main__":
    app.run(debug=True)