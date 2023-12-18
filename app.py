# Import the Flask module from the flask package
from flask import Flask, render_template, request
# Make an object that will be our application. 
app = Flask(__name__)

# Use the route() decorator create a URL route for our hello "view" function
@app.route('/hello')
def hello():
    '''Return a response containing string "Hello World!"'''
    return 'Hello World!'

# Serving HTML files
@app.route('/')
def home():
    '''View that returns a response containing the contents of index.html'''
    return render_template('index.html')

# Dynamic routing using "variable rules." 
# The variable name in the angle brackets must match the parameter label
@app.route('/name/<my_name>')
def greetings(my_name):
    '''Greet the user by name.'''
    return 'Welcome ' + my_name + '!'

# Must specify converter if URL argument to the variable rule is not a string datatype
@app.route('/square/<int:num_to_square>')
def show_square(num_to_square):
    '''View that shows the square of the number passed by URL'''
    return 'Square of ' + str(num_to_square) + ' is: ' + str(num_to_square * num_to_square)

# Query string parameters can be accessed on flask's request object
@app.route('/dog')
def report_dog():
    '''Return the query parameter pairs in a string'''
    return f'The dog named {request.values["name"]} is {request.values["age"]}'

# The request body can be accessed with the request object
@app.route('/cat', methods=['GET', 'POST'])
def report_cat():
    '''Return a modified request body as JSON'''
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            body = request.json
            body['num_legs'] = 4
            return body
        else:
            str_data = request.data.decode('utf-8')
            return str_data + ' meow!'
    else:
        return 'Meow!'

# To run our application, we need to call the run() function of our application object
if __name__ == '__main__':
    app.run(debug=True, port=3000)

# debug = By enabling debug mode, the server will automatically reload if code changes, 
# and will show an interactive debugger in the browser if an error occurs during a request.

