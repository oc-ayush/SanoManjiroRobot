import threading

from Mikey.modules.sql import BASE, SESSION
from sqlalchemy import Column, String


class Lewds(BASE):
    __tablename__ = "lewdtruechats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Lewds.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()


def is_nsfw_false(chat_id): 
  try:
    chat = SESSION.query(Lewds).get(str(chat_id))
    if chat:
      return True
    else:
      return False 
  finally:
    SESSION.close()

def set_false(chat_id):
  with INSERTION_LOCK:
    lewdfalse = SESSION.query(Lewds).get(str(chat_id))
    if not lewdfalse:
      lewdfalse = Lewds(str(chat_id))
    else:
      pass
    SESSION.add(lewdfalse)
    SESSION.commit()

def set_true(chat_id):
  with INSERTION_LOCK:
   lewdfalse = SESSION.query(Lewds).get(str(chat_id))
   if lewdfalse:
     SESSION.delete(lewdfalse)
   SESSION.commit()

def get_nsfw_false(chat_id):
  try:
    return SESSION.query(Lewds.chat_id).all()
  finally:
    SESSION.close()



