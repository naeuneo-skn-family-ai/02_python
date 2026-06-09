import streamlit as st

st.title("Media - image")

st.image('../data/집에보내줘.jpg', caption='내가 바라는 것')

image_url = 'https://i.pinimg.com/736x/11/65/83/116583471b8b650d1b6b8f76973b3e33.jpg'
st.image(image_url, caption = '내가 바라는 것')
