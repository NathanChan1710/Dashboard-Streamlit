import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👨‍💻 Mon Portfolio")
st.write("Nathan Chan Sing Man - Portfolio")
st.write("Data Scientist & Analyste de Données")

def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("menu", ["A Propos", "Compétences", "Projets", "Expérience", "Formation", "Contact", "RATP"])
    
    # Section - A Propos 
    if selection == "A Propos":
        st.header("À propos de moi")
        st.write("Bonjour, je m'appelle Nathan, étudiant en deuxième année de BUT Science des Données, passionné par l'analyse de données à des fins décisionnelles. Actuellement en alternance chez Kantar Worldpanel, je développe des solutions innovantes pour transformer les données en insights stratégiques.")
        
        st.subheader("🎯 Objectifs")
        st.write("Mon objectif est de devenir un expert en science des données, capable de transformer des données complexes en insights actionables pour aider les entreprises dans leur prise de décision stratégique.")

    elif selection == "Compétences": 
        st.header("🛠️ Compétences")
        
        st.subheader("💻 Programmation")
        st.write("• Python - R - SAS - SQL - HTML/CSS")
        
        st.subheader("📊 Outils d'Analyse")
        st.write("• Excel - Power BI - Microsoft Suite - Access")
        
        st.subheader("🔬 Data Science")
        st.write("• Analyse statistique avancée")
        st.write("• Extraction de données")
        st.write("• Visualisation de données")
        st.write("• Machine Learning")
        st.write("• Modélisation prédictive")
        
        st.subheader("🤝 Soft Skills")
        st.write("• Travail en équipe")
        st.write("• Aisance des présentations orales")
        st.write("• Rédaction de rapports / cahiers des charges")
        st.write("• Bases d'économie et de gestion")
        st.write("• Esprit analytique")
        st.write("• Résolution de problèmes")

    elif selection == "Projets":
        st.header("🚀 Projets")
        
        st.subheader("📈 Analyse des Ventes E-commerce")
        st.write("**Technologies :** Python, Pandas, Matplotlib, Seaborn")
        st.write("**Description :** Analyse complète des données de vente d'une plateforme e-commerce avec identification des tendances saisonnières et recommandations stratégiques.")
        st.write("**Résultats :** Amélioration de 15% de la stratégie marketing grâce aux insights générés.")
        
        st.subheader("🤖 Modèle de Prédiction des Prix Immobiliers")
        st.write("**Technologies :** Python, Scikit-learn, Machine Learning")
        st.write("**Description :** Développement d'un modèle de régression pour prédire les prix immobiliers en fonction de diverses caractéristiques.")
        st.write("**Résultats :** Précision de 85% sur les données de test.")
        
        st.subheader("📊 Dashboard Interactif - Analyse Marketing")
        st.write("**Technologies :** Power BI, SQL")
        st.write("**Description :** Création d'un dashboard interactif pour suivre les performances marketing en temps réel.")
        st.write("**Résultats :** Réduction de 30% du temps d'analyse pour les équipes marketing.")
        
        st.subheader("🎯 Segmentation Clientèle")
        st.write("**Technologies :** R, Clustering, Statistiques")
        st.write("**Description :** Segmentation automatique de la clientèle d'une entreprise retail pour optimiser les campagnes marketing.")
        st.write("**Résultats :** Identification de 5 segments distincts avec stratégies personnalisées.")

    elif selection == "Expérience":
        st.header("💼 Expérience Professionnelle")
        st.image("Z:/BUT 3/Dataviz/worldpanelbynumerator_logo.jpg", width=300)
        st.subheader("🏢 Alternant Data Analyst - Worldpanel by Numerator")
        st.write("**Période :** Septembre 2024 à Septembre 2026 - Alternance ")
        st.write("**Missions :**")
        st.write("• Analyse des données de panel consommateurs")
        st.write("• Développement de dashboards et rapports automatisés")
        st.write("• Création d'insights stratégiques pour les clients")
        st.write("• Participation aux projets d'innovation data")
        st.write("• Support technique aux équipes commerciales")
        

    elif selection == "Formation":
        st.header("🎓 Formation")

        st.subheader("🏫 BUT Science des Données")
        st.write("**Établissement :** IUT - Université")
        st.write("**Période :** 2023 - 2026 (en cours)")
        st.write("**Spécialisation :** Analyse de données et Intelligence Artificielle")
        st.write("**Matières principales :**")
        st.write("• Statistiques avancées")
        st.write("• Machine Learning")
        st.write("• Bases de données")
        st.write("• Visualisation de données")
        st.write("• Économie et gestion")

        
        st.subheader("🏫 Baccalauréat Général")
        st.write("**Lycée Guy de Maupassant")
        st.write("**Période :** 2020 - 2023")
        st.write("**Spécialisation :** Mathématique et Numérique Science de l'Informatique")

    elif selection == "RATP":
            st.header("🚇 Données RATP")
            st.write("Aperçu des données d'Ile de France RATP: ")
            
            df = pd.read_csv("emplacement-des-gares-idf.csv",sep=";")  
            st.write(df.head(5)) 

            # Graphique sur le nombre de stations par ligne de métro 
            stations_par_ligne = df['indice_lig'].value_counts().sort_index()
            # Titre
            st.title("Nombre de stations par ligne de métro")
            # Création du graphique avec Plotly Express
            fig = px.bar(
                x=stations_par_ligne.index,
                y=stations_par_ligne.values,
                labels={"x": "ligne de metro", "y": "Nombre de stations sur la ligne"},
                title="Stations par ligne de métro",
                color=stations_par_ligne.values,
                color_continuous_scale="Blues"
            )

            # Forcer un pas de 1 sur l'axe X
            fig.update_xaxes(dtick=1)

            # Affichage dans Streamlit
            st.plotly_chart(fig, use_container_width=True)

            # Comptage du nombre de stations par exploitant
            stations_par_exploitant = df['exploitant'].value_counts()

            # Titre
            st.title("Répartition des stations par exploitant")

            # Création du camembert avec Plotly Express
            fig = px.pie(
                names=stations_par_exploitant.index,
                values=stations_par_exploitant.values,
                title="Répartition des lignes ferroviaire en Ile de France",
                color_discrete_sequence=px.colors.qualitative.Set3  # palette sympa
            )

            # Affichage dans Streamlit
            st.plotly_chart(fig, use_container_width=True)






    elif selection == "Contact":
        st.header("📬 Contact")
        st.write("N'hésitez pas à me contacter pour discuter d'opportunités ou de collaborations !")
        
        st.subheader("📞 Informations de contact")
        st.write("📧 **Email :** nathan.chansingman@gmail.com")
        st.write("💼 **LinkedIn :** linkedin.com/in/nathan-chan-sing-man")
        st.write("💻 **GitHub :** github.com/nathan-chan")
        st.write("📍 **Localisation :** France")
        
        st.subheader("Formulaire de contact")
        with st.form("contact_form"):
            nom = st.text_input("Nom")
            email = st.text_input("Email")
            sujet = st.text_input("Sujet")
            message = st.text_area("Message")
            submitted = st.form_submit_button("Envoyer")
            
            if submitted:
                st.success("Message envoyé avec succès ! Je vous répondrai dans les plus brefs délais.")

if __name__ == "__main__":
    main()



# Pied de page
st.markdown("---")
st.write("🌟 **Disponible pour des missions en alternance, CDD ou freelance**")
