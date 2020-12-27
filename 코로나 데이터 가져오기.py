from bs4 import BeautifulSoup
import requests
import discord

def gotest(list1):
    j = ""
    for i in range(len(list1)):
        j = j + list1[i]
    return j

client = discord.Client()
token="your_discord_bot_token"

html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=8&acq=%EC%BD%94%EB%A1%9C%EB%8B%88&qdt=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%8B%88")
soup = BeautifulSoup(html.text,'html.parser')

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("COVID-19 check")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!COVID-19") or message.content.startswith("!코로나") or message.content.startswith("!covid-19") or message.content.startswith("!CORONA") or message.content.startswith("!corona"):
        finaldataint, finaldataup, finaldatastring = [], [], []
        dataint = soup.findAll('p',{'class':'info_num'})
        dataup = soup.findAll('em',{'class':'info_variation'})
        datastring = soup("strong",{"class":"info_title"})
        for i in dataint:
            finaldataint.append(i.text)
        for i in dataup:
            finaldataup.append(i.text)
        for i in datastring:
            finaldatastring.append(i.text)
            
        embed=discord.Embed(color=0x00aaaa)
        embed.set_author(name="국내 현황",icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/792613476589109279/792656481132085278/x.jpg")
        for i in range(4):
            embed.add_field(name=finaldatastring[i] + ": ", value= finaldataint[i]+ ", up: "+ finaldataup[i], inline=False)
        await message.channel.send(embed=embed)
        
        embed=discord.Embed(color=0x00aaaa)
        embed.set_author(name="국외 현황",icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/792613476589109279/792657109333704734/b14ae79652e6cc2d.jpg")
        for i in range(4,7):
            embed.add_field(name=finaldatastring[i] + ": ", value= finaldataint[i]+ ", up: "+ finaldataup[i], inline=False)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!prevent") or message.content.startswith("!예방"):
        cut = soup.findAll("ul",{"class":"step_detail"})
        finaldata1, finaldata2, finaltitle = [], [], []
        data1 = cut[0].findAll("li")
        data2 = cut[1].findAll("li")
        title = soup.findAll("h3",{"class":"title_area"})
        for i in data1:
            finaldata1.append(i.text)
        for i in data2:
            finaldata2.append(i.text)
        for i in title:
            finaltitle.append(i.text)
            
        embed=discord.Embed(color=0x00aaaa)
        embed.set_author(name="예방 수칙",icon_url=message.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/792613476589109279/792656002750087178/b32d0fcda0316b5b.jpg")
        data1string, data2string = ":\n", ":\n"
        for i in finaldata1:
            data1string += i + "\n"
        for i in finaldata2:
            data2string += i+"\n"
        embed.add_field(name=finaltitle[0], value = data1string, inline=False)
        embed.add_field(name=finaltitle[1], value = data2string, inline=False)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!help") or message.content.startswith("!도움") or message.content.startswith("!사용법") or message.content.startswith("!방법"):
        await message.channel.send('''```cs\n#It is COVID-19 bot\n#If you input to "COVID-19", It outputs you Number of people infected COVID-19 now\n#If you input to "prevent", I output preventing corona virus disease 19 to you```''')
        
client.run(token)
