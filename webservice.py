from langdetect import *  # Bibliothek zur Spracherkennung
from iso639 import languages  # Sprachenname auf Basis der iso639 Abkuerzungen

from flask import Flask, request, jsonify  # Flask Bibliothek für REST client und JSON Output

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
    catches all routes and returns "wrong path" error message
    :param path: path user tried to reach
    :return: error message
    """
    return jsonify(error=True, message="Wrong path provided")


@app.route('/lg')
def index():
    """
    Checks requested String id for language and reliability of route "lg"
    :return: reliability, language (long format), language (short format), probability
    """
    input_id = request.args.get("id")  # reads params
    if bool(input_id) and not "\"\"" in input_id:
        best_result = detect_langs(input_id)[0]  # gets saves (best) result
        is_reliable = best_result.prob > 0.5  # checks reliablity
        lang_short = best_result.lang  # gets short language name
        lang_long = languages.get(part1=lang_short).name  # gets long language name
        probability = best_result.prob * 100  # gets probability in percentage
        return jsonify(reliable=is_reliable, language=lang_long, short=lang_short, prob=probability)
    else:
        return jsonify(error=True, message="There is no input provided.")


if __name__ == '__main__':
    app.run(debug=False)
