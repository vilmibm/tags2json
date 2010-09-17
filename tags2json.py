# This program is distributed under the terms 
# of the GNU General Public License
# Copyright 2010 Nathaniel Smith

import os
import sys
import json
import time

from mutagen.oggvorbis import OggVorbis
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

if len(sys.argv) != 2:
    print "Usage: tags2json.py filename"
    sys.exit(1)

filename = os.path.abspath( sys.argv[1] )
lower_filename = filename.lower()

tags = {}

try:
    if lower_filename.endswith('.ogg'):
        audio = OggVorbis(filename)
        tags['length'] = audio.info.length
    elif lower_filename.endswith('.mp3'):
        audio = EasyID3(filename)
        tags['length'] = MP3(filename).info.length
    else:
        sys.exit(2)
except:
    sys.exit(2)

tags['length'] = time.strftime('%M:%S', time.gmtime(tags['length']))

for key in audio.keys():
    tags[key] = audio[key].pop()

print json.dumps(tags)
