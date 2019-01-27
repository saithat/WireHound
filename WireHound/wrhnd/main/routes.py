from flask import Flask, render_template, Blueprint

app = Flask(__name__)
@app.route("/")
def index():
	return render_template('index.html')

main = Blueprint('main', __name__)

@main.route("/main", methods=['GET'])
def home():
	return "Main"

