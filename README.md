# Data Vortex 2026 — Social Engine

Data cleaning, exploratory analysis, SQL investigation, NLP-based semantic analysis, and cybersecurity incident analysis for the **Data Vortex 2026 Social Engine recovery challenge**.

## Project overview

The project reconstructs the Social Engine across three stages:

- Structured data cleaning and EDA
- SQL-based analytical investigation
- NLP semantic understanding
- Real-world cybersecurity incident analysis

## Project status

**Round 1 — Phase 1: Data Cleaning & EDA: Completed** ✅  
**Round 1 — Phase 2: SQL Analysis & Insight Report: Completed** ✅  
**Round 2: NLP Semantic Understanding: Completed** ✅  
**Round 3: Cybersecurity Incident Analysis: Completed** ✅

---

# Round 1 — Data Cleaning & EDA

The project uses:

- `Social_Engine_Posts_Corrupted.csv`
- `Social_Engine_Users.csv`

The cleaned dataset contains **12,000 posts from 1,500 users**.

The cleaning workflow included:

1. Raw-data auditing
2. Duplicate detection
3. Missing-value investigation
4. Timestamp standardisation
5. Invalid-value correction
6. Text and HTML cleaning
7. User-level validation
8. Final quality checks

EDA covered platform distribution, engagement, correlations, temporal activity, user activity, and outliers.

### Key findings

- Platform post volumes were relatively balanced.
- Likes, shares, and comments showed very low linear correlation.
- No single platform consistently led across all engagement metrics.
- Monthly activity remained relatively stable.
- All 1,500 users had corresponding posts.
- No IQR-based engagement outliers were identified.

---

# Round 1 — Phase 2: SQL Analysis

The cleaned data was structured into PostgreSQL `users` and `posts` tables and analysed using joins, aggregations, CTEs, filters, and window functions.

### E2 — Most Engaged Posts

Total engagement was defined as:

`Likes + Shares + Comments`

The top 10 posts had engagement between **7,610 and 7,893**, with the highest reaching **7,893**.

### M4 — High-Follower Platform Behaviour

For users with at least 30,000 followers, **Instagram** recorded the highest average engagement per post at **4,144.59**.

### H4 — Follower-to-Engagement Analysis

**17 users** had fewer than 5,000 followers while falling within the top 10% of users by total engagement. The highest-engagement account in this group had **2,211 followers and 58,480 total engagement**.

These results identify unusual engagement patterns but do not independently establish suspicious activity.

---

# Round 2 — NLP Semantic Understanding

Round 2 rebuilt the Social Engine's semantic analysis layer using the provided **9,000-record labelled NLP dataset**.

### Tasks

**Sentiment**
- Negative
- Neutral
- Positive

**Topic**
- Account_Security
- Community_Discussion
- Feature_Feedback
- Technical_Issues

### NLP pipeline

- Text normalization
- URL and mention removal
- Hashtag normalization
- TF-IDF feature extraction
- Group-aware 75:25 train-test split
- Multiple model comparisons
- Confusion-matrix analysis
- Error analysis
- TF-IDF coefficient-based explainability

### Final models

| Task | Model | Accuracy | Macro F1 |
|---|---|---:|---:|
| Sentiment | TF-IDF + Logistic Regression | 0.5734 | 0.5730 |
| Topic | TF-IDF + Linear SVM | 0.9349 | 0.6706 |

The topic dataset was highly imbalanced, with `Community_Discussion` representing **86.13%** of the records.

Major errors included Neutral → Negative sentiment confusion and minority topic classes being frequently classified as `Community_Discussion`.

---

# Round 3 — Cybersecurity Incident Analysis

Round 3 extends the Social Engine to a self-collected real-world dataset focused on the **Boston Scientific cybersecurity incident**.

### Data collection

Sources:

- **X (Twitter)** — collected using XPorter
- **Google News** — collected using Google News RSS

The collection and preparation pipeline is:

`src/round3/round3_data_pipeline.py`

The pipeline collects, filters, standardises, combines, validates, and exports the Round 3 data.

### Dataset

Final Round 3 dataset:

- **190 records**
- **93 X posts**
- **97 Google News records**
- Time window: **26 August 2026 – 20 September 2026**

Required schema:

`text_id, source, post_text, timestamp, likes, comments, shares, sentiment_label, topic_category`

Google News engagement fields were retained as missing because the RSS source did not provide them.

### Sentiment analysis

| Sentiment | Records | Percentage |
|---|---:|---:|
| Negative | 61 | 32.11% |
| Neutral | 96 | 50.53% |
| Positive | 33 | 17.37% |

The two highest-volume dates were **26 August (44 records)** and **8 September (50 records)**. Model-classified Negative sentiment increased from **22.73% to 36.00%** between these periods.

### Activity analysis

| Date | X Posts | Likes | Comments | Shares | Total Engagement |
|---|---:|---:|---:|---:|---:|
| 2026-09-08 | 29 | 237 | 43 | 53 | 333 |
| 2026-08-26 | 22 | 143 | 40 | 84 | 267 |

The mean daily X engagement was **43.50**, with 8 September reaching approximately **7.66× the mean**.

### Topic and entity analysis

Major discussion themes included:

| Theme | Records | Percentage |
|---|---:|---:|
| Cyberattack & Cybersecurity | 189 | 99.47% |
| Operational Disruption | 90 | 47.37% |
| Financial Impact | 76 | 40.00% |
| Shipping & Medical Devices | 57 | 30.00% |
| Patient & Service Impact | 10 | 5.26% |

The discussion broadly progressed from:

`Cybersecurity incident → Operational disruption → Shipping/medical-device impact → Financial impact → Technical/service recovery`

### Limitations

- Round 3 contains 190 records, limiting detailed temporal analysis.
- Engagement metrics were available only for X.
- Sentiment predictions are based on a moderate-performing Round 2 model.
- Topic predictions were strongly influenced by the dominant `Community_Discussion` class.
- Temporal associations do not establish direct causation.

---

# Repository Structure

```text
data-vortex-social-engine/
│
├── README.md
├── data/
│   ├── raw/
│   │   ├── Social_Engine_Posts_Corrupted.csv
│   │   ├── Social_Engine_Users.csv
│   │   ├── Labeled_Social_NLP_Training_Data
│   │   └── round3/
│   │       ├── x_collection.csv
│   │       └── news_raw.csv
│   └── cleaned/
│       ├── Social_Engine_Posts_Cleaned.csv
│       └── round3/
│           ├── x_clean.csv
│           ├── round3_raw_combined.csv
│           ├── round3_dataset_for_eda.csv
│           └── Tekton_Round3_Final_Dataset.csv
│
├── notebooks/
│   ├── 01_posts_data_cleaning.ipynb
│   ├── 02_posts_eda.ipynb
│   ├── Tekton_Round2_Social_Engine_NLP_Analytics.ipynb
│   └── Tekton_Round3_Cybersecurity_Incident_Analysis.ipynb
│
├── src/
│   ├── cleaning/
│   │   └── posts_cleaning.py
│   └── round3/
│       └── round3_data_pipeline.py
│
├── sql/
│   ├── schema.sql
│   ├── E2/
│   ├── M4/
│   └── H4/
│
├── models/
│   └── Tekton_Round2_Final_NLP_Models.pkl
│
└── reports/
    ├── Social_Engine_Posts_EDA_Report.pdf
    ├── Phase_02_Insight_Report.pdf
    ├── Evaluation_Metrics_Report.pdf
    ├── Round_02_Technical_Report.pdf
    └── Round_03_Analytical_Report.pdf
