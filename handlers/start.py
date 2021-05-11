# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
          f"""<b>Haii.. {message.from_user.first_name} Aku adalah 𓊈one-heart music𓊉\n
𝘈𝘒𝘜 𝘈𝘋𝘈𝘓𝘈𝘏 𝘉𝘖𝘛 𝘔𝘜𝘚𝘐𝘒 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔 𝘠𝘈𝘕𝘎 𝘋𝘐 𝘒𝘌𝘔𝘉𝘈𝘕𝘎𝘒𝘈𝘕 𝘖𝘓𝘌𝘏 :  [Ikyy](https://t.me/boyfriendnice)
𝘈𝘗𝘈𝘉𝘐𝘓𝘈 𝘐𝘕𝘎𝘐𝘕 𝘔𝘌𝘕𝘎𝘎𝘜𝘕𝘈𝘒𝘈𝘕 𝘈𝘒𝘜 𝘐𝘕𝘝𝘐𝘛𝘌 𝘈𝘒𝘜 𝘋𝘈𝘕 𝘈𝘚𝘐𝘚𝘚𝘛𝘈𝘕𝘛 𝘕𝘠𝘈 𝘓𝘈𝘓𝘜 𝘑𝘈𝘋𝘐𝘒𝘈𝘕 𝘈𝘋𝘔𝘐𝘕 𝘒𝘌𝘋𝘜𝘈𝘕𝘠𝘈 𝘈𝘎𝘈𝘙 𝘉𝘐𝘚𝘈 𝘉𝘌𝘙𝘑𝘈𝘓𝘈𝘕 𝘋𝘌𝘕𝘎𝘈𝘕 𝘓𝘈𝘕𝘊𝘈𝘙,𝘑𝘐𝘒𝘈 𝘈𝘋𝘈 𝘒𝘌𝘕𝘋𝘈𝘓𝘈 𝘉𝘐𝘚𝘈 𝘊𝘏𝘈𝘛 𝘖𝘞𝘕𝘌𝘙𝘕𝘠𝘈.
┏━━━━━━━━━━━━━━
┣ > 𝙹𝙰𝙽𝙶𝙰𝙽 𝙻𝙸𝚂𝚃 𝙻𝙰𝙶𝚄 𝚂𝙴𝙺𝙰𝙻𝙸𝙶𝚄𝚂 𝚃𝙰𝙺𝚄𝚃 𝙴𝚁𝙾𝚁.
┣ > 𝙹𝙸𝙺𝙰 𝙷𝙰𝙱𝙸𝚂 𝙳𝙸𝙼𝙰𝚃𝙸𝙺𝙰𝙽 𝙿𝙰𝙺𝚂𝙰 𝙹𝙰𝙽𝙶𝙰𝙽 
    𝙻𝙰𝙽𝙶𝚂𝚄𝙽𝙶 𝙿𝙻𝙰𝚈 𝙻𝙰𝙶𝚄 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙴𝙱𝙴𝙽𝚃𝙰𝚁 
    𝙹𝙸𝙺𝙰 𝚃𝙸𝙳𝙰𝙺, 𝙰𝚂𝙸𝚂𝚃𝙴𝙽 𝚃𝙸𝙳𝙰𝙺 𝙰𝙺𝙰𝙽 𝙽𝙰𝙸𝙺.
┗━━━━━━━━━━━━━━
🤵𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓫𝔂 : [Ikyy](https://t.me/boyfriendnice)
☘️𝓣𝓱𝓪𝓷𝓴𝓼 𝓯𝓸𝓻 : [Grup Support](https://t.me/remaja_virtual62)
━━━━━━━━━━━━━━
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/boyfriendnice")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/remaja_virtual62"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/chvirtual62"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar musik sedang online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/remaja_virtual62"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/boyfriendnice"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar musik sedang online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/remaja_virtual62"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/boyfriendnice"
                    )
                ]
            ]
        )
   )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Panduan menggunakan bot", url="https://t.me/MusikVcgChannel/3"
                    )
                ]
            ]
        ),
    )
