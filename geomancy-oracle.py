import streamlit as st

# --- 1. DATA MAP: HAUSA & ZARMA/SONGHAY TERMINOLOGY ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {
        "latin": "Via", "hausa": "Hanya", "zarma": "Fondi",
        "meaning": {"EN": "Change and journeys.", "FR": "Changement et voyages."},
        "rec_insight": {"EN": "The path is open; the spirits of the road clear your way.", "FR": "Le chemin est ouvert ; les esprits de la route dégagent votre voie."},
        "recommendation": {
            "EN": "Pour a libation of 'Fura' (millet and milk) at a three-way crossroads.", 
            "FR": "Versez une libation de 'Fura' (mil et lait) à un carrefour à trois voies."
        }
    },
    (2, 2, 2, 2): {
        "latin": "Populus", "hausa": "Jama'a", "zarma": "Boro-boize",
        "meaning": {"EN": "Stability and public matters.", "FR": "Stabilité et affaires publiques."},
        "rec_insight": {"EN": "The community and the 'Doguwa' (Earth spirit) stand behind you.", "FR": "La communauté et la 'Doguwa' (esprit de la terre) vous soutiennent."},
        "recommendation": {
            "EN": "Offer a white hen to a communal shrine to ensure social peace.", 
            "FR": "Offrez une poule blanche à un autel pour assurer la paix sociale."
        }
    },
    (2, 1, 1, 2): {
        "latin": "Conjunctio", "hausa": "Gama", "zarma": "Marga",
        "meaning": {"EN": "Union and joining together.", "FR": "Union et rapprochement."},
        "rec_insight": {"EN": "A spiritual bond is forming; the Zima priest sees a meeting of souls.", "FR": "Un lien spirituel se forme ; le Zima voit une rencontre d'âmes."},
        "recommendation": {
            "EN": "Tie white and blue cloth together near a Baobab to bind this spiritual covenant.", 
            "FR": "Liez un tissu blanc et bleu près d'un baobab pour sceller cette alliance."
        }
    },
    (1, 2, 2, 1): {
        "latin": "Carcer", "hausa": "Sarka", "zarma": "Kase",
        "meaning": {"EN": "Restriction and delay.", "FR": "Restriction et retard."},
        "rec_insight": {"EN": "A spiritual lock exists. You are under the heavy gaze of Mai-Giro.", "FR": "Un verrou spirituel existe. Vous êtes sous le regard de Mai-Giro."},
        "recommendation": {
            "EN": "Break old iron or a dry gourd at a threshold to shatter the spiritual cage.", 
            "FR": "Brisez du vieux fer ou une calebasse à un seuil pour briser la cage spirituelle."
        }
    },
    (2, 2, 1, 1): {
        "latin": "Fortuna Major", "hausa": "Nasarawa", "zarma": "Izedu Beeri",
        "meaning": {"EN": "Great fortune and victory.", "FR": "Grande fortune et victoire."},
        "rec_insight": {"EN": "Sarkin Aljan (Spirit King) smiles upon this path.", "FR": "Sarkin Aljan (Le Roi des Esprits) sourit à ce chemin."},
        "recommendation": {
            "EN": "Sacrifice a white ram or distribute kola nuts to Bori practitioners.", 
            "FR": "Sacrifiez un bélier blanc ou donnez des noix de cola aux adeptes du Bori."
        }
    },
    (1, 1, 2, 2): {
        "latin": "Fortuna Minor", "hausa": "Bakin Wata", "zarma": "Izedu Kaina",
        "meaning": {"EN": "Small success and swift luck.", "FR": "Petite fortune et chance rapide."},
        "rec_insight": {"EN": "A quick blessing from the 'Holey' spirits is arriving.", "FR": "Une bénédiction rapide des esprits 'Holey' arrive."},
        "recommendation": {
            "EN": "Offer dates and honeyed water to children to activate the spirits of luck.", 
            "FR": "Offrez des dattes et de l'eau miellée aux enfants pour la chance."
        }
    },
    (2, 1, 2, 1): {
        "latin": "Acquisitio", "hausa": "Samu", "zarma": "Samu",
        "meaning": {"EN": "Profit and gain.", "FR": "Profit et gain."},
        "rec_insight": {"EN": "The river spirits (Harakoy) bring wealth to your bank.", "FR": "Les esprits du fleuve (Harakoy) apportent la richesse."},
        "recommendation": {
            "EN": "Bury seven cowrie shells in moist earth to ground the incoming wealth.", 
            "FR": "Enterrez sept cauris dans une terre humide pour enraciner la richesse."
        }
    },
    (1, 2, 1, 2): {
        "latin": "Amissio", "hausa": "Rashi", "zarma": "Wura",
        "meaning": {"EN": "Loss and letting go.", "FR": "Perte et lâcher-prise."},
        "rec_insight": {"EN": "The 'bad wind' must be released. Let the current take it.", "FR": "Le 'mauvais vent' doit être libéré. Laissez le courant l'emporter."},
        "recommendation": {
            "EN": "Ritual bath with black soap, then throw the sponge into a stream.", 
            "FR": "Bain rituel au savon noir, puis jetez l'éponge dans un cours d'eau."
        }
    },
    (1, 2, 2, 2): {
        "latin": "Laetitia", "hausa": "Fara'a", "zarma": "Kani-bine",
        "meaning": {"EN": "Joy and health.", "FR": "Joie et santé."},
        "rec_insight": {"EN": "The Goge fiddle plays for you; the spirits are dancing.", "FR": "Le violon Goge joue pour vous ; les esprits dansent."},
        "recommendation": {
            "EN": "Burn 'Turaren Wuta' (incense) and wear white to welcome light spirits.", 
            "FR": "Brûlez du 'Turaren Wuta' et portez du blanc pour accueillir les esprits."
        }
    },
    (2, 2, 2, 1): {
        "latin": "Tristitia", "hausa": "Bakin Ciki", "zarma": "Bine-saray",
        "meaning": {"EN": "Sorrow and depth.", "FR": "Tristesse et profondeur."},
        "rec_insight": {"EN": "The deep spirits of the caves demand heavy focus.", "FR": "Les esprits des grottes exigent une grande concentration."},
        "recommendation": {
            "EN": "Offer charcoal at a termite mound to stabilize your foundations.", 
            "FR": "Offrez du charbon sur une termitière pour stabiliser vos fondations."
        }
    },
    (1, 2, 1, 1): {
        "latin": "Puella", "hausa": "Yarinya", "zarma": "Way-boro",
        "meaning": {"EN": "Harmony and grace.", "FR": "Harmonie et grâce."},
        "rec_insight": {"EN": "The female Bori (Moussa) is present.", "FR": "Le Bori féminin (Moussa) est présent."},
        "recommendation": {
            "EN": "Apply henna (Lalle) to your palms and offer perfume to water.", 
            "FR": "Appliquez du henné (Lalle) et offrez du parfum à l'eau."
        }
    },
    (1, 1, 2, 1): {
        "latin": "Puer", "hausa": "Yaro", "zarma": "Izedu-boro",
        "meaning": {"EN": "Energy and force.", "FR": "Énergie et force."},
        "rec_insight": {"EN": "Dongo the Thunderer provides the spark. Strike now.", "FR": "Dongo le Tonnerre fournit l'étincelle. Agissez maintenant."},
        "recommendation": {
            "EN": "Offer red palm oil to iron tools to harness the heat of the fire spirit.", 
            "FR": "Versez de l'huile de palme sur des outils en fer pour l'esprit du feu."
        }
    },
    (2, 2, 1, 2): {
        "latin": "Albus", "hausa": "Fari", "zarma": "Kwaaray",
        "meaning": {"EN": "Wisdom and peace.", "FR": "Sagesse et paix."},
        "rec_insight": {"EN": "The 'White Spirits' (Bori Fari) bring a message of truth.", "FR": "Les 'Esprits Blancs' (Bori Fari) apportent la vérité."},
        "recommendation": {
            "EN": "Offer white milk and white kola to elders to invite ancestral wisdom.", 
            "FR": "Offrez du lait et des noix de cola blanches aux anciens pour la sagesse."
        }
    },
    (2, 1, 2, 2): {
        "latin": "Rubeus", "hausa": "Ja", "zarma": "Chirey",
        "meaning": {"EN": "Danger and passion.", "FR": "Danger et passion."},
        "rec_insight": {"EN": "The 'Red Winds' blow. Beware of spiritual poison.", "FR": "Les 'Vents Rouges' soufflent. Attention au poison spirituel."},
        "recommendation": {
            "EN": "Sprinkle wood ash around your gate to neutralize the Evil Eye.", 
            "FR": "Saupoudrez de la cendre à votre portail contre le mauvais œil."
        }
    },
    (2, 1, 1, 1): {
        "latin": "Caput Draconis", "hausa": "Kan Maciji", "zarma": "Dongo-me",
        "meaning": {"EN": "Beginnings and entry.", "FR": "Commencements et entrée."},
        "rec_insight": {"EN": "A new moon cycle begins. The threshold spirits are watching.", "FR": "Un nouveau cycle commence. Les esprits du seuil observent."},
        "recommendation": {
            "EN": "Plant a Neem seedling near your compound as a protective shield.", 
            "FR": "Plantez un jeune Neem près de votre concession pour la protection."
        }
    },
    (1, 1, 1, 2): {
        "latin": "Cauda Draconis", "hausa": "Wutsiyar Maciji", "zarma": "Dongo-wanda",
        "meaning": {"EN": "Endings and exit.", "FR": "Fins et sortie."},
        "rec_insight": {"EN": "The debt is paid. The old spirits depart.", "FR": "La dette est payée. Les anciens esprits s'en vont."},
        "recommendation": {
            "EN": "Sweep the entrance at sunset with a local broom to banish the past.", 
            "FR": "Balayez l'entrée au coucher du soleil pour bannir le passé."
        }
    }
}

