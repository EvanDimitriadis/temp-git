import sys
import urllib.request
import json
from bs4 import BeautifulSoup

keyApi = "449680A29CD8D9E24881E7DFA3D823C7"
MyId = "76561198015220072"

friend1 = "76561198024620160"
friend2 = "76561198118932724"

def PlayingNow (steamId,text):

	url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
	search = url + keyApi +"&steamids=" + str(steamId) 
	with urllib.request.urlopen(search) as http:
		data = json.load(http)
		#game = (data['response']['players']['gameextrainfo'])
		gamersList = data['response']['players']
		string = str(gamersList)
		pos = string.find('gameextrainfo')
		if pos:
			print("Now Playing: " + string[pos+16:-2].split("'")[1])
		else:
			print('Not found')
		return (string[pos+16:-2].split("'")[-2])

def IsPlayingSharedGame (steamId,appIdPlaying,text):

	url =  "http://api.steampowered.com/IPlayerService/IsPlayingSharedGame/v0001/?key="
	search = url + keyApi +"&steamid=" + str(steamId) + "&appid_playing=" + str(appIdPlaying) + "&format=" + text
	with urllib.request.urlopen(search) as http:
		data = json.load(http)
		print(data['response'])
		if MyId in data:
			print("User:"+steamId+"is playing one of your games")

def GetRecentlyPlayedGames (steamId,count,text):

	url =  "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key="
	search = url + keyApi +"&steamid=" + str(steamId) +  "&format=" + text
	#print(search)
	with urllib.request.urlopen(search) as http:
		data = json.load(http)
		for i in range(0,(len(data['response']['games']))):
			print(data['response']['games'][i].get('name'))

def GetListOfGames (steamId,text):

	url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key="
	search = url + keyApi +"&steamid=" + str(steamId) + "&include_appinfo=1" + "&format=" + text
	#print(search)
	with urllib.request.urlopen(search) as http:
		data = json.load(http)
		for i in range(0,(len(data['response']['games']))):
			print(data['response']['games'][i].get('name'))

def main():
    
	gameid = PlayingNow(friend2,"json")
	print(gameid)
	IsPlayingSharedGame(friend2,gameid,"json")
	#GetRecentlyPlayedGames(friend2,10,"json")
	GetListOfGames(friend1,"json")
	pass

if __name__ == '__main__':
    sys.exit(main())

