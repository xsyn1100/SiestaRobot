from SiestaRobot.modules.language import gs


def helps(chat):
    return gs(chat, "musicplayer_help")
  LUNA = "** ──「 Perintah Dasar 」── ** \n\n"
  LUNA += "• /play **(nama lagu / balas ke audio) — play musik via YouTube** \n"
  LUNA += "• /vplay ** (nama lagu / balas ke audio) – play video stream via YouTube** \n"
  LUNA += "• /playlist - **Untuk memutar playlist Anda atau playlist group anda** \n"
  LUNA += "• /song - ** (nama lagu) mendownload lagu via YouTube** \n\n"
  LUNA += "** ──「 Admin CMD 」── ** \n\n"
  LUNA += "• /music on|off - **mengaktifkan atau menonaktifkan music player di grup anda** \n"
  LUNA += "• /pause atau /vpause - **Untuk pause musik/video yang sedang di putar** \n"
  LUNA += "• /resume atau /vresume - **Untuk melanjutkan musik/video yang sedang ter pause** \n"
  LUNA += "• /skip - **Untuk melewati lagu berikutnya** \n"
  LUNA += "• /end - **Untuk memberhentikan pemutaran musik** \n"
  LUNA += "• /vstop - **Untuk memberhentikan video stream yang sedang diputar** \n"
  LUNA += "• /reload - **Untuk memperbarui admin list** \n"

  BUTTON = [[Button.url("Support", "https://t.me/synxupport"), Button.url("📡 Updates", "https://t.me/synxupdate")]]
  await tbot.send_file(event.chat_id, caption=LUNA,  buttons=BUTTON)

__mod_name__ = "Musicplayer"
