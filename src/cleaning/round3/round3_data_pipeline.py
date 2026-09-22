# ============================================================
# DATA VORTEX ROUND 3
# Public Reaction to the Boston Scientific Cyberattack
#
# Combined data collection and preparation pipeline
#
# Pipeline:
# 1. Collect Google News RSS data
# 2. Save news_raw.csv
# 3. Load X + News data
# 4. Clean and standardize the X data
# 5. Combine X + News into the Round 3 schema
# 6. Validate, sort and save the analysis dataset
# ============================================================

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import requests
import feedparser
import pandas as pd
from urllib.parse import quote


# ============================================================
# 2. COLLECT GOOGLE NEWS DATA
# ============================================================

# Boston Scientific cyberattack news search
query = '"Boston Scientific" cyberattack'

url = (
    "https://news.google.com/rss/search?q="
    + quote(query)
    + "&hl=en-IN&gl=IN&ceid=IN:en"
)

print("Fetching news...")
print("Query:", query)

response = requests.get(url, timeout=20)

print("Status code:", response.status_code)

if response.status_code != 200:
    raise SystemExit("Failed to fetch Google News RSS feed.")

feed = feedparser.parse(response.content)

rows = []

for i, entry in enumerate(feed.entries, start=1):

    published = entry.get("published", "")

    rows.append({
        "text_id": f"news_{i:04d}",
        "source": "news",
        "post_text": entry.get("title", "").strip(),
        "timestamp": published,
        "likes": pd.NA,
        "comments": pd.NA,
        "shares": pd.NA
    })

news = pd.DataFrame(rows)

news.to_csv("news_raw.csv", index=False)

print("\n===== NEWS COLLECTION =====")
print("Articles collected:", len(news))

print("\nColumns:")
print(news.columns.tolist())

print("\nMissing values:")
print(news.isna().sum())

print("\nDate range:")
print(news["timestamp"].min())
print(news["timestamp"].max())

print("\n===== SAMPLE ARTICLES =====")
print(
    news[
        ["text_id", "timestamp", "post_text"]
    ].head(10).to_string(index=False)
)

print("\nSaved as: news_raw.csv")


# ============================================================
# 3. DATA VORTEX ROUND 3
# DATA PREPARATION
# ============================================================

# Purpose:
# 1. Clean and standardize the raw X export
# 2. Standardize the collected news data
# 3. Combine both sources into one common schema
# 4. Save reproducible raw analysis dataset


# ------------------------------------------------------------
# 4. LOAD RAW DATA
# ------------------------------------------------------------

x_raw = pd.read_csv("x_collection.csv")
news_raw = pd.read_csv("news_raw.csv")

print("=" * 60)
print("DATA LOADING")
print("=" * 60)

print(f"Raw X records: {len(x_raw)}")
print(f"Raw News records: {len(news_raw)}")


# ------------------------------------------------------------
# 5. CLEAN X DATA
# ------------------------------------------------------------

# Convert text to lowercase for filtering
x_text = x_raw["text"].fillna("").str.lower()

# Keep posts mentioning Boston Scientific or its common handle
boston_mask = x_text.str.contains(
    r"boston scientific|bostonsci",
    regex=True,
    na=False
)

x_clean = x_raw[boston_mask].copy()

# Remove known contamination from the Manchester Airport incident
contamination_mask = x_clean["text"].fillna("").str.lower().str.contains(
    r"manchester airport|manchester airports|stansted|east midlands airport",
    regex=True,
    na=False
)

x_clean = x_clean[~contamination_mask].copy()


# ------------------------------------------------------------
# 6. MAP X DATA TO LOCKED ROUND 3 SCHEMA
# ------------------------------------------------------------

x_final = pd.DataFrame({
    "text_id": x_clean["id"],
    "source": "twitter",
    "post_text": x_clean["text"],
    "timestamp": x_clean["created_at"],
    "likes": x_clean["favorite_count"],
    "comments": x_clean["reply_count"],
    "shares": x_clean["retweet_count"]
})


# ------------------------------------------------------------
# 7. VALIDATE NEWS DATA
# ------------------------------------------------------------

required_news_columns = [
    "text_id",
    "source",
    "post_text",
    "timestamp",
    "likes",
    "comments",
    "shares"
]

missing_news_columns = [
    col for col in required_news_columns
    if col not in news_raw.columns
]

if missing_news_columns:
    raise ValueError(
        f"Missing columns in news_raw.csv: {missing_news_columns}"
    )

news_final = news_raw[required_news_columns].copy()


# ------------------------------------------------------------
# 8. COMBINE X + NEWS
# ------------------------------------------------------------

combined = pd.concat(
    [x_final, news_final],
    ignore_index=True
)


# ------------------------------------------------------------
# 9. STANDARDIZE TIMESTAMPS
# ------------------------------------------------------------

combined["timestamp"] = pd.to_datetime(
    combined["timestamp"],
    utc=True,
    errors="coerce"
)

invalid_timestamps = combined["timestamp"].isna().sum()

if invalid_timestamps > 0:
    print(
        f"WARNING: {invalid_timestamps} records have invalid timestamps."
    )


# ------------------------------------------------------------
# 10. SORT CHRONOLOGICALLY
# ------------------------------------------------------------

combined = (
    combined
    .sort_values("timestamp")
    .reset_index(drop=True)
)


# ------------------------------------------------------------
# 11. CHECK DUPLICATE IDS
# ------------------------------------------------------------

duplicate_ids = combined["text_id"].duplicated().sum()


# ------------------------------------------------------------
# 12. SAVE CLEAN X DATA
# ------------------------------------------------------------

x_final.to_csv(
    "x_clean.csv",
    index=False
)


# ------------------------------------------------------------
# 13. SAVE COMBINED RAW DATASET
# ------------------------------------------------------------

combined.to_csv(
    "round3_raw_combined.csv",
    index=False
)


# ------------------------------------------------------------
# 14. AUDIT SUMMARY
# ------------------------------------------------------------

print()
print("=" * 60)
print("ROUND 3 DATA PREPARATION COMPLETE")
print("=" * 60)

print(f"Clean X records: {len(x_final)}")
print(f"News records: {len(news_final)}")
print(f"Combined records: {len(combined)}")

print()
print("Source distribution:")
print(combined["source"].value_counts())

print()
print("Columns:")
print(list(combined.columns))

print()
print("Duplicate text IDs:")
print(duplicate_ids)

print()
print("Valid timestamps:")
print(combined["timestamp"].notna().sum())

print()
print("Date range:")
print(combined["timestamp"].min())
print("to")
print(combined["timestamp"].max())

print()
print("Output files:")
print("x_clean.csv")
print("round3_raw_combined.csv")

print("=" * 60)
