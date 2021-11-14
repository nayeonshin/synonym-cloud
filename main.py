from flask import Flask, render_template, request

from src.google import GoogleKeywordScreenshotTaker

app = Flask(__name__)


@app.route("/")
def index():
    word = request.args.get("word")
    if word:
        shooter = GoogleKeywordScreenshotTaker(word)
        shooter.start()
        shooter.finish()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
