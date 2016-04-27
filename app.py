from flask import Flask
from flask import render_template # Flask function to combine data with HTML and make a webpage
app = Flask(__name__)

@app.route("/") # connects index function (below) with the root URL of our site, /
def index():
    template = 'index.html'
    return render_template(template)

# function index above returns our rendered index.html template

if __name__ == '__main__':
	# Fire up the Flask test server
	app.run(debug=True, use_reloader=True)