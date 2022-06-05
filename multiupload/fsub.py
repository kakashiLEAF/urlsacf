'''MultiUpload, An Telegram Bot Project
Copyright (c) 2021 Anjana Madu and Amarnath CDJ <https://github.com/AnjanaMadu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>'''

import os
import asyncio, random
from telethon import events, Button
from multiupload import anjana
from telethon.tl.functions.channels import GetParticipantRequest as p
from telethon.errors import UserNotParticipantError

async def check_participant(user_id, chat_id, reply_id, cb=False):
	try:
		await anjana(p(chat_id, user_id))
		return True
	except:
		if not cb:
			await anjana.send_message(user_id, '**You are not joined to my update channel. Please join to my update channel and start me again 👀**', buttons=[
				Button.url('Join Now!', f't.me/{os.environ.get("CHNLUSRNME")}'),
				Button.inline('Check', data='chk')
			], reply_to=reply_id)
		return False

s = ["CAADBAADxgkAAjQF0VL5yl4Td0utTgI",
	"CAADBAADoAsAAv3iYFGE3u_w4y_1zgI",
	"CAADBAADMggAAq0Q0FK1ZIUPLNxGcAI",
	"CAADBAAD7AoAAr8i2VGALarwosnJIgI",
	"CAADBAADrQoAAmzO0VFDq1aGz7rGHgI",
	"CAADBAADbQgAAhI40VH51AABGZuwl74C"]

@anjana.on(events.CallbackQuery(pattern='chk'))
async def _(event):
	try:
		await anjana(p(f'@{os.environ.get("CHNLUSRNME")}', event.sender_id))
	except:
		await event.answer("💬 You are not Join. Please Join to Channel.", alert=True)
	else:
		await event.answer("💬 Thanks for Supporting.", alert=True)
		await event.delete()
		await anjana.send_file(event.chat_id, random.choice(s), reply_to=event)
		await event.reply(f"Hey [{xx.first_name}]({xx.id}), I am **MultiUploader** bot by **KAKASHI** leaf", buttons=[
				Button.url('Support Chat 💭', 't.me/LEGEND_BOT_update')
			])
