import streamlit as st
import random

# --- Data: The 16 Classical Figures & Meanings ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {"name": "Via", "meaning": "Change and movement. Success through moving forward and simplicity."},
    (2, 2, 2, 2): {"name": "Populus", "meaning": "The Crowd. Neutrality, following the flow, or stability in numbers."},
    (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "The Junction. Coming together, contracts, and social interactions."},
    (1, 2, 2, 1): {"name": "Carcer", "meaning": "The Prison. Delays, boundaries, and restriction. Good for secrets and stability."},
    (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Greater Fortune. Massive success, inner strength, and protection."},
    (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Lesser Fortune. Quick, external success; speed over depth."},
    (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Financial profit, spiritual growth, and taking things in."},
    (1, 2, 1, 2): {"name": "Amissio", "meaning": "Loss. Spending, letting go, or losing something for a greater cause."},
    (1, 2, 2, 2): {"name": "Laetitia", "meaning": "Joy. Health, happiness, and positive news coming from high places."},
    (2, 2, 2, 1): {"name": "Tristitia", "meaning": "Sorrow. Heavy energy, foundations, and staying low. Good for long-term structures."},
    (1, 2, 1, 1): {"name": "Puella", "meaning": "The Girl. Beauty, harmony, and pleasant social interactions."},
    (1, 1, 2, 1): {"name": "Puer", "meaning": "The Boy. Energy, aggression, and impulsive action. A call to be bold."},
    (2, 2, 1, 2): {"name": "Albus", "meaning": "White. Peace, wisdom, and clear communication. Highly favorable omen."},
    (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Red. Passion, anger, and vice. A warning to pause and reflect carefully."},
    (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Dragon's Head. New beginnings, entry points, and profit."},
    (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Dragon's Tail. Endings, exit points, and karmic completion."}
}

def generate_mother():
    """Simulates generating 4 rows of random dots and reducing to parity."""
    return [1 if random.randint(5, 20) % 2 != 0 else 2 for _ in range(4)]

def add_figs(f1, f2):
    """Adds two figures based on geomantic parity rules."""
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_fig(fig_list):
    """Formats the numerical list into a visual dot-dash string."""
    visual = ""
    for r in fig_list:
        visual += "  ●  \n" if r == 1 else "●   ●\n"
    return visual

# --- App UI Configuration ---
st.set_page_config(page_title="Classical Geomancy Oracle", layout="wide")

st.title("🔮 Classical Geomancy Oracle")
st.markdown("""
This app simulates the traditional **Science of the Sands**. By generating four rows of random dots, 
the oracle calculates the Four Mothers and derives the entire Geomantic Shield.
""")

if st.button("Cast the Shield", type="primary"):
    # 1. Mothers (M1 - M4)
    M = [generate_mother() for _ in range(4)]
    # 2. Daughters (D1 - D4) via Transposition
    D = [[M[j][i] for j in range(4)] for i in range(4)]
    # 3. Nephews (N1 - N4) via Addition
    N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
    # 4. The Court (Witnesses and Judge)
    RW = add_figs(N[0], N[1])
    LW = add_figs(N[2], N[3])
    Judge = add_figs(RW, LW)
    # 5. The Reconciler
    Reconciler = add_figs(Judge, M[0])

    # --- SECTION: Foundation ---
    st.header("1. The Foundation (Mothers & Daughters)")
    all_foundation = M + D
    cols = st.columns(8)
    for i, fig in enumerate(all_foundation):
        label = f"M{i+1}" if i < 4 else f"D{i-3}"
        with cols[i]:
            st.markdown(f"**{label}**")
            st.text(render_fig(fig))
            st.caption(GEOMANTIC_DATA[tuple(fig)]['name'])

    st.divider()

    # --- SECTION: Nephews ---
    st.header("2. The Results (Nephews)")
    n_cols = st.columns(4)
    for i in range(4):
        n_cols[i].markdown(f"**N{i+1}: {GEOMANTIC_DATA[tuple(N[i])]['name']}**")
        n_cols[i].text(render_fig(N[i]))

    st.divider()

    # --- SECTION: The Court ---
    st.header("3. ⚖️ The Court")
    c1, c2, c3 = st.columns([1, 1, 2])
    
    with c1:
        st.subheader("Right Witness")
        data = GEOMANTIC_DATA[tuple(RW)]
        st.markdown(f"**{data['name']}**")
        st.text(render_fig(RW))
        st.write(data['meaning'])

    with c2:
        st.subheader("Left Witness")
        data = GEOMANTIC_DATA[tuple(LW)]
        st.markdown(f"**{data['name']}**")
        st.text(render_fig(LW))
        st.write(data['meaning'])

    with c3:
        st.subheader("The Judge")
        j_data = GEOMANTIC_DATA[tuple(Judge)]
        st.markdown(f"### {j_data['name']}")
        st.text(render_fig(Judge))
        st.success(f"**Verdict:** {j_data['meaning']}")

    st.divider()

    # --- SECTION: The Reconciler ---
    st.header("4. 🔄 The Reconciler")
    r_data = GEOMANTIC_DATA[tuple(Reconciler)]
    r_col1, r_col2 = st.columns([1, 4])
    with r_col1:
        st.text(render_fig(Reconciler))
    with r_col2:
        st.markdown(f"**Final Insight:** {r_data['name']}")
        st.info(r_data['meaning'])