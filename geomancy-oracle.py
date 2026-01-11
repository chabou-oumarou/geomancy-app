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

HOUSE_MEANINGS = {
    1: {"EN": "Life, Soul, & Body", "FR": "Vie, Âme et Corps"},
    2: {"EN": "Wealth, Money, & Gain", "FR": "Richesse, Argent et Gain"},
    3: {"EN": "Siblings, Short Trips, & News", "FR": "Fratrie, Courts Voyages et Nouvelles"},
    4: {"EN": "Father, Home, & Ancestry", "FR": "Père, Foyer et Ascendance"},
    5: {"EN": "Children, Joy, & Creativity", "FR": "Enfants, Joie et Créativité"},
    6: {"EN": "Sickness, Service, & Work", "FR": "Maladie, Service et Travail"},
    7: {"EN": "Marriage, Partners, & Open Enemies", "FR": "Mariage, Partenaires et Ennemis Ouverts"},
    8: {"EN": "Death, Inheritances, & Hidden Things", "FR": "Mort, Héritages et Choses Cachées"},
    9: {"EN": "Religion, Long Journeys, & Wisdom", "FR": "Religion, Longs Voyages et Sagesse"},
    10: {"EN": "Power, Career, & Success", "FR": "Pouvoir, Carrière et Succès"},
    11: {"EN": "Friends, Hopes, & Desires", "FR": "Amis, Espoirs et Désirs"},
    12: {"EN": "Prison, Secret Enemies, & Sorrow", "FR": "Prison, Ennemis Secrets et Tristesse"}
}

UI_TEXT = {
    "EN": {
        "title": "Maroon Oracle", "subtitle": "Hausa & Songhay Divination", "btn": "Generate Full Shield",
        "reset": "Reset All", "foundations": "1. Foundations (Mothers & Daughters)", "houses": "2. The Twelve Houses",
        "court": "3. The Court (Witnesses & Judge)", "reconciler": "4. The Reconciler (Final Synthesis)",
        "rec_title": "Spiritual Sadaka Required", "error": "Please fill all fields."
    },
    "FR": {
        "title": "L'Oracle Marron", "subtitle": "Divination Haoussa & Songhaï", "btn": "Générer le Blason",
        "reset": "Réinitialiser", "foundations": "1. Fondations (Mères & Filles)", "houses": "2. Les Douze Maisons",
        "court": "3. La Cour (Témoins & Juge)", "reconciler": "4. Le Réconciliateur (Synthèse Finale)",
        "rec_title": "Sadaka Spirituelle Requise", "error": "Veuillez remplir tous les champs."
    }
}

MAROON = "#800000"
DARK_BLUE = "#003366"

# --- Functions ---
def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_card(fig, label, latin, hausa, zarma, color=MAROON, highlight=False, sub_label=None):
    border = f"4px solid {color}" if highlight else "1px solid #edf0f2"
    shadow = f"0 15px 40px {color}33" if highlight else "0 6px 18px rgba(0,0,0,0.06)"
    
    rows = "".join([f"<div style='font-size: 26px; color: {color}; line-height: 0.8; margin: 2px 0;'>{'●' if r == 1 else '●&nbsp;&nbsp;●'}</div>" for r in fig])
    
    sub_html = f"<div style='font-size: 0.7rem; color: #777; font-weight: bold; margin-bottom: 5px;'>{sub_label}</div>" if sub_label else ""
    
    return f"""
    <div style="background: white; border: {border}; border-radius: 18px; padding: 15px; text-align: center; box-shadow: {shadow}; margin-bottom: 12px;">
        <div style="font-size: 0.65rem; color: #a0a0a0; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px;">{label}</div>
        {sub_html}
        <div style="margin: 10px 0;">{rows}</div>
        <div style="font-size: 1.0rem; font-weight: 900; color: #111; margin-top: 5px;">{latin}</div>
        <div style="font-size: 0.85rem; color: {color}; font-weight: 700;">{hausa} / {zarma}</div>
    </div>
    """

def process_input(s):
    clean = s.replace(" ", "")
    return (1 if len(clean) % 2 != 0 else 2) if clean else None

# --- UI Layout ---
st.set_page_config(page_title="Maroon Oracle", layout="wide")
st.markdown(f"""<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;800;900&display=swap');
    html, body, [data-testid="stAppViewContainer"] {{ background-color: #f8fafc; font-family: 'Outfit', sans-serif; }}
    h1 {{ font-weight: 900; color: #1e272e !important; text-align: center; font-size: 3rem !important; }}
    h2 {{ color: {MAROON} !important; border-bottom: 3px solid {MAROON}22; padding-bottom: 8px; margin-top: 35px; font-size: 1.8rem; font-weight: 800; }}
    .stButton>button {{ background: {MAROON} !important; color: white !important; border-radius: 15px !important; height: 60px !important; width: 100%; font-size: 1.2rem !important; font-weight: 800 !important; }}
    </style>""", unsafe_allow_html=True)

# SIDEBAR
lang_choice = st.sidebar.selectbox("🌐 Language", ["English", "Français"])
L = "EN" if lang_choice == "English" else "FR"
T = UI_TEXT[L]
if st.sidebar.button(T["reset"]): st.rerun()

st.title(T["title"])
st.markdown(f"<p style='text-align: center; color: #666; margin-top:-20px; font-size: 1.2rem;'>{T['subtitle']}</p>", unsafe_allow_html=True)

