from flask import Flask, render_template, request
import language_tool_python

app = Flask(__name__)
tool = language_tool_python.LanguageTool('en-US')

@app.route("/", methods=["GET", "POST"])
def home():
    original_text = ""
    corrected_text = ""

    if request.method == "POST":
        original_text = request.form["text"]
        corrected_text = tool.correct(original_text)

    return render_template(
        "index.html",
        original_text=original_text,
        corrected_text=corrected_text
    )

if __name__ == "__main__":
    app.run(debug=True)