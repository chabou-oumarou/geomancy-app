import streamlit as st

# --- Translation Dictionary ---
LANGS = {
    "English": {
        "title": "🔮 The Complete Geomantic Oracle",
        "desc": "Type random dots or marks in the fields below to cast your figures.",
        "calc_btn": "Calculate The Shield",
        "error_msg": "is incomplete. Please add dots to all rows.",
        "foundation": "The Foundation (Mothers & Daughters)",
        "court": "⚖️ The Court",
        "judge": "The Judge",
        "reconciler": "The Reconciler",
        "verdict": "Verdict",
        "insight": "Final Insight",
        "view_all": "View Full Foundation (Mothers & Daughters)",
        "placeholder": "e.g. ....",
        "figures": {
            (1, 1, 1, 1): {"name": "Via", "meaning": "Change and movement. Success through moving forward."},
            (2, 2, 2, 2): {"name": "Populus", "meaning": "The Crowd. Neutrality, following the flow."},
            (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "The Junction. Coming together, contracts, and social interactions."},
            (1, 2, 2, 1): {"name": "Carcer", "meaning": "The Prison. Delays, boundaries, and restriction."},
            (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Greater Fortune. Massive success and protection."},
            (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Lesser Fortune. Quick, external success."},
            (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Financial profit and growth."},
            (1, 2, 1, 2): {"name": "Amissio", "meaning": "Loss. Spending or letting go."},
            (1, 2, 2, 2): {"name": "Laetitia", "meaning": "Joy. Health, happiness, and positive news."},
            (2, 2, 2, 1): {"name": "Tristitia", "meaning": "Sorrow. Heavy energy, foundations, and staying low."},
            (1, 2, 1, 1): {"name": "Puella", "meaning": "The Girl. Beauty, harmony, and pleasant social interactions."},
            (1, 1, 2, 1): {"name": "Puer", "meaning": "The Boy. Energy, aggression, and impulsive action."},
            (2, 2, 1, 2): {"name": "Albus", "meaning": "White. Peace, wisdom, and clear communication."},
            (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Red. Passion and vice. A warning to pause."},
            (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Dragon's Head. New beginnings and entry points."},
            (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Dragon's Tail. Endings and exit points."}
        }
    },
    "Français": {
        "title": "🔮 L'Oracle de Géomancie Classique",
        "desc": "Tapez des points ou des marques au hasard dans les champs ci-dessous pour créer vos figures.",
        "calc_btn": "Calculer le Blason",
        "error_msg": "est incomplète. Veuillez ajouter des points à toutes les lignes.",
        "foundation": "La Fondation (Mères & Filles)",
        "court": "⚖️ Le Tribunal",
        "judge": "Le Juge",
        "reconciler": "Le Réconciliateur",
        "verdict": "Verdict",
        "insight": "Dernier Aperçu",
        "view_all": "Voir la Fondation Complète (Mères & Filles)",
        "placeholder": "ex: ....",
        "figures": {
            (1, 1, 1, 1): {"name": "Via", "meaning": "Changement et mouvement. Succès en allant de l'avant."},
            (2, 2, 2, 2): {"name": "Populus", "meaning": "La Foule. Neutralité, suivre le flux."},
            (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "La Jonction. Union, contrats et interactions sociales."},
            (1, 2, 2, 1): {"name": "Carcer", "meaning": "La Prison. Délais, limites et restrictions."},
            (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Grande Fortune. Succès massif et protection."},
            (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Petite Fortune. Succès rapide et extérieur."},
            (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Profit financier et croissance."},
            (1, 2, 1, 2): {"name": "Amissio", "meaning": "Perte. Dépense ou lâcher-prise."},
            (1, 2, 2, 2): {"name": "Laetitia", "meaning": "La Joie. Santé, bonheur et nouvelles positives."},
            (2, 2, 2, 1): {"name": "Tristitia", "meaning": "La Tristesse. Énergie lourde, fondations et discrétion."},
            (1, 2, 1, 1): {"name": "Puella", "meaning": "La Jeune Fille. Beauté, harmonie et interactions plaisantes."},
            (1, 1, 2, 1): {"name": "Puer", "meaning": "Le Garçon. Énergie, agression et action impulsive."},
            (2, 2, 1, 2): {"name": "Albus", "meaning": "Le Blanc. Paix, sagesse et communication claire."},
            (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Le Rouge. Passion et vice. Un avertissement de pause."},
            (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Queue du Dragon. Nouveaux départs et points d'entrée."},
            (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Tête du Dragon. Fins et points de sortie."}
        }
    }
}

def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_fig(fig_list):
    visual = ""
    for r in fig_list:
        visual += "  ●  \n" if r == 1 else "●   ●\n"
    return visual

def process_input(input_str):
    clean_str = input_str.replace(" ", "")
    if not clean_str: return None
    return 1 if len(clean_str) % 2 != 0 else 2

# --- App UI ---
st.set_page_config(page_title="Geomancy Oracle", layout="wide")

# Language Selector
sel_lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])
T = LANGS[sel_lang]

st.title(T["title"])
st.write(T["desc"])

# Input Layout for 4 Mothers
mothers_input = []
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.subheader(f"Mother {i+1}" if sel_lang == "English" else f"Mère {i+1}")
        r1 = st.text_input(f"M{i+1} L1", key=f"m{i}r1", placeholder=T["placeholder"])
        r2 = st.text_input(f"M{i+1} L2", key=f"m{i}r2", placeholder=T["placeholder"])
        r3 = st.text_input(f"M{i+1} L3", key=f"m{i}r3", placeholder=T["placeholder"])
        r4 = st.text_input(f"M{i+1} L4", key=f"m{i}r4", placeholder=T["placeholder"])
        mothers_input.append([r1, r2, r3, r4])

if st.button(T["calc_btn"], type="primary"):
    M = []
    error = False
    for m_idx, m_rows in enumerate(mothers_input):
        processed_m = [process_input(r) for r in m_rows]
        if None in processed_m:
            m_label = "Mother" if sel_lang == "English" else "Mère"
            st.error(f"{m_label} {m_idx+1} {T['error_msg']}")
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
        
        # Court Display
        st.header(T["court"])
        res_c1, res_c2, res_c3 = st.columns([1, 1, 2])
        
        with res_c1:
            st.subheader("Witness/Témoin R")
            st.text(render_fig(RW))
            st.write(T["figures"][tuple(RW)]["name"])
        
        with res_c2:
            st.subheader("Witness/Témoin L")
            st.text(render_fig(LW))
            st.write(T["figures"][tuple(LW)]["name"])

        with res_c3:
            st.subheader(T["judge"])
            st.text(render_fig(Judge))
            j_data = T["figures"][tuple(Judge)]
            st.success(f"**{j_data['name']}**: {j_data['meaning']}")

        st.divider()
        
        # Reconciler
        st.header(T["reconciler"])
        r_col1, r_col2 = st.columns([1, 4])
        with r_col1:
            st.text(render_fig(Reconciler))
        with r_col2:
            r_data = T["figures"][tuple(Reconciler)]
            st.info(f"**{r_data['name']}**: {r_data['meaning']}")

        with st.expander(T["view_all"]):
            f_cols = st.columns(8)
            all_f = M + D
            for i, fig in enumerate(all_f):
                label = f"M{i+1}" if i < 4 else f"D{i-3}"
                f_cols[i].markdown(f"**{label}**")
                f_cols[i].text(render_fig(fig))
                f_cols[i].caption(T["figures"][tuple(fig)]["name"])
