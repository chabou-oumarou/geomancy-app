import streamlit as st

# --- Data: The 16 Classical Figures & Meanings ---
GEOMANTIC_DATA = {
    (1, 1, 1, 1): {"name": "Via", "meaning": "Change and movement. Success through moving forward and simplicity."},
    (2, 2, 2, 2): {"name": "Populus", "meaning": "The Crowd. Neutrality, following the flow, or stability in numbers."},
    (2, 1, 1, 2): {"name": "Conjunctio", "meaning": "The Junction. Coming together, contracts, and social interactions."},
    (1, 2, 2, 1): {"name": "Carcer", "meaning": "The Prison. Delays, boundaries, and restriction. Good for secrets."},
    (2, 2, 1, 1): {"name": "Fortuna Major", "meaning": "Greater Fortune. Massive success, inner strength, and protection."},
    (1, 1, 2, 2): {"name": "Fortuna Minor", "meaning": "Lesser Fortune. Quick, external success; speed over depth."},
    (2, 1, 2, 1): {"name": "Acquisitio", "meaning": "Gain. Financial profit, spiritual growth, and taking things in."},
    (1, 2, 1, 2): {"name": "Amissio", "meaning": "Loss. Spending, letting go, or losing something for a greater cause."},
    (1, 2, 2, 2): {"name": "Laetitia", "meaning": "Joy. Health, happiness, and positive news coming from high places."},
    (2, 2, 2, 1): {"name": "Tristitia", "meaning": "Sorrow. Heavy energy, foundations, and staying low. Good for building."},
    (1, 2, 1, 1): {"name": "Puella", "meaning": "The Girl. Beauty, harmony, and pleasant social interactions."},
    (1, 1, 2, 1): {"name": "Puer", "meaning": "The Boy. Energy, aggression, and impulsive action. Be bold."},
    (2, 2, 1, 2): {"name": "Albus", "meaning": "White. Peace, wisdom, and clear communication. Highly favorable."},
    (2, 1, 2, 2): {"name": "Rubeus", "meaning": "Red. Passion, anger, and vice. A warning to pause and reflect."},
    (2, 1, 1, 1): {"name": "Caput Draconis", "meaning": "Dragon's Head. New beginnings, entry points, and profit."},
    (1, 1, 1, 2): {"name": "Cauda Draconis", "meaning": "Dragon's Tail. Endings, exit points, and karmic completion."}
}

def add_figs(f1, f2):
    return [2 if (r1 + r2) % 2 == 0 else 1 for r1, r2 in zip(f1, f2)]

def render_fig(fig_list):
    visual = ""
    for r in fig_list:
        visual += "  ●  \n" if r == 1 else "●   ●\n"
    return visual

def process_input(input_str):
    """Counts non-space characters and returns 1 (odd) or 2 (even)."""
    clean_str = input_str.replace(" ", "")
    if not clean_str: return None
    return 1 if len(clean_str) % 2 != 0 else 2

# --- App UI ---
st.set_page_config(page_title="Geomancy Oracle", layout="wide")
st.title("🔮 The Complete Geomantic Oracle")
st.write("Type random dots or marks in the fields below to cast your figures.")

# Input Layout for 4 Mothers (16 rows total)
mothers_input = []
cols = st.columns(4)

for i in range(4):
    with cols[i]:
        st.subheader(f"Mother {i+1}")
        r1 = st.text_input(f"M{i+1} Row 1", key=f"m{i}r1", placeholder="....")
        r2 = st.text_input(f"M{i+1} Row 2", key=f"m{i}r2", placeholder="..")
        r3 = st.text_input(f"M{i+1} Row 3", key=f"m{i}r3", placeholder="...")
        r4 = st.text_input(f"M{i+1} Row 4", key=f"m{i}r4", placeholder=".")
        mothers_input.append([r1, r2, r3, r4])

if st.button("Calculate The Shield", type="primary"):
    # 1. Process Mothers
    M = []
    error = False
    for m_idx, m_rows in enumerate(mothers_input):
        processed_m = [process_input(r) for r in m_rows]
        if None in processed_m:
            st.error(f"Mother {m_idx+1} is incomplete. Please add dots to all rows.")
            error = True
            break
        M.append(processed_m)
    
    if not error:
        # 2. Derive Daughters
        D = [[M[j][i] for j in range(4)] for i in range(4)]
        # 3. Calculate Nephews
        N = [add_figs(M[0], M[1]), add_figs(M[2], M[3]), add_figs(D[0], D[1]), add_figs(D[2], D[3])]
        # 4. The Court
        RW = add_figs(N[0], N[1])
        LW = add_figs(N[2], N[3])
        Judge = add_figs(RW, LW)
        # 5. Reconciler
        Reconciler = add_figs(Judge, M[0])

        # --- Display Results ---
        st.divider()
        st.header("The Shield Analysis")
        
        # Row for Judge and Reconciler
        res_c1, res_c2 = st.columns(2)
        with res_c1:
            st.subheader("⚖️ The Judge")
            st.text(render_fig(Judge))
            j_data = GEOMANTIC_DATA[tuple(Judge)]
            st.success(f"**{j_data['name']}**: {j_data['meaning']}")
        
        with res_c2:
            st.subheader("🔄 The Reconciler")
            st.text(render_fig(Reconciler))
            r_data = GEOMANTIC_DATA[tuple(Reconciler)]
            st.info(f"**{r_data['name']}**: {r_data['meaning']}")

        # Foundation Expanders
        with st.expander("View Full Foundation (Mothers & Daughters)"):
            f_cols = st.columns(8)
            all_f = M + D
            for i, fig in enumerate(all_f):
                label = f"M{i+1}" if i < 4 else f"D{i-3}"
                f_cols[i].markdown(f"**{label}**")
                f_cols[i].text(render_fig(fig))
