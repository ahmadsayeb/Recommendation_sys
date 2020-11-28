# Movie Recommendation System
#### Authors: Ahmad Sayeb

**Hello and Welcome!!**

## About
In this project I built a hybrid movie recommendation system. I used collaborative and content based filtering. Currently the Collaborative part is fully functioning and the api can be used to connect to your React application. The Collaborative part is heavy and your computer might give you memory error. However if you have a google Collab you can run the same flask applications written in jupyter notebook and connect your application to the api.

## Disclaimer

The front side of the application was built using React. the raw files were downloaded from this repository [TylerPottsDev](https://github.com/TylerPottsDev/react-movie-database). If you are willing to download the file from there, you should have decent knowledge of React and states and axios to be able to adapt it to your own application.

## Libraries

Scikit Surprise library was used to build this model. The data was collected from MovieLens and it consist of 24 million older movies from mid 90s. The model gave good accuracy with RMSE of 0.93. In version_1 five million data is trained in version_2 five million data trained with 25 epochs. this tooke around five hours. In version three I had to decrease the epoch to 5 since simple calculation would show that it takes around thirty hours to train.


=========== **Exploratory Analysis Notebooks** ====================
-[**content based rec_basic.py**](rec_basic.py)
-[**content based rec_basic.py**](rec_basic.py)
-[**content based rec_basic.py**](rec_basic.py)
-[**content based rec_basic.py**](rec_basic.py)
