from flask import Flask, request, jsonify, render_template
import numpy as np
from PIL import Image
import io
import tensorflow as tf

app = Flask(__name__)



age_model = tf.keras.models.load_model('model_age.h5')
emotion_model = tf.keras.models.load_model('model_emotion.h5')

def preprocess_image(image):
    image = image.resize((100, 100))  
    image = image.convert('L')  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=-1)
    image = np.repeat(image, 3, axis=-1)
    image = np.expand_dims(image, axis=0)
    
    return image


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict-image', methods=['POST'])
def predict_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    image = Image.open(io.BytesIO(image_file.read()))  
    preprocessed_image = preprocess_image(image)
    age_prediction = age_model.predict(preprocessed_image)
    emotion_prediction = emotion_model.predict(preprocessed_image)
    predicted_age = age_prediction[0][0]
    predicted_emotion_class = np.argmax(emotion_prediction)
    emotion_labels = ['Angry', 'Disgusted', 'Fearful', 'Happy', 'Neutral', 'Sad', 'Surprised']
    predicted_emotion = emotion_labels[predicted_emotion_class]
    print(f"Predicted Age: {predicted_age}")
    print(f"Predicted Emotion: {predicted_emotion}")
    return render_template('result.html', age=predicted_age, emotion=predicted_emotion)

if __name__ == '__main__':
    app.run(debug=True)
