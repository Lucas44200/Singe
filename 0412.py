import streamlit as st
from streamlit_authenticator import Authenticate
import pandas as pd

st.write("Hello World")
lien='log.csv'
connect=pd.read_csv(lien)

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',

   'password': 'utilisateurMDP',

   'email': 'utilisateur@gmail.com',

   'failed_login_attemps': 0, # Sera géré automatiquement

   'logged_in': False, # Sera géré automatiquement

   'role': 'utilisateur'},

  'root': {'name': 'root',

   'password': 'rootMDP',

   'email': 'admin@gmail.com',

   'failed_login_attemps': 0, # Sera géré automatiquement

   'logged_in': False, # Sera géré automatiquement

   'role': 'administrateur'}}}


authenticator = Authenticate(

    lesDonneesDesComptes, # Les données des comptes

    "cookie name", # Le nom du cookie, un str quelconque

    "cookie key", # La clé du cookie, un str quelconque

    30, # Le nombre de jours avant que le cookie expire 

)


authenticator.login()


def accueil():

      st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")



if st.session_state["authentication_status"]:

  accueil()

  # Le bouton de déconnexion




elif st.session_state["authentication_status"] is False:

    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:

    st.warning('Les champs username et mot de passe doivent être remplie')


from streamlit_option_menu import option_menu


# Création du menu qui va afficher les choix qui se trouvent dans la variable options
if st.session_state["authentication_status"]:
    with st.sidebar:
            selection = option_menu(

            menu_title=None,

            options = ["Accueil", "Photos"]
                )
            st.write('Salut à toi jeune entrepreneur.')
            authenticator.logout("Déconnexion")
# On indique au programme quoi faire en fonction du choix

    if selection == "Accueil":

        st.write("Bienvenue sur la page d'accueil !")

    elif selection == "Photos":

        st.write("Bienvenue sur mon album photo d'orang-outan")
            
            
         
        col1, col2, col3 = st.columns(3)


        with col1:


            st.image("S1.jpg")


        with col2:


            st.image("S2.jpg")


        with col3:


            st.image("S3.jpg")

    