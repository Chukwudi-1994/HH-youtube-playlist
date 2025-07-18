import re
import os
import pickle
import yaml
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def load_config():
     #Load config files
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    return config

def extract_youtube_links(config):
    """
    Extracts all youtube links from chat.
    """
    file_path = config['SYSTEM']['CHAT_FILE']

    youtube_regex = r"(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[^\s]+)"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return list(set(re.findall(youtube_regex, content)))

def authenticate_youtube(config):
    scopes = ["https://www.googleapis.com/auth/youtube"]
    
    # Download this file from your Google API Console
    client_secrets_file = config['SYSTEM']['YOUTUBE_SECRETS']

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube

def create_playlist(youtube, config):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": config['PLAYLIST']['PLAYLIST_TITLE'],
                "description": config['PLAYLIST']['DESCRIPTION']
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()
    return response["id"]


def add_videos_to_playlist(youtube, playlist_id, video_urls):
    for url in video_urls:
        video_id = extract_video_id(url)
        if video_id:
            try:
                youtube.playlistItems().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": playlist_id,
                            "resourceId": {
                                "kind": "youtube#video",
                                "videoId": video_id
                            }
                        }
                    }
                ).execute()
                print(f"Added: {video_id}")
            except Exception as e:
                print(f"Error adding {video_id}: {e}")

def extract_video_id(url):
    # Handles both youtu.be and youtube.com
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None