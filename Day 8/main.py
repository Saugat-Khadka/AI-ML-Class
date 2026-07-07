import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello, World!")

st.write("Here's my first attempt at using data to create tables:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.button("Click me")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#HTML Language also works in streamlit. You can use HTML tags to format your text. For example, you can use the <h1> tag to create a heading.
st.write("<h1> Heading 1 </h1>", unsafe_allow_html=True)

# markdown language as alternative to html
st.markdown('# Heading 1')

# forms

num = st.number_input("Enter a number")

if st.button("Calculate"):
    st.write(f"The number is {num}")
    st.write(f"The square of the number is {num**2}")
