from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    tasks.append(request.form['task'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
