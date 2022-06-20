from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/instagram', methods=['GET'])
def instagram():
    return render_template('instagram.html')

if __name__ == '__main__':
    app.run(debug=True)