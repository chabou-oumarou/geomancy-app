import streamlit as st

# --- Translation & Figure Data ---
LANGS = {
    "English": {
        "title": "🔮 The Celestial Oracle",
        "desc": "Input your random dots below. Let the ancient patterns reveal the path.",
        "calc_btn": "Cast the Divine Shield",
        "error_msg": "is incomplete. Fill all rows to proceed.",
        "foundation": "The Foundation (Mothers & Daughters)",
        "court": "⚖️ The Sacred Court",
        "judge": "The Judge",
        "reconciler": "The Reconciler",
        "figures": {
            (1, 1, 1, 1): {"name": "Via", "meaning": "Change and movement. Success through moving forward."},
            (2, 2, 2, 2): {"name": "Populus", "meaning": "The Crowd. Stability, following the flow."},
            (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "The Junction. Union and social interactions."},
            (1, 2, 2, 1): {"name": "Carcer", "meaning": "The Prison. Delays and necessary boundaries."},
            (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Greater Fortune. Inner strength and protection."},
            (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Lesser Fortune. Quick, external success."},
            (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Financial profit and spiritual growth."},
            (1, 2, 1, 2): {"name": "Amissio", "meaning": "Loss. Spending or letting go for better."},
            (1, 2, 2, 2): {"name": "Laetitia", "meaning": "Joy. Health, happiness, and positive news."},
            (2, 2, 2, 1): {"name": "Tristitia", "meaning": "Sorrow. Heavy energy, staying low and building."},
            (1, 2, 1, 1): {"name": "Puella", "meaning": "The Girl. Beauty and pleasant interactions."},
            (1, 1, 2, 1): {"name": "Puer", "meaning": "The Boy. Energy, aggression, and bold action."},
            (2, 2, 1, 2): {"name": "Albus", "meaning": "White. Peace, wisdom, and clear communication."},
            (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Red. Passion and vice. A warning to pause."},
            (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Dragon's Head. New beginnings."},
            (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Dragon's Tail. Endings and karmic exit."}
        }
    },
    "Français": {
        "title": "🔮 L'Oracle Céleste",
        "desc": "Entrez vos points au hasard. Laissez les anciens motifs révéler le chemin.",
        "calc_btn": "Lancer le Blason Divin",
        "error_msg": "est incomplète. Remplissez toutes les lignes.",
        "foundation": "La Fondation (Mères & Filles)",
        "court": "⚖️ Le Tribunal Sacré",
        "judge": "Le Juge",
        "reconciler": "Le Réconciliateur",
        "figures": {
            (1, 1, 1, 1): {"name": "Via", "meaning": "Changement et mouvement. Succès en allant de l'avant."},
            (2, 2, 2, 2): {"name": "Populus", "meaning": "La Foule. Stabilité, suivre le flux."},
            (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "La Jonction. Union et interactions sociales."},
            (1, 2, 2, 1): {"name": "Carcer", "meaning": "La Prison. Délais et limites nécessaires."},
            (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Grande Fortune. Force intérieure et protection."},
            (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Petite Fortune. Succès rapide et extérieur."},
            (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Profit financier et croissance spirituelle."},
            (1, 2, 1, 2): {"name": "Amissio", "meaning": "Perte. Dépense ou lâcher-prise pour le mieux."},
            (1, 2, 2, 2): {"name": "Laetitia", "meaning": "La Joie. Santé, bonheur et nouvelles positives."},
            (2, 2, 2, 1): {"name": "Tristitia", "meaning": "La Tristesse. Énergie lourde, fondations et discrétion."},
            (1, 2, 1, 1): {"name": "Puella", "meaning": "La Jeune Fille. Beauté et interactions plaisantes."},
            (1, 1, 2, 1): {"name": "Puer", "meaning": "Le Garçon. Énergie, agression et action impulsive."},
            (2, 2, 1, 2): {"name": "Albus", "meaning": "Le Blanc. Paix, sagesse et communication claire."},
            (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Le Rouge. Passion et vice. Un avertissement."},
            (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Tête du Dragon. Nouveaux départs."},
            (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Queue du Dragon. Fins et achèvement karmique."}
        }
    }
}

# --- Functions ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_fig_html(fig_list, name=""):
    """Creates a beautiful HTML representation of a geomantic figure."""
    rows_html = ""
    for r in fig_list:
        dots = "●" if r == 1 else "● ●"
        rows_html += f"<div style='font-size: 24px; color: #D4AF37; line-height: 1;'>{dots}</div>"
    
    return f"""
    <div style="border: 1px solid #444; border-radius: 10px; padding: 15px; background: #1a1a1a; text-align: center; box-shadow: 2px 2px 10px rgba(0,0,0,0.5);">
        <div style="font-weight: bold; color: #E0E0E0; margin-bottom: 5px;">{name}</div>
        {rows_html}
    </div>
    """

def process_input(input_str):
    clean_str = input_str.replace(" ", "")
    if not clean_str: return None
    return 1 if len(clean_str) % 2 != 0 else 2

# --- App UI ---
st.set_page_config(page_title="Geomancy Oracle", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #D4AF37 !important; font-family: 'Garamond', serif; }
    .stTextInput input { background-color: #1a1a1a; color: #D4AF37; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

sel_lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])
T = LANGS[sel_lang]

st.title(T["title"])
st.write(f"*{T['desc']}*")

# Input Section
with st.container():
    mothers_input = []
    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            st.markdown(f"### M{i+1}")
            r1 = st.text_input(f"L1", key=f"m{i}r1")
            r2 = st.text_input(f"L2", key=f"m{i}r2")
            r3 = st.text_input(f"L3", key=f"m{i}r3")
            r4 = st.text_input(f"L4", key=f"m{i}r4")
            mothers_input.append([r1, r2, r3, r4])

st.markdown("<br>", unsafe_allow_html=True)

if st.button(T["calc_btn"], use_container_width=True):
    M = []
    error = False
    for m_idx, m_rows in enumerate(mothers_input):
        processed_m = [process_input(r) for r in m_rows]
        if None in processed_m:
            st.error(f"Mother {m_idx+1} {T['error_msg']}")
            error = True
            break
        M.append(processed_m)
    
    if not error:
        D = [[M[j][i] for j in range(4)] for i in range(4)]
        N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
        RW = add_figs(N[0], N[1])
        LW = add_figs(N[2], N[3])
        Judge = add_figs(RW, LW)
        Reconciler = add_figs(Judge, M[0])

        st.divider()
        
        # Main Display
        st.header(T["court"])
        c1, c2, c3 = st.columns([1, 1, 2])
        
        with c1:
            st.markdown(render_fig_html(RW, "Witness R"), unsafe_allow_html=True)
            st.write(f"**{T['figures'][tuple(RW)]['name']}**")
        
        with c2:
            st.markdown(render_fig_html(LW, "Witness L"), unsafe_allow_html=True)
            st.write(f"**{T['figures'][tuple(LW)]['name']}**")

        with c3:
            j_data = T["figures"][tuple(Judge)]
            st.markdown(render_fig_html(Judge, T["judge"]), unsafe_allow_html=True)
            st.success(f"### {j_data['name']}\n{j_data['meaning']}")

        st.divider()
        
        # Reconciler
        st.header(T["reconciler"])
        r_col1, r_col2 = st.columns([1, 4])
        with r_col1:
            st.markdown(render_fig_html(Reconciler), unsafe_allow_html=True)
        with r_col2:
            r_data = T["figures"][tuple(Reconciler)]
            st.info(f"**{r_data['name']}**: {r_data['meaning']}")
