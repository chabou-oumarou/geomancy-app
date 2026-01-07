import streamlit as st

# -------------------------------------------------
# 1. DATA MAP (Figures, Elements, Meanings)
# -------------------------------------------------
GEOMANTIC_DATA = {
    (1,1,1,1): {"name":"Via","element":"Water","meaning":{"EN":"Change and movement. Success through moving forward.","FR":"Changement et mouvement. Succès en allant de l'avant."}},
    (2,2,2,2): {"name":"Populus","element":"Water","meaning":{"EN":"The Crowd. Stability, neutrality, and following the flow.","FR":"La Foule. Stabilité, neutralité et suivre le flux."}},
    (2,1,1,2): {"name":"Conjunctio","element":"Air","meaning":{"EN":"The Junction. Union, contracts, and social interactions.","FR":"La Jonction. Union, contrats et interactions sociales."}},
    (1,2,2,1): {"name":"Carcer","element":"Earth","meaning":{"EN":"The Prison. Delays, boundaries, and necessary restriction.","FR":"La Prison. Délais, limites et restrictions nécessaires."}},
    (2,2,1,1): {"name":"Fortuna Major","element":"Earth","meaning":{"EN":"Greater Fortune. Massive success and inner protection.","FR":"Grande Fortune. Succès massif et protection intérieure."}},
    (1,1,2,2): {"name":"Fortuna Minor","element":"Fire","meaning":{"EN":"Lesser Fortune. Quick success; speed over depth.","FR":"Petite Fortune. Succès rapide ; la vitesse prime sur la profondeur."}},
    (2,1,2,1): {"name":"Acquisitio","element":"Air","meaning":{"EN":"Gain. Financial profit and spiritual growth.","FR":"Gain. Profit financier et croissance spirituelle."}},
    (1,2,1,2): {"name":"Amissio","element":"Fire","meaning":{"EN":"Loss. Spending or letting go for a greater cause.","FR":"Perte. Dépense ou lâcher-prise pour une cause plus grande."}},
    (1,2,2,2): {"name":"Laetitia","element":"Air","meaning":{"EN":"Joy. Health, happiness, and positive news.","FR":"La Joie. Santé, bonheur et nouvelles positives."}},
    (2,2,2,1): {"name":"Tristitia","element":"Earth","meaning":{"EN":"Sorrow. Heavy energy, foundations, and building low.","FR":"La Tristesse. Énergie lourde, fondations et discrétion."}},
    (1,2,1,1): {"name":"Puella","element":"Water","meaning":{"EN":"The Girl. Beauty, harmony, and pleasant interactions.","FR":"La Jeune Fille. Beauté, harmonie et interactions plaisantes."}},
    (1,1,2,1): {"name":"Puer","element":"Fire","meaning":{"EN":"The Boy. Energy, aggression, and impulsive bold action.","FR":"Le Garçon. Énergie, agression et action audacieuse."}},
    (2,2,1,2): {"name":"Albus","element":"Air","meaning":{"EN":"White. Peace, wisdom, and clear communication.","FR":"Le Blanc. Paix, sagesse et communication claire."}},
    (2,1,2,2): {"name":"Rubeus","element":"Fire","meaning":{"EN":"Red. Passion and vice. A warning to pause.","FR":"Le Rouge. Passion et vice. Un avertissement de pause."}},
    (2,1,1,1): {"name":"Caput Draconis","element":"Earth","meaning":{"EN":"Dragon's Head. New beginnings and entry points.","FR":"Tête du Dragon. Nouveaux départs et points d'entrée."}},
    (1,1,1,2): {"name":"Cauda Draconis","element":"Fire","meaning":{"EN":"Dragon's Tail. Endings and karmic exit points.","FR":"Queue du Dragon. Fins et achèvement karmique."}}
}

