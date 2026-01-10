import streamlit as st

# --- 1. UPDATED DATA MAP WITH RECOMMENDATIONS ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {
        "name": "Via", 
        "meaning": {"EN": "Change, movement, and journeys.", "FR": "Changement, mouvement et voyages."},
        "rec_insight": {"EN": "The path is open; keep moving to reach the final goal.", "FR": "Le chemin est ouvert ; continuez d'avancer pour atteindre le but final."},
        "recommendation": {"EN": "Leave an offering at a crossroads or take a long walk to clear energy.", "FR": "Laissez une offrande à un carrefour ou faites une longue marche pour purifier l'énergie."}
    },
    (2, 2, 2, 2): {
        "name": "Populus", 
        "meaning": {"EN": "Stability, crowds, and public matters.", "FR": "Stabilité, foules et affaires publiques."},
        "rec_insight": {"EN": "The result involves others; look for collective stability.", "FR": "Le résultat implique les autres ; recherchez la stabilité collective."},
        "recommendation": {"EN": "Host a gathering or share a meal with a group to foster unity.", "FR": "Organisez un rassemblement ou partagez un repas avec un groupe pour favoriser l'unité."}
    },
    (2, 1, 1, 2): {
        "name": "Conjunctio", 
        "meaning": {"EN": "Union, contracts, and joining together.", "FR": "Union, contrats et rapprochement."},
        "rec_insight": {"EN": "A final agreement or union will seal the outcome.", "FR": "Un accord final ou une union scellera l'issue."},
        "recommendation": {"EN": "Exchange a small token or gift with a partner to seal a bond.", "FR": "Échangez un petit gage ou un cadeau avec un partenaire pour sceller un lien."}
    },
    (1, 2, 2, 1): {
        "name": "Carcer", 
        "meaning": {"EN": "Restriction, boundaries, and delay.", "FR": "Restriction, limites et retard."},
        "rec_insight": {"EN": "The conclusion brings boundaries or heavy responsibilities.", "FR": "La conclusion apporte des limites ou de lourdes responsabilités."},
        "recommendation": {"EN": "Practice a day of silence or fasting to master your internal discipline.", "FR": "Pratiquez une journée de silence ou de jeûne pour maîtriser votre discipline interne."}
    },
    (2, 2, 1, 1): {
        "name": "Fortuna Major", 
        "meaning": {"EN": "Great fortune and inner strength.", "FR": "Grande fortune et force intérieure."},
        "rec_insight": {"EN": "Ultimate protection and victory is assured.", "FR": "La protection ultime et la victoire sont assurées."},
        "recommendation": {"EN": "Make a significant charitable donation or offer high-quality incense.", "FR": "Faites un don charitable important ou offrez de l'encens de haute qualité."}
    },
    (1, 1, 2, 2): {
        "name": "Fortuna Minor", 
        "meaning": {"EN": "Small success and swift external luck.", "FR": "Petite fortune et chance externe rapide."},
        "rec_insight": {"EN": "A quick, temporary success that requires immediate action.", "FR": "Un succès rapide et temporaire qui nécessite une action immédiate."},
        "recommendation": {"EN": "Give a small coin to a stranger or a quick gift to a friend.", "FR": "Donnez une petite pièce à un inconnu ou un cadeau rapide à un ami."}
    },
    (2, 1, 2, 1): {
        "name": "Acquisitio", 
        "meaning": {"EN": "Profit, gain, and expansion.", "FR": "Profit, gain et expansion."},
        "rec_insight": {"EN": "The reconciliation brings a significant increase or gain.", "FR": "La réconciliation apporte une augmentation ou un gain significatif."},
        "recommendation": {"EN": "Plant a seed or invest in a physical object that will grow in value.", "FR": "Plantez une graine ou investissez dans un objet physique qui prendra de la valeur."}
    },
    (1, 2, 1, 2): {
        "name": "Amissio", 
        "meaning": {"EN": "Loss and letting go.", "FR": "Perte et lâcher-prise."},
        "rec_insight": {"EN": "To secure the outcome, a sacrifice or release is needed.", "FR": "Pour sécuriser l'issue, un sacrifice ou un abandon est nécessaire."},
        "recommendation": {"EN": "Sacrifice a habit or give away a cherished item to make room for the new.", "FR": "Sacrifiez une habitude ou donnez un objet cher pour faire de la place au nouveau."}
    },
    (1, 2, 2, 2): {
        "name": "Laetitia", 
        "meaning": {"EN": "Joy, health, and positive news.", "FR": "Joie, santé et nouvelles positives."},
        "rec_insight": {"EN": "The matter concludes with happiness and true inner joy.", "FR": "L'affaire se conclut par le bonheur et une véritable joie intérieure."},
        "recommendation": {"EN": "Buy a bouquet of bright flowers or host a celebration for others.", "FR": "Achetez un bouquet de fleurs éclatantes ou organisez une fête pour les autres."}
    },
    (2, 2, 2, 1): {
        "name": "Tristitia", 
        "meaning": {"EN": "Sorrow, depth, and foundations.", "FR": "Tristesse, profondeur et fondations."},
        "rec_insight": {"EN": "The result is solid but requires a serious, heavy effort.", "FR": "Le résultat est solide mais nécessite un effort sérieux et lourd."},
        "recommendation": {"EN": "Offer a stone to the earth or donate to a land conservation cause.", "FR": "Offrez une pierre à la terre ou faites un don à une cause de conservation des terres."}
    },
    (1, 2, 1, 1): {
        "name": "Puella", 
        "meaning": {"EN": "Harmony, beauty, and grace.", "FR": "Harmonie, beauté et grâce."},
        "rec_insight": {"EN": "Harmony is restored through kindness or social charm.", "FR": "L'harmonie est restaurée par la gentillesse ou le charme social."},
        "recommendation": {"EN": "Gift jewelry, perfume, or a work of art to someone you appreciate.", "FR": "Offrez des bijoux, du parfum ou une œuvre d'art à quelqu'un que vous appréciez."}
    },
    (1, 1, 2, 1): {
        "name": "Puer", 
        "meaning": {"EN": "Energy, action, and impulsive force.", "FR": "Énergie, action et force impulsive."},
        "rec_insight": {"EN": "A bold, energetic push will decide the final result.", "FR": "Un élan audacieux et énergique décidera du résultat final."},
        "recommendation": {"EN": "Perform a strenuous physical task or gift sports equipment to a youth.", "FR": "Accomplissez une tâche physique ardue ou offrez du matériel de sport à un jeune."}
    },
    (2, 2, 1, 2): {
        "name": "Albus", 
        "meaning": {"EN": "Wisdom, peace, and clarity.", "FR": "Sagesse, paix et clarté."},
        "rec_insight": {"EN": "A clear, peaceful resolution through honest communication.", "FR": "Une résolution claire et pacifique grâce à une communication honnête."},
        "recommendation": {"EN": "Light a white candle or offer white flowers to a place of peace.", "FR": "Allumez une bougie blanche ou offrez des fleurs blanches dans un lieu de paix."}
    },
    (2, 1, 2, 2): {
        "name": "Rubeus", 
        "meaning": {"EN": "Passion, vice, and danger.", "FR": "Passion, vice et danger."},
        "rec_insight": {"EN": "Warning: the final conclusion contains hidden volatile energy.", "FR": "Attention : la conclusion finale contient une énergie volatile cachée."},
        "recommendation": {"EN": "Offer red wine or flowers to appease energy; maintain strict vigilance.", "FR": "Offrez du vin rouge ou des fleurs pour apaiser l'énergie ; maintenez une vigilance stricte."}
    },
    (2, 1, 1, 1): {
        "name": "Caput Draconis", 
        "meaning": {"EN": "Beginnings and entry points.", "FR": "Commencements et points d'entrée."},
        "rec_insight": {"EN": "The result marks the start of a completely new chapter.", "FR": "Le résultat marque le début d'un chapitre totalement nouveau."},
        "recommendation": {"EN": "Initiate a new project or gift a new book to someone starting a journey.", "FR": "Initiez un nouveau projet ou offrez un nouveau livre à quelqu'un qui commence un voyage."}
    },
    (1, 1, 1, 2): {
        "name": "Cauda Draconis", 
        "meaning": {"EN": "Endings and exit points.", "FR": "Fins et points de sortie."},
        "rec_insight": {"EN": "The matter is finished; you must leave the past behind.", "FR": "L'affaire est terminée ; vous devez laisser le passé derrière vous."},
        "recommendation": {"EN": "Discard a broken item or finalize a debt to close the cycle.", "FR": "Jetez un objet cassé ou finalisez une dette pour fermer le cycle."}
    }
}

