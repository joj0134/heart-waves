import streamlit as st
st.set_page_config(page_title="A Little Surprise", layout="wide")
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;)
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {
            background-color: black;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <canvas id="ocean"></canvas>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
       #ocean {
           position: fixed;
           top: 0;
           left: 0;
           width: 100vw;
           height: 100vh;
           z-index: 10;
       }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <script>
        const canvas = document.getELementById("ocean");
        const ctx = canvas.getContext("2d");
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        ctx.beginPath();
        ctx.arc(200, 200, 4, 0, Math.PI * 2);
        ctx.fillStyle = "#00DFFF";
        ctx.shadowBlur = 15;
        ctx.shadowColor = "#00DFFF";
        ctx.fill();
    </script>
""", unsafe_allow_html=True)
