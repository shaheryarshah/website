import streamlit as st
import pandas as pd

# Sample data to mimic product listing (mock data)
data = {
    'product_id': [1, 2, 3, 4],
    'name': ['Smartphone', 'Laptop', 'Headphones', 'Camera'],
    'category': ['Electronics', 'Electronics', 'Audio', 'Electronics'],
    'price': [300, 800, 50, 450],
    'description': [
        'A high-quality smartphone with the latest features.',
        'A powerful laptop for all your computing needs.',
        'Noise-cancelling headphones for immersive sound.',
        'Capture your best moments with this high-resolution camera.'
    ]
}

# Convert the data into a DataFrame
products_df = pd.DataFrame(data)

# Streamlit app layout
st.title("E-commerce Platform Demo")
st.sidebar.header("Filter Products")

# Search bar
search_query = st.sidebar.text_input("Search products")

# Category filter
category_filter = st.sidebar.multiselect("Category", options=products_df['category'].unique(), default=products_df['category'].unique())

# Price range filter
price_min, price_max = st.sidebar.slider("Price Range", int(products_df['price'].min()), int(products_df['price'].max()), (int(products_df['price'].min()), int(products_df['price'].max())))

# Filter products based on user input
filtered_products = products_df[
    (products_df['name'].str.contains(search_query, case=False)) &
    (products_df['category'].isin(category_filter)) &
    (products_df['price'].between(price_min, price_max))
]

# Display filtered products
for _, row in filtered_products.iterrows():
    st.subheader(row['name'])
    st.write(f"Category: {row['category']}")
    st.write(f"Price: ${row['price']}")
    st.write(row['description'])
    st.markdown("---")

# Run with pyngrok if on Colab
if "google.colab" in str(get_ipython()):
    from pyngrok import ngrok
    public_url = ngrok.connect(port='8501')
    print(f'Streamlit app is live at {public_url}')
else:
    print("Run this on Streamlit using 'streamlit run <filename>.py'")
