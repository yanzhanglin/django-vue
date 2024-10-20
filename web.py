from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run()

