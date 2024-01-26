from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_pswd", methods=["GET"])
def generate():
    if request.method is "GET":
        password = generate_password()
        return redirect(url_for("home", password = password))

    


if __name__ == "__main__":
    app.run(debug=True)