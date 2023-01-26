import streamlit as st

st.title('Page 2')

"https://docs.streamlit.io/library/cheatsheet"

if "shared" not in st.session_state:
   st.session_state["shared"] = True

st.write('Display Text')

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')