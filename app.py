from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    return render_template('result.html', result=a*b)

app.run(debug=True)
