import streamlit as st

# --- 1. DATA MAP ---
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
        "title": "The Maroon Oracle", "subtitle": "Mothers, Daughters & Nephews", "btn": "Generate Full Shield",
        "row": "Row", "foundation": "The 12 Houses (M1-M4, D1-D4, N1-N4)",
        "court": "The Final Verdict", "error": "Fill all fields.", "reset": "Reset All"
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Mères, Filles et Neveux", "btn": "Générer le Blason",
        "row": "Ligne", "foundation": "Les 12 Maisons (M1-M4, D1-D4, N1-N4)",
        "court": "Le Verdict Final", "error": "Remplissez tous les champs.", "reset": "Réinitialiser"
    }
}

MAROON = "#800000"

# --- Logic ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_small_scale(fig):
    small_html = "<div style='background: #f1f1f1; border-radius: 8px; padding: 10px; min-width: 40px;'>"
    for r in fig:
        char = "●" if r == 1 else "—"
        small_html += f"<div style='color: black; font-size: 26px; font-weight: 900; line-height: 0.8;'>{char}</div>"
    small_html += "</div>"
    return small_html

def render_card(fig, label, color=MAROON, size="35px", glow=False):
    glow_style = f"box-shadow: 0 10px 40px {color}33;" if glow else "box-shadow: 0 4px 15px rgba(0,0,0,0.05);"
    rows = "".join([f"<div style='font-size: {size}; color: {color}; line-height: 1.1; margin: 2px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;●'}</div>" for r in fig])
    
    return f"""
    <div style="background: white; border: 1px solid #edf0f2; border-radius: 20px; padding: 20px; text-align: center; {glow_style}">
        <div style="font-size: 0.75rem; color: #a0a0a0; font-weight: 800; text-transform: uppercase; margin-bottom: 12px; letter-spacing: 1px;">{label}</div>
        <div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
            <div style="flex: 1;">{rows}</div>
            {render_small_scale(fig)}
        </div>
    </div>
    """

def process_input(s):
    clean = s.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- UI Layout ---
st.set_page_config(page_title="Maroon Oracle", layout="wide")
st.markdown(f"""<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;800&display=swap');
    html, body, [data-testid="stAppViewContainer"] {{ background-color: #f8fafc; font-family: 'Outfit', sans-serif; }}
    h1 {{ font-weight: 800; color: #1e272e !important; text-align: center; font-size: 3rem !important; }}
    h2 {{ color: {MAROON} !important; border-bottom: 2px solid #edf0f2; padding-bottom: 10px; margin-top: 30px !important; }}
    .stTextInput input {{ border-radius: 10px; border: 1px solid #ddd; text-align: center; height: 35px; }}
    .stButton>button {{ background: {MAROON} !important; color: white !important; border-radius: 15px !important; height: 55px !important; font-weight: 700 !important; margin-top: 20px; }}
    </style>""", unsafe_allow_html=True)

lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]

if st.sidebar.button(T["reset"]):
    st.rerun()

st.title(T["title"])
st.markdown(f"<p style='text-align: center; color: #888;'>{T['subtitle']}</p>", unsafe_allow_html=True)

# SIDE-BY-SIDE INPUTS
st.markdown("<br>", unsafe_allow_html=True)
m_cols = st.columns(4)
mothers_input = []

for i in range(4):
    with m_cols[i]:
        st.markdown(f"<h3 style='text-align:center; color:#555;'>M{i+1}</h3>", unsafe_allow_html=True)
        m_rows = []
        for j in range(4):
            m_rows.append(st.text_input(f"M{i+1}L{j+1}", key=f"m{i}r{j}", label_visibility="collapsed", placeholder="••••"))
        mothers_input.append(m_rows)

if st.button(T["btn"], use_container_width=True, type="primary"):
    M_figs = []
    for i, rows in enumerate(mothers_input):
        proc = [process_input(r) for r in rows]
        if None in proc:
            st.error(T["error"]); st.stop()
        M_figs.append(proc)
    
    # Derivation logic
    D_figs = [[M_figs[j][i] for j in range(4)] for i in range(4)]
    N_figs = [add_figs(M_figs[0], M_figs[1]), add_figs(M_figs[2], M_figs[3]), add_figs(D_figs[0], D_figs[1]), add_figs(D_figs[2], D_figs[3])]
    RW, LW = add_figs(N_figs[0], N_figs[1]), add_figs(N_figs[2], N_figs[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M_figs[0])

    # DISPLAY 12 HOUSES (M1-M4, D1-D4, N1-N4)
    st.header(T["foundation"])
    
    # Labels and Data combined for easy looping
    house_labels = ["M1", "M2", "M3", "M4", "D1", "D2", "D3", "D4", "N1", "N2", "N3", "N4"]
    house_data = M_figs + D_figs + N_figs
    
    for row_idx in range(0, 12, 4):
        cols = st.columns(4)
        for col_idx in range(4):
            idx = row_idx + col_idx
            cols[col_idx].markdown(render_card(house_data[idx], house_labels[idx]), unsafe_allow_html=True)
            cols[col_idx].caption(f"<center><b>{GEOMANTIC_DATA[tuple(house_data[idx])]['name']}</b></center>", unsafe_allow_html=True)

    # FINAL COURT
    st.header(T["court"])
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1: st.markdown(render_card(RW, "Witness R (RW)"), unsafe_allow_html=True)
    with c2: st.markdown(render_card(LW, "Witness L (LW)"), unsafe_allow_html=True)
    with c3:
        j_info = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(render_card(Judge, "Judge", glow=True), unsafe_allow_html=True)
        st.success(f"**{j_info['name']}**: {j_info['meaning'][L]}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_card(Reconciler, "Reconciler", glow=True), unsafe_allow_html=True)
