from .. import BotzHub
from telethon import events

@BotzHub.on(events.NewMessage(pattern="/skip"))
async def oommkkj(event):
  await BotzHub.send_message(event.chat_id, "**jana lwde**")
