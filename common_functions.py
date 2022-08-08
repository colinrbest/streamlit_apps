import streamlit as st


def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
