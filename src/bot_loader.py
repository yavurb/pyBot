import os

async def bot_loader(bot):
    for filename in os.listdir('./src/cogs'):
      try:
        if filename.endswith('.py'):
          bot.load_extension(f'cogs.{filename[:-3]}')
      except:
        print(f'Failed to load cog {filename[:-3]}.')