UI_TEXT = {
    "EN": {
        "title": "Maroon Oracle", "subtitle": "Hausa & Songhay Divination", "btn": "Generate Shield",
        "reset": "Reset", "rec_label": "Synthesis (The Zima's Word)", "recommendation_title": "Sacred Offering (Sadaka)"
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Divination Haoussa & Songhaï", "btn": "Générer le Blason",
        "reset": "Réinitialiser", "rec_label": "Synthèse (La Parole du Zima)", "recommendation_title": "Offrande Sacrée (Sadaka)"
    }
}

MAROON = "#800000"

# --- Functions ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_card(fig, label, hausa, zarma, color=MAROON):
    rows = "".join([f"<div style='font-size: 35px; color: {color}; line-height: 1.1; margin: 2px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;●'}</div>" for r in fig])
    return f"""
    <div style="background: white; border: 1px solid #edf0f2; border-radius: 20px; padding: 15px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
        <div style="font-size: 0.7rem; color: #a0a0a0; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;">{label}</div>
        <div style="margin: 10px 0;">{rows}</div>
        <div style="font-size: 0.85rem; font-weight: 800; color: #333;">{hausa} / {zarma}</div>
    </div>
    """

def process_input(s):
    clean = s.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- UI Layout ---
st.set_page_config(page_title="Maroon Oracle", layout="wide")
st.markdown("""<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;800&display=swap');
    html, body, [data-testid="stAppViewContainer"] { background-color: #f8fafc; font-family: 'Outfit', sans-serif; }
    h1 { font-weight: 800; color: #1e272e !important; text-align: center; }
    .stButton>button { background: #800000 !important; color: white !important; border-radius: 15px !important; font-weight: 700 !important; }
    </style>""", unsafe_allow_html=True)

