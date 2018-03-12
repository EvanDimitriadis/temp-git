import sys
import urllib.request
import json

keyApi = "449680A29CD8D9E24881E7DFA3D823C7"
MyId = "76561198015220072"

friend1 = "76561198024620160"
friend2 = "76561198118932724"

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
    
	CivVI = "289070"
	SpellForce = "311290"
	IsPlayingSharedGame(friend2,SpellForce,"json")
	GetRecentlyPlayedGames(friend2,10,"json")
	#GetListOfGames(friend1,"json")
	pass

if __name__ == '__main__':
    sys.exit(main())

