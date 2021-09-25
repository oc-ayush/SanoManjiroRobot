from Mikey.modules.helper_funcs.chat_status import user_admin
from Mikey.modules.disable import DisableAbleCommandHandler
import os
import random2 as rdn
import json
import requests 
from Mikey import dispatcher
from telegraph import upload_file as nyah
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ParseMode, Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, Filters, CommandHandler

MARKDOWN_HELP = f"""
Markdown is a very powerful formatting tool supported by telegram. {dispatcher.bot.first_name} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

• <code>_italic_</code>: wrapping text with '_' will produce italic text
• <code>*bold*</code>: wrapping text with '*' will produce bold text
• <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
• <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
<b>Example:</b><code>[test](example.com)</code>

• <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
<b>Example:</b> <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.

Keep in mind that your message <b>MUST</b> contain some text other than just a button!
"""

@run_async
def upload_telegraph(update: Update, context: CallbackContext):
  bot = context.bot 
  msg = update.effective_message 
  user = update.effective_user 
  chat = update.effective_chat 
  reply = msg.reply_to_message
  bot.send_chat_action(chat.id, action='typing')
  if reply:
    if reply.photo:
      file = bot.get_file(reply.photo[-1].file_id)
      dl = file.download("nepo.jpg")
      kek = nyah(dl)
      link = f"https://telegra.ph{kek[0]}"
      msg.reply_text(f"*Your Link:* \n\n `{link}`", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text ="Go! Check it!", url = link)]]), parse_mode = ParseMode.MARKDOWN)
      os.remove("nepo.jpg")
    elif reply.animation:
      file = bot.get_file(reply.animation.file_id)
      dl = file.download("nepo.mp4")
      kek = nyah(dl)
      link = f"https://telegra.ph{kek[0]}"
      msg.reply_text(f"*Your Link:* \n\n `{link} `", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text ="Go! Check it!", url = link)]]), parse_mode = ParseMode.MARKDOWN)
      os.remove("nepo.mp4")
    elif reply.video:
      if reply.video.file_size <= 4194304:
        file = bot.get_file(reply.video.file_id)
        dl = file.download("nwp.mp4")
        kek = nyah(dl)
        link = f"https://telegra.ph{kek[0]}"
        msg.reply_text(f"*Your Link:* \n\n `{link}`", reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text =" Go! Check it!", url = link)]]), parse_mode = ParseMode.MARKDOWN)
        os.remove("nwp.mp4")
      else:
        msg.reply_text("_Nyo_ videos bigger than 4mb supported!!", parse_mode = ParseMode.MARKDOWN)
    else:
      msg.reply_text("Ahh, its works on, image, gifs, and videos shorter than 4mb", parse_mode = ParseMode.MARKDOWN)
      
@run_async 
def gifufinder(update: Update, context: CallbackContext):
  bot = context.bot 
  args = context.args 
  msg = update.effective_message 
  chat = update.effective_chat 
  user = update.effective_user 
  apikey = str(GIF_API)
  if apikey == "None": 
    return msg.reply_text("Gif api not set!!")
  lmt = 30
  if args:
    search_term = args
  else:
    msg.reply_text(f"Gimme something to search {user.first_name}")
    return 
  r = requests.get(
    "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
  if r.status_code == 200:
    bot.send_chat_action(chat.id, action ="upload_video")
    toper= json.loads(r.content) 
    top = toper.get('results')
    med = rdn.choice(top)
    gif = med['media'][0]['mp4']['url'] 
    bot.send_animation(chat.id, animation = gif, reply_to_message_id = msg.message_id) 
  else:
    msg.reply_text("Looks Like api is down.., Gomenasai!!")
     
@run_async
@user_admin
def echo(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            args[1], parse_mode="MARKDOWN", disable_web_page_preview=True)
    else:
        message.reply_text(
            args[1],
            quote=False,
            parse_mode="MARKDOWN",
            disable_web_page_preview=True)
    message.delete()


def markdown_help_sender(update: Update):
    update.effective_message.reply_text(
        MARKDOWN_HELP, parse_mode=ParseMode.HTML)
    update.effective_message.reply_text(
        "Try forwarding the following message to me, and you'll see, and Use #test!"
    )
    update.effective_message.reply_text(
        "/save test This is a markdown test. _italics_, *bold*, code, "
        "[URL](example.com) [button](buttonurl:github.com) "
        "[button2](buttonurl://google.com:same)")


@run_async
def markdown_help(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        update.effective_message.reply_text(
            'Contact me in pm',
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "Markdown help",
                    url=f"t.me/{context.bot.username}?start=markdownhelp")
            ]]))
        return
    markdown_help_sender(update)


__help__ = """
*Available commands:*
*Markdown:*
 • `/markdownhelp`*:* quick summary of how markdown works in telegram - can only be called in private chats
*Paste:*
 • `/paste`*:* Saves replied content to `nekobin.com` and replies with a url
*React:*
 • `/react`*:* Reacts with a random reaction 
*Urban Dictonary:*
 • `/ud <word>`*:* Type the word or expression you want to search use
*Wikipedia:*
 • `/wiki <query>`*:* wikipedia your query
*Wallpapers:*
 • `/wall <query>`*:* get a wallpaper from wall.alphacoders.com
*Currency converter:* 
 • `/cash`*:* currency converter
Example:
 `/cash 1 USD INR`  
      _OR_
 `/cash 1 usd inr`
Output: `1.0 USD = 75.505 INR`
"""

ECHO_HANDLER = DisableAbleCommandHandler("echo", echo, filters=Filters.group)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help)
TM_HANDLER = DisableAbleCommandHandler("tm", upload_telegraph)
GIF_HANDLER = DisableAbleCommandHandler("gif", gifufinder)

dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)
dispatcher.add_handler(TM_HANDLER)
dispatcher.add_handler(GIF_HANDLER)

__mod_name__ = "Extras"
__command_list__ = ["id", "echo", "tm"]
__handlers__ = [
    ECHO_HANDLER,
    MD_HELP_HANDLER,
]
