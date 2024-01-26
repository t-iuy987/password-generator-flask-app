from flask import Flask, render_template, request, session
from generate_password import generate_password

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_pswd", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        min_length = request.form.get("min_length")
        spec_chars = request.form.get("spec_chars")
        numbers = request.form.get("numbers")
        password = generate_password(spec_chars, numbers, min_length)
        return render_template("index.html", password = password)

    


if __name__ == "__main__":
    app.run(debug=True)