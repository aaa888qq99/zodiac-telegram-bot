from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
zodiacs = ["牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座",
           "天秤座", "天蠍座", "射手座", "摩羯座", "水瓶座", "雙魚座"]

def get_horoscope(zodiac):
    stars = ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆", "★★★★☆", "★★★★★"]
    return f"✨ {zodiac} 今日運勢：\n愛情運：{random.choice(stars)}\n事業運：{random.choice(stars)}\n財運：{random.choice(stars)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("請輸入 /運勢 星座名稱，例如：/運勢 處女座")

async def horoscope(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or context.args[0] not in zodiacs:
        await update.message.reply_text("請輸入正確的星座名稱")
    else:
        await update.message.reply_text(get_horoscope(context.args[0]))

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("運勢", horoscope))
    app.run_polling()
