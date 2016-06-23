# Bot-Telegram-CDPC
Telegram Bot programmed in Python3 for a Barcelona programming club.

This bot has four commands:

/start --> This command is the first command executed. It's used to save the user's ID to the user's file.

/assitir --> This command is used by a student to communicate to the admin (someone of the club) that he'll come to class.

/absencia --> This command is used by a student to communicate to the admin (someone of the club) that he won't come to class.

/contacta --> This command is used by a student to communicate something to the club and by an admin (someone of the club) to send a message to everybody of the user's file.

## Libraries needed:
- pyTelegramBotAPI (telebot)
- time 

## How to start:
You'll need to register a bot using @BotFather in Telegram. This bot will give you the token required to make the code work. You'll need to register the commands too in @BotFather using the command /setcommands. Don't forget to enter the admin's ID in the var, because if you don't introduce the admin's ID the code won't work.
