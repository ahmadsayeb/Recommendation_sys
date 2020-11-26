import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

final = pd.read_csv('data/movie_lens/bag_words_ready.csv').drop(columns=['Unnamed: 0'])
#calculating cosime similarity
count = CountVectorizer()
count_matrix = count.fit_transform(final['Bag_of_words'])
cosine_sim = cosine_similarity(count_matrix,count_matrix)
indices = pd.Series(final['title'])
#function to recommend movies
@app.route('/api',methods=['GET'])
def recommend():
    recommended_movies = []
    title = request.args.get('title')
    idx = indices[indices.str.contains(title)].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    top_10_indices = list(score_series.iloc[1:11].index)

    for i in top_10_indices:
        recommended_movies.append(list(final['title'])[i])

    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(port=5000,debug=True)