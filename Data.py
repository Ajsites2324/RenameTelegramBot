from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey Baby {}

Welcome to {} fantastic rename bot 

You can use me to rename documents and files with certain other features. Use `/help` to learn how !

┏❖ Bot created by 
┗ ☞@PAPA_BOL_SAKTEHO

┏❖ Feelings 
┗ ☞ @ABOUT_AJEET
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/About_AJEET")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/AJEET_BOTS")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/MODERN_ELEMENTS")],
    ]

    # Help Message
    HELP = """
Just send a document / video to start renaming. Then when asked, give the new name for the file. The bot will download the file and upload with new name.

1) To have a custom thumbnail on your file, add an 'jpg' image as thumbnail using /thumbnail command.
2) By default, videos are uploaded as videos. To prompt the bot to upload video as document, use /settings to change settings.

✨ **Available Commands** ✨

/thumbnail - Change thumbnail settings
/settings - Change default settings
/about - About The Bot
/help - This Message
/start - Start the Bot
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram rename bot by @ABOUT_AJEET

More bots : [Click Here](https://t.me/ajeet_bots)

Source Code : [Click Here](https://t.me/papa_bol_sakteho)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [𓆩〭⃛〬𓆩〭⃛〬➤⃝✖‿✖•Ajͥeeͣtͫ](https://t.me/papa_bol_sakteho)
    """
