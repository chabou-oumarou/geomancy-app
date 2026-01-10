import streamlit as st

# --- 1. SPIRITUALLY FOCUSED DATA MAP (AFRICAN CONTEXT) ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {
        "name": "Via", 
        "meaning": {"EN": "Change, movement, and journeys.", "FR": "Changement, mouvement et voyages."},
        "rec_insight": {"EN": "The path is open; keep moving to reach the final goal.", "FR": "Le chemin est ouvert ; continuez d'avancer pour atteindre le but final."},
        "recommendation": {
            "EN": "Pour a libation of cool water at the threshold of your home to clear the way for the ancestors.", 
            "FR": "Versez une libation d'eau fraîche au seuil de votre maison pour ouvrir la voie aux ancêtres."
        }
    },
    (2, 2, 2, 2): {
        "name": "Populus", 
        "meaning": {"EN": "Stability, crowds, and public matters.", "FR": "Stabilité, foules et affaires publiques."},
        "rec_insight": {"EN": "The result involves others; look for collective stability.", "FR": "Le résultat implique les autres ; recherchez la stabilité collective."},
        "recommendation": {
            "EN": "Offer a communal bowl of kola nuts or fruit to the spirits of the marketplace to secure public favor.", 
            "FR": "Offrez un bol de noix de cola ou de fruits aux esprits du marché pour obtenir la faveur du public."
        }
    },
    (2, 1, 1, 2): {
        "name": "Conjunctio", 
        "meaning": {"EN": "Union, contracts, and joining together.", "FR": "Union, contrats et rapprochement."},
        "rec_insight": {"EN": "A final agreement or union will seal the outcome.", "FR": "Un accord final ou une union scellera l'issue."},
        "recommendation": {
            "EN": "Bind two white threads around a sacred tree or family shrine to lock a spiritual covenant.", 
            "FR": "Liez deux fils blancs autour d'un arbre sacré ou d'un autel familial pour sceller une alliance spirituelle."
        }
    },
    (1, 2, 2, 1): {
        "name": "Carcer", 
        "meaning": {"EN": "Restriction, boundaries, and delay.", "FR": "Restriction, limites et retard."},
        "rec_insight": {"EN": "The conclusion brings boundaries or heavy responsibilities.", "FR": "La conclusion apporte des limites ou de lourdes responsabilités."},
        "recommendation": {
            "EN": "Offer a small iron padlock or chain at an old crossroads to break spiritual stagnation.", 
            "FR": "Offrez un petit cadenas ou une chaîne en fer à un vieux carrefour pour briser la stagnation spirituelle."
        }
    },
    (2, 2, 1, 1): {
        "name": "Fortuna Major", 
        "meaning": {"EN": "Great fortune and inner strength.", "FR": "Grande fortune et force intérieure."},
        "rec_insight": {"EN": "Ultimate protection and victory is assured.", "FR": "La protection ultime et la victoire sont assurées."},
        "recommendation": {
            "EN": "Offer honey and expensive white cloth to the Orishas/Divinities as a 'Ebo' of gratitude for royal favor.", 
            "FR": "Offrez du miel et un pagne blanc de prix aux Divinités en guise d'Ebo de gratitude pour la faveur royale."
        }
    },
    (1, 1, 2, 2): {
        "name": "Fortuna Minor", 
        "meaning": {"EN": "Small success and swift external luck.", "FR": "Petite fortune et chance externe rapide."},
        "rec_insight": {"EN": "A quick, temporary success that requires immediate action.", "FR": "Un succès rapide et temporaire qui nécessite une action immédiate."},
        "recommendation": {
            "EN": "Distribute small coins to the elders of your community to activate the blessing of the lineage.", 
            "FR": "Distribuez des petites pièces aux anciens de votre communauté pour activer la bénédiction de la lignée."
        }
    },
    (2, 1, 2, 1): {
        "name": "Acquisitio", 
        "meaning": {"EN": "Profit, gain, and expansion.", "FR": "Profit, gain et expansion."},
        "rec_insight": {"EN": "The reconciliation brings a significant increase or gain.", "FR": "La réconciliation apporte une augmentation ou un gain significatif."},
        "recommendation": {
            "EN": "Bury a silver coin in a fertile patch of earth or at the foot of an Iroko tree to ground your wealth.", 
            "FR": "Enterrez une pièce d'argent dans une terre fertile ou au pied d'un arbre Iroko pour enraciner votre richesse."
        }
    },
    (1, 2, 1, 2): {
        "name": "Amissio", 
        "meaning": {"EN": "Loss and letting go.", "FR": "Perte et lâcher-prise."},
        "rec_insight": {"EN": "To secure the outcome, a sacrifice or release is needed.", "FR": "Pour sécuriser l'issue, un sacrifice ou un abandon est nécessaire."},
        "recommendation": {
            "EN": "Sacrifice a personal garment or a portion of your meal to the river spirits to wash away bad luck.", 
            "FR": "Sacrifiez un vêtement personnel ou une portion de votre repas aux esprits de la rivière pour laver la malchance."
        }
    },
    (1, 2, 2, 2): {
        "name": "Laetitia", 
        "meaning": {"EN": "Joy, health, and positive news.", "FR": "Joie, santé et nouvelles positives."},
        "rec_insight": {"EN": "The matter concludes with happiness and true inner joy.", "FR": "L'affaire se conclut par le bonheur et une véritable joie intérieure."},
        "recommendation": {
            "EN": "Perform a 'Lustration' (ritual bath) with palm wine and sweet herbs to attract benevolent spirits.", 
            "FR": "Effectuez une lustration (bain rituel) au vin de palme et aux herbes douces pour attirer les esprits bienveillants."
        }
    },
    (2, 2, 2, 1): {
        "name": "Tristitia", 
        "meaning": {"EN": "Sorrow, depth, and foundations.", "FR": "Tristesse, profondeur et fondations."},
        "rec_insight": {"EN": "The result is solid but requires a serious, heavy effort.", "FR": "Le résultat est solide mais nécessite un effort sérieux et lourd."},
        "recommendation": {
            "EN": "Offer dark earth or clay to the spirits of the underworld to stabilize a shaky foundation.", 
            "FR": "Offrez de la terre noire ou de l'argile aux esprits du monde souterrain pour stabiliser une fondation fragile."
        }
    },
    (1, 2, 1, 1): {
        "name": "Puella", 
        "meaning": {"EN": "Harmony, beauty, and grace.", "FR": "Harmonie, beauté et grâce."},
        "rec_insight": {"EN": "Harmony is restored through kindness or social charm.", "FR": "L'harmonie est restaurée par la gentillesse ou le charme social."},
        "recommendation": {
            "EN": "Offer sweet scents or cowrie shells to the spirits of the water (Mami Wata) to preserve your beauty/grace.", 
            "FR": "Offrez des parfums doux ou des cauris aux esprits de l'eau (Mami Wata) pour préserver votre beauté et votre grâce."
        }
    },
    (1, 1, 2, 1): {
        "name": "Puer", 
        "meaning": {"EN": "Energy, action, and impulsive force.", "FR": "Énergie, action et force impulsive."},
        "rec_insight": {"EN": "A bold, energetic push will decide the final result.", "FR": "Un élan audacieux et énergique décidera du résultat final."},
        "recommendation": {
            "EN": "Light a fire or offer red palm oil to the divinity of iron/war (Ogun) to sharpen your resolve.", 
            "FR": "Allumez un feu ou offrez de l'huile de palme rouge à la divinité du fer (Ogun) pour aiguiser votre détermination."
        }
    },
    (2, 2, 1, 2): {
        "name": "Albus", 
        "meaning": {"EN": "Wisdom, peace, and clarity.", "FR": "Sagesse, paix et clarté."},
        "rec_insight": {"EN": "A clear, peaceful resolution through honest communication.", "FR": "Une résolution claire et pacifique grâce à une communication honnête."},
        "recommendation": {
            "EN": "Offer white chalk (Efun) or milk at your family altar to invite ancestors of wisdom and peace.", 
            "FR": "Offrez de la craie blanche (Efun) ou du lait sur votre autel familial pour inviter les ancêtres de sagesse et de paix."
        }
    },
    (2, 1, 2, 2): {
        "name": "Rubeus", 
        "meaning": {"EN": "Passion, vice, and danger.", "FR": "Passion, vice et danger."},
        "rec_insight": {"EN": "Warning: the final conclusion contains hidden volatile energy.", "FR": "Attention : la conclusion finale contient une énergie volatile cachée."},
        "recommendation": {
            "EN": "Sprinkle salt and pepper at your gate to confuse negative energies and avert the 'Evil Eye'.", 
            "FR": "Saupoudrez du sel et du poivre à votre portail pour égarer les énergies négatives et détourner le mauvais œil."
        }
    },
    (2, 1, 1, 1): {
        "name": "Caput Draconis", 
        "meaning": {"EN": "Beginnings and entry points.", "FR": "Commencements et points d'entrée."},
        "rec_insight": {"EN": "The result marks the start of a completely new chapter.", "FR": "Le résultat marque le début d'un chapitre totalement nouveau."},
        "recommendation": {
            "EN": "Crack a fresh coconut and pour the water over your head to baptize your new path in life.", 
            "FR": "Cassez une noix de coco fraîche et versez l'eau sur votre tête pour baptiser votre nouveau chemin de vie."
        }
    },
    (1, 1, 1, 2): {
        "name": "Cauda Draconis", 
        "meaning": {"EN": "Endings and exit points.", "FR": "Fins et points de sortie."},
        "rec_insight": {"EN": "The matter is finished; you must leave the past behind.", "FR": "L'affaire est terminée ; vous devez laisser le passé derrière vous."},
        "recommendation": {
            "EN": "Sweep your house with a traditional broom and burn the dust at a crossroads to banish the old cycle.", 
            "FR": "Balayez votre maison avec un balai traditionnel et brûlez la poussière à un carrefour pour bannir l'ancien cycle."
        }
    }
}

