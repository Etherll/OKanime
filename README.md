


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

    from ok_anime import Anime
    ok = Anime('Anime Name')
    print(ok.title)

index:	
	#json of all searchs in OKAnime for anime name
	print(ok.search)
	#get anime title
    	print(ok.title)
	#get anime genre
	print(ok.genre)
	#get anime url
	print(ok.url)
	#get anime cover
	print(ok.cover)
	#get anime status
	print(ok.status)
	#get anime year
	print(ok.year)
	#get anime episodes
	print(ok.episodes)
	#get anime age_classification
	print(ok.age_classification)
	print(ok.rate)
	#get anime rate
	print(ok.description)
	#get anime
	print(ok.trailer)
	#get anime
	print(ok.studio)
	#get anime
	print(ok.director)
	#get anime
	

this information is fetched from OkAnime

Make sure you don't spam the tests too quickly! One of the tests involves POSTing invalid credentials to OKAnime, so you're likely to be IP-banned if you do this too much in too short a span of time.
