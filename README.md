


Dependencies
============

- python 3.*
- requests
- bs4

Installation
============

pip install ok-anime

example
==========
```pyton

from ok_anime import Anime
ok = Anime('Anime Name')
print(ok.title)
```

index:	
```python
#json of all searchs in OKAnime
print(ok.search)

print(ok.title)

print(ok.genre)

print(ok.url)

print(ok.cover)

print(ok.status)

print(ok.year)

print(ok.episodes)

print(ok.age_classification)

print(ok.rate)

print(ok.description)

print(ok.trailer)

print(ok.studio)

print(ok.director)
```
	

this information is fetched from OkAnime

Make sure you don't spam the tests too quickly! One of the tests involves POSTing invalid credentials to OKAnime, so you're likely to be IP-banned if you do this too much in too short a span of time.
