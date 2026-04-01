import streamlit as st
import pandas as pd

st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC;
    }
    .stDataFrame {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Load data
df = pd.read_csv("products.csv")

# Title
st.markdown("""
# Olympus Product Explorer
### Product discovery and filtering interface (Prototype)

---
""")

# Filters
family = st.selectbox("Product Family", ["All"] + list(df["product_family"].unique()))
clinical = st.selectbox("Clinical Area", ["All"] + list(df["clinical_area"].unique()))
search = st.text_input("Search")

# Filtering logic
filtered = df.copy()

if family != "All":
    filtered = filtered[filtered["product_family"] == family]

if clinical != "All":
    filtered = filtered[filtered["clinical_area"] == clinical]

if search:
    filtered = filtered[
        filtered["product_name"].str.contains(search, case=False) |
        filtered["description"].str.contains(search, case=False)
    ]

# Display
st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)
st.markdown("### Selected Product")

if not filtered.empty:
    selected_product = st.selectbox(
        "Choose a product",
        filtered["product_name"]
    )

    product = filtered[filtered["product_name"] == selected_product].iloc[0]

    st.markdown(f"""
    **Product Name:** {product['product_name']}  
    **Family:** {product['product_family']}  
    **Clinical Area:** {product['clinical_area']}  
    **Type:** {product['product_type']}  

    **Description:**  
    {product['description']}
    """)