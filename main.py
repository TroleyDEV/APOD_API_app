import requests as req
import streamlit as st

api_key = "AbaL9cPx1JwfVIzk67pv41Ve4WTnzzhjUW9sor9O"
request = req.get("https://api.nasa.gov/planetary/apod"
                  f"?api_key={api_key}")

request = request.json()

st.title(request["title"])
st.image(request["url"])
st.write(request["explanation"])
