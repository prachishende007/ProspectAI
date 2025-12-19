import streamlit as st
import os
import pandas as pd
from scoring import load_and_process_results

st.set_page_config(page_title="ProspectAI", layout="wide")

st.title("ProspectAI: Lead Generation Agent")
st.markdown("### Ranking results for 3D In-Vitro Model Prospects")

# File Paths
LI_FILE = "Data/linkedin.csv"
PUB_FILE = "Data/pubmed_data.csv"

if os.path.exists(LI_FILE) and os.path.exists(PUB_FILE):
    # Process Data
    df = load_and_process_results(LI_FILE, PUB_FILE)

    # Filter/Search Bar
    search = st.text_input("🔍 Search by HQ, Company, or Keyword (e.g., 'Boston' or 'Safety')")
    if search:
        df = df[df.apply(lambda r: search.lower() in str(r).lower(), axis=1)]

    # Display Leads
    st.subheader(f"Found {len(df)} Qualified Leads")
    
    st.dataframe(
        df[['Probability_Score', 'Name', 'Title', 'Company', 'HQ', 'Funding Status', 'LinkedIn_URL']],
        column_config={
            "Probability_Score": st.column_config.ProgressColumn(
                "Propensity to Buy", format="%d%%", min_value=0, max_value=100
            ),
            "LinkedIn_URL": st.column_config.LinkColumn("LinkedIn")
        },
        hide_index=True,
        use_container_width=True
    )

    # Export
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Ranked Leads", csv, "ranked_leads.csv", "text/csv")
else:
    st.error("Data files missing. Please ensure 'linkedin_data.csv' and 'Data/pubmed_data.csv' are uploaded.")