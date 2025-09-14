import discord
from discord.ext import commands, tasks
import asyncio

TOKEN = "YOUR_BOT_TOKEN"  # replace with your bot token
PREFIX = "!"
WELCOME_CHANNEL = "orientation"
ANNOUNCE_CHANNEL = "announcements"
DEFAULT_ROLE = "Aspiring Hero"
ANNOUNCEMENT_LIFETIME = 24 * 60 * 60
FORBIDDEN_KEYWORDS = ["villainous spam","unauthorized link","off-topic disruption","menacing threats"]
WISDOM = {
    "rules": " Midtown Tech Rules:\n1. Respect all members\n2. No spam or offensive content\n3. Stay on topic & collaborate constructively!",
    
    "resources": " Helpful Resources:\n- https://docs.python.org/3/\n- https://discordpy.readthedocs.io/\n- Free tutorials and community support available in #resources channel!",
    
    "contact": "Contact Faculty:\n- Ping @Administrator or @Faculty role\n- Or DM a moderator for urgent issues."
    }
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
@bot.event
async def on_member_join(member: discord.Member):
    channel = discord.utils.get(member.guild.text_channels, name=WELCOME_CHANNEL)
    role = discord.utils.get(member.guild.roles, name=DEFAULT_ROLE)
    if role:
        await member.add_roles(role)
    if channel:
        await channel.send(f"Welcome {member.mention} to Midtown Tech! You are now an **{DEFAULT_ROLE}**. "f"Check out #rules and start your hero journey!")
@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    lowered = message.content.lower()
    if any(keyword in lowered for keyword in FORBIDDEN_KEYWORDS):
        try:
            await message.delete()
            await message.author.send(
                f"Hi {message.author.name}, your message was removed because it violated Midtown Tech’s code of conduct.\n"
                f"Please keep discussions constructive and positive. "
            )
        except discord.Forbidden:
            pass
    await bot.process_commands(message)
@bot.command(name="bugle")
@commands.has_any_role("Faculty", "Administrator")
async def bugle(ctx, *, announcement: str):
    channel = discord.utils.get(ctx.guild.text_channels, name=ANNOUNCE_CHANNEL)
    if channel:
        msg = await channel.send(f"**Daily Bugle Announcement:**\n{announcement}")
        async def delete_later(message):
            await asyncio.sleep(ANNOUNCEMENT_LIFETIME)
            try:
                if not message.pinned:
                    await message.delete()
            except discord.NotFound:
                pass
        bot.loop.create_task(delete_later(msg))
@bot.command(name="wisdom")
async def wisdom(ctx, topic: str):
    topic = topic.lower()
    if topic in WISDOM:
        await ctx.send(WISDOM[topic])
    else:
        await ctx.send("I don’t have wisdom on that topic. Try `rules`, `resources`, or `contact`.")
@bugle.error
async def bugle_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send(" Only Faculty or Administrators can use the Bugle command.")
bot.run(TOKEN)
