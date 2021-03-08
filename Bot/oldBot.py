"""import types
from telebot import telebot

bot = telebot.TeleBot("1331725231:AAFeXIFblqd6pE-Fdfbr3V0v3NPwSzuaCQA")
non = "488764861"
@bot.message_handler(commands=["start"])
def welcome(message):
        markup = types.InlineKeyboardMarkup(3)
        butt1 = types.InlineKeyboardButton("Ցույց տալ օրինակները", callback_data="1")
        butt2 = types.InlineKeyboardButton("Հիմնականում տրվող հարցեր", callback_data="2")
        markup.add(butt1)
        markup.add(butt2)
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=4)
        butt=types.KeyboardButton("/addorder")
        markup1.add(butt)
        bot.send_message(message.chat.id, ":wave:Ողջու՛յն։ Ուզու՞մ ես յուրահատուկ նկար ձեռք բերել կամ նվիրել որևէ մեկին։" +
                                           "\n" + ":heart_eyes: Դու ճիշտ հասցեով ես եկել։" , reply_markup=markup)
        bot.send_message(message.chat.id,":grin:Մանրամասների համար սեղմիր կոճակներից որևէ մեկը :point_up_2:", reply_markup=markup1)

@bot.message_handler(commands=["addorder"])
def order(message):
        markup1 = types.InlineKeyboardMarkup(3)
        butt1 = types.InlineKeyboardButton("Ավելացնել ինֆորմացիա ձեր մասին", callback_data="3")
        butt2 = types.InlineKeyboardButton("Ավելացնել նկար🖼", callback_data="4")
        markup1.add(butt1)
        markup1.add(butt2)
        bot.send_message(message.chat.id, "Ընտրեք", reply_markup=markup1)

@bot.callback_query_handler(func=lambda call:True)
def inline(call):
        if call.data == "1":
            markup = types.InlineKeyboardMarkup(3)
            butt2 = types.InlineKeyboardButton("Հիմնականում տրվող հարցեր", callback_data="2")
            markup.add(butt2)
            img1 = open("/home/Parciffal/.local/photo/2.jpg","rb")
            img2 = open("/home/Parciffal/.local/photo/3.jpg", "rb")
            img3 = open("/home/Parciffal/.local/photo/4.jpg", "rb")
            img4 = open("/home/Parciffal/.local/photo/5.jpg", "rb")
            img5 = open("/home/Parciffal/.local/photo/6.jpg", "rb")
            img6 = open("/home/Parciffal/.local/photo/7.jpg", "rb")
            img7 = open("/home/Parciffal/.local/photo/8.jpg", "rb")
            bot.send_message(call.message.chat.id, "🧞♂Cartoon")
            bot.send_photo(call.message.chat.id,img1)
            bot.send_message(call.message.chat.id, "Ուզու՞մ ես դառնալ մուլտհերոս։🤪" + "\n" +
                             "Ուղարկի՛ր նկարդ։ :inbox_tray:" + "\n" + "Նշի՛ր ինչ չափի նկար ես ուզում։ "
                                                                      ":triangular_ruler:" + "\n" + "(A2 - 13000դր , A3-10000դր , A4-7000դր🖨)" +
                             "\n" + "Միայն նկարը օնլայն տարբերակով 6000 դրամ։:computer:")
            bot.send_message(call.message.chat.id, "🦋 Abstraction")
            bot.send_media_group(call.message.chat.id, (types.InputMediaPhoto(img2), types.InputMediaPhoto(img3), types.InputMediaPhoto(img4)))
            bot.send_message(call.message.chat.id, "Աբստրակտ նկարները ինտերիերի լավ մաս կարող են դառնալ։ 🤩" + "\n" +
                             "Ուղարկի՛ր նկարներ:inbox_tray:,որոնք կցանքանաս աբստրակտ տարբերակով տեսնել" +
                             "\n" "կամ պարզապես այդ ոճի նկարների օրինակներ, և մենք կստեղծենք քոնը։" + "\n" + " :wink:(A2 - 13000դր , A3-10000դր , A4-7000դր🖨)"
                             + "\n" + "Միայն նկարը օնլայն տարբերակով 6000 դրամ։:computer:")
            bot.send_message(call.message.chat.id, ":pencil2: Sketch")
            bot.send_media_group(call.message.chat.id, [types.InputMediaPhoto(img5), types.InputMediaPhoto(img6), types.InputMediaPhoto(img7)])
            bot.send_message(call.message.chat.id, "Յուրահատուկ դիմանկարներ գծային՝ սկետչ տարբերակով։:pencil2:" + "\n"
                             + "Լա՛վ ընտրություն։:heart_eyes:" + "\n" + "Ուղարկի՛ր ցանկացած նկար։(A2 - 13000դր , A3-10000դր , A4-7000դր🖨)"
                             + "\n" + "Միայն նկարը օնլայն տարբերակով 6000 դրամ։:computer:",reply_markup=markup)
        elif call.data == "2":
            markup = types.InlineKeyboardMarkup(3)
            butt1 = types.InlineKeyboardButton("Ցույց տալ օրինակները", callback_data="1")
            buttom = types.InlineKeyboardButton("Ուղարկեք ձեր հարցը", callback_data="5")
            markup.add(buttom)
            markup.add(butt1)
            bot.send_message(call.message.chat.id, "Հիմնականում տրվող հարցեր" + "\n" + " :mag: Կնկարագրեք ձեր աշխատանքը")
            bot.send_message(call.message.chat.id, "Օրիգինալ նվեր կամ պարզապես զվարճանք։ 🤪" + "\n" +
                             "Մենք առաջարկում ենք Ձեզ տարբեր տեսակի և ոճի նկարների ստեղծում։" +
                             "\n" + "Դուք ուղարկում եք Ձեր նկարները,մենք՝ ստեղծում նորը։ 🤩" + "\n"
                             + "Նկարները կարող են լինել օնլայն տարբերակով և տպագրված։" + "\n"
                             + "Սկզբից կստանաք նամակ պատվերը ընդունելու մասին" +
                             "\n" + "Հետո միջանկյալ նկար եվ նամակ աշխատանքի մասին" +
                             "\n" + "Վերջում նկարը online կամ offline տարբերակներով:")
            bot.send_message(call.message.chat.id, " :mag: Ինչ որակի կարողեն լինել նկարները" +
                                                    "\n" + "Նկարները պետք է լինեն լավ որակի։"
                                                     + "\n" + "Արժեք:money_with_wings:?")
            bot.send_message(call.message.chat.id, "Օնլայն տարբերակ:computer: _ 6000֏" + "A4 տպագրություն 🖨_ 7000֏"
                             + "\n" + "A3 տպագրություն 🖨_ 10000֏" + "\n" + "A2 տպագրություն🖨 _ 13000֏")
            bot.send_message(call.message.chat.id, " :mag: Ինչպես կարողենք կապնվել ձեր հետ?")
            bot.send_message(call.message.chat.id, "Նկարի պատրաստ լինելու դեպքում,մենք կկապնվենք Ձեր հետ։", reply_markup=markup)
        elif call.data == "3":
            bot.send_message(call.message.chat.id,"Գրեք ձեր անունը,ազգանունը,հեռախոսի համարը "+"\n"+
                                                    "ինչ ոճի նկար եք ուզում եվ տարբերակը"+"\n"+"Օրինակ»Արամ Սարգսյան ,0**-**-**-**,sketch,A2")
            @bot.message_handler(content_types="Text")
            def info_mess(message):
                info = message.text
                print(info)
                bot.send_message(non, info + "id:" + str(message.chat.id))
        elif call.data == "4":
             bot.send_message(call.message.chat.id,"Ավելացնել նկար")
             @bot.message_handler(content_types=['document'])
             def handle_docs_photo(message):
                 file_info = bot.get_file(message.document.file_id)
                 downloaded_file = bot.download_file(file_info.file_path)
                 src = '/home/Parciffal/.local/photo/getted/'+str(message.document.file_name)+"id"+str(message.chat.id)+".png" with open(src, 'wb') as new_file: new_file.write(downloaded_file)
                 img0=open('/home/Parciffal/.local/photo/getted/' +str(message.document.file_name)+"id"+str(message.chat.id)+".png","rb")
                 bot.send_photo(non,img0)
        elif call.data == "5":
             @bot.message_handler(content_types="Text")
             def info_mess(message):
                 info = message.text
                 bot.send_message(non,info)


"""