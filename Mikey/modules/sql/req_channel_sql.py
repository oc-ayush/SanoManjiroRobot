import threading

from Mikey.modules.sql import BASE, SESSION
from sqlalchemy import Column, String, distinct, func


class ReqLogs(BASE):
    __tablename__ = "req_channels"
    chat_id = Column(String(14), primary_key=True)
    req_channel = Column(String(14), nullable=False)

    def __init__(self, chat_id, req_channel):
        self.chat_id = str(chat_id)
        self.req_channel = str(req_channel)


ReqLogs.__table__.create(checkfirst=True)

LOGS_INSERTION_LOCK = threading.RLock()

CHANNELS = {}


def set_chat_req_channel(chat_id, req_channel):
    with LOGS_INSERTION_LOCK:
        res = SESSION.query(ReqLogs).get(str(chat_id))
        if res:
            res.req_channel = req_channel
        else:
            res = ReqLogs(chat_id, req_channel)
            SESSION.add(res)

        CHANNELS[str(chat_id)] = req_channel
        SESSION.commit()


def get_chat_req_channel(chat_id):
    return CHANNELS.get(str(chat_id))


def stop_chat_logging(chat_id):
    with LOGS_INSERTION_LOCK:
        res = SESSION.query(ReqLogs).get(str(chat_id))
        if res:
            if str(chat_id) in CHANNELS:
                del CHANNELS[str(chat_id)]

            req_channel = res.req_channel
            req_channel = res.req_channel
            SESSION.delete(res)
            SESSION.commit()
            return req_channel


def num_logchannels():
    try:
        return SESSION.query(func.count(distinct(ReqLogs.chat_id))).scalar()
    finally:
        SESSION.close()


def migrate_chat(old_chat_id, new_chat_id):
    with LOGS_INSERTION_LOCK:
        chat = SESSION.query(ReqLogs).get(str(old_chat_id))
        if chat:
            chat.chat_id = str(new_chat_id)
            SESSION.add(chat)
            if str(old_chat_id) in CHANNELS:
                CHANNELS[str(new_chat_id)] = CHANNELS.get(str(old_chat_id))

        SESSION.commit()


def __load_req_channels():
    global CHANNELS
    try:
        all_chats = SESSION.query(ReqLogs).all()
        CHANNELS = {chat.chat_id: chat.req_channel for chat in all_chats}
    finally:
        SESSION.close()


__load_req_channels()
