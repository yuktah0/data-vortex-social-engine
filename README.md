# Data Vortex 2026 — Social Engine

Data cleaning, data quality analysis, exploratory data analysis, SQL-based analytical investigation, and NLP-based semantic analysis for the **Data Vortex 2026 Social Engine recovery challenge**.

## Project Overview

The project focuses on recovering and analysing the Social Engine across multiple stages, from corrupted structured data to NLP-based semantic understanding.

The complete workflow includes:

- Raw data auditing
- Duplicate detection and handling
- Missing-value investigation
- Invalid-value correction
- Timestamp standardisation
- Text and HTML cleaning
- User-level validation
- Exploratory Data Analysis (EDA)
- Final data quality checks
- Relational database design
- Analytical SQL queries
- Behavioural and anomaly analysis
- Insight reporting
- NLP text preprocessing
- Sentiment classification
- Topic classification
- Model comparison and evaluation
- Error analysis and explainability

## Project Status

**Round 1 — Phase 1: Data Cleaning & EDA: Completed** ✅  
**Round 1 — Phase 2: SQL Analysis & Insight Report: Completed** ✅  
**Round 2: NLP Semantic Understanding: Completed** ✅

## Round 1 — Dataset

The project uses two raw datasets:

- `Social_Engine_Posts_Corrupted.csv`
- `Social_Engine_Users.csv`

The final processed dataset is:

- `Social_Engine_Posts_Cleaned.csv`

The cleaned Posts dataset contains **12,000 posts from 1,500 users**.

---

# Phase 1 — Data Cleaning & EDA

The Posts dataset was cleaned through the following stages:

1. Load raw data
2. Create raw-data audit
3. Handle exact duplicates
4. Standardise timestamps
5. Investigate missing values
6. Fix invalid numerical values
7. Clean text and HTML artifacts
8. Validate against the Users dataset
9. Perform final quality checks
10. Export the cleaned dataset

Unrecoverable missing values were retained as missing rather than replaced with fabricated values.

### Exploratory Data Analysis

EDA was performed on the cleaned dataset to analyse:

- Platform distribution
- Engagement distributions
- Engagement by platform
- Correlation between engagement metrics
- Monthly posting activity
- Hourly posting activity
- Engagement over time
- User posting activity
- Engagement outliers

### Phase 1 Key Findings

- The five known platforms have relatively balanced post volumes.
- Likes, shares, and comments show almost no linear correlation.
- No single platform consistently leads across all engagement metrics.
- Monthly posting activity remains relatively stable.
- Average engagement remains relatively stable over time.
- All 1,500 users have at least one corresponding post.
- No IQR-based statistical outliers were identified in the engagement metrics.

---

# Phase 2 — SQL Analytical Investigation

The cleaned dataset was structured into relational **PostgreSQL** tables:

- `users` — user-level information and follower counts
- `posts` — post-level activity and engagement metrics

The tables are connected using `user_id`, allowing user-level and post-level information to be analysed together.

The Phase 2 analysis uses SQL joins, aggregations, CTEs, filtering, and window functions.

### Analytical Challenges

#### E2 — Most Engaged Posts

Identified the **top 10 posts by total engagement**, where:

`Total Engagement = Likes + Shares + Comments`

Posts with missing likes were excluded to avoid fabricating engagement values.

**Finding:** The top 10 posts recorded total engagement between **7,610 and 7,893**, with the highest-engagement post reaching **7,893**.

#### M4 — Platform Behaviour by High Follower Users

Compared average engagement per post across platforms for users with **at least 30,000 followers**.

**Finding:** **Instagram** recorded the highest average engagement per post at **4,144.59**, while the platform averages remained relatively close overall.

#### H4 — Follower to Engagement Anomaly

Identified users with **fewer than 5,000 followers** whose total engagement falls within the **top 10% of all users**.

**Finding:** **17 users** satisfied both conditions. The highest-engagement account in this group had **2,211 followers and 58,480 total engagement**, highlighting a significant follower-to-engagement imbalance.

These results identify potentially unusual high-performing accounts but do not independently establish suspicious activity.

