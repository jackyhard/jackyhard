import telebot
import time
import random
from PIL import Image,ImageDraw
m = []
m2 = []
diic = {}
sot = []
use = []
jas = ()
cab = ()
ver = []
agebar = []
group = -1001939034501
bot = telebot.TeleBot("6831042263:AAHcwRStj9FTQrHyPnTT8TA467Eil5pgVfU")
print("Bot started!")
picha = ["spy.jpg","spy2.jpg","spy3.png","spy4.png","spy5.png","spy6.png","spy7.png"]
admin = [1121363981,1235363769,6543038140,1423582035,6856601960,5038831752,1847093888]
picasl = random.choice(picha)
owner = 1235363769



@bot.message_handler(commands=['startt'])
def send_welcome(message):
    msid = message.message_id
    global ver
    if message.from_user.id in ver:
        bot.send_message(group,"شما قبلا احراز هویت انجام داده اید!",reply_to_message_id=msid)
    else:
        global cab
        captcha_num = str(random.randint(1000,9999))
        cab = ()
        cab = captcha_num
        captcha_image = create_captcha_image(captcha_num)

        bot.send_photo(group,captcha_image,caption=f"عدد داخل تصویر رو به این شکل داخل گروه بنویس\n/verify {captcha_num}",reply_to_message_id=msid)

@bot.message_handler(func=lambda message:message.text,commands=['verify'])
def verify(message):
    msid = message.message_id
    global cab
    global ver
    if message.from_user.id in ver:
        bot.send_message(group,"شما قبلا احراز هویت انجام داده اید!",reply_to_message_id=msid)
    else:
        user_input = message.text.split(' ')[1]
        print(cab)
        print(user_input)
        if user_input == cab:
            bot.send_message(group,"احراز هویت شما تکمیل شد!",reply_to_message_id=msid)
            ver.append(message.from_user.id)

        else:
            bot.send_message(group,"اشتباه نوشتی کصخل",reply_to_message_id=msid)


def create_captcha_image(captcha_num):
    image = Image.new('RGB', (200,100),color = "white")
    draw = ImageDraw.Draw(image)

    #font = ImageFont.truetype("arial.ttf",40)
    draw.text((50,40),captcha_num ,fill = 'black')

    return image



@bot.message_handler(func=lambda message:message.text,commands=['add'])
def add_user(message):
        msid = message.message_id
        global m
        global m2
        global use
        global admin
        global ver
        if message.from_user.id in admin:
            if message.from_user in ver:
                asam = message.text[5:]
                try:
                            players = asam.split('/')
                            cou = len(players)
                            for j in players:
                                m.append(j)
                                m2.append(j)
                            for i in m:
                                l = bot.get_chat(i)
                                if l.first_name in use:
                                    pass
                                else:
                                    use.append(l.first_name)
                            bot.send_message(group,f"Save {cou} Players!",reply_to_message_id=msid)
                except Exception:
                            bot.send_message(group,"ارور دادم!دوباره تس,ت کن!",reply_to_message_id=msid)

            else:
                bot.send_message(group,"شما هنوز احراز هویت نکرده اید!برای احراز هویت دستور /startt رو داخل گروه بنویسید",reply_to_message_id=msid)

