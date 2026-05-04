import streamlit as st
import pandas as pd
import os

BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOOD_PATH  = os.path.join(BASE_DIR, 'data', 'food_dataset.csv')

@st.cache_data
def load_food():
    df = pd.read_csv(FOOD_PATH)
    df.columns   = df.columns.str.strip()
    df['Disease']  = df['Disease'].str.strip().str.lower()
    df['Nutrient'] = df['Nutrient'].str.strip().str.lower()
    df['Veg_Non']  = df['Veg_Non'].str.strip().str.lower()
    df['Name']     = df['Name'].str.strip().str.title()
    df['catagory'] = df['catagory'].str.strip().str.title()
    df['Price']    = pd.to_numeric(df['Price'], errors='coerce').fillna(0).astype(int)
    return df

def show():
    st.markdown('<div class="page-title">🥗 Food Recommendations</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Discover foods recommended for diabetes management, filtered by your preferences.</div>', unsafe_allow_html=True)

    df = load_food()

    # ── Filters ──────────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3, gap="medium")

    nutrients = sorted(df['Nutrient'].dropna().unique().tolist())
    with col1:
        nutrient = st.selectbox("🧬 Focus Nutrient", ["All"] + nutrients,
                                help="Filter by the key nutrient you want more of")
    with col2:
        food_type = st.selectbox("🌿 Food Type", ["Both", "Veg", "Non-Veg"])
    with col3:
        sort_by = st.selectbox("📊 Sort By", ["Name (A-Z)", "Price (Low-High)", "Price (High-Low)"])

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Filter: diabetes foods only ──────────────────────────────────────────
    filtered = df[df['Disease'].str.contains('diabeties', case=False, na=False)].copy()

    # Nutrient filter (skip if "All")
    if nutrient != "All":
        filtered = filtered[filtered['Nutrient'].str.contains(nutrient, case=False, na=False)]

    # Veg filter
    if food_type == "Veg":
        filtered = filtered[filtered['Veg_Non'] == 'veg']
    elif food_type == "Non-Veg":
        filtered = filtered[filtered['Veg_Non'] == 'non-veg']

    # Sort
    if sort_by == "Name (A-Z)":
        filtered = filtered.sort_values('Name')
    elif sort_by == "Price (Low-High)":
        filtered = filtered.sort_values('Price')
    else:
        filtered = filtered.sort_values('Price', ascending=False)

    filtered = filtered.reset_index(drop=True)

    # ── Stats row ─────────────────────────────────────────────────────────────
    c1, c2, c3 = st.columns(3)
    c1.metric("Results Found",    len(filtered))
    c2.metric("Veg Options",      len(filtered[filtered['Veg_Non'] == 'veg']))
    c3.metric("Non-Veg Options",  len(filtered[filtered['Veg_Non'] == 'non-veg']))

    st.markdown("---")

    if filtered.empty:
        st.warning("No foods found for the selected filters. Try selecting **All** nutrients or a different food type.")
        return

    # ── Food cards ────────────────────────────────────────────────────────────
    for _, row in filtered.iterrows():
        veg   = row['Veg_Non'] == 'veg'
        badge = "<span class='badge-veg'>🌿 Veg</span>" if veg else "<span class='badge-nonveg'>🍖 Non-Veg</span>"
        price = f"₹{row['Price']}" if row['Price'] > 0 else "—"
        st.markdown(f"""
        <div class='food-card'>
            <div style='display:flex; justify-content:space-between; align-items:flex-start;'>
                <div>
                    <div class='food-name'>{row['Name']}</div>
                    <div class='food-meta'>
                        Category: {row['catagory']} &nbsp;|&nbsp;
                        Nutrient: <b>{row['Nutrient'].title()}</b>
                    </div>
                </div>
                <div style='text-align:right;'>
                    {badge}<br>
                    <span style='font-weight:700; color:#1e293b; font-size:1rem;'>{price}</span>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>")
    st.caption("💡 Tip: These recommendations are curated for diabetes management. Consult a dietitian for a personalised meal plan.")
