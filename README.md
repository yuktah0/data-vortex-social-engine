# Data Vortex 2026 — Social Engine

Data cleaning, data quality analysis, and exploratory data analysis for the
Data Vortex 2026 Social Engine recovery challenge.

## Project Overview

The project focuses on recovering and analysing a corrupted Social Engine
dataset containing social media posts and user information.

The workflow includes:

- Raw data auditing
- Duplicate detection and handling
- Missing-value investigation
- Invalid-value correction
- Timestamp standardisation
- Text and HTML cleaning
- User-level validation
- Exploratory Data Analysis (EDA)
- Final data quality checks
  
## Project Status

**Phase 1 — Data Cleaning & EDA: Completed**

## Dataset

The project uses two raw datasets:

- `Social_Engine_Posts_Corrupted.csv`
- `Social_Engine_Users.csv`

The final processed dataset is:

- `Social_Engine_Posts_Cleaned.csv`

The cleaned Posts dataset contains **12,000 posts from 1,500 users**.

## Data Cleaning

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

Unrecoverable missing values were retained as missing rather than replaced
with fabricated values.

## Exploratory Data Analysis

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

### Key Findings

- The five known platforms have relatively balanced post volumes.
- Likes, shares, and comments show almost no linear correlation.
- No single platform consistently leads across all engagement metrics.
- Monthly posting activity remains relatively stable.
- Average engagement remains relatively stable over time.
- All 1,500 users have at least one corresponding post.
- No IQR-based statistical outliers were identified in the engagement metrics.

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
└── reports/
    └── Social_Engine_Posts_EDA_Report.pdf
