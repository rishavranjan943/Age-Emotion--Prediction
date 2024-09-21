Age and Emotion Prediction System :

This project is a deep learning application designed to predict both age (Data -> imdbwikiimagedataset)and emotions(Data -> emotion-detection-fer) from an image using two separate models. The emotion model classifies emotions into the following categories: Angry, Disgusted, Fearful, Happy, Neutral, Sad, and Surprised.

The backend is powered by Flask, which serves the models for real-time predictions.


Table of Contents

    1.Installation
    2.Models
    3.Usage
    4.Model Accuracy
    5.Features
    6.Contributing
    7.License

1.Installation

a.Clone the Repository
b.First, clone the repository to your local machine:
    git clone https://github.com/username/age-emotion-prediction.git
    cd age-emotion-prediction
c.Install Dependencies
Install the required dependencies using pip:
    pip install -r requirements.txt



2.Model

Ensure the two .h5 files for age and emotion prediction are located in a models directory at the root of your project. The directory structure should look like this:
age-emotion-prediction/
│
├── app.py                
├── templates/               
│   ├── index.html      
│   └── result.html 
├── model_age.h5      
├── model_emotion.h5      
├── Untitled0.ipynb      
└── requirements.txt   

Age Model: A .h5 file that predicts the age of a person from an image.

Emotion Model: A .h5 file that predicts the emotion of a person, classifying into one of seven categories:
Angry
Disgusted
Fearful
Happy
Neutral
Sad
Surprised



3.Usage

To start the Flask server, run:
    python app.py

The server will start running on http://127.0.0.1:5000/.



4.Model Accuracy

Note: The accuracy of the models may be lower because they were trained with a limited dataset and for fewer epochs. Fine-tuning the models with more data and training them for additional epochs may improve their performance.

The age prediction model is relatively simple and might not always give highly accurate results.
The emotion prediction model can classify emotions into seven categories but may occasionally misclassify emotions, especially when facial expressions are ambiguous or subtle.

Future improvements could involve:

    Training for more epochs to improve accuracy.
    Using a larger dataset for both models.


5.Features

Age Prediction: Predicts the approximate age of a person from an image.

Emotion Prediction: Classifies emotions into seven categories: Angry, Disgusted, Fearful, Happy, Neutral, Sad, and Surprised.

Web Interface: Allows users to upload images via a simple web form.

REST API: Offers a simple API for predicting age and emotion from an image.

6.Contributing

If you’d like to contribute to this project:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

7.License

This project is licensed under the MIT License - see the LICENSE file for details.