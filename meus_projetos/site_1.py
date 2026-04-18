from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/inicio')
def homepage():
    return render_template('homepage.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')


if __name__ == '__main__':
 app.run(debug=True)
