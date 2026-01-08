import streamlit as st

# --- 1. DATA MAP (Figures, Elements, Meanings) ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {"name": "Via", "element": "Water", "meaning": {"EN": "Change and movement. Success through moving forward.", "FR": "Changement et mouvement. Succès en allant de l'avant."}},
    (2, 2, 2, 2): {"name": "Populus", "element": "Water", "meaning": {"EN": "The Crowd. Stability, neutrality, and following the flow.", "FR": "La Foule. Stabilité, neutralité et suivre le flux."}},
    (2, 1, 1, 2): {"name": "Conjunctio", "element": "Air", "meaning": {"EN": "The Junction. Union, contracts, and social interactions.", "FR": "La Jonction. Union, contrats et interactions sociales."}},
    (1, 2, 2, 1): {"name": "Carcer", "element": "Earth", "meaning": {"EN": "The Prison. Delays, boundaries, and necessary restriction.", "FR": "La Prison. Délais, limites et restrictions nécessaires."}},
    (2, 2, 1, 1): {"name": "Fortuna Major", "element": "Earth", "meaning": {"EN": "Greater Fortune. Massive success and inner protection.", "FR": "Grande Fortune. Succès massif et protection intérieure."}},
    (1, 1, 2, 2): {"name": "Fortuna Minor", "element": "Fire", "meaning": {"EN": "Lesser Fortune. Quick success; speed over depth.", "FR": "Petite Fortune. Succès rapide ; la vitesse prime sur la profondeur."}},
    (2, 1, 2, 1): {"name": "Acquisitio", "element": "Air", "meaning": {"EN": "Gain. Financial profit and spiritual growth.", "FR": "Gain. Profit financier et croissance spirituelle."}},
    (1, 2, 1, 2): {"name": "Amissio", "element": "Fire", "meaning": {"EN": "Loss. Spending or letting go for a greater cause.", "FR": "Perte. Dépense ou lâcher-prise pour une cause plus grande."}},
    (1, 2, 2, 2): {"name": "Laetitia", "element": "Air", "meaning": {"EN": "Joy. Health, happiness, and positive news.", "FR": "La Joie. Santé, bonheur et nouvelles positives."}},
    (2, 2, 2, 1): {"name": "Tristitia", "element": "Earth", "meaning": {"EN": "Sorrow. Heavy energy, foundations, and building low.", "FR": "La Tristesse. Énergie lourde, fondations et discrétion."}},
    (1, 2, 1, 1): {"name": "Puella", "element": "Water", "meaning": {"EN": "The Girl. Beauty, harmony, and pleasant interactions.", "FR": "La Jeune Fille. Beauté, harmonie et interactions plaisantes."}},
    (1, 1, 2, 1): {"name": "Puer", "element": "Fire", "meaning": {"EN": "The Boy. Energy, aggression, and impulsive bold action.", "FR": "Le Garçon. Énergie, agression et action audacieuse."}},
    (2, 2, 1, 2): {"name": "Albus", "element": "Air", "meaning": {"EN": "White. Peace, wisdom, and clear communication.", "FR": "Le Blanc. Paix, sagesse et communication claire."}},
    (2, 1, 2, 2): {"name": "Rubeus", "element": "Fire", "meaning": {"EN": "Red. Passion and vice. A warning to pause.", "FR": "Le Rouge. Passion et vice. Un avertissement de pause."}},
    (2, 1, 1, 1): {"name": "Caput Draconis", "element": "Earth", "meaning": {"EN": "Dragon's Head. New beginnings and entry points.", "FR": "Tête du Dragon. Nouveaux départs et points d'entrée."}},
    (1, 1, 1, 2): {"name": "Cauda Draconis", "element": "Fire", "meaning": {"EN": "Dragon's Tail. Endings and karmic exit points.", "FR": "Queue du Dragon. Fins et achèvement karmique."}}
}

