import pandas as pd
import re

def normalize_name(name):
    """Removes titles like Dr., PhD and extra spaces for better merging."""
    if pd.isna(name): return ""
    name = str(name).lower()
    name = re.sub(r'^(dr\.|dr|phd|prof\.|prof)\s+', '', name)
    return name.strip()

def calculate_propensity_score(row):
    """
    Weighted scoring engine based on ProspectAI requirements.
    Max Score: 100
    """
    score = 0
    
    # 1. Role Fit (+30)
    title = str(row.get('Title', '')).lower()
    if any(word in title for word in ['toxicology', 'safety', 'hepatic', '3d', 'preclinical']):
        score += 30
        
    # 2. Company Intent / The Budget (+20)
    # Checks 'Funding Status' based on your new CSV header
    funding = str(row.get('Funding Status', '')).lower()
    if any(f in funding for f in ['series a', 'series b', 'series e', 'partnered']):
        score += 20
        
    # 3. Location Hubs (+10)
    hq = str(row.get('HQ', '')).lower()
    hubs = ['boston', 'cambridge', 'bay area', 'san francisco', 'basel', 'london']
    if any(hub in hq for hub in hubs):
        score += 10
        
    # 4. Scientific Relevance (+40)
    pub_title = str(row.get('Publication_Title', '')).lower()
    pub_year = row.get('Publication_Year')
    
    # Keywords: Liver, Toxicity, DILI, 3D, Organoid
    keywords = ['liver', 'dili', 'toxicity', '3d', 'organoid', 'organ-chip']
    is_relevant = any(k in pub_title for k in keywords)
    is_recent = pd.notnull(pub_year) and pub_year >= 2023
    
    if is_relevant and is_recent:
        score += 40
        
    return min(score, 100)

def load_and_process_results(li_path, pub_path):
    """Merges and ranks the leads."""
    # Read with bad line handling to prevent ParserError
    df_li = pd.read_csv(li_path, on_bad_lines='skip')
    df_pub = pd.read_csv(pub_path, on_bad_lines='skip')

    # Create a normalized name column for merging
    df_li['name_clean'] = df_li['Name'].apply(normalize_name)
    df_pub['name_clean'] = df_pub['Name'].apply(normalize_name)

    # Merge on clean names
    df = pd.merge(df_li, df_pub.drop(columns=['Name']), on="name_clean", how="left")

    # Calculate Score
    df['Probability_Score'] = df.apply(calculate_propensity_score, axis=1)
    
    return df.sort_values(by='Probability_Score', ascending=False)