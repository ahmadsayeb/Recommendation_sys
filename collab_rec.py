import pandas as pd
import pickle
import requests
import json
from flask import Flask, request, jsonify
import surprise

app = Flask(__name__)
movie_df = pd.read_csv('data/movie_lens/movie.csv')
rating_df = pd.read_csv('data/movie_lens/rating.csv')

combined_small = pd.read_csv('data/movie_lens/combined_small.csv')
model = surprise.dump.load('pickle_files/my_model')
predictions = model[0][:1000]
print(predictions[0])
#create index item name and value item id series
movie_rating_combined = pd.merge(movie_df,rating_df,on='movieId')
movie_info_small = movie_rating_combined.iloc[:5000000]
movies_list_id = pd.Series(movie_info_small['movieId'].unique(),
                            index=movie_info_small['title'].unique())



@app.route('/api',methods=['GET'])
def get_movies_recommendation():
  item_id = []
  movie_name = request.args.get('title')
  movie_id = movies_list_id.loc[movies_list_id.index == movie_name][0]
  user_id = combined_small.loc[combined_small.item == movie_id]['user'].tolist()[:5]
  for id in user_id:
    for i in range(len(predictions)):
      if predictions[i].uid == id:
        item_id.append(predictions[i].iid)
  movies_names = movies_list_id.loc[movies_list_id.isin(item_id)].index.tolist()[:5]
  return jsonify(movies_names)

if __name__=='__main__':
    app.run(port=5000,debug=True)
    