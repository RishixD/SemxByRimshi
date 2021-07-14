# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, custom, Button
SMEX_PIC = "https://telegra.ph/file/e9aa64297e9ffffd118ad.jpg"
@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await BotzHub.send_file(event.chat_id,
                                  SMEX_PIC,
                                  caption="ＨＥＬＬＯ  ＶＭＲＯ!!\n𝙸𝙼 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 @RiSHi_iNTROVERT \n𝙿𝚁𝙴𝚂𝚂 𝚃𝙷𝙴 𝙱𝙴𝙻𝙾𝚆 𝙱𝚄𝚃𝚃𝙾𝙽 𝚃𝙾 𝙺𝙽𝙾𝚆 𝙼𝙾𝚁𝙴 𝙰𝙱𝙾𝚄𝚃 𝚁𝙸𝚂𝙷𝙸",
                                  buttons=[
                                      (Button.inline(
                                          "plugins >>",
                                          data="mhelp"))]
                                  )

@BotzHub.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁's 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @RiSHi_iNTROVERT", show_alert=True)

########################################################################################################################################


@BotzHub.on(events.callbackquery.CallbackQuery(data="mhelp"))
async def ommmmk(event):
    await event.edit("HELP MENU",
                    buttons=[
                        [Button.inline("Master tool >>", data="ots")],
                        [Button.inline("tools", data="mhelpk")]
                    ])
                     
@BotzHub.on(events.callbackquery.CallbackQuery(data="ots"))
async def oppppppppp(event):
    await event.edit("•/skem to start smexing.\n•/stop to stop smex.\n•/alive to check bot is alive or not.")
    
@BotzHub.on(events.callbackquery.CallbackQuery(data="mhelpk"))
async def oooooookk(event):
    await event.edit("BEHEN KE LAUDE TERE LIYE NHI HAI YEH 😂😘")
