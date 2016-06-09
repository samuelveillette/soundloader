"""
soundloader is a simple program to download songs from soundcloud.

soundloader require a download directory, a soundcloud client id
and a url representing a single track to work. It does not handle
any error.
"""

import os

import requests
import soundcloud


DOWNLOAD_DIR = ""
CLIENT_ID = ""
TRACK_URL = ""


class Soundloader:
    def __init__(self, client_id):
        self.client = soundcloud.Client(client_id=client_id)

    def download_track(self, track_url):
        """ Download a soundcloud track given a URL """
        track = self.client.get('/resolve', url=track_url)
        stream_url = self.client.get(track.stream_url, allow_redirects=False)
        audiofile = DOWNLOAD_DIR + track.title + '.mp3'
        with open(audiofile, 'wb') as handle:
            resp = requests.get(stream_url.location, stream=True)
            for block in resp.iter_content(1024):
                handle.write(block)


if __name__ == '__main__':
    s = Soundloader(CLIENT_ID)
    s.download_track(TRACK_URL)
