# 📊 YouTube Channel Analytics Pipeline

This project builds a simple yet scalable **data engineering pipeline** to extract, process, and store metadata for YouTube channels using the **YouTube Data API v3**, with a focus on automation and data quality.

---

## 📌 Project Overview

An automated pipeline to fetch and process channel-level insights (subscribers, views, videos) using:

- **Python**: Core scripting language  
- **YouTube Data API v3**: To access public channel statistics  
- **SQLite**: Lightweight database for storage  
- **Pandas**: For data cleaning and transformation  
- **Apache Airflow**: For scheduling daily ETL jobs  

---

## 🗂️ Folder Structure
youtube_project/
│
├── dag/
│ └── youtube_dag.py ← Airflow DAG for scheduling ETL
├── scripts/
│ └──data/
│     └── youtube_data.db ← SQLite database storing channel stats
│ └── fetch_youtube.py ← Script to extract and store data
└── README.md ← Project documentatio
└── display.py ← show channels details from db column




---

## ⚙️ How It Works

1. **Input**: A list of YouTube channel names.  
2. **API Call**: Each name is resolved to a channel ID using the YouTube Search API.  
3. **Data Extraction**: Channel statistics (subscribers, views, video count) are fetched.  
4. **Transformation**: Data is structured in a clean Pandas DataFrame.  
5. **Load**: The final dataset is saved to a local SQLite database.  
6. **Automation**: Apache Airflow can be used to schedule this pipeline daily.

---

## 🚀 Technologies Used

| Tool            | Purpose                            |
|-----------------|-------------------------------------|
| Python          | Main programming language           |
| YouTube API v3  | Fetch channel-level statistics      |
| Pandas          | Data cleaning and aggregation       |
| SQLite          | Local database for storage          |
| Apache Airflow  | Task scheduling and orchestration   |

---

## 📦 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/youtube-pipeline.git
   cd youtube-pipeline


# ⚙️ Setup & Usage Guide

Follow these steps to set up and run the YouTube Channel Analytics Pipeline:

---

## 📦 1. Install Dependencies

Make sure Python 3.x is installed, then install the required packages:

```bash
pip install -r requirements.txt
```
## 🔑 2. Add Your YouTube Data API Key
Open the file:

scripts/fetch_youtube.py
Locate the following line
API_KEY = 'YOUR_YOUTUBE_API_KEY'
Replace 'YOUR_YOUTUBE_API_KEY' with your actual API key.

You can get one from the Google Cloud Console.
