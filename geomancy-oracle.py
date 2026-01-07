import streamlit as st

# --- Data: The 16 Classical Figures, Meanings, and Elemental Associations ---
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

def render_fig_html(fig_list, name="", color="#D4AF37"):
    rows_html = "".join([f"<div style='font-size: 20px; color: {color}; line-height: 1.1;'>{'●' if r == 1 else '● ●'}</div>" for r in fig_list])
    return f"""<div style="border: 1px solid {color}44; border-radius: 12px; padding: 10px; background: #111; text-align: center; margin-bottom: 10px;">
               <div style="font-size: 0.7em; color: #888; text-transform: uppercase;">{name}</div>{rows_html}</div>"""

def process_input(input_str):
    clean = input_str.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- UI Setup ---
st.set_page_config(page_title="Geomancy Oracle", layout="wide")
sel_lang = st.sidebar.selectbox("🌐 Language / Langue", ["English", "Français"])
lang_code = "EN" if sel_lang == "English" else "FR"

st.title("🔮 " + ("The Celestial Oracle" if lang_code == "EN" else "L'Oracle Céleste"))

# Input Section
mothers_input = []
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.markdown(f"### M{i+1}")
        mothers_input.append([st.text_input(f"L{j+1}", key=f"m{i}r{j}", placeholder="....") for j in range(4)])

if st.button("Cast the Divine Shield" if lang_code == "EN" else "Lancer le Blason Divin", use_container_width=True, type="primary"):
    M = []
    error = False
    for i, rows in enumerate(mothers_input):
        processed = [process_input(r) for r in rows]
        if None in processed:
            st.error(f"Mother {i+1} incomplete.")
            error = True; break
        M.append(processed)
    
    if not error:
        D = [[M[j][i] for j in range(4)] for i in range(4)]
        N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
        RW, LW = add_figs(N[0], N[1]), add_figs(N[2], N[3])
        Judge = add_figs(RW, LW)
        Reconciler = add_figs(Judge, M[0])
        
        # Dynamic Theme Logic
        rec_data = GEOMANTIC_DATA[tuple(Reconciler)]
        theme_map = {"Fire": "#FF4B4B", "Air": "#00D4FF", "Water": "#00FFC2", "Earth": "#D4AF37"}
        theme_color = theme_map.get(rec_data["element"], "#D4AF37")

        st.markdown(f"<style>h1, h2, h3 {{ color: {theme_color} !important; }} .stButton>button {{ border-color: {theme_color}; }}</style>", unsafe_allow_html=True)

        # MANDATORY DISPLAY OF FOUNDATION
        st.header("1. " + ("The Foundation" if lang_code == "EN" else "La Fondation"))
        f_cols = st.columns(8)
        for i, fig in enumerate(M + D):
            f_cols[i].markdown(render_fig_html(fig, f"{'M' if i < 4 else 'D'}{i+1 if i < 4 else i-3}", theme_color), unsafe_allow_html=True)
            f_cols[i].caption(f"<center>{GEOMANTIC_DATA[tuple(fig)]['name']}</center>", unsafe_allow_html=True)

        st.header("2. " + ("The Nephews" if lang_code == "EN" else "Les Neveux"))
        n_cols = st.columns(4)
        for i, fig in enumerate(N):
            n_cols[i].markdown(render_fig_html(fig, f"N{i+1}", theme_color), unsafe_allow_html=True)

        # FINAL RESULTS
        st.divider()
        st.header("3. " + ("The Sacred Court" if lang_code == "EN" else "Le Tribunal Sacré"))
        res1, res2, res3 = st.columns([1, 1, 2])
        with res1: st.markdown(render_fig_html(RW, "Witness R", theme_color), unsafe_allow_html=True)
        with res2: st.markdown(render_fig_html(LW, "Witness L", theme_color), unsafe_allow_html=True)
        with res3:
            j_data = GEOMANTIC_DATA[tuple(Judge)]
            st.markdown(render_fig_html(Judge, "Judge", theme_color), unsafe_allow_html=True)
            st.success(f"### {j_data['name']}\n{j_data['meaning'][lang_code]}")

        st.info(f"**Reconciler:** {rec_data['name']} ({rec_data['element']}) - {rec_data['meaning'][lang_code]}")
