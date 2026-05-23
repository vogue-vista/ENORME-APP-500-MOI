import streamlit as st

# 1. CONFIGURATION DE LA MÉGA-APP
st.set_page_config(page_title="Nexus OS - Business Tout-en-Un", page_icon="🌐", layout="wide")

# Masquer le menu Streamlit pour faire un vrai logiciel pro
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stSidebarNav"] {display: none !important;}
title-text { font-family: 'Poppins', sans-serif; }
</style>
""", unsafe_allow_html=True)

# 2. SÉCURITÉ & ACCÈS PREMIUM (500$/mois)
if "premium_active" not in st.session_state:
    st.session_state.premium_active = False

if not st.session_state.premium_active:
    st.title("🌐 Nexus OS — Le Système d'Exploitation des Entreprises")
    st.subheader("Débloquez 40+ outils d'élite pour automatiser votre business.")
    st.info("💡 Remplacez vos abonnements de logiciels actuels et économisez des milliers de dollars par mois.")
    
    col_pay, _ = st.columns([1, 2])
    with col_pay:
        if st.button("🚀 Activer l'accès entreprise (500 $/mois) - Démo Checkout"):
            st.session_state.premium_active = True
            st.rerun()
    st.stop()

# 3. LE TABLEAU DE BORD CENTRAL (Une fois connecté)
st.title("🌐 Nexus OS Enterprise")

# Organisation par Catégories d'outils
categorie = st.selectbox(
    "📂 Choisissez une division :",
    ["🎬 Création de Contenu & IA", "📊 Marketing & Ventes", "🛠️ Productivité & Automatisation", "📈 Finance & Données"]
)

st.divider()

# --- DIVISION 1 : CRÉATION DE CONTENU & IA ---
if categorie == "🎬 Création de Contenu & IA":
    outil = st.radio(
        "🧰 Sélectionnez un outil :",
        ["🎬 Outil 1: ShortsScript IA Pro", "📝 Outil 2: Générateur de Blog SEO", "🎨 Outil 3: Analyseur de Visuels IA", "🤖 Outil 4: Chatbot Client Auto"],
        horizontal=True
    )
    
    st.write(f"### {outil}")
    
    if "ShortsScript IA Pro" in outil:
        # On injecte ton premier script ici !
        st.info("Bienvenue dans le générateur à haute rétention.")
        prompt = st.text_input("Sujet de la vidéo :")
        if st.button("Générer le script"):
            st.success(f"Script généré pour : {prompt} (Connecter l'API Groq ici)")

# --- DIVISION 2 : MARKETING & VENTES ---
elif categorie == "📊 Marketing & Ventes":
    outil = st.radio(
        "🧰 Sélectionnez un outil :",
        ["📧 Outil 5: Cold Email Automatique", "📱 Outil 6: Planificateur LinkedIn", "🔍 Outil 7: Gratteur de Leads Web"],
        horizontal=True
    )
    st.write(f"### {outil}")
    st.write("Espace de développement pour la division Marketing.")

# --- DIVISION 3 : PRODUCTIVITÉ & AUTOMATISATION ---
elif categorie == "🛠️ Productivité & Automatisation":
    outil = st.radio(
        "🧰 Sélectionnez un outil :",
        ["📁 Outil 8: Convertisseur Universel de Fichiers", "⏱️ Outil 9: Tracker de Temps Équipe", "📝 Outil 10: Générateur de Contrats Légaux"],
        horizontal=True
    )
    st.write(f"### {outil}")
    st.write("Espace de développement pour la division Productivité.")

# --- DIVISION 4 : FINANCE & DONNÉES ---
elif categorie == "📈 Finance & Données":
    outil = st.radio(
        "🧰 Sélectionnez un outil :",
        ["🧾 Outil 11: Facturation Automatique", "📊 Outil 12: Calculateur de Marge de Profit"],
        horizontal=True
    )
    st.write(f"### {outil}")
    st.write("Espace de développement pour la division Finance.")