UI_TEXT = {
    "EN": {
        "title": "The Maroon Oracle", "subtitle": "Classical Science of the Sands", "btn": "Generate Full 16-Figure Shield",
        "mother": "Mother", "daughter": "Daughter", "nephew": "Nephew", "row": "Row",
        "foundation": "I. The Foundation (Mothers & Daughters)", "nephews_sec": "II. The Nephews", "court": "III. The Verdict",
        "witness_r": "Right Witness", "witness_l": "Left Witness", "judge": "The Judge",
        "reconciler": "The Reconciler", "error": "Incomplete! Please fill all 16 rows.", "reset": "Reset All Inputs"
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Science Classique des Sables", "btn": "Générer le Blason Complet (16 Figures)",
        "mother": "Mère", "daughter": "Fille", "nephew": "Neveu", "row": "Ligne",
        "foundation": "I. La Fondation (Mères & Filles)", "nephews_sec": "II. Les Neveux", "court": "III. Le Verdict",
        "witness_r": "Témoin Droit", "witness_l": "Témoin Gauche", "judge": "Le Juge",
        "reconciler": "Le Réconciliateur", "error": "Incomplet ! Veuillez remplir les 16 lignes.", "reset": "Réinitialiser Tout"
    }
}

MAROON = "#800000"

# --- 2. CORE LOGIC FUNCTIONS ---
def add_figs(f1, f2):
    """Geomantic Addition: Even+Even=Even, Odd+Odd=Even, Odd+Even=Odd."""
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_dot_mirror(input_str):
    """Live visual feedback for dot inputs."""
    clean = input_str.replace(" ", "")
    if not clean: return "<div style='height:25px;'></div>"
    dots = "● " * len(clean)
    return f"<div style='color: {MAROON}; font-size: 1.2rem; margin-top: -15px; margin-bottom: 5px;'>{dots}</div>"

def render_card(fig, label, color=MAROON, size="35px", glow=False):
    """Renders the geomantic figure card with large, readable maroon dots."""
    glow_style = f"box-shadow: 0 10px 40px {color}33;" if glow else "box-shadow: 0 4px 15px rgba(0,0,0,0.05);"
    rows = "".join([f"<div style='font-size: {size}; color: {color}; line-height: 1.1; margin: 4px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;&nbsp;&nbsp;●'}</div>" for r in fig])
    return f"""
    <div style="background: white; border: 1px solid #edf0f2; border-radius: 20px; padding: 20px; text-align: center; {glow_style}">
        <div style="font-size: 0.65rem; color: #a0a0a0; font-weight: 800; text-transform: uppercase; margin-bottom: 12px; letter-spacing: 1.5px;">{label}</div>
        {rows}
    </div>
    """

def process_input(s):
    """Determines parity (1 or 2) from string length."""
    clean = s.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- 3. APP UI ---
st.set_page_config(page_title="Maroon Oracle", layout="wide")

