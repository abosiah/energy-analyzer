import streamlit as st

st.set_page_config(page_title="تحليل الطاقة", layout="centered")
st.title("تطبيق تحليل استهلاك الطاقة")
st.write("أهلاً بك! هذا أول تطبيق Streamlit لك على GitHub!")

input_value = st.number_input("أدخل استهلاك الطاقة بالكيلو واط:")
st.success(f"الاستهلاك اليومي هو: {input_value * 24} كيلو واط")
