import requests
import json

book = ""
verse = ""
url = "http://getbible.net/json?passage="

end = "&raw=true"


def specific_bible():
	global book
	try:
		book = input('Which Book are you looking for? ').capitalize()
		chapter = input ('Which Chapter are you looking for? ')
		verse = ("Which Verse are you looking for? ")
		url_response = url + book + chapter + ":" + verse + end + '&version-kjv'
		response = requests.get(url_response).json()
		verse_upper = response["book"][0]["chapter"]
		verse_lower = verse_upper[verse]["verse"]
		print(verse_lower)
	except KeyError:
		print ("I don't know that book...")
	except json.decoder.JSONDecodeError:
		print ("There are not that many books... yet...")




def search_bible():
	global book, verse
	try:
		book = input('Which Book are you looking for? ').capitalize()
		chapter = input ('Which Chapter are you looking for? ')
		# verse = ("Which verse are you looking for?")
		verse_int = 1
		while True:
			verse = str(verse_int)
			url_response = url + book + chapter + ":" + verse + end + '&version-kjv'
			response = requests.get(url_response).json()
			verse_upper = response["book"][0]["chapter"]
			verse_lower = verse_upper[verse]["verse"]
			print("Verse " + verse + ": " + verse_lower)
			verse_int = verse_int + 1
	except KeyError:
		print ("End of chapter.")
	except json.decoder.JSONDecodeError:
		print ("That's all the verses in " + book + ".")




#uncomment the function to choose

#specific_bible()
search_bible()