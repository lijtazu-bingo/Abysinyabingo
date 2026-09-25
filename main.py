import os
import telebot

# 🤖 የቦት ቶከን ማዋቀሪያ
TOKEN = os.getenv(''8019235278:AAFkH3vjc4YDSqHC-_SE4QMwFQgfjacyvCA
bot = telebot.TeleBot(TOKEN)

# 🔗 ያንተ የረንደር ቋሚ የቢንጎ ጨዋታ መድረሻ ሊንክ
SERVER_URL = "https://onrender.com"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_play = telebot.types.KeyboardButton("🎰 PLAY BINGO")
    markup.add(btn_play)
    bot.send_message(message.chat.id, "እንኳን ወደ አቢሲኒያ ቢንጎ በደህና መጡ✅\nቢንጎ ለመጫወት ከታች ያለውን ቁልፍ ይጫኑ👇", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["🎰 PLAY BINGO", "🎮 ቢንጎ ይግቡ"])
def play_bingo_logic(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # 🎯 ይህ ቁልፍ ነው የ 1-400 ላቬንደር ገጹን ቴሌግራም ውስጥ በቀጥታ (Directly) የሚሰብረው
    btn_web = telebot.types.InlineKeyboardButton(
        text="🎮 ቢንጎ ይግቡ (ጨዋታውን ክፈት)", 
        web_app=telebot.types.WebAppInfo(url=SERVER_URL)
    )
    markup.add(btn_web)
    bot.send_message(message.chat.id, "የካርቴላ መምረጫ ገጹን ለመክፈት ከታች ያለውን ሰማያዊ ቁልፍ ይጫኑ፡", reply_markup=markup)

if __name__ == '__main__':
    print("ቦቱ መስራት ጀምሯል...")
    bot.infinity_polling()
