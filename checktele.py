import random
import threading
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopasdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'
z = 'ertiopasflzxc'

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+d+d+d+c+c
        f2 = c+c+d+d+d+c
        f3 = c+c+c+d+d+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(b) for i in range(1))))
            f1 = c+d+d+d+c+c
            f2 = c+c+d+d+d+c
            f3 = c+c+c+d+d+d
            f = f1,f2,f3
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "2":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(a) for i in range(1))))
        f1 = c+'x'+'x'+'x'+d
        f2 = c+d+'x'+'x'+'x'
        f3 = 'x'+'x'+'x'+c+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(a) for i in range(1))))
            f1 = c+'x'+'x'+'x'+d
            f2 = c+d+'x'+'x'+'x'
            f3 = 'x'+'x'+'x'+c+d
            f = f1,f2,f3
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "3":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(a) for i in range(1))))
        s = str(''.join((random.choice(a) for i in range(1))))
        f1 = c+s+d+d+d
        f2 = c+d+d+d+s
        f3 = c+c+c+s+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(a) for i in range(1))))
            s = str(''.join((random.choice(a) for i in range(1))))
            f1 = c+s+d+d+d
            f2 = c+d+d+d+s
            f3 = c+c+c+s+d
            f = f1,f2,f3
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "4":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        s = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+s+d+d+d
        f2 = c+d+d+d+s
        f3 = c+c+c+s+d
        f4 = c+c+s+s+s+s
        f5 = c+s+s+s+s+c
        f = f1,f2,f3,f4,f5
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(e) for i in range(1))))
            s = str(''.join((random.choice(e) for i in range(1))))
            f1 = c+s+d+d+d
            f2 = c+d+d+d+s
            f3 = c+c+c+s+d
            f4 = c+c+s+s+s+s
            f5 = c+s+s+s+s+c
            f = f1,f2,f3,f4,f5
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "5":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(z) for i in range(1))))
        f1 = c+c+d+d+d
        f2 = c+d+d+d+c
        f3 = c+c+d+d+d+d
        f4 = c+d+d+d+d+c
        f5 = d+d+d+d+c+c
        f6 = c+d+d+d+d
        f7 = d+c+d+d+d
        f8 = d+d+c+d+d
        f9 = d+d+d+d+c
        f = f1,f2,f3,f4,f5,f6,f7,f8,f9
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(z) for i in range(1))))
            f1 = c+c+d+d+d
            f2 = c+d+d+d+x
            f3 = c+c+d+d+d+d
            f4 = c+d+d+d+d+c
            f5 = d+d+d+d+c+c
            f6 = c+d+d+d+d
            f7 = d+c+d+d+d
            f8 = d+d+c+d+d
            f9 = d+d+d+d+c
            f = f1,f2,f3,f4,f5,f6,f7,f8,f9
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "6":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice('x') for i in range(1))))
        f1 = c+c+d+d+d
        f2 = c+d+d+d+c
        f3 = c+c+d+d+d+d
        f4 = c+d+d+d+d+c
        f5 = d+d+d+d+c+c
        f6 = c+d+d+d+d
        f7 = d+c+d+d+d
        f8 = d+d+c+d+d
        f9 = d+d+d+d+c
        f = f1,f2,f3,f4,f5,f6,f7,f8,f9
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice('x') for i in range(1))))
            f1 = c+c+d+d+d
            f2 = c+d+d+d+x
            f3 = c+c+d+d+d+d
            f4 = c+d+d+d+d+c
            f5 = d+d+d+d+c+c
            f6 = c+d+d+d+d
            f7 = d+c+d+d+d
            f8 = d+d+c+d+d
            f9 = d+d+d+d+c
            f = f1,f2,f3,f4,f5,f6,f7,f8,f9
            f = random.choice(f)
            username = f
        else:
            pass
    return username

@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker)
        
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay2[0] == "yes":
        await sython.send_file(event.chat_id, 'banned.txt')


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.eo"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
# صيد عدد نوع قناة


@sython.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        trys = 0
        await event.edit(f"Okay, I'll check the type `{choice}` From the ministers on `{ch}` , By number `{msg[0]}` Of attempts !")

        @sython.on(events.NewMessage(outgoing=True, pattern=r"\.GG"))
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"Attempts arrived ({trys})")
                elif "off" in isclaim:
                    await event.edit("لايوجد صيد شغال !")
                else:
                    await event.edit("خطأ")
            else:
                pass
        for i in range(int(msg[0])):
            if ispay2[0] == 'no':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await sython(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await event.client.send_message("@i_R_Y", f'''
Caught by a sheikh 💸
⤷ ID : @{username}
⌯ Clicks ⤷ : {trys}
⤷ Sheikh : @P8_PP - @x_o_x 
    ''')
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    await sython.send_message("@i_R_Y", f'''Feature @{username} ⏎ ''')
                    if "A wait of" in str(eee):
                        break
                    else:
                        await sython.send_message(event.chat_id, "𝙳𝙾𝙽𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙿𝚁𝙾𝙿𝙴𝚁𝚃𝚈 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 ⏎")
            else:
                pass
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        await event.client.send_message(event.chat_id, "⤷ 𝚃𝙷𝙴 𝙷𝚄𝙽𝚃𝙸𝙽𝙶 𝙸𝚂 𝙾𝚅𝙴𝚁 𝙾𝚁 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙾𝙵 𝚃𝙷𝙴 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 ⏎")
        
@sython.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

            @sython.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت التلقائي"))
            async def _(event):
                if "on" in isauto:
                    msg = await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
                elif "off" in isauto:
                    await event.edit("لايوجد تثبيت شغال !")
                else:
                    await event.edit("خطأ")
            for i in range(int(msg[0])):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await sython(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message("@i_R_Y", f'''
Caught by a sheikh 💸
⤷ ID : @{username}
⌯ Clicks ⤷ : {trys}
⤷ Sheikh : @P8_PP - @x_o_x 
    ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await sython.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                trys += 1

                await asyncio.sleep(8)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await sython.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await sython(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message("@i_R_Y", f'''
Caught by a sheikh 💸
⤷ ID : @{username}
⌯ Clicks ⤷ : {trys}
⤷ Sheikh : @P8_PP - @x_o_x 
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await sython.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
Threads=[] 
for t in range(200):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
    