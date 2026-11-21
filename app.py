import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="A Little Surprise", layout="wide")
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
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
    <canvas id="ocean"></canvas>
    <script>
        const canvas = document.getElementById("ocean");
        const ctx = canvas.getContext("2d");
        let particle = {
            x: canvas.width / 2,
            y: canvas.height / 2,
            size: 3,
            speed: 1
        };
        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particle.x += particle.speed;
            if (particle.x > canvas.width || particle.x < 0) {
                particle.speed *= -1;
            }
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            ctx.fillStyle = "#00DFFF";
            ctx.shadowBlur = 15;
            ctx.shadowColor = "#00DFFF";
            ctx.fill();
            requestAnimationFrame(animate);
        }
        animate();
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
