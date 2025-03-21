from flask import Flask, render_template, request
from summarizer import neuro_semantic_summarizer
import nltk
import spacy

nltk.download('punkt')
spacy.load("en_core_web_sm")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.form.get("input_text", "")
    tone = request.form.get("tone", "joy")
    summary_ratio = float(request.form.get("ratio", 0.2))
    config = {
        "summary_ratio": summary_ratio,
        "tone": tone,
        "tier_1_words": 20,
        "tier_2_words": 100,
        "top_n": 5
    }
    summary = neuro_semantic_summarizer(text, config)
    return render_template("index.html", summary=summary, input_text=text, tone=tone, ratio=summary_ratio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
