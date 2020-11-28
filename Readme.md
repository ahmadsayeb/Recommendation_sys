# Movie Recommendation System
#### Authors: Ahmad Sayeb

**Hello and Welcome!!**

## About
In this project I built a hybrid movie recommendation system. I used collaborative and content based filtering. Currently the Collaborative part is fully functioning and the api can be used to connect to your React application. The Collaborative part is heavy and your computer might give you memory error. However if you have a google Collab you can run the same flask applications written in jupyter notebook and connect your application to the api.

## Disclaimer

The front side of the application was built using React. the raw files were downloaded from this repository [TylerPottsDev](https://github.com/TylerPottsDev/react-movie-database). If you are willing to download the file from there, you should have decent knowledge of React and states and axios to be able to adapt it to your own application.

## Libraries

Scikit Surprise library was used to build this model. The data was collected from MovieLens and it consist of 24 million older movies from mid 90s. The model gave good accuracy with RMSE of 0.93. In version_1 five million data is trained in version_2 five million data trained with 25 epochs. this tooke around five hours. In version three I had to decrease the epoch to 5 since simple calculation would show that it takes around thirty hours to train.


=========== **Content Based** ====================

* [**content based rec_basic.py**](rec_basic.py)
* [**content based basic app.py**](app.py)
* [**content based bag of word content_based_rec.ipynb**](content_based_rec.ipynb)

=========== **Version one** ====================
* [**collab version_1 collaborative_recommendation.ipynb**](collaborative_recommendation.ipynb)
* [**collab version 1 python file collab_app.py**](collab_app.py)
* [**collab version 1 ipynb file collab_app.ipynb**](collab_app.ipynb)

=========== **Version two** ====================
* [**collab version 2 collaborative_reccommendation_version2.ipynb**](collaborative_reccommendation_version2.ipynb)
* [**collab version 2 python app**](collab_app_v2.py)
* [**collab version 2 ipynb app**](collab_app_v2.ipynb)

=========== **Version three** ====================
* [**collab version 3 collaborative_recommendation_v3**](collaborative_recommendation_v3.ipynb)
* [**collab verions 3 recommend_predict_v3**](recommend_predict_version_3.ipynb)
* [**collab version 3 flask_app_collab_rec_v3.ipynb**](flask_app_collab_rec_v3.ipynb)

===========================================================================================

### System Requirements
**Operating System**: Windows
**Programming Language**: Python and Jupyter lab

Flask deployed both on python and jupyter. apart from content based, the other models needs a minimum ram of 16gb and higher. To deal with this problem, you can jupyter notebooks of the same file and upload it to the google collab. you can run you falsk from google collab using the jupyter files.
