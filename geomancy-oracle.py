import streamlit as st

# --- Translation & Figure Data ---
LANGS = {
    "English": {
        "title": "🔮 The Celestial Geomancy Oracle",
        "desc": "Traditional 'Science of the Sands'. Type random dots in the boxes below to cast your destiny.",
        "calc_btn": "Cast the Divine Shield",
        "error_msg": "is incomplete. Please fill all rows.",
        "foundation": "The Foundation",
        "nephews": "The Nephews (Results)",
        "court": "⚖️ The Sacred Court",
        "judge": "The Judge",
        "reconciler": "The Reconciler",
        "view_shield": "View Full Shield (Mothers & Daughters)",
        "figures": {
            (1, 1, 1, 1): {"name": "Via", "meaning": "Change and movement. Success through moving forward."},
            (2, 2, 2, 2): {"name": "Populus", "meaning": "The Crowd. Stability, neutrality, and following the flow."},
            (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "The Junction. Union, contracts, and social interactions."},
            (1, 2, 2, 1): {"name": "Carcer", "meaning": "The Prison. Delays, boundaries, and necessary restriction."},
            (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Greater Fortune. Massive success and inner protection."},
            (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Lesser Fortune. Quick, external success; speed over depth."},
            (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Financial profit and spiritual growth."},
            (1, 2, 1, 2): {"name": "Amissio", "meaning": "Loss. Spending or letting go for a greater cause."},
            (1, 2, 2, 2): {"name": "Laetitia", "meaning": "Joy. Health, happiness, and positive news."},
            (2, 2, 2, 1): {"name": "Tristitia", "meaning": "Sorrow. Heavy energy, foundations, and building low."},
            (1, 2, 1, 1): {"name": "Puella", "meaning": "The Girl. Beauty, harmony, and pleasant interactions."},
            (1, 1, 2, 1): {"name": "Puer", "meaning": "The Boy. Energy, aggression, and impulsive bold action."},
            (2, 2, 1, 2): {"name": "Albus", "meaning": "White. Peace, wisdom, and clear communication."},
            (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Red. Passion and vice. A warning to pause and reflect."},
            (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Dragon's Head. New beginnings and entry points."},
            (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Dragon's Tail. Endings and karmic exit points."}
        }
    },
    "Français": {
        "title": "🔮 L'Oracle de Géomancie Céleste",
        "desc": "La 'Science des Sables' traditionnelle. Tapez des points au hasard pour créer vos figures.",
        "calc_btn": "Lancer le Blason Divin",
        "error_msg": "est incomplète. Remplissez toutes les lignes.",
        "foundation": "La Fondation",
        "nephews": "Les Neveux (Résultats)",
        "court": "⚖️ Le Tribunal Sacré",
        "judge": "Le Juge",
        "reconciler": "Le Réconciliateur",
        "view_shield": "Voir le Blason Complet (Mères & Filles)",
        "figures": {
            (1, 1, 1, 1): {"name": "Via", "meaning": "Changement et mouvement. Succès en allant de l'avant."},
            (2, 2, 2, 2): {"name": "Populus", "meaning": "La Foule. Stabilité, neutralité et suivre le flux."},
            (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "La Jonction. Union, contrats et interactions sociales."},
            (1, 2, 2, 1): {"name": "Carcer", "meaning": "La Prison. Délais, limites et restrictions nécessaires."},
            (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Grande Fortune. Succès massif et protection intérieure."},
            (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Petite Fortune. Succès rapide et extérieur."},
            (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Profit financier et croissance spirituelle."},
            (1, 2, 1, 2): {"name": "Amissio", "meaning": "Perte. Dépense ou lâcher-prise pour une cause plus grande."},
            (1, 2, 2, 2): {"name": "Laetitia", "meaning": "La Joie. Santé, bonheur et nouvelles positives."},
            (2, 2, 2, 1): {"name": "Tristitia", "meaning": "La Tristesse. Énergie lourde, fondations et discrétion."},
            (1, 2, 1, 1): {"name": "Puella", "meaning": "La Jeune Fille. Beauté, harmonie et interactions plaisantes."},
            (1, 1, 2, 1): {"name": "Puer", "meaning": "Le Garçon. Énergie, agression et action audacieuse."},
            (2, 2, 1, 2): {"name": "Albus", "meaning": "Le Blanc. Paix, sagesse et communication claire."},
            (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Le Rouge. Passion et vice. Un avertissement de pause."},
            (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Tête du Dragon. Nouveaux départs et points d'entrée."},
            (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Queue du Dragon. Fins et achèvement karmique."}
        }
    }
}

# --- Core Logic ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_fig_html(fig_list, name=""):
    rows_html = ""
    for r in fig_list:
        dots = "●" if r == 1 else "● ●"
        rows_html += f"<div style='font-size: 22px; color: #D4AF37; margin: 2px 0;'>{dots}</div>"
    return f"""
    <div style="border: 1px solid #444; border-radius: 12px; padding: 15px; background: #1a1a1a; text-align: center; margin-bottom: 10px;">
        <div style="font-size: 0.8em; color: #888; text-transform: uppercase; letter-spacing: 1px;">{name}</div>
        {rows_html}
    </div>
    """

def process_input(input_str):
    clean = input_str.replace(" ", "")
    if not clean: return None
    return 1 if len(clean) % 2 != 0 else 2

# --- UI Setup ---
st.set_page_config(page_title="Geomancy Oracle", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; }
    .stTextInput input { background-color: #1a1a1a; color: #D4AF37; border: 1px solid #444; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

sel_lang = st.sidebar.selectbox("🌐 Language / Langue", ["English", "Français"])
T = LANGS[sel_lang]

st.title(T["title"])
st.write(f"<center>*{T['desc']}*</center>", unsafe_allow_html=True)

# 1. Inputs for the 4 Mothers
st.markdown("---")
mothers_input = []
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.markdown(f"### M{i+1}")
        r1 = st.text_input(f"Row 1", key=f"m{i}r1", label_visibility="collapsed", placeholder="....")
        r2 = st.text_input(f"Row 2", key=f"m{i}r2", label_visibility="collapsed", placeholder="..")
        r3 = st.text_input(f"Row 3", key=f"m{i}r3", label_visibility="collapsed", placeholder="...")
        r4 = st.text_input(f"Row 4", key=f"m{i}r4", label_visibility="collapsed", placeholder=".")
        mothers_input.append([r1, r2, r3, r4])

st.markdown("<br>", unsafe_allow_html=True)

if st.button(T["calc_btn"], use_container_width=True, type="primary"):
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
        # Calculations
        D = [[M[j][i] for j in range(4)] for i in range(4)]
        N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
        RW = add_figs(N[0], N[1])
        LW = add_figs(N[2], N[3])
        Judge = add_figs(RW, LW)
        Reconciler = add_figs(Judge, M[0])

        # --- RESULTS DISPLAY ---
        
        # A. The Court (The Verdict)
        st.header(T["court"])
        c1, c2, c3 = st.columns([1, 1, 2])
        with c1:
            st.markdown(render_fig_html(RW, "Right Witness"), unsafe_allow_html=True)
            st.caption(f"<center><b>{T['figures'][tuple(RW)]['name']}</b></center>", unsafe_allow_html=True)
        with c2:
            st.markdown(render_fig_html(LW, "Left Witness"), unsafe_allow_html=True)
            st.caption(f"<center><b>{T['figures'][tuple(LW)]['name']}</b></center>", unsafe_allow_html=True)
        with c3:
            j_data = T["figures"][tuple(Judge)]
            st.markdown(render_fig_html(Judge, T["judge"]), unsafe_allow_html=True)
            st.success(f"### {j_data['name']}\n{j_data['meaning']}")

        # B. The Reconciler
        st.divider()
        st.header(T["reconciler"])
        r_col1, r_col2 = st.columns([1, 3])
        with r_col1:
            st.markdown(render_fig_html(Reconciler), unsafe_allow_html=True)
        with r_col2:
            r_data = T["figures"][tuple(Reconciler)]
            st.info(f"**{r_data['name']}**: {r_data['meaning']}")

        # C. Full Foundation & Nephews
        st.divider()
        with st.expander(T["view_shield"]):
            # Display Mothers and Daughters
            st.subheader(T["foundation"])
            f_cols = st.columns(8)
            all_f = M + D
            for i, fig in enumerate(all_f):
                label = f"M{i+1}" if i < 4 else f"D{i-3}"
                f_cols[i].markdown(render_fig_html(fig, label), unsafe_allow_html=True)
                f_cols[i].caption(f"<center>{T['figures'][tuple(fig)]['name']}</center>", unsafe_allow_html=True)
            
            # Display Nephews
            st.subheader(T["nephews"])
            n_cols = st.columns(4)
            for i in range(4):
                n_cols[i].markdown(render_fig_html(N[i], f"N{i+1}"), unsafe_allow_html=True)
                n_cols[i].caption(f"<center>{T['figures'][tuple(N[i])]['name']}</center>", unsafe_allow_html=True)
