from application import app
from flask import Flask, render_template, url_for
from .forms import ClientIntrestForm


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    form = ClientIntrestForm()
    return render_template('home.jinja2', form=form)


@app.route('/blog')
def blog():
    return render_template('blog_not_ready.jinja2', blog=True)
