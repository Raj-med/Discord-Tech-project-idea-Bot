# Discord-Tech-project-idea-Bot
A  Discord bot that provides random tech project ideas and includes a daily request limit for each user.

![](https://github.com/Raj-med/Discord-Tech-project-idea-Bot/blob/main/ezgif-1-d3debed2c8.gif)

## Features
Greeting Message: When a user says "hi", "hello", "hey", or "hola", the bot responds with instructions on how to get tech project ideas.
Tech Project Ideas: Users can request a random tech project idea by typing !idea.
Rate Limiting: Each user can make up to 25 requests per day.
Daily Reset: Request counts are reset daily at midnight UTC.
Help Command: Provides information on how to use the bot.

### Installation
Clone the Repository:


git clone[ https://github.com/yourusername/tech-project-idea-bot.git](https://github.com/Raj-med/Discord-Tech-project-idea-Bot.git)
cd tech-project-idea-bot


#### Install Dependencies:
Make sure you have Python 3.8 or higher installed. Then, install the required libraries using pip:


pip install discord apscheduler
##### Setup:

Replace "YOUR_DISCORD_BOT_TOKEN" in client.run("YOUR_DISCORD_BOT_TOKEN") with your actual Discord bot token.
Running the Bot
###### Start the bot using Python:


python bot.py
###### Commands
!idea: Get a random tech project idea (25 requests per day).
!help: Display help information.
######## Notes
Make sure your bot has permission to read and send messages in the channels where it will be used.
The bot uses the apscheduler library to reset the request counts daily at midnight UTC.
####### License
MIT
This project is licensed under the MIT License - see the LICENSE file for details.

######## Contact
For questions or suggestions, please open an issue on the GitHub repository.
