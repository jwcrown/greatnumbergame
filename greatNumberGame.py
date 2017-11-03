from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/', methods=["GET", "POST"])
def index():
    if "number" not in session:
        import random
        session['number'] = random.randrange(0, 101)
    if request.method == "POST":
        print type(request.form['guess'])
        print session['number']
        if int(request.form['guess']) == session['number']:
            return render_template('index.html', result = "winner")

        if int(request.form['guess']) < session['number']:
            return render_template('index.html', result = "Higher")

        if int(request.form['guess']) > session['number']:

            return render_template('index.html', result = "Lower")
    
    print session['number']
    return render_template('index.html')
@app.route('/reset',  methods=["POST"])
def reset():
    session.pop('number')
    return render_template('index.html', result = "")
app.run(debug=True)