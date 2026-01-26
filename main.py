import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
general_id = int(os.getenv("GENERAL_ID"))
spam_id = int(os.getenv("SPAM_ID"))

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

    if "💋" in message.content:
        await message.author.send(f"I want to be your girlfriend uwu {message.author.mention}")
        
    await bot.process_commands(message)

@bot.command()
async def help(ctx, *, command: str = ""):
    new_command = command.strip().lower()

    spam = bot.get_channel(spam_id)
    match new_command:
        case "":
            await ctx.send(f"""**List of all commands in Flix**
`&help`: Shows all command. If you want a specific command, do `&help <command_name>`
`&spam`: Spam something for an amount of time. Syntax: `&spam <amount> <message>`. Note that only use this in {spam.mention}""")
        case "help":
            await ctx.send("`&help`: Shows all command. If you want a specific command, do `&help <command_name>`")
        case "spam":
            await ctx.send(f"`&spam`: Spam something for an amount of time. Syntax: `&spam <amount> <message>`. Note that only use this in {spam.mention}")
        case _:
            await ctx.send("Invalid command, please use `&help` for a list of commands")

@bot.command()
async def spam(ctx, amount: int, *, message: str):
    for i in range(amount):
        await ctx.send(message)

bot.run(token)
