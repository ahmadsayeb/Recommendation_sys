import pandas as pd
import pickle
import requests
import json
from flask import Flask, request, jsonify
import surprise

app = Flask(__name__)
movie_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/movie_lens/movie.csv')
rating_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/movie_lens/rating.csv')

combined_small = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/movie_lens/combined_small.csv')
model = surprise.dump.load('/content/drive/MyDrive/Colab Notebooks/movie_lens/my_model_v2')
predictions = model[0]
print(predictions[0])
#create index item name and value item id series
movie_rating_combined = pd.merge(movie_df,rating_df,on='movieId')
movie_info_small = movie_rating_combined.iloc[:5000000]
movie_info_small['title'] = movie_info_small['title'].apply(string_preprocess)
movies_list_id = pd.Series(movie_info_small['movieId'].unique(),
                            index=movie_info_small['title'].unique())


@app.route('/api',methods=['GET'])
def get_api_recommendation():
  item_id = []
  movie_name = request.args.get('title')
  print('-------------------------->',movie_name)
  movie_id = movies_list_id.loc[movies_list_id.index == movie_name][0]
  user_id = combined_small.loc[combined_small.item == movie_id]['user'].tolist()[:5]
  print('useeeeeeeeeeeeer:',user_id)
  for id in user_id:
    for i in range(len(predictions)):
      if predictions[i].uid == id:
        print("--------------------> I am inside if",predictions[i])
        item_id.append(predictions[i].iid)
  movies_names = movies_list_id.loc[movies_list_id.isin(item_id)].index.tolist()[:5]
  return jsonify(movies_names)

@app.route('/movie',methods=['GET'])
def get_movies_recommendation():
  movie_name = request.args.get('title')
  movie_name = movie_name.lower()
  item_id = []
  rating = []
  movie_id = movies_list_id.loc[movies_list_id.index.str.contains(movie_name)][0]
  user_id = combined_small.loc[combined_small.item == movie_id]['user'].tolist()[:5]
  for id in user_id:
    for i in range(len(predictions)):
      if predictions[i].uid == id:
        item_id.append(predictions[i].iid)
        rating.append(predictions[i].est)
  movies_names = movies_list_id.loc[movies_list_id.isin(item_id)].index.tolist()[:5]
  for names in movies_names:
    if names.strip() == movie_name:
      movies_names.remove(names)
      movies_names.append(movies_list_id.loc[movies_list_id.isin(item_id)].index.tolist()[6])
  final = dict(zip(movies_names,rating))
  return jsonify(final)

if __name__=='__main__':
    app.run(port=5000,debug=True)