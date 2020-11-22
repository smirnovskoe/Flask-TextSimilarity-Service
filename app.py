from ml import text_similarity, model_multiling
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

@app.route('/api/ml', methods=['POST'])
def get_score():
    if request.method == 'POST':
        if 'text1' not in request.json or 'text2' not in request.json:
            abort(404)

        score = text_similarity(request.json['text1'], request.json['text2'], model_multiling)
     
        return jsonify({'score': score})

    return jsonify({'response': 'GET not define'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}))

if __name__ == "__main__":
    port = 9999
    host = '0.0.0.0'
    app.run(port=port, host=host, debug=True)