# Credit DaisyXMusic, Changes By UserLazy, Improve Code By UserLazy

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from callsmusic.callsmusic import client as USER
from config import SUDO_USERS

@Client.on_message(filters.command(["katil","katil@jestermusicbot"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>önce beni admin olarak ekle</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "@jesterasistan"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"<b>{user.first_name} Bu Gruba şimdiden katılır</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Flood Wait Error\n{user.first_name}, userbot için çok sayıda katılma isteği nedeniyle grubunuza katılamıyor! Kullanıcının grupta yasaklanmadığından emin olun."
            "\n\nVeya Asistan botunu Grubunuza manuel olarak ekleyin ve tekrar deneyin.</b>",
        )

        return
    await message.reply_text(
        f"<b>{user.first_name} Başarıyla Katıldı</b>",
    )


@USER.on_message(filters.group & filters.command (["ayril","ayril@jestermusicbot"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Kullanıcılar grubunuzdan ayrılamaz! Muhtemelen sel bekliyor."
            "\n\nYa da beni Grubunuzdan manuel olarak çıkarın</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left=0
    failed=0
    lol = await message.reply("**Asisten Meninggalkan semua obrolan**")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
        except:
            failed += 1
            await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["katilkanal","katilkanal@jestermusicbot"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("bağlı mısın?")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Önce beni Admin olarak ekle</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "@jesterasistan"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"<b>{user.first_name} zaten kanalınızda</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>Flood Wait Error\n{user.first_name} userbot için çok sayıda katılma isteği nedeniyle grubunuza katılamıyor! Kullanıcının grupta yasaklanmadığından emin olun."
            "\n\nYa da Asistan botunu Grubunuza manuel olarak ekleyin ve tekrar deneyin.</b>",
        )
        return
    await message.reply_text(
        f"<b>{user.first_name} sohbetinize zaten katıldı</b>",
    )
