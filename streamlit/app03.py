import streamlit as st
h = st.header('My Web Site')
s = st.subheader('เว็บไซต์ส่วนตัว')
p = st.write('เว็บไซต์นี้เเลกมาด้วยหยาดเหงื่อเเละความอดทน')
banner = st.image('http://picsum.photos/800/250')
b = st.button('click me')
text = st.text_input('prompt:')
if text:
    #text
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ...')