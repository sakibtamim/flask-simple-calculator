from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']

        addition = float(a) + float(b)
        return render_template('addresult.html', addition=addition)


@app.route('/sub', methods=['GET', 'POST'])
def sub():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']

        subtraction = float(a) - float(b)
        return render_template('subresult.html', subtraction=subtraction)


@app.route('/mult', methods=['GET', 'POST'])
def mult():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']

        multiplication = float(a) * float(b)
        return render_template('multresult.html', multiplication=multiplication)


@app.route('/div', methods=['GET', 'POST'])
def div():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']

        division = float(a) / float(b)
        return render_template('divresult.html', division=division)


if __name__ == '__main__':
    app.run(debug=True)
