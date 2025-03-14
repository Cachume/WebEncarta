from flask import Flask, render_template
from markupsafe import escape
app= Flask(__name__)

@app.route('/')
def hello():
    name = "Albert"
    friends = ["Yoni","Natha","Gabo", "Yai","Chichis"]
    return render_template('index.html', nombre = name, amigos=friends)

@app.route('/login/<username>')
def login(username):
    return f"Vista de login {username}"

@app.route('/code/<code>')
def code(code):
    return f'<code>{escape(code)}</code>'