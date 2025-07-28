import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pandas as pd

st.title("🌸 Iris Classifier")

iris = load_iris()
X = iris.data
y = iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

sepal_length = st.slider('Sepal Length', 4.0, 8.0, 5.1)
sepal_width = st.slider('Sepal Width', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal Length', 1.0, 7.0, 1.4)
petal_width = st.slider('Petal Width', 0.1, 2.5, 0.2)

input_df = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                        columns=iris.feature_names)

prediction = model.predict(input_df)[0]
st.success(f"Predicted: {iris.target_names[prediction]}")
