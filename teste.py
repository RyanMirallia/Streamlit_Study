import streamlit as st

st.title("title")
st.header("header")
st.subheader("subheader")
st.text("text")
st.markdown("### markdown")
st.success("success")
st.warning("warning")
st.info("info")
st.error("error")
exp = ZeroDivisionError("ZeroDivisionError")
st.exception(exp)

"""imagens podem ser adicionadas pela biblioteca PIL
from PIL import Image
img = Image.open("img.png")
e então exibida com st.image(img)"""

if st.checkbox("show/hide"):
    st.text("conteudo")

status = st.radio("Select Gender: ", ['Male', 'Female'], index=None)

if status == 'Male':
    st.success("Male")
elif status == 'Female':    
    st.success("Female")

hobby = st.selectbox("Select your hobby: ", ["Dancing", "Singing", "Cooking"], index=None, placeholder="Select your hobby")
st.write("Your hobby is: ", hobby)

name = st.text_input("Enter your name: ", placeholder="Type here")

if st.button("Submit"):
    st.write("Your name is: ", name)

