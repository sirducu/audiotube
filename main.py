from bs4 import BeautifulSoup
import edge_tts, asyncio, requests, random, os

path = "/home/radu/Projects/workspace/lightnovelworld/audio"

url = "https://www.lightnovelworld.co/novel/vainqueur-the-dragon-1519/chapter-1" #Vainqueur the Dragon

intros = ["Please like, subscribe and share! With each chapter, new mysteries await, new adventures beckon, and new characters come to life. So, without further ado, let's dive back into the enchanting world of [Vainqueur the Dragon]. FULL STORY available in advance on patreon, the link is in the comments!", "Please like, subscribe and share! As we turn the page to a new chapter, the journey continues. Brace yourself for what lies ahead as we delve deeper into the unfolding tale of [Vainqueur the Dragon]. FULL STORY available in advance on patreon, the link is in the comments!", "Please like, subscribe and share! Without further ado, let us continue our odyssey through the captivating world of [Vainqueur the Dragon]. FULL STORY available in advance on patreon! the link is in the comments!", "For the journey ahead holds wonders yet untold, and the chapters yet to come are brimming with anticipation. Please like, subscribe and share!. FULL STORY available in advance on patreon! the link is in the comments!"]
introducere = "Welcome to a realm where dreams intertwine with reality, and mysteries await around every corner. Join us on a journey beyond imagination, where each word is a brushstroke painting the canvas of adventure. Without further ado, welcome to 'Vainqueur the Dragon'. If possible, please support me on patreon! the link is in the comments!"
iesire = "Hello guys, please subscribe, hit the notification bell, comment and share this video to your friends if you like the audiobook. If possible, please support me on patreon! the link is in the comments!  I also make audiobooks on request for subscribers!"
ending = "\nAnd with this, our story has concluded, please don't forget to like, share and subscribe to our channel! Also, i make audiobooks on request, so please feel free to make a request in the comments and please check out our other stories. Rhadoo out!. If possible, please support me on patreon! the link is in the comments!"


intro = random.choice(intros)


headers = { 'Accept-Language' : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"}

async def speech(data, nr):
    voice = "en-CA-LiamNeural"
    communicate = edge_tts.Communicate(data, voice)
    await communicate.save(f"{path}/mp3/{nr}.mp3") 

def getData(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def getNextUrl(data):
    url = data.find('a', rel="next")['href']
    url1 = f"https://www.lightnovelworld.com{url}"
    return url1

nr = 1
x = True
while nr <= 152:
    soup1 = getData(url)
    ptags = soup1.find_all('p')
    titlu = soup1.find('span', attrs={"class":"chapter-title"}).get_text()
    url = getNextUrl(soup1)
    lista = []
    for p in ptags:
        print(p)
        if p == "":
                continue
        else:
            try:
                text = p.get_text()
                for word in interzis():
                    word = word.lower()
                    text = text.lower()
                    if word in text:
                        text = ""
                wordlist = text.split()
                for index, data in enumerate(wordlist):
                    data = data.lower()
                    for key, value in modificat.items():
                        if key == data:
                            print(f"{data} a fost inlocuit")
                            wordlist[index] = data.replace(key, modificat[key])
                text = ' '.join(wordlist)
                lista.append(text)
            except Exception as e:
                print(e)
    story = '\n'.join(map(str, lista))
    if nr == 1 or nr == 26 or nr == 51 or nr == 76 or nr == 101 or nr == 126:
        with open(f"{path}/txt/{nr}.txt", "a", encoding='UTF-8') as f:
            f.write(intro + "\n" + titlu +"\n"+ story)
        scris = intro + "\n" + story
        print(f"{intro}\n{titlu}")
    elif nr == 25 or nr == 50 or nr == 75 or nr == 100 or nr == 125 or nr == 152:
        with open(f"{path}/txt/{nr}.txt", "a", encoding='UTF-8') as f:
            f.write(titlu + "\n" + story + "\n" + iesire)
        scris = story + "\n" + iesire
        print(f"{titlu}\n{iesire}")
    else:
        with open(f"{path}/txt/{nr}.txt", "a", encoding='UTF-8') as f:
            f.write(titlu +"\n"+ story)
        scris = story
        print(titlu)

    asyncio.run(speech(scris, nr))
    nr += 1
    print(url)
    if not url:
        x = False

os.system(f'curl -d "Am terminat cu SCRAPE-ul" https://ntf.ducu.dev/home')
