import discord
import random
from datetime import datetime, timedelta
from collections import defaultdict
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Initialize the client with the necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
client = discord.Client(intents=intents)

# Dictionary to keep track of user requests
user_requests = defaultdict(lambda: {'count': 0, 'reset_time': datetime.utcnow()})

# Function to reset request counts at midnight UTC
def reset_request_counts():
    for user_id in user_requests:
        user_requests[user_id]['count'] = 0
        user_requests[user_id]['reset_time'] = datetime.utcnow()

# Scheduler to reset counts daily
scheduler = AsyncIOScheduler()
scheduler.add_job(reset_request_counts, 'cron', hour=0, minute=0)
scheduler.start()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages from the bot itself

    user_id = message.author.id
    now = datetime.utcnow()
    
    # Reset the count if the reset time has passed
    if now >= user_requests[user_id]['reset_time']:
        user_requests[user_id]['count'] = 0
        user_requests[user_id]['reset_time'] = now + timedelta(days=1)

    # Check if the message is a greeting
    if message.content.lower() in ['hi', 'hello', 'hey', 'hola']:
        user_name = message.author.name
        await message.channel.send(
            f'Hello, {user_name}! I am a tech project generator app. '
            'Please type `!idea` to generate a tech project idea.'
        )

    # Command to get a random tech project idea with rate limiting
    elif message.content.startswith('!idea'):
        if user_requests[user_id]['count'] < 25:
            tech_ideas = [
                "Build a personal blog using a static site generator like Jekyll or Hugo.",
                "Create a weather app that fetches data from an API.",
                "Develop a simple to-do list application with user authentication.",
                "Set up a home automation system using a Raspberry Pi.",
                "Create a chatbot using natural language processing.",
                "Build a stock price tracker that sends alerts on significant changes.",
                "Develop a personal finance tracker app.",
                "Create a recipe app with a meal planner and shopping list features.",
                "Build a web scraper to collect data from a website.",
                "Develop a mobile app using Flutter or React Native."
            ]
            
            response = random.choice(tech_ideas)
            await message.channel.send(response)
            
            user_requests[user_id]['count'] += 1
        else:
            await message.channel.send('You have reached the daily limit of 25 requests. Please try again tomorrow.')

    # Command to display help information
    elif message.content.startswith('!help'):
        help_message = (
            "Here are the commands you can use:\n"
            "!idea - Get a random tech project idea (25 requests per day)\n"
            "!help - Display this help message"
        )
        await message.channel.send(help_message)

# Run the bot with your token
client.run(xxxxxx)