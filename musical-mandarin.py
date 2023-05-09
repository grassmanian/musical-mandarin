import requests
from requests import HTTPError
from pydub import AudioSegment
from pydub.playback import play
import io
import argparse

def fetch_audio(text):
    try:
        response = requests.get('https://translate.google.com/translate_tts?ie=UTF-8&tl=zh_CN&client=tw-ob&q={}'.format(text))
    except:
        print('Error connecting to Google Translate')
    else:
        try:
            response.raise_for_status()
        except HTTPError:
            print('HTTP request returned status {}'.format(response))
        return response.content

parser = argparse.ArgumentParser(
                    prog='musical-mandarin',
                    description='Play toned audio for input Chinese')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--string', help='Input string of Chinese characters to pronounce')
group.add_argument('-i', '--interactive', action='store_true', help="Interactive mode. Accept input, produce audio, repeat")
args = parser.parse_args()

if args.interactive:
    while True:
        user_string = input('> ')

        if True:
            # Do something
            continue
        else:
            #Do something
            break
else:
    song = AudioSegment.from_file(io.BytesIO(fetch_audio(args.string)), format="mp3")
    play(song)
