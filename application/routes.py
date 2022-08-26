from application import app
from flask import render_template, url_for
from .forms import ClientIntrestForm
from flask_mail import Message


@app.route("/",methods=['GET','POST'])
@app.route("/home")
@app.route("/index")
def home():
    form = ClientIntrestForm()
    return render_template('home.jinja2', form=form)


@app.route('/blog')
def blog():
    return render_template('blog_not_ready.jinja2', blog=True)


@app.route('/submit')
def submit():
    msg = Message(str='', sender="Terry.Arthur@BrooksJr.com",recipients=["dnathw2@yahoo.com"] )
    return 'Form Submitted'