import streamlit as st
from gtts import gTTS
import os

# Titre de l'application
st.title("Text to Speech Converter")

# Zone de texte pour l'entrée utilisateur
text = st.text_input("Entrez votre texte ici")

# Bouton pour lancer la conversion
if st.button("Convertir en audio"):
    if text:
        # Créer l'objet gTTS
        tts = gTTS(text=text, lang='fr')  # 'fr' pour le français
        
        # Sauvegarder le fichier audio
        tts.save("welcome.mp3")
        
        # Jouer le fichier audio
        st.audio("welcome.mp3")
        
        # Optionnel: Supprimer le fichier après lecture
        os.remove("welcome.mp3")
    else:
        st.warning("Veuillez entrer un texte à convertir.")