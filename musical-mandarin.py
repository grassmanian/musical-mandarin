import requests
from requests import HTTPError
from pydub import AudioSegment
from pydub.playback import play
import io

try:
    response = requests.get('https://translate.google.com/translate_tts?ie=UTF-8&tl=zh_CN&client=tw-ob&q=話說天下大勢，分久必合，合久必分')
except:
    print('Error connecting to Google Translate')
else:
    try:
        response.raise_for_status()
    except HTTPError:
        print('HTTP request returned status {}'.format(response))


song = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
play(song)

