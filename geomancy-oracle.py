import streamlit as st

# --- 1. DATA MAP ---
# Added 'rec_insight' to provide context specifically for the Reconciler's role
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {"name": "Via", "element": "Water", "rec_insight": {"EN": "The path remains open; you must continue moving forward to reach the end.", "FR": "Le chemin reste ouvert ; vous devez continuer à avancer pour atteindre le but."}},
    (2, 2, 2, 2): {"name": "Populus", "element": "Water", "rec_insight": {"EN": "The outcome is public or involves many people. A stable, collective result.", "FR": "L'issue est publique ou implique de nombreuses personnes. Un résultat stable et collectif."}},
    (2, 1, 1, 2): {"name": "Conjunctio", "element": "Air", "rec_insight": {"EN": "A final agreement or contract will bind the seeker to the result.", "FR": "Un accord final ou un contrat liera le demandeur au résultat."}},
    (1, 2, 2, 1): {"name": "Carcer", "element": "Earth", "rec_insight": {"EN": "The result brings isolation or heavy responsibility. A binding conclusion.", "FR": "Le résultat apporte l'isolement ou une lourde responsabilité. Une conclusion contraignante."}},
    (2, 2, 1, 1): {"name": "Fortuna Major", "element": "Earth", "rec_insight": {"EN": "Ultimate success. The seeker is perfectly aligned with a powerful victory.", "FR": "Succès ultime. Le chercheur est parfaitement aligné avec une victoire puissante."}},
    (1, 1, 2, 2): {"name": "Fortuna Minor", "element": "Fire", "rec_insight": {"EN": "A swift, temporary success. Enjoy the moment, but don't expect it to last forever.", "FR": "Un succès rapide et temporaire. Profitez du moment, mais ne vous attendez pas à ce qu'il dure éternellement."}},
    (2, 1, 2, 1): {"name": "Acquisitio", "element": "Air", "rec_insight": {"EN": "You gain more than you expected. The reconciliation brings profit.", "FR": "Vous gagnez plus que ce que vous espériez. La réconciliation apporte du profit."}},
    (1, 2, 1, 2): {"name": "Amissio", "element": "Fire", "meaning": {"EN": "Loss.", "FR": "Perte."}, "rec_insight": {"EN": "To gain the result, something must be sacrificed. A let-go is necessary.", "FR": "Pour obtenir le résultat, quelque chose doit être sacrifié. Un lâcher-prise est nécessaire."}},
    (1, 2, 2, 2): {"name": "Laetitia", "element": "Air", "rec_insight": {"EN": "The matter ends in celebration and true inner joy.", "FR": "L'affaire se termine par une célébration et une véritable joie intérieure."}},
    (2, 2, 2, 1): {"name": "Tristitia", "element": "Earth", "rec_insight": {"EN": "The result is solid but heavy. It may bring sadness or require hard labor.", "FR": "Le résultat est solide mais lourd. Il peut apporter de la tristesse ou exiger un travail acharné."}},
    (1, 2, 1, 1): {"name": "Puella", "element": "Water", "rec_insight": {"EN": "Harmony is restored through grace or the intervention of a woman.", "FR": "L'harmonie est restaurée par la grâce ou l'intervention d'une femme."}},
    (1, 1, 2, 1): {"name": "Puer", "element": "Fire", "rec_insight": {"EN": "The outcome is reached through conflict or bold, masculine action.", "FR": "Le résultat est atteint par le conflit ou une action audacieuse et masculine."}},
    (2, 2, 1, 2): {"name": "Albus", "element": "Air", "rec_insight": {"EN": "A peaceful resolution. Communication clarifies the final position.", "FR": "Une résolution pacifique. La communication clarifie la position finale."}},
    (2, 1, 2, 2): {"name": "Rubeus", "element": "Fire", "rec_insight": {"EN": "A warning: the result contains hidden danger or explosive emotions.", "FR": "Un avertissement : le résultat contient un danger caché ou des émotions explosives."}},
    (2, 1, 1, 1): {"name": "Caput Draconis", "element": "Earth", "rec_insight": {"EN": "A door opens to a completely new chapter of life.", "FR": "Une porte s'ouvre sur un chapitre de vie complètement nouveau."}},
    (1, 1, 1, 2): {"name": "Cauda Draconis", "element": "Fire", "rec_insight": {"EN": "The matter is finally over. You must leave the past behind completely.", "FR": "L'affaire est enfin terminée. Vous devez laisser le passé derrière vous complètement."}}
}

