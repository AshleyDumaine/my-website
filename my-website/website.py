from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thesis')
def thesis():
    return render_template('thesis.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
