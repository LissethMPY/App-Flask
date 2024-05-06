from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/apruebo')
def apruebo():
    return render_template('apruebo.html')

@app.route('/compruebo')
def compruebo():
    return render_template('compruebo.html')

if __name__ == '__main__':
    app.run(debug=True)
