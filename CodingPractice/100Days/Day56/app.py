from flask import Flask     
app = Flask(__name__)  


@app.route('/')       
def hello(): 
    return 'Welcome to Main Page'

@app.route('/hello/<name>')       
def string(name): 
    return "My name is %s" % name 

@app.route('/int/<int:age>')       
def integer(age): #so naming of functions here are any ra? 
    return "I am %d years old" % age 
  




app.run(debug=True)