# 🧬 ProspectAI: AI-Driven Lead Scoring & Data Pipeline

**ProspectAI** is a modular data engineering pipeline designed to identify, enrich, and rank high-probability B2B leads for 3D in-vitro liver models. This project demonstrates an automated ETL workflow that bridges professional networking data with scientific research intent.

---

## 🏗️ Technical Architecture

The system is architected as a decoupled pipeline to ensure scalability and maintainability, separating the UI layer from the core algorithmic logic.

1.  **Data Ingestion:** Aggregates fragmented CSV datasets from LinkedIn (Market Metadata) and PubMed (Scientific Intent).
2.  **Normalization Engine:** Utilizes Regular Expressions (RegEx) to standardize lead names (stripping titles like Dr./PhD) for high-integrity relational joins.
3.  **Heuristic Model:** A weighted scoring engine translates categorical and temporal features into a numerical "Propensity to Buy" score.
4.  **Dashboarding:** An interactive Streamlit application for real-time lead exploration and data export.

---

## 📊 The Scoring Engine (Heuristic Model)

The agent calculates a **Propensity Score ($S$)** using a weighted matrix. In a production environment, these weights ($w$) serve as the baseline for future supervised learning optimization.

$$S = \sum (Feature \times Weight)$$

| Feature Set | Weight (w) | Logic / Criteria |
| :--- | :--- | :--- |
| **Role Alignment** | 30 | Keyword matching for Toxicology, Safety, and Preclinical titles. |
| **Capital Availability** | 20 | Detection of Series A/B/E funding or Strategic Partnerships. |
| **Geospatial Hub** | 10 | Proximity to Biotech clusters (Boston, Basel, SF, etc.). |
| **Scientific Intent** | 40 | Analysis of publications ($\geq 2023$) regarding DILI or Organ-Chips. |


---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Data Analysis:** `pandas` (Vectorized operations and Dataframe merging)
* **String Manipulation:** `re` (RegEx) for advanced data cleaning.
* **Deployment:** Streamlit Community Cloud.

## 📂 Project Structure

```text
├── app.py              # Streamlit UI & Dashboard Logic
├── scoring.py          # ETL Pipeline & Heuristic Model
├── requirements.txt    # Dependency Manifest
├── linkedin_data.csv   # Professional Dataset
└── pubmed_data.csv     # Scientific Dataset
```

---

## ⚙️ Execution Guide

**Local Setup**

1.**Clone the repository:** 
  bash
  ```
  git clone [https://github.com/your-username/prospect-ai.git](https://github.com/your-username/prospect-ai.git)
  cd prospect-ai
  ```

2. **Install dependencies:**
   bash
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   bash
   ```
   streamlit run app.py
   ```

---

 ## 🗺️ Roadmap: AI & ML Integration Phase

The following milestones outline the transition from a heuristic-based engine to a production-grade ML pipeline.

### Phase 1: Semantic Enrichment (NLP) 
- [ ] **Embedding Generation:** Replace keyword matching with `Sentence-BERT` (SBERT) to vectorize publication abstracts.
- [ ] **Cosine Similarity:** Rank leads by calculating the distance between their research vectors and our product's "Solution Vector."

### Phase 2: Automated Pipeline (Data Engineering)
- [ ] **API Orchestration:** Implement `FastAPI` to trigger scrapers for real-time lead enrichment.
- [ ] **Validation Layer:** Integrate `Pydantic` models to ensure data schema integrity across the ETL process.

### Phase 3: Predictive Modeling (Machine Learning)
- [ ] **Feature Store:** Catalog historical lead data to build training sets.
- [ ] **Model Selection:** Train an `XGBoost` Classifier to predict lead conversion probability.

---

### 🧪 Technical Preview: Future Semantic Scoring Logic
Below is the conceptual Python implementation for the **Phase 1** NLP upgrade:

```python
from sentence_transformers import SentenceTransformer, util

def calculate_semantic_relevance(publication_abstract, product_solution_text):
    """
    Proposed ML Upgrade: Replaces keyword counting with semantic similarity.
    Uses a pre-trained Transformer model (e.g., 'all-MiniLM-L6-v2').
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Encode the research and the product capability into vector space
    pub_vec = model.encode(publication_abstract, convert_to_tensor=True)
    sol_vec = model.encode(product_solution_text, convert_to_tensor=True)
    
    # Calculate Cosine Similarity (Result: 0.0 to 1.0)
    relevance_score = util.pytorch_cos_sim(pub_vec, sol_vec)
    
    return float(relevance_score) * 100
```

---

### Why this helps your application:
* **Demonstrates Vision:** It shows Akash that you aren't just a "task-doer," but someone who understands how to scale a project into a real AI product.
* **Technical Vocabulary:** Using terms like "Cosine Similarity," "Embedding Generation," and "Vector Space" signals that you have the theoretical knowledge required for an AI/ML role.
* **Code Proficiency:** Providing the pseudo-code for the SBERT implementation proves you know which libraries (`sentence-transformers`) are standard in the industry.

**Next Step:** Since your code is now complete, would you like me to help you write a **Professional Summary** for your Resume that highlights this project?

---
## Contact
Prachi Shende
Email: prachishende182@gmail.com
