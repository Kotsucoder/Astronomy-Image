import streamlit as st
import requests
import os

apikey = os.getenv("NASA_API")
url = f"https://api.nasa.gov/planetary/apod?api_key={apikey}"

response = requests.get(url).json()
image_res = requests.get(response["url"])
image = image_res.content

st.title(response["title"])
st.image(image)
st.markdown(f"*Copyright: {response['copyright']}*")
st.write(response['explanation'])