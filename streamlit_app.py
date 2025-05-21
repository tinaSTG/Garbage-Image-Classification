# # import libraries
# import streamlit as st
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import load_img, img_to_array

# # Class label
# class_names = ['glass', 'metal', 'paper', 'plastic', 'trash']

# # Fungsi untuk menentukan apakah sampah bisa didaur ulang
# def is_recyclable(label):
#     return label in {'glass', 'metal', 'paper', 'plastic'}

# # Fungsi prediksi gambar
# def import_and_predict(image_data, model):
#     img = load_img(image_data, target_size=(128, 128))
#     img_array = img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)

#     predictions = model.predict(img_array)[0]
#     predicted_index = np.argmax(predictions)
#     predicted_label = class_names[predicted_index]
#     confidence = predictions[predicted_index]
#     recyclable = is_recyclable(predicted_label)

#     return predicted_label, confidence, recyclable

# # Streamlit app
# def run():
#     st.title("Garbage Image Classification App ♻️")
#     st.write("Upload a picture of garbage and the model will predict its category.")

#     file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

#     if file is None:
#         st.info("Please upload an image file to begin.")
#     else:
#         st.image(file, caption="Uploaded Image", use_column_width=True)

#         # Load model (tanpa custom object)
#         model = load_model('model_garbage_classification.keras')

#         label, confidence, recyclable = import_and_predict(file, model)

#         st.markdown(f"**Prediction:** `{label}`")
#         st.markdown(f"**Confidence:** `{confidence:.2f}`")
#         st.markdown(f"**Recyclable?** `{recyclable}`")

# if __name__ == "__main__":
#     run()

# import libraries
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Class label
class_names = ['glass', 'metal', 'paper', 'plastic', 'trash']

# Fungsi untuk menentukan apakah sampah bisa didaur ulang
def is_recyclable(label):
    return label in {'glass', 'metal', 'paper', 'plastic'}

# Fungsi prediksi gambar
def import_and_predict(image_data, model):
    img = load_img(image_data, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)[0]
    predicted_index = np.argmax(predictions)
    predicted_label = class_names[predicted_index]
    confidence = predictions[predicted_index]
    recyclable = is_recyclable(predicted_label)

    return predicted_label, confidence, recyclable

# Streamlit app
def run():
    st.title("Garbage Image Classification App ♻️")
    st.write("Upload a picture of garbage and the model will predict its category.")

    file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if file is None:
        st.info("Please upload an image file to begin.")
    else:
        # Ganti use_column_width → use_container_width
        st.image(file, caption="Uploaded Image", use_container_width=True)

        # Load model (tanpa custom object)
        model = load_model('model_garbage_classification.keras')

        label, confidence, recyclable = import_and_predict(file, model)

        st.markdown(f"**Prediction:** `{label}`")
        st.markdown(f"**Confidence:** `{confidence:.2f}`")
        st.markdown(f"**Recyclable?** `{recyclable}`")

if __name__ == "__main__":
    run()
