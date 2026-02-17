import streamlit as st

#st.Ttitle est emplyé pour écrire le titre de l'application
st.title("IMC")

#st.number_input est utilisé pour entrer une valeur de type nombre

poids = st.number_input("veuiller dodder le poid du patient:")
taille = st.number_input("veiller donner la taille du patient")

#calcul a faire

if st.button("calcul") :
    
    imc = poids/(taille**2)
    
    st.write(imc)
    
    if imc < 18.5 :
     
       st.warning("Maigre")
     
    elif 18.5<imc<25 :
     
       st.success("poids normal")
     
    elif 25 < imc < 30 :
     
       st.warning ("surpoids")
     
    elif imc >= 30 :
     
      st.warning ("obése")
     
    else:
     
      st.info("ceci n'est pas un nombre")