# bot_polling.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found! Please set it as an environment variable.")


# --- Welcome Message Function ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Main formatted text
    message_text = (
        "➡️ Mega : te1egram.me/megafolder\n\n"
        "➡️ Key : zu_4MYhVAtHfQ2n2FcOEiA\n\n"
        "Share the group 3 times to unlock your group"
    )

    # Inline buttons (under the text)
    keyboard = [
        [InlineKeyboardButton("Group To Unlock 🔒", url="https://te1egram.me/+1aBvGqO9TyYzMWQy")],
        [InlineKeyboardButton("Free Extracts 😊", url="te1egram.me/freeextracts")],
    ]
    inline_markup = InlineKeyboardMarkup(keyboard)

    # Send main message with inline buttons
    await update.message.reply_text(
        message_text,
        reply_markup=inline_markup,
        disable_web_page_preview=True
    )

    # Send plain “Main Menu” text below
    await update.message.reply_text(
        "🔝 Main Menu",
        disable_web_page_preview=True
    )


# --- Handle any normal text by showing the menu again ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


# --- Main function ---
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
