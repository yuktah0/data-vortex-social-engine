# Data Vortex 2026 — Social Engine

Data cleaning, data quality analysis, exploratory data analysis, and SQL-based analytical investigation for the **Data Vortex 2026 Social Engine recovery challenge**.

## Project Overview

The project focuses on recovering and analysing a corrupted Social Engine dataset containing social media posts and user information.

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

## Project Status

**Phase 1 — Data Cleaning & EDA: Completed** ✅  
**Phase 2 — SQL Analysis & Insight Report: Completed** ✅

## Dataset

The project uses two raw datasets:

- `Social_Engine_Posts_Corrupted.csv`
- `Social_Engine_Users.csv`

The final processed dataset is:

- `Social_Engine_Posts_Cleaned.csv`

The cleaned Posts dataset contains **12,000 posts from 1,500 users**.

## Phase 1 — Data Cleaning & EDA

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

## Phase 2 — SQL Analytical Investigation

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

## Repository Structure

```text
data-vortex-social-engine/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── Social_Engine_Posts_Corrupted.csv
│   │   └── Social_Engine_Users.csv
│   │
│   └── cleaned/
│       └── Social_Engine_Posts_Cleaned.csv
│
├── notebooks/
│   ├── 01_posts_data_cleaning.ipynb
│   └── 02_posts_eda.ipynb
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
└── reports/
    ├── Social_Engine_Posts_EDA_Report.pdf
    └── Phase_02_Insight_Report.pdf
