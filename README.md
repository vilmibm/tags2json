tags2json.py
============

This simple script prints a JSON representation of an audio track to STDOUT. It
is intended for use in larger projects as a way to abstract out processing
audio tags.

It is written in Python and distributable under the GPL.

It uses the [mutagen](http://code.google.com/p/mutagen/ "mutagen") library.

Usage
-----

    $: tags2json.py ~/Music/03_doe_deer.MP3
    {"album": "Crystal Castles II", "title": "Doe Deer", "artist": "Crystal Castles", "genre": "Electronic", "length": "01:37", "composer": "A. Glass", "date": "2010", "tracknumber": "3"}

Todo
----
* Support audio types other than Ogg and mp3

Author
------
Nathaniel Smith [(blog)](http://chiptheglasses.com "blog")
