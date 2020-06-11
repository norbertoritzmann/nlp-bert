from questionanswer.indexed_question import ask_index
from flask import Flask, jsonify
app = Flask(__name__)


def to_json(answer):
    return {'answer': answer['answer'],
            'context': answer['context'],
            'confidence': answer['confidence']
            }


@app.route('/ask/<question>')
def ask(question: str):

    answers = ask_index(question, 10)

    return jsonify([to_json(answer) for answer in answers])


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.

    try:
        app.run(host='127.0.0.1', port=8080, debug=True)
    except Exception as e:
        print(e.__cause__)
        raise e
