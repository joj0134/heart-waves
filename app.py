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
        let particles = [];
        for (let i = 0; i < 100; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 3 + 1,
                speed: Math.random() * 2 + 0.5
            });
        }
        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let particle of particles) {
                particle.x += particle.speed;
                if (particle.x > canvas.width) {
                    particle.x = 0;
                }
                ctx.beginPath();
                ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                ctx.fillStyle = "#00DFFF";
                ctx.shadowBlur = 15;
                ctx.shadowColor = "#00DFFF";
                ctx.fill();
            }
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
