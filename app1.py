from flask import Flask
app = Flask(__name__)
@app.route("/home")
def home():#home route
    return "Home Page"
@app.route("/users")
def users():#static route
    return "Welcome to user page"
@app.route("/user/<name>")#dynamic route
def user (name):
    return f" Hello {name}"
if __name__ == "__main__":
    app.run(debug=True)