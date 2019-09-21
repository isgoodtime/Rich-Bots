import discord
import os
import datetime
import openpyxl
import requests
import asyncio
from json import loads

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Rich Bot Play")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "트위치 아이디"
    name = "이름"
    channel = client.get_channel(617599319565926426)
    a = 0
    while True:
        headers = {'Client-ID': '클라이언트 아이디'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "님이 방송중입니다.")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요 전 리치 봇입니다!")
    if message.content.startswith("!잘가"):
        await message.channel.send("야호! 퇴근이다! @===^--^")
    if message.content.startswith("!오목"):
        await message.channel.send("전 오목을 할줄 몰라요. 하지만 제 친구 시리는 할줄 알아요 데려올까요?")
    if message.content.startswith("!서버"):
        await message.channel.send("저희 서버는 24시간 서버입니다. 하지만 후원금이나 사정에 따라 서버온 시간이 지연됨을 알려드립니다")
    if message.content.startswith("!문의"):
        await message.channel.send("문의는 에이든님께 하시면 됩니다.")
    if message.content.startswith("!인증"):
        await message.channel.send("인증 방법은 양식입니다.\n1. 디스코드 닉네임을 고유번호 | 직업 | 닉네임으로 변경해주세요:\n2. 당신은 RP와 Non-RP의 정의를 지키고 플레이에 임할것을 약속합니다:\n3. 서버의 개인정도 아이피 유출 , 서버의 여러가지 개인정보를 유출하거나 비하할시 법적으로 해결할것입니다. 이에 동의하십니까?\n4. 모든 사람들을 평등하게 생각하고 여길것입니까?:\n5. 들어온 경로를 알려주세요.\n6. 디스코드 서버 목록이 보이게 캡처해주세요.\n들어갈시 고유번호는 ??로 직업은 무직으로")
    if message.content.startswith("!조스바보"):
        await message.channel.send("조스님은 바보입니다. ^__^ 튀어!")
    if message.content.startswith("!또치바보"):
        await message.channel.send("또치님도 바보입니다! ㅋㅋㅋㅋㅋㅋㅋㅋ")
    if message.content.startswith("!주식 DB"):
        await message.channel.send("```diff\nDB 손해보험 ^7.38%\n```")
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "년" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[2]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[3]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[4]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[5]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[6]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[7]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[8]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[9]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[10]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[11]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[12]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[13]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[14]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[15]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[16]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[17]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[18]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[19]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[20]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[21]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/채널메세지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)

    if message.content.startswith("/경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고 2회 누적입니다 서버에서 추방됩니다.")
                else:
                    await message.channel.send("경고 1회를 받았습니다")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1회 받았습니다")
                break
            i += 1

    if message.content.startswith(""):
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [100, 200, 300, 400, 500]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 8
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.channel.send(
                        "레벨이 올랐습니다.\n현재 레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(
                            sheet["B" + str(i)].value))
                file.save("레벨.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                break

            i += 1


access_token = os.environ["BOT_TOKEN]     
client.run(access_token)
