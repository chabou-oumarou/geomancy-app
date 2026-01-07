import streamlit as st

# --- 1. FULL TRANSLATION & DATA MAP ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {"name": "Via", "element": "Water", "meaning": {"EN": "Change and movement. Success through moving forward.", "FR": "Changement et mouvement. Succès en allant de l'avant."}},
    (2, 2, 2, 2): {"name": "Populus", "element": "Water", "meaning": {"EN": "The Crowd. Stability, neutrality, and following the flow.", "FR": "La Foule. Stabilité, neutralité et suivre le flux."}},
    (2, 1, 1, 2): {"name": "Conjunctio", "element": "Air", "meaning": {"EN": "The Junction. Union, contracts, and social interactions.", "FR": "La Jonction. Union, contrats et interactions sociales."}},
    (1, 2, 2, 1): {"name": "Carcer", "element": "Earth", "meaning": {"EN": "The Prison. Delays, boundaries, and necessary restriction.", "FR": "La Prison. Délais, limites et restrictions nécessaires."}},
    (2, 2, 1, 1): {"name": "Fortuna Major", "element": "Earth", "meaning": {"EN": "Greater Fortune. Massive success and inner protection.", "FR": "Grande Fortune. Succès massif et protection intérieure."}},
    (1, 1, 2, 2): {"name": "Fire", "element": "Fire", "meaning": {"EN": "Lesser Fortune. Quick success; speed over depth.", "FR": "Petite Fortune. Succès rapide ; la vitesse prime sur la profondeur."}},
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
        "title": "Celestial Oracle", "subtitle": "Modern Geomancy Portal", "btn": "Cast the Divine Shield",
        "mother_tab": "Mother", "row": "Row", "foundation": "I. The Foundation",
        "nephews": "II. The Nephews", "court": "III. The Verdict",
        "witness_r": "Right Witness", "witness_l": "Left Witness", "judge": "The Judge",
        "reconciler": "The Reconciler", "element": "Element", "error": "Fill all fields."
    },
    "FR": {
        "title": "Oracle Céleste", "subtitle": "Portail de Géomancie Moderne", "btn": "Générer le Blason Divin",
        "mother_tab": "Mère", "row": "Ligne", "foundation": "I. La Fondation",
        "nephews": "II. Les Neveux", "court": "III. Le Verdict",
        "witness_r": "Témoin Droit", "witness_l": "Témoin Gauche", "judge": "Le Juge",
        "reconciler": "Le Réconciliateur", "element": "Élément", "error": "Remplissez tous les champs."
    }
}

# --- 2. LOGIC FUNCTIONS ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_card(fig, label, color, size="35px", glow=False):
    """Renders dots significantly larger and spaced for readability."""
    glow_style = f"box-shadow: 0 10px 40px {color}44;" if glow else "box-shadow: 0 4px 20px rgba(0,0,0,0.06);"
    
    # Using larger Unicode dots and non-breaking spaces for the dash
    rows = "".join([f"<div style='font-size: {size}; color: {color}; line-height: 1; margin: 4px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;&nbsp;&nbsp;●'}</div>" for r in fig])
    
    return f"""
    <div style="background: white; border: 1px solid #f0f0f0; border-radius: 24px; padding: 25px; 
                text-align: center; {glow_style} transition: transform 0.2s ease;">
        <div style="font-size: 0.7rem; color: #a0a0a0; font-weight: 800; text-transform: uppercase; margin-bottom: 15px; letter-spacing: 2px;">{label}</div>
        {rows}
    </div>
    """

def process_input(s):
    clean = s.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- 3. APP UI ---
st.set_page_config(page_title="Celestial Oracle", layout="wide")

lang_choice = st.sidebar.selectbox("Language / Langue", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]

