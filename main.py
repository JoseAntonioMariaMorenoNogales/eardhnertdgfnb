print("""  _____            _       _    ____        _ _                 
 / ____|          (_)     | |  / __ \      | (_)                
| (___   ___   ___ _  __ _| | | |  | |_ __ | |_ _ __   ___ _ __ 
 \___ \ / _ \ / __| |/ _` | | | |  | | '_ \| | | '_ \ / _ \ '__|
 ____) | (_) | (__| | (_| | | | |__| | | | | | | | | |  __/ |   
|_____/ \___/ \___|_|\__,_|_|  \____/|_| |_|_|_|_| |_|\___|_|   """)
print("By: Odyx#4288")
print("")
print("[i] Importing modules...")
import json
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import websocket, asyncio
from colorama import Fore
#import pyfade

types = ['Playing', 'Streaming', 'Watching', 'Listening']
status = ['online', 'dnd', 'idle']

############################################ Change here

GAME = "Twitch"  # enter what you want the status to be
type_ = types[1]  # 0: Playing, 1: Streaming, 2: Watching, 3: Listening
status = status[1]  # 0: Online, 1: Do Not Disturb, 2: Idle
random_ = True  # True: Random status and type, False: Game status and type
stream_text = "https://twitch.tv/xxpandoszxx"  # enter what you want the stream to be

############################################ Stop changing here

with open("tokens.txt", "r") as f:
    al = f.read().split("\n")
    #print(len(al))
    if len(al) <= 1:
        if len(al[0]) <= 10:
            print(f"{Fore.RED}[!] No tokens found in tokens.txt")
            exit()
        else:
            print(f"{Fore.GREEN}[i] 1 token found in tokens.txt")
    else:
        print(f"{Fore.GREEN}[i] {len(al)} tokens found in tokens.txt")

print("[i] Starting...")

c = 0
l = len(al)

def online(token, game, type, status):
    global c
    global l
    if random_:
        type = random.choice(['Playing', 'Streaming', 'Watching', 'Listening', ''])
        status = ['online', 'dnd', 'idle']
        status = random.choice(status)

        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        if type == "Playing":
            game = random.choice(['Minecraft', 'Rust', 'VRChat', 'reeeee', 'MORDHAU', 'Fortnite', 'Apex Legends', 'Escape from Tarkov', 'Rainbow Six Siege', 'Counter-Strike: Global Offense', 'Sinner: Sacrifice for Redemption', 'Minion Masters', 'King of the Hat', 'Bad North', 'Moonlighter', 'Frostpunk', 'Starbound', 'Masters of Anima', 'Celeste', 'Dead Cells', 'CrossCode', 'Omensight', 'Into the Breach', 'Battle Chasers: Nightwar', 'Red Faction Guerrilla Re-Mars-tered Edition', 'Spellforce 3', 'This is the Police 2', 'Hollow Knight', 'Subnautica', 'The Banner Saga 3', 'Pillars of Eternity II: Deadfire', 'This War of Mine', 'Last Day of June', 'Ticket to Ride', 'RollerCoaster Tycoon 2: Triple Thrill Pack', '140', 'Shadow Tactics: Blades of the Shogun', 'Pony Island', 'Lost Horizon', 'Metro: Last Light Redux', 'Unleash', 'Guacamelee! Super Turbo Championship Edition', 'Brutal Legend', 'Psychonauts', 'The End Is Nigh', 'Seasons After Fall', 'SOMA', 'Trine 2: Complete Story', 'Trine 3: The Artifacts of Power', 'Trine Enchanted Edition', 'Slime-San', 'The Inner World', 'Bridge Constructor', 'Bridge Constructor Medieval', 'Dead Age', 'Risk of Rain', "Wasteland 2: Director's Cut", 'The Metronomicon: Slay The Dance Floor', 'TowerFall Ascension + Expansion', 'Nidhogg', 'System Shock: Enhanced Edition', 'System Shock 2', "Oddworld:New 'n' Tasty!", 'Out of the Park Baseball 18', 'Hob', 'Destiny 2', 'Torchlight', 'Torchlight 2', 'INSIDE', 'LIMBO', "Monaco: What's Yours Is Mine", 'Tooth and Tail', 'Dandara', 'GoNNER', 'Kathy Rain', 'Kingdom: Classic', 'Kingdom: New Lands', 'Tormentor X Punisher', 'Chaos Reborn', 'Ashes of the Singularity: Escalation', 'Galactic Civilizations III', 'Super Meat Boy', 'Super Hexagon', 'de Blob 2', 'Darksiders II Deathinitive Edition', 'Darksiders Warmastered Edition', 'de Blob', 'Red Faction 1', 'Dungeon Defenders', ])
            gamejson = {
                "name": game,
                "type": 0
            }
        elif type == 'Streaming':
            gamejson = {
                "name": game,
                "type": 1,
                "url": stream_text
            }
        elif type == "Listening":
            game = random.choice(["Spotify", "Deezer", "Apple Music", "YouTube", "SoundCloud", "Pandora", "Tidal", "Amazon Music", "Google Play Music", "Apple Podcasts", "iTunes", "Beatport"])
            gamejson = {
                "name": game,
                "type": 2
            }
        elif type == "Watching":
            game = random.choice(["YouTube"])
            gamejson = {
                "name": game,
                "type": 3
            }
        else:
            gamejson = {
                "name": game,
                "type": 0
            }

        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
        }
        ws.send(json.dumps(auth))
        ack = {
            "op": 1,
            "d": None
        }
        while True:
            time.sleep(heartbeat_interval / 1000)
            try:
                c += 1
                print(f"{Fore.GREEN}[i] {token} is online {c}/{l}")
                ws.send(json.dumps(ack))

            except Exception as e:
                print("[!] Error: " + str(e))
                break
    else:
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        if type == "Playing":
            gamejson = {
                "name": game,
                "type": 0
            }
        elif type == 'Streaming':
            gamejson = {
                "name": game,
                "type": 1,
                "url": stream_text
            }
        elif type == "Listening":
            gamejson = {
                "name": game,
                "type": 2
            }
        elif type == "Watching":
            gamejson = {
                "name": game,
                "type": 3
            }
        else:
            gamejson = {
                "name": game,
                "type": 0
            }

        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
        }
        ws.send(json.dumps(auth))
        ack = {
            "op": 1,
            "d": None
        }
        while True:
            time.sleep(heartbeat_interval / 1000)
            try:
                c += 1
                print(f"{Fore.GREEN}[i] {token} is online {c}/{l}")
                ws.send(json.dumps(ack))

            except Exception as e:
                print("[!] Error: " + str(e))
                break


with open("tokens.txt", "r") as f:
    al = f.read().split("\n")

l = len(al)


threads = []
for i in range(l):
    t = threading.Thread(target=online, args=(al[i], GAME, type_, status)).start()


print(f"{Fore.GREEN} [+] Tokens are online")
