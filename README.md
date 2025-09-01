# HH-youtube-playlist

## Background

This repo allows you to take all youtube links posted in a whatsapp group chat and to create a youtube playlist. 

## Prerequisites

1. You'll need to export the chat you're interested in in Whatsapp web right click the chat in Whatsapp web and click 'export chat' which will export the chat as a txt file. Then save the chat in the root of this repo as 'chat.txt'.
2. You'll need to create a project in GCP which allows you access to the youtube API and obtain OAuth credentials. To do this:
    1. [Open google cloud console](https://console.cloud.google.com/)
    2. Click the project dropdown at the top of the page and click "New Project", name it and create.
    3. Enable the youtube API - in the left menu click APIs and services -> Library, search for "Youtube Data API c3" and then click "Enable".
    4. Go to APIs and Services -> Auth Consent screen. Choose External. Fill in the required fields. Add your gmail as a test user.
    5. Go to "Credentials" -> "Create Credentials" -> "OAuth Client ID". Application type: Desktop App. Give it a name. Click Create
    6. Download the file `client_secret.json` save it in the root directory of this folder. Note that these are important credentials so do not push them to your own github or leave them anywhere they shouldn't be.

## Use

Once you've set up all the prerequisites you can create the playlist by doing the following:
1. In the config file change the name of the playlist and the descriptions as you please.
2. Run the following in the terminal

```
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

The playlist should then be created on your own youtube account.