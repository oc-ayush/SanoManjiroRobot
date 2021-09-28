import html

from Mikey.modules.disable import (DisableAbleCommandHandler, DisableAbleMessageHandler) 
from Mikey import (LOGGER, DRAGONS, TIGERS, WOLVES, dispatcher)
from Mikey.modules.helper_funcs.chat_status import (user_admin,
                                                           user_not_admin)
from Mikey.modules.log_channel import loggable
from Mikey.modules.sql import req_channel_sql as sql
from telegram import (Chat, InlineKeyboardButton, InlineKeyboardMarkup,
                      ParseMode, Update)
from telegram.error import BadRequest, Unauthorized
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          Filters, MessageHandler, run_async)
from telegram.utils.helpers import mention_html

NOTIF_GROUP = 12
REPORT_IMMUNE_USERS = DRAGONS + TIGERS + WOLVES

@run_async
@user_admin
def setreq(update: Update, context: CallbackContext):
  bot = context.bot
  message = update.effective_message
  chat = update.effective_chat
  if chat.type == chat.CHANNEL:
    message.reply_text("Now, forward the /setreq to the group you want to tie this channel to!")
  elif message.forward_from_chat:
    sql.set_chat_req_channel(chat.id, message.forward_from_chat.id)
    try:
      message.delete()
    except BadRequest as excp:
      if excp.message == "Message to delete not found":
        pass
      else:
        LOGGER.exception("Error deleting message in log channel. Should work anyway though.")
    try:
      bot.send_message(message.forward_from_chat.id, f"This channel has been set as the requests logger channel for {chat.title or chat.first_name}.")
    except Unauthorized as excp:
      if excp.message == "Forbidden: bot is not a member of the channel chat":
          bot.send_message(chat.id, "Successfully set requests logs channel!")
      else:
        LOGGER.exception("ERROR in setting the log channel.")
    bot.send_message(chat.id, "Successfully set requests log channel!")
  else:
    message.reply_text("The steps to set a request log channel are:\n"
                               " - add bot to the desired channel\n"
                               " - send /setlog to the channel\n"
                               " - forward the /setlog to the group\n")



@run_async 
def req(update: Update, context: CallbackContext):
  bot = context.bot 
  message =update.effective_message
  ms = message.reply_to_message
  user = update.effective_user 
  chat = update.effective_chat 
  if not sql.get_chat_req_channel(chat.id):
    return
  message_id = update.effective_message.message_id
  if message.text.startswith("/req"):
    pass
  elif message.text.startswith("#"):
    mse = message.text.split(None, 1)
    rig = mse[0]
    if rig == "#request":
      pass
    else:
      print("Called by # but was not #req")
      return
  if message.reply_to_message:
    kek = message.reply_to_message
    if message.reply_to_message.caption:
      argue = message.reply_to_message.caption.split(None, 1)
    else:
      argue = message.reply_to_message.text.split(None, 1)
  else:
    kek = message 
    argue = message.text.split(None, 1)
  if len(argue) >= 2:
    args = argue[1]
  else:
    args = "None"
  
  if chat:
        msg = update.effective_message
        if msg.reply_to_message:
          req_user = msg.reply_to_message.from_user
        else:
          req_user = user
        chat_name = chat.title or chat.first or chat.username
        admin_list = chat.get_administrators()
        message = kek

        if args == "None":
            message.reply_text("Request something!!")
            return "" 
        if chat and chat.type == Chat.SUPERGROUP:
          requested = "Request accepted!!" 
          msg = f"<b>{html.escape(chat.title)}</b>\n<b>Requested: </b> {args}\n<b>Requesting User:</b> {mention_html(req_user.id, req_user.first_name)}"
          if chat.username:
            link = f'\n<b> </b> <a href="https://t.me/{chat.username}/{message.message_id}">.......</a>'
          else:
            link = " "
        if sql.get_chat_req_channel(chat.id):
            bot.send_message(sql.get_chat_req_channel(chat.id), msg + link, parse_mode = ParseMode.HTML)
        else:
            bot.send_message(chat.id, "Req Channel Not set!" )

        message.reply_text("Request Accepted!!") 
        return msg

        return ""  
  
REQU_HANDLER = DisableAbleCommandHandler ("request", req) 
REQ_HANDLER = DisableAbleMessageHandler(Filters.regex(r"^#[^\s]+"), req, friendly="request")
SET_HANDLER = DisableAbleCommandHandler("setreq", setreq)
 
#dispatcher.add_handler(REQU_HANDLER, NOTIF_GROUP)
dispatcher.add_handler(SET_HANDLER)
#dispatcher.add_handler(REQ_HANDLER, NOTIF_GROUP)
            
          
