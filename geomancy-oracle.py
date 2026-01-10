import streamlit as st

# --- 1. DATA MAP: HAUSA (MAGUZAWA) & ZARMA/SONGHAY CONTEXT ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {
        "name": "Via", 
        "meaning": {"EN": "Change, movement, and journeys.", "FR": "Changement, mouvement et voyages."},
        "rec_insight": {"EN": "The path is open; the spirits of the road clear your way.", "FR": "Le chemin est ouvert ; les esprits de la route dégagent votre voie."},
        "recommendation": {
            "EN": "Pour a libation of 'Fura' (millet and milk) at a three-way crossroads to appease the spirits of movement.", 
            "FR": "Versez une libation de 'Fura' (mil et lait) à un carrefour à trois voies pour apaiser les esprits du mouvement."
        }
    },
    (2, 2, 2, 2): {
        "name": "Populus", 
        "meaning": {"EN": "Stability, crowds, and public matters.", "FR": "Stabilité, foules et affaires publiques."},
        "rec_insight": {"EN": "The ancestors and the community (Jama'a) stand behind this matter.", "FR": "Les ancêtres et la communauté (Jama'a) soutiennent cette affaire."},
        "recommendation": {
            "EN": "Offer a white hen to the village elders or a communal shrine to ensure the 'Doguwa' (Earth spirit) remains peaceful.", 
            "FR": "Offrez une poule blanche aux anciens ou à un autel communautaire pour que la 'Doguwa' reste paisible."
        }
    },
    (2, 1, 1, 2): {
        "name": "Conjunctio", 
        "meaning": {"EN": "Union, contracts, and joining together.", "FR": "Union, contrats et rapprochement."},
        "rec_insight": {"EN": "A spiritual bond is forming; the Zima (priest) sees a meeting of souls.", "FR": "Un lien spirituel se forme ; le Zima (prêtre) voit une rencontre d'âmes."},
        "recommendation": {
            "EN": "Tie a piece of white and blue cloth together and leave it near a Baobab tree to bind this agreement spiritually.", 
            "FR": "Liez ensemble un morceau de tissu blanc et bleu et laissez-le près d'un baobab pour sceller cet accord."
        }
    },
    (1, 2, 2, 1): {
        "name": "Carcer", 
        "meaning": {"EN": "Restriction, boundaries, and delay.", "FR": "Restriction, limites et retard."},
        "rec_insight": {"EN": "A spiritual 'lock' exists. You are under the gaze of Mai-Giro.", "FR": "Un verrou spirituel existe. Vous êtes sous le regard de Mai-Giro."},
        "recommendation": {
            "EN": "Break a piece of old iron or a dry gourd at a threshold to shatter the spiritual cage holding you.", 
            "FR": "Brisez un morceau de vieux fer ou une calebasse sèche à un seuil pour briser la cage spirituelle qui vous retient."
        }
    },
    (2, 2, 1, 1): {
        "name": "Fortuna Major", 
        "meaning": {"EN": "Great fortune and inner strength.", "FR": "Grande fortune et force intérieure."},
        "rec_insight": {"EN": "Sarkin Aljan (the King of Spirits) smiles upon this path.", "FR": "Sarkin Aljan (le Roi des Esprits) sourit à ce chemin."},
        "recommendation": {
            "EN": "Sacrifice a white ram or distribute high-quality kola nuts to the Bori practitioners as a thank offering.", 
            "FR": "Sacrifiez un bélier blanc ou distribuez des noix de cola de qualité aux adeptes du Bori en guise d'offrande."
        }
    },
    (1, 1, 2, 2): {
        "name": "Fortuna Minor", 
        "meaning": {"EN": "Small success and swift external luck.", "FR": "Petite fortune et chance externe rapide."},
        "rec_insight": {"EN": "A quick blessing from the 'Holey' spirits is arriving. Catch it fast.", "FR": "Une bénédiction rapide des esprits 'Holey' arrive. Saisissez-la vite."},
        "recommendation": {
            "EN": "Offer sweet dates and honeyed water to children in your compound to activate the spirits of luck.", 
            "FR": "Offrez des dattes et de l'eau miellée aux enfants de votre concession pour activer les esprits de la chance."
        }
    },
    (2, 1, 2, 1): {
        "name": "Acquisitio", 
        "meaning": {"EN": "Profit, gain, and expansion.", "FR": "Profit, gain et expansion."},
        "rec_insight": {"EN": "The spirits of the river (Harakoy) bring wealth to your bank.", "FR": "Les esprits du fleuve (Harakoy) apportent la richesse sur votre rive."},
        "recommendation": {
            "EN": "Bury a silver ring or seven cowrie shells in moist earth to ground the incoming wealth.", 
            "FR": "Enterrez une bague en argent ou sept cauris dans une terre humide pour enraciner la richesse à venir."
        }
    },
    (1, 2, 1, 2): {
        "name": "Amissio", 
        "meaning": {"EN": "Loss and letting go.", "FR": "Perte et lâcher-prise."},
        "rec_insight": {"EN": "The 'bad wind' must be released. Let the current take it.", "FR": "Le 'mauvais vent' doit être libéré. Laissez le courant l'emporter."},
        "recommendation": {
            "EN": "Perform a ritual bath with black soap and 'Scent Leaf,' then throw the sponge into a moving stream.", 
            "FR": "Faites un bain rituel avec du savon noir et du basilic africain, puis jetez l'éponge dans un cours d'eau."
        }
    },
    (1, 2, 2, 2): {
        "name": "Laetitia", 
        "meaning": {"EN": "Joy, health, and positive news.", "FR": "Joie, santé et nouvelles positives."},
        "rec_insight": {"EN": "The 'Goge' fiddle plays in your honor; the spirits are dancing.", "FR": "Le violon 'Goge' joue en votre honneur ; les esprits dansent."},
        "recommendation": {
            "EN": "Burn 'Turaren Wuta' (traditional incense) and wear your finest white garment to welcome the light spirits.", 
            "FR": "Brûlez du 'Turaren Wuta' (encens traditionnel) et portez votre plus beau vêtement blanc pour accueillir les esprits."
        }
    },
    (2, 2, 2, 1): {
        "name": "Tristitia", 
        "meaning": {"EN": "Sorrow, depth, and foundations.", "FR": "Tristesse, profondeur et fondations."},
        "rec_insight": {"EN": "The deep spirits of the caves demand a heavy focus.", "FR": "Les esprits profonds des grottes exigent une grande concentration."},
        "recommendation": {
            "EN": "Offer charcoal and dark grains at the base of a termite mound to stabilize your spiritual foundations.", 
            "FR": "Offrez du charbon et des graines sombres au pied d'une termitière pour stabiliser vos fondations."
        }
    },
    (1, 2, 1, 1): {
        "name": "Puella", 
        "meaning": {"EN": "Harmony, beauty, and grace.", "FR": "Harmonie, beauté et grâce."},
        "rec_insight": {"EN": "The spirits of beauty (Moussa or female Bori) are present.", "FR": "Les esprits de la beauté (Moussa ou Bori féminins) sont présents."},
        "recommendation": {
            "EN": "Apply henna (Lalle) to your palms or offer sweet perfume to a sacred water source.", 
            "FR": "Appliquez du henné (Lalle) sur vos paumes ou offrez du parfum doux à une source d'eau sacrée."
        }
    },
    (1, 1, 2, 1): {
        "name": "Puer", 
        "meaning": {"EN": "Energy, action, and impulsive force.", "FR": "Énergie, action et force impulsive."},
        "rec_insight": {"EN": "Dongo (the Thunderer) provides the spark. Strike while the iron is hot.", "FR": "Dongo (le Tonnerre) fournit l'étincelle. Battez le fer tant qu'il est chaud."},
        "recommendation": {
            "EN": "Offer a red rooster or spill red palm oil on iron tools to harness the heat of the 'Holey' of fire.", 
            "FR": "Offrez un coq rouge ou versez de l'huile de palme sur des outils en fer pour canaliser la chaleur de l'esprit du feu."
        }
    },
    (2, 2, 1, 2): {
        "name": "Albus", 
        "meaning": {"EN": "Wisdom, peace, and clarity.", "FR": "Sagesse, paix et clarté."},
        "rec_insight": {"EN": "The 'White Spirits' (Bori Fari) bring a message of truth.", "FR": "Les 'Esprits Blancs' (Bori Fari) apportent un message de vérité."},
        "recommendation": {
            "EN": "Offer a bowl of white milk and white kola nuts to the elders of your family to invite ancestral wisdom.", 
            "FR": "Offrez un bol de lait blanc et des noix de cola blanches aux anciens de votre famille pour inviter la sagesse."
        }
    },
    (2, 1, 2, 2): {
        "name": "Rubeus", 
        "meaning": {"EN": "Passion, vice, and danger.", "FR": "Passion, vice et danger."},
        "rec_insight": {"EN": "The 'Red Winds' are blowing. Beware of spiritual 'poison'.", "FR": "Les 'Vents Rouges' soufflent. Attention au 'poison' spirituel."},
        "recommendation": {
            "EN": "Sprinkle wood ash around your sleeping area to neutralize negative charms and 'Evil Eye'.", 
            "FR": "Saupoudrez de la cendre de bois autour de votre lit pour neutraliser les charmes négatifs et le mauvais œil."
        }
    },
    (2, 1, 1, 1): {
        "name": "Caput Draconis", 
        "meaning": {"EN": "Beginnings and entry points.", "FR": "Commencements et points d'entrée."},
        "rec_insight": {"EN": "A new moon cycle begins. The spirits of the gate are watching.", "FR": "Un nouveau cycle lunaire commence. Les esprits du seuil observent."},
        "recommendation": {
            "EN": "Plant a Tamarind or Neem seedling near your compound to grow a new protective spiritual shield.", 
            "FR": "Plantez un jeune plant de tamarinier ou de neem près de votre concession pour faire croître un nouveau bouclier."
        }
    },
    (1, 1, 1, 2): {
        "name": "Cauda Draconis", 
        "meaning": {"EN": "Endings and exit points.", "FR": "Fins et points de sortie."},
        "rec_insight": {"EN": "The debt is paid. The old spirits depart.", "FR": "La dette est payée. Les anciens esprits s'en vont."},
        "recommendation": {
            "EN": "Discard an old calabash or sweep the entrance of your home at sunset to banish the past.", 
            "FR": "Jetez une vieille calebasse ou balayez l'entrée de votre maison au coucher du soleil pour bannir le passé."
        }
    }
}

