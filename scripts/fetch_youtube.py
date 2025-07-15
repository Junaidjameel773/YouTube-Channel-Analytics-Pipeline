from googleapiclient.discovery import build
import pandas as pd
import sqlite3
from datetime import datetime
import time
import os

# Create the 'data' directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# === CONFIGURATION ===
API_KEY = 'API Key'  # Replace with your actual API key

CHANNEL_NAMES = [
    'MrBeast',
    'Tech Burner',
    'Traversy Media',
    'Google Developers',
    'CodeWithHarry',
    'Simplilearn',
    'Tech With Tim',
    'freeCodeCamp.org',
    'TED',
    'CrashCourse',
    'Veritasium',
    'Kurzgesagt – In a Nutshell',
    'Ali Abdaal',
    'The Coding Train',
    'Programming with Mosh',
    'CS Dojo',
    'Sentdex',
    'Anas Bukhash',
    'Hamza Ahmed',
    'The Futur',
    'Joma Tech',
    'Fireship',
    'Python Programmer',
    'The Linux Foundation',
    'HowToBasic',
    'Nadir Ali',
    'The School of Life',
    'Big Think',
    'Bloomberg Technology',
    'Gaurav Taneja',
    'BB Ki Vines',
    'Dhruv Rathee',
    'Nas Daily',
    'Mark Rober',
    'NASA',
    'MKBHD',
    'Linus Tech Tips',
    'Mrwhosetheboss',
    'Slayy Point',
    'Abhi and Niyu',
    'The Infographics Show',
    'Chai aur Code',
    'T-Series',
    'Sony Entertainment Television',
    'SNL',
    'Netflix',
    'Screen Junkies',
    'Marques Brownlee',
    'The Try Guys'
]

# === YOUTUBE API SETUP ===
def get_youtube_client():
    return build('youtube', 'v3', developerKey=API_KEY)


# === GET CHANNEL ID FROM CHANNEL NAME ===
def get_channel_id(youtube, name):
    try:
        request = youtube.search().list(
            q=name,
            part='snippet',
            type='channel',
            maxResults=1
        )
        response = request.execute()
        return response['items'][0]['snippet']['channelId']
    except Exception as e:
        print(f"Error getting channel ID for {name}: {e}")
        return None


# === FETCH CHANNEL STATS ===
def get_channel_stats(youtube, channel_ids):
    all_data = []

    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(channel_ids)
    )
    response = request.execute()

    for item in response['items']:
        data = {
            'channel_id': item['id'],
            'channel_name': item['snippet']['title'],
            'subscribers': int(item['statistics'].get('subscriberCount', 0)),
            'views': int(item['statistics'].get('viewCount', 0)),
            'total_videos': int(item['statistics'].get('videoCount', 0)),
            'fetched_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        all_data.append(data)

    return pd.DataFrame(all_data)


# # === SAVE TO SQLITE DATABASE ===
# def save_to_sqlite(df, db_name='data/youtube_data.db'):
#     conn = sqlite3.connect(db_name)
#     df.to_sql('channel_stats', conn, if_exists='append', index=False)
#     conn.close()
def save_to_sqlite(df, db_name='data/youtube_data.db'):
    os.makedirs('data', exist_ok=True)  # Ensure folder exists
    conn = sqlite3.connect(db_name)
    df.to_sql('channel_stats', conn, if_exists='append', index=False)
    print(f"✅ {len(df)} rows saved to {db_name}")
    conn.close()


# === MAIN FUNCTION FOR AIRFLOW OR CLI ===
def fetch_and_store():
    print("Setting up YouTube client...")
    youtube = get_youtube_client()

    channel_ids = []
    for name in CHANNEL_NAMES:
        print(f"Resolving channel name: {name}")
        channel_id = get_channel_id(youtube, name)
        if channel_id:
            channel_ids.append(channel_id)
        time.sleep(1)  # Respect rate limits

    if not channel_ids:
        print("No channel IDs found. Exiting.")
        return

    print("Fetching channel statistics...")
    df = get_channel_stats(youtube, channel_ids)
    print(df)

    print("Saving data to SQLite...")
    save_to_sqlite(df)
    print("Done!")


# === RUN DIRECTLY (OPTIONAL) ===
if __name__ == '__main__':
    fetch_and_store()
