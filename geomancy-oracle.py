import streamlit as st

# --- 1. DATA MAP: TRILINGUAL TERMINOLOGY & SPIRITUAL ACTIONS ---
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

HOUSE_METADATA = {
    1: {"EN": "Life, Soul & Persona", "FR": "Vie, Âme et Personnalité"},
    2: {"EN": "Wealth & Assets", "FR": "Richesse et Biens"},
    3: {"EN": "Communication & Siblings", "FR": "Communication et Fratrie"},
    4: {"EN": "The Home & Ancestry", "FR": "Foyer et Ascendance"},
    5: {"EN": "Creativity & Children", "FR": "Créativité et Enfants"},
    6: {"EN": "Service & Health", "FR": "Service et Santé"},
    7: {"EN": "Partnership & Marriage", "FR": "Partenariat et Mariage"},
    8: {"EN": "Transformation & Debt", "FR": "Transformation et Dettes"},
    9: {"EN": "Wisdom & Journeys", "FR": "Sagesse et Voyages"},
    10: {"EN": "Honor & Career", "FR": "Honneur et Carrière"},
    11: {"EN": "Friends & Hopes", "FR": "Amis et Espoirs"},
    12: {"EN": "Subconscious & Solitude", "FR": "Inconscient et Solitude"}
}

UI_TEXT = {
    "EN": {
        "title": "Maroon Oracle", "subtitle": "Hausa & Songhay Divination", "btn": "Unlock the Twelve Houses",
        "reset": "Reset Oracle", "houses": "I. The Twelve Houses of Existence",
        "court": "II. The Court of Finality", "reconciler": "III. The Great Reconciler",
        "rec_title": "Spiritual Sadaka Required", "error": "All 4 Mothers must be entered."
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Divination Haoussa & Songhaï", "btn": "Déverrouiller les Douze Maisons",
        "reset": "Réinitialiser", "houses": "I. Les Douze Maisons de l'Existence",
        "court": "II. La Cour de Finalité", "reconciler": "III. Le Grand Réconciliateur",
        "rec_title": "Sadaka Spirituelle Requise", "error": "Les 4 Mères doivent être remplies."
    }
}

MAROON = "#800000"
GOLD = "#D4AF37"
DARK_BLUE = "#001F3F"

# --- Logic Functions ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def process_input(s):
    clean = s.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

def render_house_card(fig, h_num, info, lang):
    """Refined UI for individual houses"""
    meta = HOUSE_METADATA[h_num][lang]
    dots = "".join([f"<div style='font-size: 24px; color: {MAROON}; line-height: 0.7; margin: 4px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;●'}</div>" for r in fig])
    
    return f"""
    <div style="background: white; border-top: 5px solid {MAROON}; border-radius: 12px; padding: 15px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin-bottom: 20px;">
        <div style="font-size: 0.7rem; color: #888; font-weight: 800; letter-spacing: 1px;">HOUSE {h_num}</div>
        <div style="font-size: 0.85rem; color: {DARK_BLUE}; font-weight: 700; margin-bottom: 8px; height: 35px;">{meta}</div>
        <div style="margin: 15px 0;">{dots}</div>
        <div style="font-size: 1.1rem; font-weight: 900; color: #111;">{info['hausa']}</div>
        <div style="font-size: 0.7rem; color: #666; font-style: italic;">({info['latin']})</div>
    </div>
    """

# --- App Config ---
st.set_page_config(page_title="Maroon Oracle", layout="wide")
st.markdown(f"""<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] {{ background-color: #fdfcfb; font-family: 'Outfit', sans-serif; }}
    .stButton>button {{ background: linear-gradient(135deg, {MAROON}, #a00000) !important; color: white !important; border-radius: 10px !important; font-weight: 800 !important; letter-spacing: 1px; }}
    h1 {{ font-weight: 900; letter-spacing: -1px; color: {DARK_BLUE} !important; }}
    h2 {{ color: {MAROON} !important; font-weight: 800; border-left: 5px solid {GOLD}; padding-left: 15px; }}
    </style>""", unsafe_allow_html=True)

# SIDEBAR
lang_choice = st.sidebar.radio("Language", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]
if st.sidebar.button(T["reset"]): st.rerun()

# HEADER
st.title(f"🏺 {T['title']}")
st.markdown(f"<p style='text-align: center; color: #555; font-size: 1.2rem; margin-top: -20px;'>{T['subtitle']}</p>", unsafe_allow_html=True)

