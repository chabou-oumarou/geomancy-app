import streamlit as st

# --- 1. FULL TRANSLATION & DATA MAP ---
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
        "title": "Celestial Oracle", "subtitle": "Modern Geomancy Portal", "btn": "Cast the Shield",
        "mother_tab": "Mother", "row": "Row", "foundation": "I. The Foundation",
        "nephews": "II. The Nephews", "court": "III. The Verdict",
        "witness_r": "Right Witness", "witness_l": "Left Witness", "judge": "The Judge",
        "reconciler": "The Reconciler", "element": "Element", "error": "Fill all fields."
    },
    "FR": {
        "title": "Oracle Céleste", "subtitle": "Portail de Géomancie Moderne", "btn": "Générer le Blason",
        "mother_tab": "Mère", "row": "Ligne", "foundation": "I. La Fondation",
        "nephews": "II. Les Neveux", "court": "III. Le Verdict",
        "witness_r": "Témoin Droit", "witness_l": "Témoin Gauche", "judge": "Le Juge",
        "reconciler": "Le Réconciliateur", "element": "Élément", "error": "Remplissez tous les champs."
    }
}

# --- 2. LOGIC FUNCTIONS ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_card(fig, label, color, size="18px", glow=False):
    glow_style = f"box-shadow: 0 10px 30px {color}33;" if glow else "box-shadow: 0 4px 12px rgba(0,0,0,0.05);"
    rows = "".join([f"<div style='font-size: {size}; color: {color}; margin: 2px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;&nbsp;●'}</div>" for r in fig])
    return f"""
    <div style="background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); 
                border: 1px solid #e0e0e0; border-radius: 20px; padding: 20px; 
                text-align: center; {glow_style} transition: all 0.3s ease;">
        <div style="font-size: 0.75em; color: #888; font-weight: 600; text-transform: uppercase; margin-bottom: 12px; letter-spacing: 1px;">{label}</div>
        {rows}
    </div>
    """

def process_input(s):
    clean = s.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- 3. APP UI ---
st.set_page_config(page_title="Oracle 2026", layout="wide")

lang_choice = st.sidebar.selectbox("Language / Langue", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]

# Celestial Platinum Theme CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=Outfit:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] { 
        background: linear-gradient(135deg, #f8f9ff 0%, #eef2f7 100%); 
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #2d3436;
    }
    h1 { font-family: 'Outfit', sans-serif; font-weight: 800; color: #1e272e !important; text-align: center; font-size: 3.5rem !important; margin-bottom: 0px !important;}
    .stTextInput input { 
        background: white; border: 2px solid #eef2f7; border-radius: 12px; 
        color: #4a69bd; text-align: center; font-weight: bold; height: 50px;
    }
    .stTabs [data-baseweb="tab"] { font-weight: 600; color: #888; }
    .stTabs [data-baseweb="tab-list"] { background: transparent; }
    div[data-testid="stExpander"] { background: white; border-radius: 15px; border: none; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
    </style>
    """, unsafe_allow_html=True)

st.title(T["title"])
st.markdown(f"<p style='text-align: center; color: #888; font-size: 1.1rem; margin-top: -10px;'>{T['subtitle']}</p>", unsafe_allow_html=True)

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
    # Soft Modern Colors
    colors = {"Fire": "#f76b1c", "Air": "#4a69bd", "Water": "#00b894", "Earth": "#636e72"}
    C = colors.get(rec_data["element"], "#4a69bd")

    st.markdown(f"<style>h2, h3 {{ color: {C} !important; }} .stButton>button {{ background: {C} !important; border: none !important; border-radius: 15px; height: 55px; font-weight: 700; }}</style>", unsafe_allow_html=True)

    # 1. Foundation
    st.header(T["foundation"])
    f_cols = st.columns(8)
    for i, fig in enumerate(M + D):
        label = f"{'M' if i < 4 else 'D'}{i+1 if i < 4 else i-3}"
        f_cols[i].markdown(render_card(fig, label, C), unsafe_allow_html=True)
        f_cols[i].caption(f"<center><b>{GEOMANTIC_DATA[tuple(fig)]['name']}</b></center>", unsafe_allow_html=True)

    # 2. Nephews
    st.header(T["nephews"])
    n_cols = st.columns(4)
    for i, fig in enumerate(N):
        n_cols[i].markdown(render_card(fig, f"N{i+1}", C), unsafe_allow_html=True)

    # 3. Court
    st.divider()
    st.header(T["court"])
    
    wit1, wit2 = st.columns(2)
    wit1.markdown(render_card(RW, T["witness_r"], C), unsafe_allow_html=True)
    wit2.markdown(render_card(LW, T["witness_l"], C), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    res_j, res_r = st.columns(2)
    
    with res_j:
        j_info = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(render_card(Judge, T["judge"], C, size="35px", glow=True), unsafe_allow_html=True)
        st.markdown(f"<div style='background: white; padding: 25px; border-radius: 20px; border-bottom: 5px solid {C}; box-shadow: 0 4px 15px rgba(0,0,0,0.05);'><h3>{j_info['name']}</h3>{j_info['meaning'][L]}</div>", unsafe_allow_html=True)
        
    with res_r:
        st.markdown(render_card(Reconciler, T["reconciler"], C, size="35px", glow=True), unsafe_allow_html=True)
        st.markdown(f"<div style='background: white; padding: 25px; border-radius: 20px; border-bottom: 5px solid {C}; box-shadow: 0 4px 15px rgba(0,0,0,0.05);'><h3>{rec_data['name']}</h3><b>{T['element']}: {rec_data['element']}</b><br><br>{rec_data['meaning'][L]}</div>", unsafe_allow_html=True)
