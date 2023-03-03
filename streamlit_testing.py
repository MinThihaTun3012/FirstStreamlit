import datetime
import streamlit as st

st.write("Sgin up ")

title = st.text_input('Enter Your name', 'Full name')
st.write('The current full name is', title)

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


option = st.selectbox(
    'Your Gender',
    ('Male', 'Female', 'I do not want to share '))

st.write('You selected:', option)



agree = st.checkbox('I accept every rules of this website')

if agree:
    st.write('Great!')
    
import streamlit as st

if st.button('Enter'):
    st.write('Loading')
else:
    st.write('if you clike enter,It will create new acc')
