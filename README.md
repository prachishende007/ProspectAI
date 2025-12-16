# ProspectAI – Lead Intelligence & Ranking Demo

ProspectAI is a **demo lead-intelligence pipeline** built as part of an internship screening assignment.  
It simulates how a business development team can **identify, enrich, and prioritize high-intent biotech decision-makers** using scientific, role-based, and business signals.

The project focuses on **clarity of thought, explainable logic, and end-to-end execution**, rather than production-scale scraping.

---

## 🚀 Problem Statement

Biotech BD teams often struggle with:
- Large volumes of unqualified leads
- Lack of scientific context behind prospects
- No clear way to prioritize who to contact first

ProspectAI addresses this by building a **lightweight web agent** that:
1. Identifies relevant professionals
2. Enriches them with contextual signals
3. Ranks them using a transparent *Propensity to Buy* score

---

## 🧠 What This Demo Does

The pipeline follows three stages:

### 1️⃣ Identification
- Simulates discovery of relevant profiles (e.g., Directors of Toxicology, Safety Assessment Leads)
- Uses **real scientific publication data** from PubMed
- Merges with mock LinkedIn-style professional data

### 2️⃣ Enrichment
For each identified profile, the system adds:
- Business email (pattern-based)
- Personal location vs company HQ
- Company funding stage (mocked)
- Research recency and scientific focus
- Biotech hub indicator (Boston, Bay Area, UK, Basel)

### 3️⃣ Ranking (Probability Engine)
Each lead is scored (0–100) based on weighted signals:
- Role seniority
- Recent funding activity
- Scientific intent (recent publications)
- Location relevance

The result is a **ranked list of leads**, ordered by likelihood to engage.

---

## 📊 Final Output

An interactive **Streamlit dashboard** that provides:
- Ranked leads table
- Search and filter functionality
- Clear probability scores
- CSV export for downstream use

**Sample Columns:**
Rank | Probability | Name | Title | Company | Location | HQ | Email | LinkedIn

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-----|-----------|--------|
| Language | Python | Core logic |
| Data Handling | Pandas | Data processing |
| APIs | PubMed Entrez | Scientific signals |
| Scoring | Rule-based engine | Explainable ranking |
| UI | Streamlit | Interactive dashboard |
| Storage | CSV | Lightweight persistence |

---

## 📁 Project Structure

prospectai/
│
├── data/
│   ├── raw/
│   │   ├── pubmed_data.csv
│   │   └── linkedin_mock.csv
│   ├── processed/
│   │   ├── identified_leads.csv
│   │   ├── enriched_leads.csv
│   │   └── ranked_leads.csv
│
├── src/
│   ├── identification.py
│   ├── enrichment.py
│   ├── scoring.py
│   └── utils.py
│
├── app.py          # Streamlit dashboard
├── requirements.txt
└── README.md

---

## ⚙️ How the Scoring Works

The probability score is computed using simple, transparent rules:

- Senior role (Director / Head): **+30**
- Company funded (Series A/B): **+20**
- Recent relevant publication: **+40**
- Biotech hub location: **+10**

Scores are normalized to a **0–100 scale** to allow easy comparison.

> The emphasis is on **interpretability**, not black-box ML.

---

## ▶️ How to Run the Demo

1. Clone the repository
```bash
git clone https://github.com/your-username/prospectai.git
cd prospectai
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the dashboard
```bash
streamlit run app.py
```
## 📌 Notes & Assumptions

- LinkedIn data is **mocked** to avoid scraping restrictions  
- Funding and email enrichment are simulated  
- The system is designed for **demo and evaluation purposes**, not production deployment  

---

## 🔮 Future Improvements

- Replace mock data with APIs (Proxycurl, Crunchbase)  
- Add NLP-based paper relevance scoring  
- Introduce ML-based propensity modeling  
- Add user-defined weighting controls  

---

## 👤 Author

**Prachi Shende**  
PreFinal Year B.Tech Student
Email: prachishende182@gmail.com
