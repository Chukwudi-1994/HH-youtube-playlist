from Functions.helpers import *

CONFIG = load_config()

print(CONFIG['SYSTEM']['CHAT_FILE'])

youtube_links = extract_youtube_links(CONFIG)

print(youtube_links)

client = authenticate_youtube(CONFIG)

playlist_id = create_playlist(client,CONFIG)

add_videos_to_playlist(client, playlist_id, youtube_links)