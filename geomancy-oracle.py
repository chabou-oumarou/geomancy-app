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

# --- Logic ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_fig_html(fig_list, name="", color="#D4AF37", size="20px"):
    rows_html = "".join([f"<div style='font-size: {size}; color: {color}; line-height: 1.1;'>{'●' if r == 1 else '● ●'}</div>" for r in fig_list])
    return f"""<div style="border: 2px solid {color}66; border-radius: 12px; padding: 15px; background: #111; text-align: center; margin-bottom: 10px; box-shadow: 0 4px 15px {color}22;">
               <div style="font-size: 0.75em; color: #aaa; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">{name}</div>{rows_html}</div>"""

def process_input(input_str):
    clean = input_str.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- UI Setup ---
st.set_page_config(page_title="Geomancy Oracle", layout="wide")
sel_lang = st.sidebar.selectbox("🌐 Language / Langue", ["English", "Français"])
L = "EN" if sel_lang == "English" else "FR"

# Section Titles
T_FOUNDATION = "The Foundation" if L == "EN" else "La Fondation"
T_NEPHEWS = "The Nephews (Results)" if L == "EN" else "Les Neveux (Résultats)"
T_COURT = "⚖️ The Sacred Court" if L == "EN" else "⚖️ Le Tribunal Sacré"
T_CAST = "Cast the Divine Shield" if L == "EN" else "Lancer le Blason Divin"

st.title("🔮 " + ("The Celestial Oracle" if L == "EN" else "L'Oracle Céleste"))

# Input Grid
mothers_input = []
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.markdown(f"### M{i+1}")
        mothers_input.append([st.text_input(f"L{j+1}", key=f"m{i}r{j}", label_visibility="collapsed", placeholder="....") for j in range(4)])

if st.button(T_CAST, use_container_width=True, type="primary"):
    M = []
    error = False
    for i, rows in enumerate(mothers_input):
        proc = [process_input(r) for r in rows]
        if None in proc:
            st.error(f"Mother {i+1} incomplete / Mère {i+1} incomplète")
            error = True; break
        M.append(proc)
    
    if not error:
        # Mathematical derivation
        D = [[M[j][i] for j in range(4)] for i in range(4)]
        N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
        RW, LW = add_figs(N[0], N[1]), add_figs(N[2], N[3])
        Judge = add_figs(RW, LW)
        Reconciler = add_figs(Judge, M[0])
        
        # Dynamic CSS Theme based on Reconciler Element
        rec_info = GEOMANTIC_DATA[tuple(Reconciler)]
        theme_color = {"Fire": "#FF4B4B", "Air": "#00D4FF", "Water": "#00FFC2", "Earth": "#D4AF37"}.get(rec_info["element"])
        
        st.markdown(f"""<style>
            h1, h2, h3 {{ color: {theme_color} !important; font-family: 'serif'; }}
            .stButton>button {{ border: 2px solid {theme_color} !important; color: {theme_color} !important; }}
            </style>""", unsafe_allow_html=True)

        # 1. Mandatory Display: Foundation
        st.header("1. " + T_FOUNDATION)
        f_cols = st.columns(8)
        all_f = M + D
        for i, fig in enumerate(all_f):
            label = f"{'M' if i < 4 else 'D'}{i+1 if i < 4 else i-3}"
            f_cols[i].markdown(render_fig_html(fig, label, theme_color), unsafe_allow_html=True)
            f_cols[i].caption(f"<center>{GEOMANTIC_DATA[tuple(fig)]['name']}</center>", unsafe_allow_html=True)

        # 2. Results: Nephews
        st.header("2. " + T_NEPHEWS)
        n_cols = st.columns(4)
        for i, fig in enumerate(N):
            n_cols[i].markdown(render_fig_html(fig, f"N{i+1}", theme_color), unsafe_allow_html=True)
            n_cols[i].caption(f"<center>{GEOMANTIC_DATA[tuple(fig)]['name']}</center>", unsafe_allow_html=True)

        # 3. Final Verdict: The Court & Reconciler
        st.divider()
        st.header(T_COURT)
        
        # Witnesses Row
        wit1, wit2 = st.columns(2)
        with wit1: st.markdown(render_fig_html(RW, "Witness R / Témoin D", theme_color), unsafe_allow_html=True)
        with wit2: st.markdown(render_fig_html(LW, "Witness L / Témoin G", theme_color), unsafe_allow_html=True)
        
        # Judge and Reconciler Row
        st.markdown("<br>", unsafe_allow_html=True)
        res_j, res_r = st.columns(2)
        
        with res_j:
            j_data = GEOMANTIC_DATA[tuple(Judge)]
            st.markdown(render_fig_html(Judge, "The Judge / Le Juge", theme_color, size="32px"), unsafe_allow_html=True)
            st.success(f"### {j_data['name']}\n{j_data['meaning'][L]}")
            
        with res_r:
            st.markdown(render_fig_html(Reconciler, "The Reconciler / Le Réconciliateur", theme_color, size="32px"), unsafe_allow_html=True)
            st.info(f"### {rec_info['name']}\n**Element: {rec_info['element']}**\n\n{rec_info['meaning'][L]}")
