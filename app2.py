from flask import Flask, render_template, request, url_for, flash, redirect, Blueprint

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

readToday = False

@app.route('/', methods = ('GET', 'POST'))
def index():
    if request.method == 'POST':
        global readToday
        readToday = True
    #return render_template('index.html', messages = messages)
    return render_template('index.html', readToday = readToday)

@app.route('/reset.html', methods = ['POST'])
def reset():
    if request.method == 'POST':
        global readToday
        readToday = False
    return redirect(url_for('index'))
    #return render_template('index.html', readToday = readToday)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
