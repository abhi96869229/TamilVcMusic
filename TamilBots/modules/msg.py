import os
from TamilBots.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I Am An Advanced Bot Created For Playing Music In The Voice Chats Of Telegram Groups & Channels.\n\n✅ Hits /help For More Info. Report 🐛 Bugs At : @TamilSupport."
      HELP_MSG = [
        ".",
f"""
**Hello, Welcome to {PROJECT_NAME}

⭕ I Can Play Music In Your Group's Voice Chat As Well As Channel Voice Chats.

⭕ Assistant: @{ASSISTANT_NAME}\n\nClick Next ➡️ for Instructions.**
""",

f"""
**Setting Up**

1) Make bot admin (Group and in channel if use cplay),
2) Start a voice chat,
3) Try /play `<song name>` for the first time by an admin,
 If Userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry.
 
**For Channel Music Play**
1) Make me admin of your channel,
2) Send /joinchannel in linked group,
3) Now send commands in linked group.

**Commands**

**=>> Song Playing 🎧**

- /play `<song name>`: Select the Given Below Keyboard,
- /play `<yt url>` : Play the given YouTube URL,
- /ytplay: Directly play song via YouTube Music,
- /dplay: Play song via deezer,
- /splay: Play song via jio saavn.

**=>> Playback ⏯**

- /player: Open Settings menu of player,
- /skip: Skips the current track,
- /pause: Pause track,
- /resume: Resumes the paused track,
- /end: Stops media playback,
- /current: Shows the current Playing track,
- /playlist: Shows playlist.

**Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.**
""",
        
f"""
**=>> Channel Music Play 👨‍🎤**

**⭕ For linked group admins only:**

- /cplay `<song name>`: Play song you requested,
- /cdplay `<song name>`: Play song you requested via deezer,
- /csplay `<song name>`: Play song you requested via jio saavn,
- /cplaylist: Show now playing list,
- /cccurrent: Show now playing,
- /cplayer: Open music player settings panel,
- /cpause: Pause song play,
- /cresume: Resume song play,
- /cskip: Play next song,
- /cend: Stop music play,
- /joinchannel: Invite assistant to your chat.

**Channel is also can be used instead of c** ( /cplay = /channelplay )

**⭕ If you donlt like to play in linked group:**

1) Get your channel ID,
2) Create a group with tittle: Channel Music: your_channel_id,
3) Add bot as Channel admin with full perms,
4) Add @{ASSISTANT_NAME} to the channel as an admin,
5) Simply send commands in your group.
""",

f"""
**=>> More tools 😬**

- /musicplayer `<on/off>`: Enable/Disable Music player,
- /reload: Updates admin info of your group. Try if bot isn't recognize admin,
- /join: Invite @{ASSISTANT_NAME} Userbot to your chat.

**=>> Commands for Sudo Users 👷**

 - /leaveall - Remove assistant from all chats,
 - /gcast `<reply to message>` - Globally brodcast replied message to all chats,
 - /pmpermit `<on/off>` - Enable/Disable PM Permit message.
**Sudo Users can execute any command in any groups.**

"""
      ]
