import streamlit as st
st.header('RAMACHANDRA COLLEGE OF ENGINEERING')
a=st.number_input('enter any value')
if st.button('HIT ME'):
  st.success(f'your lucky number is {a}')
