from flask import Flask, render_template, request, jsonify
from utils.parser import analyze_page

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    url = data.get("url")

    result = analyze_page(url)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)