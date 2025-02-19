import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import config  # Importa il file con le credenziali
import os


# Logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Ciao! Sono il tuo bot.")

# Comando /reboot (solo per un utente specifico)
async def reboot(update: Update, context: CallbackContext):
    if update.message.from_user.username == config.AUTHORIZED_USER:
        await update.message.reply_text("Riavvio in corso...")
        os.system("sudo reboot")
    else:
        await update.message.reply_text("Non sei autorizzato a riavviare il server.")

# Avvio del bot
def main():
    app = Application.builder().token(config.TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reboot", reboot))

    logging.info("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
