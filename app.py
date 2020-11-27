from flask import Flask,request, jsonify
from flask_cors import CORS
import rec_basic

app = Flask(__name__)
CORS(app)

@app.route('/movie',methods=['GET'])
def recommend_movies():
    res = rec_basic.results(request.args.get('title'))[:10]
    return jsonify(res)

if __name__=='__main__':
    app.run(port=5000,debug=True)

