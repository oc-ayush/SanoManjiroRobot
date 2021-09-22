import requests
from Mikey import dispatcher
from Mikey.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


@run_async
def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len('/ud '):]
    if text == "simp":
      message.reply_text("simp\n\nSomeone who puts the hoes before the bros, simps will do or say anything to please someone, particularly a girl, in the hopes that they will be in gain favor with that person.\n\n<i>Today adc was too peaceful, simp [_chirag_] was offline</i>\n<i>Heyy you know the [owner of adc], he's a big [simp]</i>", parse_mode = ParseMode.HTML)
      return
    results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud)

dispatcher.add_handler(UD_HANDLER)

__command_list__ = ["ud"]
__handlers__ = [UD_HANDLER]
