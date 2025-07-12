import streamlit as st
import os


st.write("Hello World 1234")
st.write(True)

"hello World" #magic method

pressed = st.button("First Buttton")
print('First:',pressed) # always false when i click on that button it is true

pressed1 = st.button("Second Button")
print('Second:',pressed1)

st.title("Super Simple Title")
st.header('You are a header')
st.subheader('You are a subheader')
st.markdown("This is **Markdown**")
st.caption('small text')

code_example = """
    def greet(name):
        print('hello',name)
"""

st.code(code_example, language="python")
st.divider()

st.image(os.path.join(os.getcwd(),"static","crop.jpeg"))
st.image(os.path.join(os.getcwd(),"static","crop.jpeg"),width=100)