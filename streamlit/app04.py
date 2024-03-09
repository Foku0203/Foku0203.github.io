<<<<<<< HEAD
import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline as DP

st.title('Diffusion')
st.subheader("เว็บไซต์สำหรับแปลงข้อความเป็นภาพ")

text = st.text_input("prompt: ")
if text:
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    image_data = dp(text).images[0]
    st.image(image_data, caption='Output Image', use_column_width=True)

st.write("ไม่มีอะไรเพื่อแสดงผล")  # เพิ่มข้อความนี้เพื่อให้แสดงผลทันทีหลังจากใส่ข้อความ

if st.button("จะไปต่อหรือ"):
    st.write("สิ้นสุดการทดลอง")  # เพิ่มข้อความนี้เพื่อให้แสดงผลเมื่อกดปุ่ม "จะไปต่อหรือ"
=======
import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline as DP

st.title('Diffusion')
st.subheader("เว็บไซต์สำหรับแปลงข้อความเป็นภาพ")

text = st.text_input("prompt: ")
if text:
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    image_data = dp(text).images[0]
    st.image(image_data, caption='Output Image', use_column_width=True)

st.write("ไม่มีอะไรเพื่อแสดงผล")  # เพิ่มข้อความนี้เพื่อให้แสดงผลทันทีหลังจากใส่ข้อความ

if st.button("จะไปต่อหรือ"):
    st.write("สิ้นสุดการทดลอง")  # เพิ่มข้อความนี้เพื่อให้แสดงผลเมื่อกดปุ่ม "จะไปต่อหรือ"
>>>>>>> 5abdf33380d3fe1729fa10362042f8450881f5a6