@bot.message_handler(func=lambda message:message.text,commands=['poll'])
def create_poll(message):
        msid = message.message_id
        user_id = message.from_user.username
        global m
        global diic
        global m2
        global admin
        global sot
        global agebar
        global use
        global jas
        global ver
        if message.from_user.id in admin:
            if message.from_user.id in ver:
                paly = list(use)
                try:
                    f = bot.get_chat(jas)
                    f = f.first_name
                    diic.clear()
                    agebar.clear()
                    poll = bot.send_poll(group,f"کاربر       @{user_id}    این نظر سنجی رو ساخت!\nکدام یک جاسوس هستند؟\n30 ثانیه مهلت جواب دادن از الان!",paly,reply_to_message_id=msid)
                    time.sleep(0.5)
                    msgid = poll.message_id
                    time.sleep(25)
                    res = bot.stop_poll(group,msgid)
                    for o in res.options:
                                diic[o.text] = o.voter_count

                    sorted_dic = {key: value for key,value in sorted(diic.items(),key=lambda item: item[1])}
                    doc = list(sorted_dic.items())
                    if doc[-1][1] == doc[-2][1]:
                            bot.send_message(group,f"رای دو نفر برابر شد\n{doc[-1][0]} با {doc[-1][1]} رای \n{doc[-2][0]} با {doc[-2][1]} رای.",reply_to_message_id=msgid)
                            agebar.append(doc[-1][0])
                            agebar.append(doc[-2][0])
                            pool = bot.send_poll(group,"به دلیل برابر شدن رای دو پلیر این نظرسنجی خودکار ساخته شد!\nکدام یک جاسوس هستند؟\nمهلت 30 ثانیه برای جواب دادن!",agebar)
                            time.sleep(0.5)
                            msgid2 = pool.message_id
                            time.sleep(25)
                            res = bot.stop_poll(group,msgid2)
                            diic.clear()
                            for q in res.options:
                                diic[q.text] = q.voter_count
                            sorted_dicc = {key: value for key,value in sorted(diic.items(),key=lambda item: item[1])}
                            doc2 = list(sorted_dicc.items())
                            if doc2[0][1] == doc2[1][1]:
                                bot.send_message(group,"دیگه به تخمم رای هارو برابر کردید بقیش با خودتون",reply_to_message_id=msgid2)
                            else:
                                if doc2[-1][0] == f:
                                    bot.send_message(group,f"تبریک!جاسوس رو درست حدس زدید:)\nجاسوس {doc2[-1][0]} بود که شما با {doc2[-1][1]} رای اون رو انتخاب کردید!حالا نوبت حدس کلمه توسط جاسوسه\nاگه جاسوس کلمه رو درست حدس زد میبره ولی اگه اشتباه حدس زد کصخله و باخته!",reply_to_message_id=msgid2)
                                else:
                                    bot.send_message(group,f"تبریک!شما ریدید و اشتباه جاسوس رو حدس زدید:)\nجاسوس {f} بود که شما ریدید و انتخابش نکردید!")

                    else:
                            if doc[-1][0] == f:
                                bot.send_message(group,f"تبریک!جاسوس رو درست حدس زدید:)\nجاسوس {doc[-1][0]} بود که شما با {doc[-1][1]} رای اون رو انتخاب کردید!حالا نوبت حدس کلمه توسط جاسوسه\nاگه جاسوس کلمه رو درست حدس زد میبره ولی اگه اشتباه حدس زد کصخله و باخته!",reply_to_message_id=msgid)

                            else:
                                bot.send_message(group,f"تبریک!شما ریدید و اشتباه جاسوس رو حدس زدید:)\nجاسوس {f} بود که شما ریدید و انتخابش نکردید!",reply_to_message_id=msgid)

                except Exception:
                    bot.send_message(group,"ارور دادم!دوباره تست کن!",reply_to_message_id=msid)


            else:
                bot.send_message(group,"شما هنوز احراز هویت نکرده اید!برای احراز هویت دستور /startt رو داخل گروه بنویسید",reply_to_message_id=msid)


@bot.message_handler(func=lambda message:message.text,commands=['clear'])
def clear_user(message):
    msid = message.message_id
    global m2
    global m
    global use
    global ver
    global admin
    if message.from_user.id in admin:
        if message.from_user.id in ver:
            m.clear()
            m2.clear()
            use.clear()
            bot.send_message(group,"Clear List Of Players!",reply_to_message_id=msid)

        else:
            bot.send_message(group,"شما هنوز احراز هویت نکرده اید!برای احراز هویت دستور /startt رو داخل گروه بنویسید",reply_to_message_id=msid)





@bot.message_handler(func=lambda message: message.text)
def keyboard(message):
    chat_id = message.chat.id
    global m
    global diic
    global m2
    global sot
    global agebar
    global use
    global jas
    global ver

    if message.text.startswith("/") and chat_id in admin:
            sot.clear()
            msg = message.text[1:]

            if msg == "شما جاسوس شدید!" or msg == "شما جاسوس شدید":
                bot.send_message(chat_id,"امکان فرستادن این کلمه به پلیر ها وجود نداره!کلمه دیگری بفرستید!")
            else:
                if message.chat.id in ver:
                    try:
                        if len(m) == 0:
                            bot.send_message(chat_id,"کسی داخل لیست پلیر ها نیست!")
                        else:
                            jasos = random.choice(m)
                            if jasos == chat_id:
                                jasos = random.choice(m)
                                m.remove(jasos)
                                jas = ()
                                jas = jasos
                            else:
                                m.remove(jasos)
                                jas = ()
                                jas = jasos
                            for i in m:
                                    bot.send_message(i,msg)
                            bot.send_message(jasos,"شما جاسوس شدید!")
                            for l in m2:
                                k = bot.get_chat(l)
                                k = k.first_name
                                sot.append(k)
                            random.shuffle(sot)
                            sort_user = "\n".join(f"{index + 1}. {user}" for index, user in enumerate(sot))
                            time.sleep(1)
                            phot = Image.open(picasl)
                            bot.send_photo(chat_id=group,photo=phot,caption=f"کلمه ها ارسال شدند شروع کنید!\nنوبت حرف زدن پلیر ها بر اساس اسم:\n{sort_user}")
                            phot = phot.close()

                    except Exception:
                        bot.send_message(chat_id,"یک نفر بات رو استارت نکرده!")


                else:
                    bot.send_message(chat_id,"شما هنوز احراز هویت نکرده اید!برای احراز هویت دستور /startt رو داخل گروه بنویسید")



    elif message.text.startswith(":") and chat_id == owner:
        ms = message.text[1:]
        try:
            bot.send_message(group,ms)
            time.sleep(1)
            bot.send_message(owner,"Ok!")
        except Exception:
            bot.send_message(owner,"Error!")

bot.infinity_polling()