# INPUT AREA
st.markdown("---")
m_cols = st.columns(4)
mothers_input = []
for i in range(4):
    with m_cols[i]:
        st.markdown(f"<div style='text-align:center; font-weight:900; color:{MAROON};'>MOTHER {i+1}</div>", unsafe_allow_html=True)
        m_rows = [st.text_input(f"M{i+1}L{j+1}", key=f"m{i}r{j}", label_visibility="collapsed", placeholder="••••") for j in range(4)]
        mothers_input.append(m_rows)

if st.button(T["btn"], use_container_width=True):
    # Core Logic
    M_figs = []
    for rows in mothers_input:
        proc = [process_input(r) for r in rows]
        if None in proc: st.error(T["error"]); st.stop()
        M_figs.append(proc)
    
    # Generate the 12 Houses
    D_figs = [[M_figs[j][i] for j in range(4)] for i in range(4)]
    N_figs = [add_figs(M_figs[0], M_figs[1]), add_figs(M_figs[2], M_figs[3]), 
              add_figs(D_figs[0], D_figs[1]), add_figs(D_figs[2], D_figs[3])]
    
    # Full list for indexing Houses 1-12
    HOUSES = M_figs + D_figs + N_figs
    
    # Witnesses and Judge
    RW = add_figs(N_figs[0], N_figs[1])
    LW = add_figs(N_figs[2], N_figs[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M_figs[0])

    # DISPLAY 1: TWELVE HOUSES
    st.header(T["houses"])
    h_grid = st.columns(4)
    for i in range(12):
        with h_grid[i % 4]:
            info = GEOMANTIC_DATA[tuple(HOUSES[i])]
            st.markdown(render_house_card(HOUSES[i], i+1, info, L), unsafe_allow_html=True)

    # DISPLAY 2: THE COURT
    st.header(T["court"])
    c_cols = st.columns([1, 1, 2])
    
    with c_cols[0]:
        info_rw = GEOMANTIC_DATA[tuple(RW)]
        st.markdown(f"<div style='text-align:center; padding:10px; border:1px solid #ddd; border-radius:10px;'><strong>Right Witness</strong><br>{info_rw['hausa']}</div>", unsafe_allow_html=True)
        st.markdown(render_house_card(RW, "RW", info_rw, L), unsafe_allow_html=True)
    with c_cols[1]:
        info_lw = GEOMANTIC_DATA[tuple(LW)]
        st.markdown(f"<div style='text-align:center; padding:10px; border:1px solid #ddd; border-radius:10px;'><strong>Left Witness</strong><br>{info_lw['hausa']}</div>", unsafe_allow_html=True)
        st.markdown(render_house_card(LW, "LW", info_lw, L), unsafe_allow_html=True)
    with c_cols[2]:
        info_j = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(f"""<div style='background:{DARK_BLUE}; color:white; padding:30px; border-radius:15px; border-bottom: 8px solid {GOLD};'>
                        <h3 style='margin:0; color:{GOLD};'>THE JUDGE: {info_j['hausa']}</h3>
                        <p style='font-size:1.2rem; line-height:1.4;'>{info_j['meaning'][L]}</p>
                        <div style='margin-top:20px; padding:15px; background:rgba(255,255,255,0.1); border-radius:8px;'>
                            <strong>⚖️ Guidance:</strong> {info_j['recommendation'][L]}
                        </div>
                    </div>""", unsafe_allow_html=True)

    # DISPLAY 3: RECONCILER
    st.header(T["reconciler"])
    info_rec = GEOMANTIC_DATA[tuple(Reconciler)]
    st.markdown(f"""<div style='background:white; border:2px solid {MAROON}; border-radius:20px; overflow:hidden; box-shadow:0 20px 50px rgba(0,0,0,0.1);'>
                    <div style='background:{MAROON}; color:white; padding:20px; text-align:center;'>
                        <h1 style='color:{GOLD} !important; margin:0;'>{info_rec['hausa']} / {info_rec['zarma']}</h1>
                        <span style='text-transform:uppercase; letter-spacing:3px; font-size:0.8rem;'>{info_rec['latin']}</span>
                    </div>
                    <div style='padding:40px;'>
                        <p style='font-size:1.6rem; font-weight:700; color:{DARK_BLUE}; text-align:center;'>"{info_rec['rec_insight'][L]}"</p>
                        <div style='margin-top:30px; background:#fff9f9; padding:30px; border-radius:15px; border: 1px dashed {MAROON};'>
                            <h4 style='color:{MAROON}; margin-top:0;'>🔥 {T['rec_title']}</h4>
                            <p style='font-size:1.3rem; color:#333; font-weight:600;'>{info_rec['recommendation'][L]}</p>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)
