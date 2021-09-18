from flask import Flask, render_template,redirect,url_for,abort
from markupsafe import escape


app = Flask(__name__)

# Route to direct to the home/general page
@app.route('/')
def hello_Peter():
    return 'Hello, Peter!'

# Route to direct to the hi endpoint
#the redirect function direct the user to a hello page
@app.route('/hi')
def hi(): 
    return redirect(url_for('hello' ))   

#Adding username to the url variable
@app.route('/user/<username>')
def user(username): 
    return 'Welcome user: %s' %escape(username)


#Rendering html file/pages
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name) 


#Hndling errors ie for wrong page/url
@app.errorhandler(404)   
def error(error):
    return render_template('error.html'),404    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)