import discord   
from discord.ext import commands
import rick
from random import choice

client = commands.Bot(command_prefix = "rickroll ")

@client.event
async def on_ready():
    print("bot is ready")

@client.command(name="me", help="  Rickrolls you")
async def me(ctx):
    author_id = ctx.message.author.id
    await ctx.send("<@{}>".format(author_id) + " " + ": " + rick.roll())
    print("<@{}>".format(author_id) + " rickrolled themselves")

@client.command(name="everyone", help="  Rickrolls everyone")
async def everyone(ctx):
    author_id = ctx.message.author.id
    await ctx.send("@everyone " + ": " + rick.roll())
    print("<@{}>".format(author_id) + " rickrolled everyone")

@client.command(name="user", help="  Ping a user of your choice, you monster")
async def user(ctx, arg):
    author_id = ctx.message.author.id
    await ctx.send((arg) + " " + ": " + rick.roll())
    print("<@{}>".format(author_id) + " rickrolled " + (arg))

@client.command(name="someone", help="  Rickrolls someone. you monster.")
@commands.guild_only()
async def someone(ctx):
    author_id = ctx.message.author.id
    await ctx.send(choice(tuple(member.mention for member in ctx.guild.members if not member.bot)) + ": " + rick.roll())
    print("<@{}>".format(author_id) + " rickrolled a random person")

@client.command(name="bot", help="  Displays a greeting")
async def bot(ctx):
    author_id = ctx.message.author.id
    await ctx.send("Hello, " + "<@{}>".format(author_id))
    print("<@{}>".format(author_id) + " said hi.")

client.run(CLIENTID HERE)
