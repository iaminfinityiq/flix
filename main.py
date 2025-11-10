import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
general_id = int(os.getenv("GENERAL_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="&", intents=intents, help_command=None)

@bot.event
async def on_ready():
    if not bot_loop.is_running():
        bot_loop.start()

@bot.event
async def on_member_join(member):
    general = bot.get_channel(general_id)
    await general.send(f"Greetings, {member.mention}! Welcome to Fluentix. Come here and chat with us")

@tasks.loop(seconds=1)
async def bot_loop():
    pass

@bot_loop.error
async def bot_loop_error(error):
    channel = bot.get_channel(general)
    await channel.send(f"❌ Bot loop error: {error}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    await ctx.send("!help is in maintainence, cannot use for now 💀💀💀☠️☠️☠️")

bot.run(token)
