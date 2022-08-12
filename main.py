from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('home.jinja2')

@app.route('/blog')
def blog():
    return render_template('blog_not_ready.jinja2')
