from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
#from flask_mysqldb import MySQL
#from wftorms import Form, StringField, TextAreaField, PassworField, validators
from passlib.hash import  sha256_crypt

app = Flask(__name__) #inicializace pohledu (view)

@app.route('/')
def index():
    return render_template('home.tpl')


@app.route('/wiki')
def wiki():
    return render_template('wiki.tpl')

@app.route('/servers')
def about():
    return render_template('servers.tpl')

if __name__ == "__main__":
    app.debug = True
    app.run()