# Theme CSS
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;800&display=swap');
    html, body, [data-testid="stAppViewContainer"] {{ background-color: #f8fafc; font-family: 'Outfit', sans-serif; color: #1e272e; }}
    h1 {{ font-weight: 800; color: #1e272e !important; text-align: center; font-size: 3.2rem !important; margin-bottom: 0px !important; }}
    h2 {{ color: {MAROON} !important; border-bottom: 2px solid #edf0f2; padding-bottom: 10px; margin-top: 40px !important; }}
    .stTextInput input {{ border-radius: 12px; border: 2px solid #edf0f2; height: 45px; text-align: center; font-weight: 600; }}
    .stButton>button {{ background: {MAROON} !important; color: white !important; border-radius: 20px !important; height: 65px !important; font-weight: 700 !important; font-size: 1.2rem !important; border: none !important; margin-top: 20px; }}
    </style>
    """, unsafe_allow_html=True)

# Sidebar
lang_choice = st.sidebar.selectbox("🌐 Language / Langue", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]

if st.sidebar.button(T["reset"]):
    st.rerun()

st.title(T["title"])
st.markdown(f"<p style='text-align: center; color: #888; font-size: 1.1rem;'>{T['subtitle']}</p>", unsafe_allow_html=True)

# --- THE RITUAL INPUT SECTION ---
st.markdown("<br>", unsafe_allow_html=True)
mothers_input = []
tabs = st.tabs([f"{T['mother_tab']} {i+1}" for i in range(4)])

for i in range(4):
    with tabs[i]:
        cols = st.columns(4)
        m_rows = []
        for j in range(4):
            with cols[j]:
                val = st.text_input(f"{T['row']} {j+1}", key=f"m{i}r{j}")
                st.markdown(render_dot_mirror(val), unsafe_allow_html=True)
                m_rows.append(val)
        mothers_input.append(m_rows)

# --- EXECUTION ---
if st.button(T["btn"], use_container_width=True, type="primary"):
    # 1. Process Mothers
    M_figs = []
    for i, rows in enumerate(mothers_input):
        proc = [process_input(r) for r in rows]
        if None in proc:
            st.error(T["error"]); st.stop()
        M_figs.append(proc)
    
    # 2. Derive Daughters (Transposition)
    D_figs = [[M_figs[j][i] for j in range(4)] for i in range(4)]
    
    # 3. Derive Nephews
    N_figs = [
        add_figs(M_figs[0], M_figs[1]), # N1
        add_figs(M_figs[2], M_figs[3]), # N2
        add_figs(D_figs[0], D_figs[1]), # N3
        add_figs(D_figs[2], D_figs[3])  # N4
    ]
    
    # 4. Derive Witnesses, Judge, and Reconciler
    RW = add_figs(N_figs[0], N_figs[1])
    LW = add_figs(N_figs[2], N_figs[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M_figs[0])

    # --- DISPLAYING THE 16 FIGURES ---

    # I. FOUNDATION (M1-M4, D1-D4)
    st.header(T["foundation"])
    f_cols = st.columns(8)
    for i in range(4):
        f_cols[i].markdown(render_card(M_figs[i], f"M{i+1}"), unsafe_allow_html=True)
        f_cols[i].caption(f"<center><b>{GEOMANTIC_DATA[tuple(M_figs[i])]['name']}</b></center>", unsafe_allow_html=True)
    for i in range(4):
        f_cols[i+4].markdown(render_card(D_figs[i], f"D{i+1}"), unsafe_allow_html=True)
        f_cols[i+4].caption(f"<center><b>{GEOMANTIC_DATA[tuple(D_figs[i])]['name']}</b></center>", unsafe_allow_html=True)

    # II. NEPHEWS (N1-N4)
    st.header(T["nephews_sec"])
    n_cols = st.columns(4)
    for i in range(4):
        n_cols[i].markdown(render_card(N_figs[i], f"N{i+1}", size="40px"), unsafe_allow_html=True)
        n_cols[i].caption(f"<center><b>{GEOMANTIC_DATA[tuple(N_figs[i])]['name']}</b></center>", unsafe_allow_html=True)

    # III. THE COURT (Witnesses, Judge, Reconciler)
    st.header(T["court"])
    
    # Witnesses
    w_cols = st.columns(2)
    w_cols[0].markdown(render_card(RW, T["witness_r"], size="45px"), unsafe_allow_html=True)
    w_cols[1].markdown(render_card(LW, T["witness_l"], size="45px"), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Final Two
    res_j, res_r = st.columns(2)
    with res_j:
        j_info = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(render_card(Judge, T["judge"], size="60px", glow=True), unsafe_allow_html=True)
        st.markdown(f"<div style='background: white; padding: 25px; border-radius: 24px; border-bottom: 6px solid {MAROON}; box-shadow: 0 4px 15px rgba(0,0,0,0.05);'><h3>{j_info['name']}</h3>{j_info['meaning'][L]}</div>", unsafe_allow_html=True)
    
    with res_r:
        r_info = GEOMANTIC_DATA[tuple(Reconciler)]
        st.markdown(render_card(Reconciler, T["reconciler"], size="60px", glow=True), unsafe_allow_html=True)
        st.markdown(f"<div style='background: white; padding: 25px; border-radius: 24px; border-bottom: 6px solid {MAROON}; box-shadow: 0 4px 15px rgba(0,0,0,0.05);'><h3>{r_info['name']}</h3><b>{r_info['element']}</b><br><br>{r_info['meaning'][L]}</div>", unsafe_allow_html=True)
