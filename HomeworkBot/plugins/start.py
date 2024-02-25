# // @RiotOreo //
from .. import RiotOreo
from telethon import events, Button

@RiotOreo.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/riotoreo")],
                        [Button.inline("Inline Button",data="example")]
                    ])

@RiotOreo.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