# -------------------------------------------------
# UI TEXT
# -------------------------------------------------
UI_TEXT = {
    "EN": {"title":"Celestial Star Oracle","subtitle":"Ancient Wisdom in Golden Stars","btn":"Cast the Divine Shield",
           "mother_tab":"Mother","row":"Row","foundation":"I. The Foundation",
           "nephews":"II. The Nephews","court":"III. The Verdict",
           "witness_r":"Right Witness","witness_l":"Left Witness","judge":"The Judge",
           "reconciler":"The Reconciler","element":"Element","error":"Fill all fields."},
    "FR": {"title":"Oracle de l'Étoile Céleste","subtitle":"Sagesse Ancienne en Étoiles d'Or","btn":"Générer le Blason Divin",
           "mother_tab":"Mère","row":"Ligne","foundation":"I. La Fondation",
           "nephews":"II. Les Neveux","court":"III. Le Verdict",
           "witness_r":"Témoin Droit","witness_l":"Témoin Gauche","judge":"Le Juge",
           "reconciler":"Le Réconciliateur","element":"Élément","error":"Remplissez tous les champs."}
}

# -------------------------------------------------
# LOGIC
# -------------------------------------------------
def add_figs(f1, f2):
    return [2 if (a+b) % 2 == 0 else 1 for a,b in zip(f1,f2)]

def process_input(s):
    s = s.replace(" ", "")
    return (1 if len(s) % 2 else 2) if s else None

def render_card(fig, label, color="#D4AF37", size="44px", glow=False):
    glow_css = f"box-shadow:0 14px 50px {color}55;" if glow else "box-shadow:0 6px 22px rgba(0,0,0,.08);"
    rows = "".join(
        f"<div style='font-size:{size}; line-height:1.15; color:{color};'>"
        f"{'★' if r==1 else '★&nbsp;&nbsp;&nbsp;★'}</div>" for r in fig
    )
    return f"""
    <div style="background:#fff;border-radius:26px;padding:26px;
                border:1px solid #edf0f2;text-align:center;
                transition:transform .2s ease;{glow_css}">
        <div style="font-size:.7rem;font-weight:800;letter-spacing:2px;
                    color:#aaa;margin-bottom:14px;text-transform:uppercase;">
            {label}
        </div>
        {rows}
    </div>
    """

# -------------------------------------------------
# APP UI
# -------------------------------------------------
st.set_page_config(page_title="Star Oracle", layout="wide")

lang = st.sidebar.selectbox("Language / Langue", ["English", "Français"])
L = "EN" if lang == "English" else "FR"
T = UI_TEXT[L]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
html,body,[data-testid="stAppViewContainer"]{background:#f8fafc;font-family:'Outfit',sans-serif;}
h1{text-align:center;font-size:3.2rem!important;font-weight:800;}
h2,h3{text-align:center;color:#D4AF37!important;}
.stTextInput input{
    border-radius:18px;border:2px solid #edf0f2;
    text-align:center;font-weight:600;font-size:1.05rem;
}
.stTextInput input:focus{border-color:#D4AF37;}
.stButton>button{
    background:#D4AF37!important;color:#fff!important;
    border-radius:24px;height:62px;font-weight:800;border:none;
}
</style>
""", unsafe_allow_html=True)

st.title(T["title"])
st.markdown(f"<p style='text-align:center;color:#888;font-size:1.15rem;margin-top:-12px;'>{T['subtitle']}</p>", unsafe_allow_html=True)

# -------------------------------------------------
# INPUT
# -------------------------------------------------
mothers_input = []
tabs = st.tabs([f"{T['mother_tab']} {i+1}" for i in range(4)])

for i in range(4):
    with tabs[i]:
        cols = st.columns(4)
        mothers_input.append([
            cols[j].text_input(f"{T['row']} {j+1}", key=f"m{i}r{j}", placeholder="•••••")
            for j in range(4)
        ])

# -------------------------------------------------
# COMPUTE
# ------------------
