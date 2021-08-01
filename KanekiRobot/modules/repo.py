from pyrogram import filters
from KanekiRobot import pbot as app
from KanekiRobot.utils.errors import capture_err
from KanekiRobot.utils.http import get


@app.on_message(filters.command("repo") & ~filters.edited)
@capture_err
async def repo(_, message):
    users = await get(
        "https://api.github.com/repos/rizkyoye/Kaneki-robot/contributors"
    )
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (
            f"**{count}.** [{user['login']}]({user['html_url']})\n"
        )
        count += 1

    text = f"""[Bot](https://t.me/kanekiexbot) | [Support](https://t.me/kanekisupport)
```----------------
| Contributors |
----------------```
{list_of_users}
buttons = [
        [
        InlineKeyboardButton(
            text="💾Repository", url="https://github.com/rizkyoye/Kaneki-robot"),
    ],"""
    await app.send_message(
        message.chat.id, text=text, disable_web_page_preview=True
    )
