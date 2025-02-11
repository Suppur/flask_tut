from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

# to specify allowed API methods on a route, use `methods=[]`, by default only GET is supported
# diff between different HTTP methods is not a technical one but rather convention one
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "You made a GET request\n"
    elif request.method == 'POST':
        return "You made a POST request\n"
    else:
        return "You will never see this!"



@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

# URL processors: (can also specify type with `type:`)
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting'] #can do this directly since its a dict
        #alternatively : `greeting = request.args.get('greeting')`
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return "Some params are missing"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)