from flask import Flask, request

app = Flask(__name__, template_folder='temp_forms')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


