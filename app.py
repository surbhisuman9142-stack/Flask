from flask import Flask
app = Flask(__name__)
@app.route("/home")
def home():
    return "Hello Page"
@app.route("/about")
def about():
    return "Welcome to about page"
@app.route("/contact")
def contact():
    return "Welcome to contact page"
if __name__ == "__main__":
    app.run(debug=True)