import streamlit as st
import streamlit.components.v1 as components
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
components.html("""
    <style>
        body {
            margin: 0;
            background: black;
        }
    </style>
    <canvas id="ocean></canvas>
    <script>
        const canvas = document.getELementById("ocean");
        const ctx = canvas.getContext("2d");
        canvas.width = 1000;
        canvas.height = 700;
        canvas.style.width = "100%";
        canvas.style.height = "700px";
        ctx.beginPath();
        ctx.arc(200, 200, 4, 0, Math.PI * 2);
        ctx.fillStyle = "#00DFFF";
        ctx.shadowBlur = 15;
        ctx.shadowColor = "#00DFFF";
        ctx.fill();
    </script>
""", height=700)
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
