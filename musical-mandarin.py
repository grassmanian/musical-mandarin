import requests
from pydub import AudioSegment
from pydub.playback import play
import io

response = requests.get('https://translate.google.com/translate_tts?ie=UTF-8&tl=zh_CN&client=tw-ob&q=話說天下大勢，分久必合，合久必分')

song = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
play(song)