UI_TEXT = {
    "EN": {
        "title": "Maroon Oracle", "subtitle": "Mothers, Houses & Shield", "btn": "Generate Full Shield",
        "row": "Row", "foundation": "The 12 Houses (M1-M4, D1-D4, N1-N4)",
        "court": "The Final Verdict", "rec_label": "The Reconciler (Synthesis)", "error": "Fill all fields.", 
        "reset": "Reset All", "recommendation_title": "Spiritual Action (Ebo/Offering)"
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Maisons et Blason", "btn": "Générer le Blason",
        "row": "Ligne", "foundation": "Les 12 Maisons (M1-M4, D1-D4, N1-N4)",
        "court": "Le Verdict Final", "rec_label": "Le Réconciliateur (Synthèse)", "error": "Remplissez tout.", 
        "reset": "Réinitialiser", "recommendation_title": "Action Spirituelle (Ebo/Offrande)"
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
                                <span style='font-size:0.75rem; color:#880000;'>✨ {fig_info['recommendation'][L]}</span>
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
                        <p style='background:#f9f1f1; border:1px solid #eedddd; padding:12px; border-radius:10px; color:#700000; font-weight:bold; font-size:0.95rem;'>🏺 {T['recommendation_title']}: {j_info['recommendation'][L]}</p>
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
                        <div style='margin-top:20px; padding:20px; background:#fffafa; border:2px dashed {MAROON}; border-radius:12px;'>
                            <strong style='color:{MAROON}; font-size:1.1rem;'>🕊️ {T['recommendation_title']}:</strong><br>
                            <span style='font-size:1.25rem; color:#1e272e; font-style: italic;'>"{r_info['recommendation'][L]}"</span>
                        </div>
                        </div>""", unsafe_allow_html=True)