# General translations and UI settings
UI_TEXT = {
    "EN": {"rec_title": "The Reconciler's Interpretation", "rec_desc": "Bridges the Seeker to the Outcome"},
    "FR": {"rec_title": "Interprétation du Réconciliateur", "rec_desc": "Relie le Chercheur au Résultat"}
}

MAROON = "#800000"

# --- Logic & UI Functions ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_small_scale(fig):
    """Large black Mini-Map (2 dots = 1 dash)"""
    small_html = "<div style='background: #f1f1f1; border-radius: 8px; padding: 10px;'>"
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

# --- Main App ---
st.set_page_config(page_title="Maroon Oracle", layout="wide")
st.markdown(f"<style>h1, h2, h3 {{ color: {MAROON} !important; text-align: center; font-family: 'Outfit', sans-serif; }} .stButton>button {{ background: {MAROON} !important; color: white !important; }}</style>", unsafe_allow_html=True)

lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"

st.title("L'Oracle Marron" if L == "FR" else "The Maroon Oracle")

# Inputs
m_cols = st.columns(4)
mothers_input = []
for i in range(4):
    with m_cols[i]:
        st.markdown(f"### M{i+1}")
        mothers_input.append([st.text_input(f"M{i+1}L{j+1}", key=f"m{i}r{j}", label_visibility="collapsed", placeholder="••••") for j in range(4)])

if st.button("Generate Shield / Générer le Blason", use_container_width=True, type="primary"):
    M_figs = []
    for i, rows in enumerate(mothers_input):
        proc = [process_input(r) for r in rows]
        if None in proc: st.error("Fill all fields"); st.stop()
        M_figs.append(proc)
    
    # Derivation
    D_figs = [[M_figs[j][i] for j in range(4)] for i in range(4)]
    N_figs = [add_figs(M_figs[0], M_figs[1]), add_figs(M_figs[2], M_figs[3]), add_figs(D_figs[0], D_figs[1]), add_figs(D_figs[2], D_figs[3])]
    RW, LW = add_figs(N_figs[0], N_figs[1]), add_figs(N_figs[2], N_figs[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M_figs[0])
    
    # 1. Show Foundation (House M1-M4, D1-D4, N1-N4)
    st.header("The 12 Houses / Les 12 Maisons")
    h_data = M_figs + D_figs + N_figs
    h_labels = ["M1", "M2", "M3", "M4", "D1", "D2", "D3", "D4", "N1", "N2", "N3", "N4"]
    for row in range(0, 12, 4):
        cols = st.columns(4)
        for c in range(4):
            idx = row + c
            cols[c].markdown(render_card(h_data[idx], h_labels[idx]), unsafe_allow_html=True)
            cols[c].caption(f"<center><b>{GEOMANTIC_DATA[tuple(h_data[idx])]['name']}</b></center>", unsafe_allow_html=True)

    # 2. Show Court
    st.header("The Verdict / Le Verdict")
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1: st.markdown(render_card(RW, "Witness R (RW)"), unsafe_allow_html=True)
    with c2: st.markdown(render_card(LW, "Witness L (LW)"), unsafe_allow_html=True)
    with c3:
        st.markdown(render_card(Judge, "Judge", glow=True), unsafe_allow_html=True)
        st.info(f"**{GEOMANTIC_DATA[tuple(Judge)]['name']}**")

    # 3. THE RECONCILER INTERPRETATION
    st.divider()
    rec_fig_data = GEOMANTIC_DATA[tuple(Reconciler)]
    st.header(UI_TEXT[L]["rec_title"])
    
    col_a, col_b = st.columns([1, 3])
    with col_a:
        st.markdown(render_card(Reconciler, "Reconciler", glow=True), unsafe_allow_html=True)
    with col_b:
        st.markdown(f"""
        <div style="background: white; border-left: 10px solid {MAROON}; padding: 30px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h2 style="margin-top:0; color:{MAROON};">{rec_fig_data['name']}</h2>
            <p style="font-size: 1.1rem; color: #555;"><i>{UI_TEXT[L]["rec_desc"]}</i></p>
            <hr>
            <p style="font-size: 1.3rem; font-weight: bold; color: #2d3436;">{rec_fig_data['rec_insight'][L]}</p>
        </div>
        """, unsafe_allow_html=True)
