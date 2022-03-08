#Copyright ©️ 2021-2022 Rendy. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [BotStatus Telegram bot by Rendy] (https://github.com/Randi356/Powerfull-BotStatus)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/Randi356/Powerfull-BotStatus/blob/master/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_rencprx():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_rencprx = f"📊 **<u>LIVE BOT STATUS</u>**\n\n**💬 {CHANNEL_OR_GROUP_TYPE}**: {CHANNEL_OR_GROUP_NAME}"
                for bot in BOT_LIST:
                    try:
                        yyy_rencprx = await app.send_message(bot, "/start")
                        aaa = yyy_rencprx.message_id
                        await asyncio.sleep(10)
                        zzz_rencprx = await app.get_history(bot, limit = 1)
                        for ccc in zzz_xsvshacker:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xxx_rencprx += f"\n\n🤖 **BOT**: @{bot}\n🔴 **STATUS**: down ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            xxx_rencprx += f"\n\n🤖 **BOT**: @{bot}\n🟢 **STATUS**: alive ✅"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_rencprx += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n<i>♻️ Updates every 45min - Powered by Powerful Bot Status</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_xsvshacker)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(2700)
                        
app.run(main_rencprx())

#Copyright ©️ 2021-2022 rendy. All Rights Reserved
