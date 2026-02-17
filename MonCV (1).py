import streamlit as st
from PIL import Image
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="CV Assane Ndione - Géomaticien", layout="wide")

# --- STYLE CSS POUR UN RENDU PROFESSIONNEL ET RICHE ---
st.markdown("""
    <style>
    .stApp { background-color: #FDFEFE; }
    .section-box {
        padding: 25px;
        border-radius: 15px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
    }
    .profil-box { background: linear-gradient(90deg, #2E4053, #5D6D7E); }
    .competence-box { background: linear-gradient(90deg, #1D8348, #2ecc71); }
    .technique-box { background: linear-gradient(90deg, #CA6F1E, #E67E22); }
    
    /* Style pour la sidebar */
    [data-testid="stSidebar"] {
        background-color: #1B2631;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (INFOS PERSONNELLES) ---
with st.sidebar:
    st.markdown("<h1 style='color: white;'>📍 Contact</h1>", unsafe_allow_html=True)
    
    # Gestion de la photo
    try:
        image = Image.open("photo.jpg")
        st.image(image, width=200)
    except:
        st.info("👤 [Photo de profil]")

    st.markdown(f"""
    **Assane NDIONE** 📞 {770153073}  
    📧 { 'assane.ndione1@unchk.edu.sn' }  
    🇸🇳 Sénégal
    """)
    
    st.divider()
    st.subheader("🎓 Parcours Académique")
    st.write("**BTS en Géomatique** (En cours)")
    st.caption("Université Numérique Cheikh Hamidou Kane (UNCHK)")
    st.write("**Baccalauréat L2**")
    

# --- CONTENU PRINCIPAL ---
st.title("🛰️ Curriculum Vitae Numérique")
st.subheader("Technicien Supérieur en Géomatique")

# Section 1 : Profil
st.markdown("Passionné par la Géomatique,la Cartographie, le traitement et l'analyse des données géographiques.Je suis determine et rigoureux ,mon sens de responsabilte me permet de travailler en equipe pour bien ,mener a des projets ")

# Section 2 : Compétences Métiers
st.markdown(f'''<div class="section-box competence-box">
            <h3>🛠️ Compétences en Géomatique</h3>
            <ul>
                <li><b>Topographie :</b> Levés topographiques, altimétrie et lecture de plans complexes.</li>
                <li><b>Systèmes d'Information Géographique (SIG) :</b> Analyse spatiale et cartographie.</li>
                <li><b>Bases de Données :</b> Structuration et gestion de données géolocalisées.</li>
            </ul>
            </div>''', unsafe_allow_html=True)

# Section 3 : Programmation
st.markdown(f'''<div class="section-box technique-box">
            <h3>💻 Informatique & Programmation</h3>
            <p>Maîtrise de l'environnement <b>Streamlit</b> pour la visualisation de données et 
            utilisation de <b>Python</b> pour l'automatisation des tâches géographiques.</p>
            </div>''', unsafe_allow_html=True)

# Section 4 : Visualisation (La Carte)
st.subheader("📍 Visualisation de Données Spatiales")
st.write("Exemple d'intégration de carte interactive :")
# Coordonnées approximatives du Sénégal/Dakar
map_data = pd.DataFrame({'lat': [14.7167], 'lon': [-17.4677]})
st.map(map_data)