UI_TEXT = {
    "EN": {
        "title": "Maroon Oracle", "subtitle": "Mothers, Houses & Shield", "btn": "Generate Full Shield",
        "row": "Row", "foundation": "The 12 Houses (M1-M4, D1-D4, N1-N4)",
        "court": "The Final Verdict", "rec_label": "The Reconciler (Synthesis)", "error": "Fill all fields.", 
        "reset": "Reset All", "recommendation_title": "Action / Gift Recommendation"
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Maisons et Blason", "btn": "Générer le Blason",
        "row": "Ligne", "foundation": "Les 12 Maisons (M1-M4, D1-D4, N1-N4)",
        "court": "Le Verdict Final", "rec_label": "Le Réconciliateur (Synthèse)", "error": "Remplissez tout.", 
        "reset": "Réinitialiser", "recommendation_title": "Action / Recommandation de Cadeau"
    }
}

MAROON = "#800000"

# --- Functions ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_small_scale(fig):
    small_html = "<div style='background: #f1f1f1; border-radius: 8px; padding: 10px; min-width: 50px;'>"
    for r in fig:
        char = "●" if r == 1 else "—"
        small_html += f"<div style='color: black; font-size: 32px; font-weight: 900; line-height: 0.7;'>{char}</div>"
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
    h2 {{ color: {MAROON} !important; border-bottom: 2px solid #edf0f2; padding-bottom: 10px; }}
    .stTextInput input {{ border-radius: 10px; border: 1px solid #ddd; text-align: center; height: 35px; font-size: 1.1rem; }}
    .stButton>button {{ background: {MAROON} !important; color: white !important; border-radius: 15px !important; height: 55px !important; font-weight: 700 !important; }}
    </style>""", unsafe_allow_html=True)

lang_choice = st.sidebar.selectbox("🌐 Language / Langue", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]

if st.sidebar.button(T["reset"]): st.rerun()

st.title(T["title"])
st.markdown(f"<p style='text-align: center; color: #888;'>{T['subtitle']}</p>", unsafe_allow_html=True)

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
        if None in proc: st.error(T["error"]); st.stop()
        M_figs.append(proc)
    
    D_figs = [[M_figs[j][i] for j in range(4)] for i in range(4)]
    N_figs = [add_figs(M_figs[0], M_figs[1]), add_figs(M_figs[2], M_figs[3]), add_figs(D_figs[0], D_figs[1]), add_figs(D_figs[2], D_figs[3])]
    RW, LW = add_figs(N_figs[0], N_figs[1]), add_figs(N_figs[2], N_figs[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M_figs[0])

    # 1. THE 12 HOUSES
    st.header(T["foundation"])
    labels = ["M1", "M2", "M3", "M4", "D1", "D2", "D3", "D4", "N1", "N2", "N3", "N4"]
    data = M_figs + D_figs + N_figs
    for row in range(0, 12, 4):
        cols = st.columns(4)
        for c in range(4):
            idx = row + c
            fig_tuple = tuple(data[idx])
            fig_info = GEOMANTIC_DATA[fig_tuple]
            cols[c].markdown(render_card(data[idx], labels[idx]), unsafe_allow_html=True)
            cols[c].markdown(f"""<center><b>{fig_info['name']}</b><br>
                                <span style='font-size:0.8rem; color:#888;'><i>{fig_info['recommendation'][L]}</i></span>
                                </center>""", unsafe_allow_html=True)

    # 2. THE FINAL VERDICT (JUDGE)
    st.header(T["court"])
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1: st.markdown(render_card(RW, "RW (Witness R)"), unsafe_allow_html=True)
    with c2: st.markdown(render_card(LW, "LW (Witness L)"), unsafe_allow_html=True)
    with c3:
        j_info = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(render_card(Judge, "The Judge", glow=True), unsafe_allow_html=True)
        st.markdown(f"""<div style='background:white; border-left:8px solid {MAROON}; padding:20px; border-radius:15px; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-top:10px;'>
                        <h3 style='margin:0; color:{MAROON};'>{j_info['name']}</h3>
                        <p style='color:#666; font-size:1.1rem;'><b>{j_info['meaning'][L]}</b></p>
                        <p style='background:#fff5f5; padding:10px; border-radius:10px; color:#c0392b; font-weight:bold;'>💡 {T['recommendation_title']}: {j_info['recommendation'][L]}</p>
                        </div>""", unsafe_allow_html=True)

    # 3. THE RECONCILER
    st.divider()
    st.header(T["rec_label"])
    res_a, res_b = st.columns([1, 3])
    with res_a:
        st.markdown(render_card(Reconciler, "Reconciler", glow=True), unsafe_allow_html=True)
    with res_b:
        r_info = GEOMANTIC_DATA[tuple(Reconciler)]
        st.markdown(f"""<div style='background:white; border-left:12px solid {MAROON}; padding:30px; border-radius:15px; box-shadow:0 10px 30px rgba(0,0,0,0.08);'>
                        <h2 style='margin:0; color:{MAROON};'>{r_info['name']}</h2>
                        <p style='color:#555; font-size:1.2rem; margin-bottom:10px;'><i>{r_info['meaning'][L]}</i></p>
                        <hr style='border:1px solid #eee;'>
                        <p style='font-size:1.4rem; font-weight:bold; color:#2d3436; line-height:1.4;'>{r_info['rec_insight'][L]}</p>
                        <div style='margin-top:20px; padding:15px; background:#fdf2f2; border:1px dashed {MAROON}; border-radius:12px;'>
                            <strong style='color:{MAROON};'>{T['recommendation_title']}:</strong><br>
                            <span style='font-size:1.2rem; color:#444;'>{r_info['recommendation'][L]}</span>
                        </div>
                        </div>""", unsafe_allow_html=True)
