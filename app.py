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
        canvas.width = window.innerWidth;
        canvas.height = 700;
        canvas.style.width = "100%";
        canvas.style.height = "700px";
        let particles = [];
        for (let i = 0; i < 2500; i++) {
        let starTY = canvas.height * 0.45
            + Math.random() * canvas.height * 0.55;
            let layer = Math.floor(Math.random() * 3);
            particles.push({
                layer: layer,
                x: Math.random() * canvas.width,
                y: starTY,
                baseY: starTY,
                waveOffset: Math.random() * Math.PI * 2,
                size: layer === 0 
                    ? Math.random() * 1 + 0.5
                    : layer === 1
                        ? Math.random() * 2 + 1
                        : Math.random() * 3 + 2,
                speed: layer === 0
                    ? Math.random() * 0.5 + 0.2,
                    : layer === 1
                        ? Math.random() * 1 + 0.5
                        : Math.random() * 2 + 1,
                waveStrength: Math.random() * 20 + 15,
                waveSpeed: Math.random() * 0.5 + 0.5,
            });
        }
        let time = 0;
        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            time += 0.02;
            for (let particle of particles) {
                particle.x += particle.speed;
                particle.y = particle.baseY +
                    Math.sin(particle.x * 0.008 + time * particle.waveSpeed + particle.waveOffset) * particle.waveStrength +
                    Math.sin(particle.x * 0.015 - time * 0.7) * 10;
                if (particle.x > canvas.width) {
                    particle.x = 0;
                }
                ctx.beginPath();
                ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                ctx.globalAlpha = particle.layer === 0 ? 0.3 :
                    particle.layer === 1 ? 0.65 : 1;
                ctx.shadowBlur = particle.size * 4;
                ctx.shadowColor = "#00DFFF";
                ctx.fill();
            }
            ctx.glabalAlpha = 1;
            requestAnimationFrame(animate);
        }
        animate();
    </script>
""", height=700)