lang_choice = st.sidebar.selectbox("Language / Langue", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]

st.title(T["title"])
st.markdown(f"<p style='text-align: center; color: #888;'>{T['subtitle']}</p>", unsafe_allow_html=True)

m_cols = st.columns(4)
mothers_input = []
for i in range(4):
    with m_cols[i]:
        st.markdown(f"<h4 style='text-align:center;'>M{i+1}</h4>", unsafe_allow_html=True)
        m_rows = [st.text_input(f"M{i+1}L{j+1}", key=f"m{i}r{j}", label_visibility="collapsed") for j in range(4)]
        mothers_input.append(m_rows)

if st.button(T["btn"], use_container_width=True):
    M_figs = []
    for rows in mothers_input:
        proc = [process_input(r) for r in rows]
        if None in proc: st.error("Fill all fields."); st.stop()
        M_figs.append(proc)
    
    D_figs = [[M_figs[j][i] for j in range(4)] for i in range(4)]
    N_figs = [add_figs(M_figs[0], M_figs[1]), add_figs(M_figs[2], M_figs[3]), add_figs(D_figs[0], D_figs[1]), add_figs(D_figs[2], D_figs[3])]
    RW, LW = add_figs(N_figs[0], N_figs[1]), add_figs(N_figs[2], N_figs[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M_figs[0])

    # DISPLAY 12 HOUSES
    labels = ["M1", "M2", "M3", "M4", "D1", "D2", "D3", "D4", "N1", "N2", "N3", "N4"]
    data = M_figs + D_figs + N_figs
    for row in range(0, 12, 4):
        cols = st.columns(4)
        for c in range(4):
            idx = row + c
            info = GEOMANTIC_DATA[tuple(data[idx])]
            cols[c].markdown(render_card(data[idx], labels[idx], info['hausa'], info['zarma']), unsafe_allow_html=True)
            cols[c].markdown(f"<div style='font-size:0.7rem; color:#800000; text-align:center;'>🏺 {info['recommendation'][L]}</div>", unsafe_allow_html=True)

    # FINAL SYNTHESIS
    st.divider()
    res_a, res_b = st.columns([1, 2])
    r_info = GEOMANTIC_DATA[tuple(Reconciler)]
    with res_a:
        st.markdown(render_card(Reconciler, T["rec_label"], r_info['hausa'], r_info['zarma']), unsafe_allow_html=True)
    with res_b:
        st.markdown(f"""<div style='background:white; border-left:12px solid {MAROON}; padding:25px; border-radius:15px; box-shadow:0 10px 30px rgba(0,0,0,0.08);'>
                        <h2 style='margin:0; color:{MAROON};'>{r_info['hausa']} / {r_info['zarma']}</h2>
                        <p style='font-size:1.3rem; font-weight:bold; color:#2d3436;'>{r_info['rec_insight'][L]}</p>
                        <div style='margin-top:15px; padding:15px; background:#fffafa; border:2px dashed {MAROON}; border-radius:12px;'>
                            <strong style='color:{MAROON};'>✨ {T['recommendation_title']}:</strong><br>
                            <span style='font-size:1.1rem; color:#444;'>"{r_info['recommendation'][L]}"</span>
                        </div>
                        </div>""", unsafe_allow_html=True)