# Platinum Theme CSS Updates
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] { 
        background-color: #fcfdfe;
        font-family: 'Outfit', sans-serif;
        color: #1e272e;
    }
    h1 { font-weight: 800; color: #1e272e !important; text-align: center; font-size: 3.5rem !important; margin-bottom: 0px !important;}
    .stTextInput input { 
        background: #f8f9fa; border: 2px solid #edf0f2; border-radius: 16px; 
        color: #2f3542; text-align: center; font-weight: 600; height: 55px; font-size: 1.1rem;
    }
    .stTabs [data-baseweb="tab"] { font-size: 1.1rem; padding: 10px 20px; }
    .stButton>button { 
        border-radius: 20px !important; height: 60px !important; font-size: 1.2rem !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); transition: all 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

st.title(T["title"])
st.markdown(f"<p style='text-align: center; color: #888; font-size: 1.2rem; margin-top: -5px;'>{T['subtitle']}</p>", unsafe_allow_html=True)

# Input Section
st.markdown("<br>", unsafe_allow_html=True)
mothers_input = []
tabs = st.tabs([f"{T['mother_tab']} {i+1}" for i in range(4)])
for i in range(4):
    with tabs[i]:
        cols = st.columns(4)
        m_rows = []
        for j in range(4):
            m_rows.append(cols[j].text_input(f"{T['row']} {j+1}", key=f"m{i}r{j}", placeholder="••••"))
        mothers_input.append(m_rows)

st.markdown("<br>", unsafe_allow_html=True)

if st.button(T["btn"], use_container_width=True, type="primary"):
    M = []
    for i, rows in enumerate(mothers_input):
        proc = [process_input(r) for r in rows]
        if None in proc:
            st.error(T["error"])
            st.stop()
        M.append(proc)
    
    # Derivations
    D = [[M[j][i] for j in range(4)] for i in range(4)]
    N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
    RW, LW = add_figs(N[0], N[1]), add_figs(N[2], N[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M[0])
    
    # Dynamic Elements
    rec_data = GEOMANTIC_DATA[tuple(Reconciler)]
    colors = {"Fire": "#FF4757", "Air": "#546de5", "Water": "#1abc9c", "Earth": "#f39c12"}
    C = colors.get(rec_data["element"], "#546de5")

    st.markdown(f"<style>h2, h3 {{ color: {C} !important; }} .stButton>button {{ background: {C} !important; border: none !important; }}</style>", unsafe_allow_html=True)

    # 1. Foundation
    st.header(T["foundation"])
    f_cols = st.columns(8)
    all_f = M + D
    for i, fig in enumerate(all_f):
        label = f"{'M' if i < 4 else 'D'}{i+1 if i < 4 else i-3}"
        f_cols[i].markdown(render_card(fig, label, C, size="28px"), unsafe_allow_html=True)
        f_cols[i].caption(f"<center><b>{GEOMANTIC_DATA[tuple(fig)]['name']}</b></center>", unsafe_allow_html=True)

    # 2. Nephews
    st.header(T["nephews"])
    n_cols = st.columns(4)
    for i, fig in enumerate(N):
        n_cols[i].markdown(render_card(fig, f"N{i+1}", C, size="32px"), unsafe_allow_html=True)
        n_cols[i].caption(f"<center><b>{GEOMANTIC_DATA[tuple(fig)]['name']}</b></center>", unsafe_allow_html=True)

    # 3. Court
    st.divider()
    st.header(T["court"])
    
    wit1, wit2 = st.columns(2)
    wit1.markdown(render_card(RW, T["witness_r"], C, size="40px"), unsafe_allow_html=True)
    wit2.markdown(render_card(LW, T["witness_l"], C, size="40px"), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    res_j, res_r = st.columns(2)
    
    with res_j:
        j_info = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(render_card(Judge, T["judge"], C, size="55px", glow=True), unsafe_allow_html=True)
        st.markdown(f"<div style='background: white; padding: 30px; border-radius: 28px; border-bottom: 6px solid {C}; box-shadow: 0 10px 30px rgba(0,0,0,0.04);'><h3>{j_info['name']}</h3>{j_info['meaning'][L]}</div>", unsafe_allow_html=True)
        
    with res_r:
        st.markdown(render_card(Reconciler, T["reconciler"], C, size="55px", glow=True), unsafe_allow_html=True)
        st.markdown(f"<div style='background: white; padding: 30px; border-radius: 28px; border-bottom: 6px solid {C}; box-shadow: 0 10px 30px rgba(0,0,0,0.04);'><h3>{rec_data['name']}</h3><span style='color:{C}; font-weight:800;'>{T['element']}: {rec_data['element']}</span><br><br>{rec_data['meaning'][L]}</div>", unsafe_allow_html=True)
