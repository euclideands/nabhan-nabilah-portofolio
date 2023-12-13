import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Nabhan's Portofolio",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="	:milky_way:"
)

base="dark"
primaryColor="#503380"

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Profile Picture.png" 

# --- GENERAL SETTINGS ---
NAME = "Nabhan Nabilah"
POSITION = """
Entry-level Data Scientist
"""
DESCRIPTION = """
Final year student of Applied Statistics and Computation at Universitas Negeri Semarang
"""
EMAIL = "nabilahnabhann@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nabhannabilah/",
    "GitHub": "https://github.com/euclideands",
    "X": "https://twitter.com/switchcasse",
}
LOGO_IMAGES = {
    "LinkedIn": "https://github.com/gauravghongde/social-icons/blob/master/PNG/White/LinkedIN_white.png?raw=true",
    "GitHub": "https://github.com/gauravghongde/social-icons/blob/master/PNG/White/Github_white.png?raw=true",
    "X": "https://github.com/gauravghongde/social-icons/blob/master/PNG/White/Twitter_white.png?raw=true"
}

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

def main():
    a1, a2= st. columns((2,8))
    
    with a1:
        st.write("")
        st.write("")
        image_path = "https://github.com/euclideands/Projects/blob/main/Nabhan%20Portofolio/Profile%20Picture.png?raw=true"  # Replace with the actual path or URL of your image
        st.image(image_path, 
                #  caption='Your Image Caption', 
                 width = 180)
               
    with a2:
        st.title("Nabhan Nabilah's Portofolio Site")
        st.write(DESCRIPTION)
        st.download_button(
            label = " 📄 Download Resume",
            data = PDFbyte,
            file_name = resume_file.name,
            mime = "application/octet-stream",
        )
        st.write("📫", EMAIL)
        
    z1, z2 = st.columns((1.8,8.2))
    with z1:
        # st.header("")
        custom_width = 33
        custom_height = 33
        cols = st.columns(len(SOCIAL_MEDIA))

        for col, (platform, link) in zip(cols, SOCIAL_MEDIA.items()):
            # Create a clickable image with a hyperlink and custom size
            image_html = f"<a href='{link}' target='_blank'><img src='{LOGO_IMAGES[platform]}' alt='{platform}' width='{custom_width}' height='{custom_height}' style='margin-bottom: 20px; margin-top: 10px;'></a>"
            col.markdown(image_html, unsafe_allow_html=True)
    with z2:
        st.write("")
        
    st.markdown('<div><h3>Future Career Interest ✨</h3></div>', unsafe_allow_html=True)
    y1, y2, y3, y4, y5 = st.columns((2,2,2,2,2))
    with y1:
        st.markdown('<div class="career">Data Scientist</div>', unsafe_allow_html=True)
    with y2:
        st.markdown('<div class="career">Data Analyst</div>', unsafe_allow_html=True)
    with y3:
        st.markdown('<div class="career">Data Engineer</div>', unsafe_allow_html=True)
    with y4:
        st.markdown('<div class="career">AI/ML Engineer</div>', unsafe_allow_html=True)
    with y5:
        st.markdown('<div class="career">Business Intelligent</div>', unsafe_allow_html=True)
    
    st.header("")    
    st.markdown('<div><h3>Checkout My Profile 🔍</h3></div>', unsafe_allow_html=True)

    b1, b2 = st.columns((2,8))
    with b1:
        # st.markdown('<div class="profile-title">Future Career Interest', unsafe_allow_html=True)
        st.markdown('<div class="profile-1">Certification:</div>', unsafe_allow_html=True)
        st.markdown('<div class="profile-2">Experience:</div>', unsafe_allow_html=True)
    with b2:
        st.markdown("""
            <div class="profile">
                <a href="https://scl.io/NDeKs3c" target="_blank">
                    <img src="https://github.com/euclideands/Projects/blob/main/Nabhan%20Portofolio/assets/933b34b7-70f2-4c60-be6e-6df161bd3a3d.png?raw=true" alt="Profile Image" width="50" height="50" style="margin-right: 10px; float: left;">
                </a>
                <p style="margin-bottom: 0;">Certified Tensorflow Developer</p>
                <a href="https://scl.io/NDeKs3c" target="_blank">See credential</a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="profile">Core Team GDSC UNNES 2023 - Academy Division - ML Path</div>', unsafe_allow_html=True)
        
        st.markdown('''<div class="profile"><p style="margin-bottom: 0;">Assistant Product Database Intern at BLOOM Outdoor Möbel</p>
                    <a href="https://github.com/euclideands/Projects/blob/main/Nabhan%20Portofolio/assets/bloom_intern.pdf" target="_blank">See certificate</a></div>''', unsafe_allow_html=True)
        st.markdown('''<div class="profile"><p style="margin-bottom: 0;">Machine Learning Student at Bangkit Academy</p>
                    <a href="https://github.com/euclideands/Projects/blob/main/Nabhan%20Portofolio/assets/Bangkit_cert.pdf" target="_blank">See certificate</a></div>''', unsafe_allow_html=True)
    
    st.header("")    
    st.markdown('<div><h3>Project Portofolio 🗂️</h3></div>', unsafe_allow_html=True)
    st.write("")
       
    c1, c2, c3 = st.columns((10/3,10/3,10/3))
    with c1:
        st.markdown('''<div class="metric-container"><a href="https://github.com/mas-tour" target="_blank">MasTour; An Innovative Tourism Application</a></div>''', unsafe_allow_html=True)
        
    with c2:
        st.markdown('''<div class="metric-container"><a href="https://github.com/euclideands/Projects/blob/main/Wine%20Classification/KNN.ipynb" 
                    target="_blank">Wine Classification Using KNN</a></div>''', unsafe_allow_html=True)
        
    with c3:
        st.markdown('''<div class="metric-container"><a href="https://github.com/euclideands/Projects/blob/main/Computer%20Vision/rpc-classification/RPS_Classification.ipynb" 
                    target="_blank">Computer Vision; Rock, Paper, Scissors Classification</a></div>''', unsafe_allow_html=True)
    
    d1, d2, d3 = st.columns((10/3,10/3,10/3))
    with d1:
        st.markdown('''<div class="metric-container"><a href="https://statkes.000webhostapp.com/" target="_blank">Website for Mental Health Survey (HTML, CSS, JS, PHP)</a></div>''', unsafe_allow_html=True)
   
    with d2:
        st.markdown('''<div class="metric-container"><a href="https://github.com/euclideands/klasifikasi-sdg/blob/main/DIMAS-TI%202023_Data%20Mining_Sementara%20Ngene%20Sek_Nabhan%20Nabilah_Universitas%20Negeri%20Semarang.pdf" 
                    target="_blank">Klasifikasi 17 Kategori SDG pada Judul Berita Berbahasa Indonesia Menggunakan Algoritma IndoBERT</a></div>''', unsafe_allow_html=True)    
    with d3:
        st.markdown('''<div class="metric-container"><a href="https://github.com/euclideands/Projects/blob/main/LDA/StudiKasus-LDA-Kelompok4.Rmd" 
                    target="_blank">Region Classification Using LDA on the Boston Housing Dataset in R</a></div>''', unsafe_allow_html=True)
    
    st.header("")    
    st.markdown('<div><h3>Coming Soon 🧐</h3></div>', unsafe_allow_html=True)
    st.write("")
    
    e1, e2, e3 = st.columns((10/3,10/3,10/3))  
    with e1:
        st.markdown('''
            <div class="metric-container-2">
                <a href="https://github.com/euclideands/DAC-2023" target="_blank" style="color: gray;">
                    Network Intrusion Detection System Using Hierarchical Multi-label Classification (Coming Soon ...)
                </a>
            </div>
        ''', unsafe_allow_html=True)
    with e2:
        st.markdown('''<div class="metric-container-2"><a href="https://github.com/euclideands/Projects" 
                    target="_blank">Dashboard Hasil Survey Kesehatan Mental Mahasiswa Staterkom Using Streamlit</a></div>''', unsafe_allow_html=True) 
             
if __name__ == "__main__":
    main()

