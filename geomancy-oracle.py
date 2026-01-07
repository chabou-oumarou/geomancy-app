import streamlit as st

# --- Data: Figures, Elements, and Bilingual Meanings ---
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

# --- Core Logic ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_fig_modern(fig_list, name="", color="#D4AF37", size="18px", glow=False):
    glow_style = f"box-shadow: 0 0 15px {color}66;" if glow else ""
    rows_html = "".join([f"<div style='font-size: {size}; color: {color}; margin: 5px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;&nbsp;●'}</div>" for r in fig_list])
    return f"""
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); 
                border: 1px solid {color}44; border-radius: 15px; padding: 20px; 
                text-align: center; {glow_style} transition: transform 0.3s ease;">
        <div style="font-size: 0.7em; color: #aaa; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px;">{name}</div>
        {rows_html}
    </div>
    """

def process_input(input_str):
    clean = input_str.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- UI Setup ---
st.set_page_config(page_title="Geomancy 2026", layout="wide", initial_sidebar_state="collapsed")

# Inject Modern CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&family=Playfair+Display:wght@700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460);
        font-family: 'Inter', sans-serif;
    }
    h1 { font-family: 'Playfair Display', serif; font-size: 3.5rem !important; text-align: center; margin-bottom: 0px !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; background-color: transparent; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.05); border-radius: 10px 10px 0 0;
        padding: 10px 20px; color: white; border: none;
    }
    .stTextInput input {
        border-radius: 10px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
        color: #D4AF37; text-align: center; font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Language Switch
sel_lang = st.selectbox("", ["English", "Français"], label_visibility="collapsed")
L = "EN" if sel_lang == "English" else "FR"

st.title("Celestial Oracle" if L == "EN" else "L'Oracle Céleste")
st.markdown(f"<p style='text-align: center; color: #888; margin-bottom: 50px;'>{'The Modern Science of the Sands' if L == 'EN' else 'La Science Moderne des Sables'}</p>", unsafe_allow_html=True)

# 1. Stepper Input for the 4 Mothers
st.subheader("I. Initiation" if L == "EN" else "I. Initiation")
tabs = st.tabs(["Mother 1", "Mother 2", "Mother 3", "Mother 4"] if L == "EN" else ["Mère 1", "Mère 2", "Mère 3", "Mère 4"])
mothers_input = []

for i in range(4):
    with tabs[i]:
        c1, c2, c3, c4 = st.columns(4)
        m_rows = []
        for j, col in enumerate([c1, c2, c3, c4]):
            m_rows.append(col.text_input(f"M{i+1}L{j+1}", key=f"m{i}r{j}", label_visibility="collapsed", placeholder="••••"))
        mothers_input.append(m_rows)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("Unveil the Shield" if L == "EN" else "Dévoiler le Blason", use_container_width=True, type="primary"):
    M = []
    error = False
    for i, rows in enumerate(mothers_input):
        proc = [process_input(r) for r in rows]
        if None in proc:
            st.error(f"Incomplete Data / Données Incomplètes")
            error = True; break
        M.append(proc)
    
    if not error:
        # Math
        D = [[M[j][i] for j in range(4)] for i in range(4)]
        N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
        RW, LW = add_figs(N[0], N[1]), add_figs(N[2], N[3])
        Judge = add_figs(RW, LW)
        Reconciler = add_figs(Judge, M[0])
        
        # Element Theme
        rec_info = GEOMANTIC_DATA[tuple(Reconciler)]
        theme_color = {"Fire": "#FF4B2B", "Air": "#00d2ff", "Water": "#00f2fe", "Earth": "#f9d423"}.get(rec_info["element"])

        # Update Headings with Glow
        st.markdown(f"<style>h1, h2, h3 {{ color: {theme_color} !important; text-shadow: 0 0 20px {theme_color}44; }}</style>", unsafe_allow_html=True)

        # II. Mandatory Display: The Shield
        st.header("II. The Universal Shield" if L == "EN" else "II. Le Blason Universel")
        
        # Display M and D in an elegant grid
        f_cols = st.columns(8)
        for i, fig in enumerate(M + D):
            label = f"{'M' if i < 4 else 'D'}{i+1 if i < 4 else i-3}"
            f_cols[i].markdown(render_fig_modern(fig, label, theme_color), unsafe_allow_html=True)

        # III. The Court
        st.divider()
        st.header("III. The Sacred Decree" if L == "EN" else "III. Le Décret Sacré")
        
        w1, w2 = st.columns(2)
        w1.markdown(render_fig_modern(RW, "Right Witness", theme_color), unsafe_allow_html=True)
        w2.markdown(render_fig_modern(LW, "Left Witness", theme_color), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        res_j, res_r = st.columns(2)
        with res_j:
            j_data = GEOMANTIC_DATA[tuple(Judge)]
            st.markdown(render_fig_modern(Judge, "Judge", theme_color, size="30px", glow=True), unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center;'>{j_data['name']}</h3><p style='text-align:center;'>{j_data['meaning'][L]}</p>", unsafe_allow_html=True)
            
        with res_r:
            st.markdown(render_fig_modern(Reconciler, "Reconciler", theme_color, size="30px", glow=True), unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center;'>{rec_info['name']}</h3><p style='text-align:center;'><b>Element: {rec_info['element']}</b><br>{rec_info['meaning'][L]}</p>", unsafe_allow_html=True)