# INPUT SECTION
st.markdown("<br>", unsafe_allow_html=True)
m_cols = st.columns(4)
mothers_input = []
for i in range(4):
    with m_cols[i]:
        st.markdown(f"<div style='text-align:center; font-weight:900; font-size:1.2rem; color:#444; margin-bottom:10px;'>M{i+1}</div>", unsafe_allow_html=True)
        m_rows = [st.text_input(f"M{i+1}L{j+1}", key=f"m{i}r{j}", label_visibility="collapsed", placeholder="••••") for j in range(4)]
        mothers_input.append(m_rows)

if st.button(T["btn"], type="primary"):
    M_figs = []
    for rows in mothers_input:
        proc = [process_input(r) for r in rows]
        if None in proc: st.error(T["error"]); st.stop()
        M_figs.append(proc)
    
    D_figs = [[M_figs[j][i] for j in range(4)] for i in range(4)]
    N_figs = [add_figs(M_figs[0], M_figs[1]), add_figs(M_figs[2], M_figs[3]), 
              add_figs(D_figs[0], D_figs[1]), add_figs(D_figs[2], D_figs[3])]
    
    # 12 Houses Mapping: H1-4(M), H5-8(D), H9-12(N)
    HOUSES = M_figs + D_figs + N_figs
    
    RW = add_figs(N_figs[0], N_figs[1])
    LW = add_figs(N_figs[2], N_figs[3])
    Judge = add_figs(RW, LW)
    Reconciler = add_figs(Judge, M_figs[0])

    # DISPLAY 1: FOUNDATIONS (Mothers & Daughters)
    st.header(T["foundations"])
    f_cols = st.columns(8)
    f_labels = ["M1", "M2", "M3", "M4", "D1", "D2", "D3", "D4"]
    f_data = M_figs + D_figs
    for i in range(8):
        info = GEOMANTIC_DATA[tuple(f_data[i])]
        f_cols[i].markdown(render_card(f_data[i], f_labels[i], info['latin'], info['hausa'], info['zarma']), unsafe_allow_html=True)

    # DISPLAY 2: THE TWELVE HOUSES
    st.header(T["houses"])
    h_row1 = st.columns(4)
    h_row2 = st.columns(4)
    h_row3 = st.columns(4)
    all_h_cols = h_row1 + h_row2 + h_row3
    
    for i in range(12):
        info = GEOMANTIC_DATA[tuple(HOUSES[i])]
        h_meaning = HOUSE_MEANINGS[i+1][L]
        all_h_cols[i].markdown(render_card(HOUSES[i], f"House {i+1}", info['latin'], info['hausa'], info['zarma'], sub_label=h_meaning), unsafe_allow_html=True)

    # DISPLAY 3: COURT
    st.header(T["court"])
    c_cols = st.columns([1, 1, 2])
    with c_cols[0]:
        info_rw = GEOMANTIC_DATA[tuple(RW)]
        st.markdown(render_card(RW, "RW", info_rw['latin'], info_rw['hausa'], info_rw['zarma']), unsafe_allow_html=True)
    with c_cols[1]:
        info_lw = GEOMANTIC_DATA[tuple(LW)]
        st.markdown(render_card(LW, "LW", info_lw['latin'], info_lw['hausa'], info_lw['zarma']), unsafe_allow_html=True)
    with c_cols[2]:
        info_j = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(render_card(Judge, "JUDGE", info_j['latin'], info_j['hausa'], info_j['zarma'], highlight=True), unsafe_allow_html=True)
        st.markdown(f"""<div style='background:#fff; border-left:8px solid {MAROON}; padding:20px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.08);'>
                        <p style='margin:0; font-weight:900; color:{MAROON}; font-size:1.3rem;'>{info_j['meaning'][L]}</p>
                        <p style='font-size:1.2rem; color:{DARK_BLUE}; margin-top:10px;'>🏺 <b>{info_j['recommendation'][L]}</b></p></div>""", unsafe_allow_html=True)

    # DISPLAY 4: RECONCILER
    st.header(T["reconciler"])
    rec_cols = st.columns([1, 3])
    info_rec = GEOMANTIC_DATA[tuple(Reconciler)]
    with rec_cols[0]:
        st.markdown(render_card(Reconciler, "RECONCILER", info_rec['latin'], info_rec['hausa'], info_rec['zarma'], highlight=True), unsafe_allow_html=True)
    with rec_cols[1]:
        st.markdown(f"""<div style='background:white; border-left:14px solid {MAROON}; padding:35px; border-radius:20px; box-shadow:0 15px 45px rgba(0,0,0,0.12);'>
                        <h2 style='margin:0; color:{MAROON}; border:none; font-size:2.2rem; font-weight:900;'>{info_rec['hausa']} / {info_rec['zarma']}</h2>
                        <p style='font-size:0.9rem; color:#888; text-transform:uppercase; letter-spacing:2px;'>{info_rec['latin']}</p>
                        <p style='font-size:1.5rem; font-weight:800; color:#1a1a1a; margin:15px 0; line-height:1.4;'>{info_rec['rec_insight'][L]}</p>
                        <hr style='border:1px solid #eee; margin:20px 0;'>
                        <div style='background:#fdf2f2; padding:25px; border:2px dashed {MAROON}; border-radius:15px;'>
                            <strong style='color:{MAROON}; font-size:1.2rem; display:block; margin-bottom:8px;'>🔥 {T['rec_title']}:</strong>
                            <span style='font-size:1.5rem; color:{DARK_BLUE}; line-height:1.5;'><b>"{info_rec['recommendation'][L]}"</b></span>
                        </div>
                        </div>""", unsafe_allow_html=True)