---

# Round 2 — NLP Semantic Understanding

Round 2 focuses on rebuilding the Social Engine's failed **semantic understanding layer**, which was unable to properly understand the meaning, tone, and intent of human language. The provided labelled textual dataset was used to rebuild this NLP-driven module. :contentReference[oaicite:0]{index=0}

### Dataset

The NLP dataset contains:

- **9,000 text records**
- `text_id`
- `post_text`
- `sentiment_label`
- `topic_category`

Two classification tasks were performed:

**Sentiment Classification**
- Negative
- Neutral
- Positive

**Topic Classification**
- Account_Security
- Community_Discussion
- Feature_Feedback
- Technical_Issues

### NLP Pipeline

The NLP workflow included:

1. Dataset quality assessment
2. Duplicate-text investigation
3. Text normalization
4. URL and mention removal
5. Hashtag normalization
6. Special-character removal while preserving alphanumeric tokens
7. Whitespace normalization
8. TF-IDF feature extraction
9. Group-aware 75:25 train-test splitting
10. Lightweight machine-learning model evaluation
11. Deep-learning model evaluation
12. Confusion-matrix analysis
13. Error analysis
14. TF-IDF coefficient-based explainability

Because repeated text entries were present, the train-test split was grouped by cleaned text to prevent identical texts from appearing in both sets.

### Models Evaluated

- TF-IDF + Logistic Regression
- Improved TF-IDF + Logistic Regression
- VADER
- Multinomial Naive Bayes
- Linear SVM
- Simple Deep Learning
- BiLSTM

### Final Selected Models

**Sentiment:** TF-IDF + Logistic Regression  
**Topic:** TF-IDF + Linear SVM

Final test performance:

| Task | Model | Accuracy | Macro F1 |
|---|---|---:|---:|
| Sentiment | TF-IDF + Logistic Regression | 0.5734 | 0.5730 |
| Topic | TF-IDF + Linear SVM | 0.9349 | 0.6706 |

The topic dataset was highly imbalanced, with **Community_Discussion accounting for 86.13%** of the records. Therefore, macro F1 and class-wise metrics were used alongside accuracy to evaluate minority-class performance. :contentReference[oaicite:1]{index=1}

### Round 2 Error Analysis

The major observed error patterns were:

- Sentiment predictions showed substantial confusion involving the **Neutral** class.
- The largest sentiment confusion was **Neutral → Negative (189 cases)**.
- The largest topic confusion was **Technical_Issues → Community_Discussion (65 cases)**.
- **Feature_Feedback → Community_Discussion** occurred in 45 cases.
- Minority topic classes were more frequently misclassified as the dominant `Community_Discussion` class.
- TF-IDF coefficients provided feature-level information about the statistical associations learned by the linear models.

---

# Repository Structure

```text
data-vortex-social-engine/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── Social_Engine_Posts_Corrupted.csv
        ├── Social_Engine_Users.csv
│   │   └── Labeled_Social_NLP_Training_Data
│   │
│   └── cleaned/
│       └── Social_Engine_Posts_Cleaned.csv
│
├── notebooks/
│   ├── 01_posts_data_cleaning.ipynb
│   ├── 02_posts_eda.ipynb
│   └── Tekton_Round2_Social_Engine_NLP_Analytics.ipynb
│
├── src/
│   └── cleaning/
│       └── posts_cleaning.py
│
├── sql/
│   ├── schema.sql
│   ├── E2/
│   │   ├── E2_query.sql
│   │   └── E2_output.png
│   │
│   ├── M4/
│   │   ├── M4_query.sql
│   │   └── M4_output.png
│   │
│   └── H4/
│       ├── H4_01_query.sql
│       ├── H4_02_query.sql
│       └── H4_output.png
│
├── models/
│   └── Tekton_Round2_Final_NLP_Models.pkl
│
└── reports/
    ├── Social_Engine_Posts_EDA_Report.pdf
    ├── Phase_02_Insight_Report.pdf
    ├── Evaluation_Metrics_Report.pdf
    └── Round_02_Technical_Report.pdf
