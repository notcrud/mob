from flask import Flask, render_template, redirect, session
import hashlib
from flask_debugtoolbar import DebugToolbarExtension
from models import backend, User, Post, Comment, Vote
from conf import SECRET_KEY

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = SECRET_KEY
toolbar = DebugToolbarExtension(app)



if __name__ == '__main__':
	app.run(host=0.0.0.0, port=8899)