UI_TEXT = {
    "EN": {
        "title": "Maroon Oracle", "subtitle": "Hausa & Songhay Tradition", "btn": "Generate Full Shield",
        "row": "Row", "foundation": "The 12 Houses (M1-N4)",
        "court": "The Bori Court (Judge)", "rec_label": "The Zima's Synthesis", "error": "Fill all fields.", 
        "reset": "Reset All", "recommendation_title": "Sacred Action (Sadaka/Offerings)"
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Tradition Haoussa & Songhaï", "btn": "Générer le Blason",
        "row": "Ligne", "foundation": "Les 12 Maisons (M1-N4)",
        "court": "La Cour du Bori (Juge)", "rec_label": "Synthèse du Zima", "error": "Remplissez tout.", 
        "reset": "Réinitialiser", "recommendation_title": "Action Sacrée (Sadaka/Offrandes)"
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
                                <span style='font-size:0.75rem; color:#880000;'>🏺 {fig_info['recommendation'][L]}</span>
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
                        <p style='background:#fdf5f5; border:1px solid #eedddd; padding:12px; border-radius:10px; color:#900000; font-weight:bold; font-size:0.95rem;'>🕯️ {T['recommendation_title']}: {j_info['recommendation'][L]}</p>
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
                        <div style='margin-top:20px; padding:20px; background:#f9f9f9; border:2px dashed {MAROON}; border-radius:12px;'>
                            <strong style='color:{MAROON}; font-size:1.1rem;'>✨ {T['recommendation_title']}:</strong><br>
                            <span style='font-size:1.25rem; color:#1e272e; font-style: italic;'>"{r_info['recommendation'][L]}"</span>
                        </div>
                        </div>""", unsafe_allow_html=True)
