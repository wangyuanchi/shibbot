import discord
import os
import PIL
import random
from discord.ext import commands
from io import BytesIO
from keep_alive import keep_alive
from PIL import Image, ImageDraw, ImageFont
from replit import db

# setting up the bot
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

# need to create database if it does not exist
# db["gemstone"] = {}
# db["item"] = {}

# update gemstone database
def update_gemstone_database(user, index, amount):
  # each index represents amount of a specific gem
  new_gemstone_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  if user in db["gemstone"].keys():
    db["gemstone"][user][index] += amount
  else:
    db["gemstone"][user] = new_gemstone_list
    db["gemstone"][user][index] += amount
      
# update item database
def update_item_database(user, item):
  if user in db["item"]:
    db["item"][user].append(item)
  else:
    db["item"][user] = [item]

# help command that shows all possible commands
@bot.command()
async def help(ctx):
  embed = discord.Embed(
      title="Commands List:",
      description=
      "**Prefix ($):** *buy, equip, gems, inv, items, items_pricing, lb, profile, set_gem, upgrade, upgrade_cost*",
      color=discord.Color.red())
  embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
  await ctx.send(embed=embed)
    
# spawn a certain amount of a certain type of gem for the specified user
@bot.command(name='spawn')
async def spawn(ctx, member: discord.Member=None, index=None, amount=None):
  # private command is only accessible by set user id 
  if ctx.author.id != 315107540138721280:
    await ctx.channel.send("**You cannot use this command!**")
  else:
    update_gemstone_database(str(member.id), int(index), int(amount))

# buy a pickaxe using gems
@bot.command(name='buy')
async def buy(ctx, item=None):
  # key = name of pickaxe, value = list of tuples, where each tuple contains the index of the gem required and the amount of it that will be spent
  pickaxe = {
      "PX-IR": [(11, 200)],
      "PX-GO": [(10, 100)],
      "PX-DI": [(9, 100)],
      "PX-EM": [(8, 60), (11, 150)],
      "PX-SA": [(7, 30), (11, 250)],
      "PX-RU": [(6, 20), (11, 250)],
      "PX-JA": [(5, 15), (11, 500)],
      "PX-OP": [(4, 5), (11, 1250)],
      "PX-AM": [(3, 5), (10, 1000)],
      "PX-TO": [(7, 150), (8, 100), (9, 300)],
      "PX-ON": [(4, 20), (5, 25), (6, 50)],
      "PX-IC": [(1, 5), (2, 10), (3, 5)],
      "PX-A": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), 
               (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)],
      "PX-X2": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), 
                (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)],
      "PX-1": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), 
               (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)],
      "PX-T": [(0, 1)]
  }
  
  if item not in pickaxe.keys():
    embed = discord.Embed(
        title="Missing or Invalid Argument!",
        description=
        "**Try:** $buy (*specific_item*) \n **Arguments:** *PX-IR, PX-GO, PX-DI, PX-EM, PX-SA, PX-RU, PX-JA, PX-OP, PX-AM, PX-TO, PX-ON, PX-IC, PX-A, PX-X2, PX-1, PX-T*",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return

  # get user relevant information from database
  user = str(ctx.author.id)
  user_items, user_gems = [], []
  if user in db["gemstone"].keys():
    user_gems = db["gemstone"][user]
  if user in db["item"].keys():
    user_items = db["item"][user]

  # if the user already has the item
  for i in user_items:
    if item in i:
      await ctx.channel.send("**You already have this item!**")
      return

  # if the user does not have enough gems to afford the item
  for gem_info in pickaxe[item]:
    if user_gems[gem_info[0]] < gem_info[1]:
      await ctx.channel.send(
          "**You do not have enough gems to buy this item!**")
      return

  # if the user has enough gems to afford the item
  for gem_info in pickaxe[item]:
    update_gemstone_database(user, gem_info[0], -gem_info[1])
  update_item_database(user, item)
  await ctx.channel.send("**You have successfully bought the item!**")

# function that updates name of item to be upgraded in the user's inventory, and returns the updated name of item
def upgrade_pickaxe(user, item):
  # key = old reforge of pickaxe, value = new reforge of pickaxe
  update_name = {
      "GOOD": "PROPER",
      "PROPER": "DECENT",
      "DECENT": "STRONG",
      "STRONG": "POLISHED",
      "POLISHED": "REFINED",
      "REFINED": "PERFECT"
  }

  # get index of item to be upgraded
  index = db["item"][user].index(item)

  # if the item is in its base form, i.e. PX-(shorted_name_of_gem)
  if len(item) == 5:
    db["item"][user][index] = "GOOD-" + db["item"][user][index]
    return db["item"][user][index]
    
  reforge, pickaxe_name = "", ""
  # set to True when char has looped to the start of pickaxe_name, after "-"
  passed = False

  # if the item already has a reforge, get the name of reforge and original pickaxe_name
  for char in db["item"][user][index]:
    if char != "-" and passed == False:
      reforge += char
    else:
      passed = True
      pickaxe_name += char

  # update name of pickaxe and return it
  db["item"][user][index] = update_name[reforge] + pickaxe_name
  return db["item"][user][index]

# command to set a gem to mine for pickaxe "PX-1" that will append a relevant letter to the end of its name e.g. "PX-1A"
@bot.command()
async def set_gem(ctx, gem=None):
  # key = type of gem, value = corresponding letter to append
  gem_letter = {
      "iron": "A",
      "gold": "B",
      "diamond": "C",
      "emerald": "D",
      "sapphire": "E",
      "ruby": "F",
      "jade": "G",
      "opal": "H",
      "amethyst": "I",
      "topaz": "J",
      "onyx": "K",
      "ic": "L"
  }

  if gem not in gem_letter.keys():
    embed = discord.Embed(
        title="Missing or Invalid Argument!",
        description=
        "**Try:** $set_gem (*specific_gem*) \n **Arguments:** *iron, gold, diamond, emerald, sapphire, ruby, jade, opal, amethyst, topaz, onyx, ic*",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return

  # get user relevant information from database
  user = str(ctx.author.id)
  user_items = []
  if user in db["item"].keys():
    user_items = db["item"][user]

  # loop through user's items to find index of PX-1 (includes those with letters appended)
  for i in range(len(user_items)):
    if "PX-1" in user_items[i]:
      # append relevant letter to base name
      name = "PX-1" + gem_letter[gem]
      db["item"][user][i] = name
      await ctx.channel.send(f"**Successfully set PX-1 to mine only {gem}! It has been renamed to {name}!**")
      return

  # cannot find item in user's items
  await ctx.channel.send("**You do not have PX-1 and cannot set a gem for it to mine!**")

# spend gems to upgrade a pickaxe
@bot.command(name='upgrade')
async def upgrade(ctx, item=None):
  if item == None:
    embed = discord.Embed(
        title="Missing Argument!",
        description=
        "**Try:** $upgrade (*specific_pickaxe*)\n*Please check your inventory for available pickaxes to upgrade using $inv.*",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return
    
  # get user relevant information from database
  user = str(ctx.author.id)
  user_items, user_gems = [], []
  if user in db["gemstone"].keys():
    user_gems = db["gemstone"][user]
  if user in db["item"].keys():
    user_items = db["item"][user]
  
  # if user does not have the item
  if item not in user_items:
    await ctx.channel.send("**You do not have this item!**")
    return

  # key = upgradable item, value = list of tuples, where each tuple contains the index of the gem required and the amount of it that will be spent
  upgrade_cost = {
      "PX-IR": [(11, 20)],
      "GOOD-PX-IR": [(11, 25)],
      "PROPER-PX-IR": [(11, 33)],
      "DECENT-PX-IR": [(11, 40)],
      "STRONG-PX-IR": [(11, 50)],
      "POLISHED-PX-IR": [(11, 200)],
      "PX-GO": [(10, 10)],
      "GOOD-PX-GO": [(10, 12)],
      "PROPER-PX-GO": [(10, 16)],
      "DECENT-PX-GO": [(10, 20)],
      "STRONG-PX-GO": [(10, 25)],
      "POLISHED-PX-GO": [(10, 100)],
      "PX-DI": [(9, 10)],
      "GOOD-PX-DI": [(9, 12)],
      "PROPER-PX-DI": [(9, 16)],
      "DECENT-PX-DI": [(9, 20)],
      "STRONG-PX-DI": [(9, 25)],
      "POLISHED-PX-DI": [(9, 100)],
      "PX-EM": [(8, 6)],
      "GOOD-PX-EM": [(8, 8)],
      "PROPER-PX-EM": [(8, 12)],
      "DECENT-PX-EM": [(8, 15)],
      "STRONG-PX-EM": [(8, 18)],
      "POLISHED-PX-EM": [8, 75],
      "PX-SA": [(7, 4)],
      "GOOD-PX-SA": [(7, 5)],
      "PROPER-PX-SA": [(7, 6)],
      "DECENT-PX-SA": [(7, 8)],
      "STRONG-PX-SA": [(7, 10)],
      "POLISHED-PX-SA": [(7, 40)],
      "PX-RU": [(11, 125)],
      "GOOD-PX-RU": [(11, 150)],
      "PROPER-PX-RU": [(11, 200)],
      "DECENT-PX-RU": [(11, 250)],
      "STRONG-PX-RU": [(11, 300)],
      "POLISHED-PX-RU": [(11, 1250)],
      "PX-JA": [(11, 200)],
      "GOOD-PX-JA": [(11, 250)],
      "PROPER-PX-JA": [(11, 333)],
      "DECENT-PX-JA": [(11, 400)],
      "STRONG-PX-JA": [(11, 500)],
      "POLISHED-PX-JA": [(11, 2000)],
      "PX-OP": [(10, 100)],
      "GOOD-PX-OP": [(10, 125)],
      "PROPER-PX-OP": [(10, 166)],
      "DECENT-PX-OP": [(10, 200)],
      "STRONG-PX-OP": [(10, 250)],
      "POLISHED-PX-OP": [(10, 1000)],
      "REFINED-PX-OP": [(4, 10)],
      "PX-AM": [(10, 200)],
      "GOOD-PX-AM": [(10, 250)],
      "PROPER-PX-AM": [(10, 333)],
      "DECENT-PX-AM": [(10, 400)],
      "STRONG-PX-AM": [(10, 500)],
      "POLISHED-PX-AM": [(10, 2000)],
      "REFINED-PX-AM": [(3, 10)],
      "PX-TO": [(9, 125)],
      "GOOD-PX-TO": [(9, 155)],
      "PROPER-PX-TO": [(9, 208)],
      "DECENT-PX-TO": [(9, 250)],
      "STRONG-PX-TO": [(9, 312)],
      "POLISHED-PX-TO": [(9, 1250)],
      "REFINED-PX-TO": [(2, 6)],
      "PX-ON": [(9, 250)],
      "GOOD-PX-ON": [(9, 312)],
      "PROPER-PX-ON": [(9, 416)],
      "DECENT-PX-ON": [(9, 500)],
      "STRONG-PX-ON": [(9, 625)],
      "POLISHED-PX-ON": [(9, 2500)],
      "REFINED-PX-ON": [(1, 5)],
      "PX-IC": [(8, 250)],
      "GOOD-PX-IC": [(8, 312)],
      "PROPER-PX-IC": [(8, 416)],
      "DECENT-PX-IC": [(7, 200)],
      "STRONG-PX-IC": [(7, 250)],
      "POLISHED-PX-IC": [(7, 1000)],
      "REFINED-PX-IC": [(0, 1)],
  }

  # unupgradable item, i.e. maxed reforge (Perfect)
  if item not in upgrade_cost.keys():
    await ctx.channel.send("**You cannot upgrade this item!**")
    return

  # if the user cannot afford to upgrade the item
  for gem_info in upgrade_cost[item]:
    if user_gems[gem_info[0]] < gem_info[1]:
      await ctx.channel.send(
          "**You do not have enough gems to buy this item!**")
      return
      
  # if user can afford to upgrade the item
  for gem_info in upgrade_cost[item]:
    update_gemstone_database(user, gem_info[0], -gem_info[1])
  upgraded_pickaxe_name = upgrade_pickaxe(user, item)
  await ctx.channel.send(f"**Successfully upgraded your {item} to {upgraded_pickaxe_name} **")

# showcases all possible items available to be bought
@bot.command()
async def items(ctx):
  embed = discord.Embed(
      title="Items List:",
      description=
      "**Pickaxes:**\n**PX-GEM:** Increase chance to find the gemstone that the pickaxe is made of by 100%.\n**PX-A:** Increase chance to find any gemstone by 75%. [cannot be upgraded]\n**PX-X2:** Decreases chance to find any gemstone by 25%, but every gem found is doubled. [cannot be upgraded]\n**PX-1:** Increase chance of set gem to be found by 500%, but doesn't find any other gems. [cannot be upgraded]\n**PX-T:** Ability to find tokens when mining. [cannot be upgraded]",
      color=discord.Color.red())
  embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
  await ctx.send(embed=embed)

# shows the prices of all available items 
@bot.command()
async def items_pricing(ctx):
  embed = discord.Embed(
      title="Items Pricing:",
      description=
      "*This list shows the price of items that you can potentially buy. Once bought, the gems would be deducted from your balance and your networth will also decrease accordingly. Once an item is bought, you have to equip it to use it.*",
      color=discord.Color.red())

  # text to be added to pillow image
  items_name = "PX-IR\nPX-GO\nPX-DI\nPX-EM\nPX-SA\nPX-RU\nPX-JA\nPX-OP\nPX-AM\nPX-TO\nPX-ON\nPX-IC\nPX-A\nPX-X2\nPX-1\nPX-T"
  items_price = "200 Iron\n100 Gold\n100 Diamond\n60 Emerald + 150 Iron\n30 Sapphire + 250 Iron\n20 Ruby + 250 Iron\n15 Jade + 500 Iron\n5 Opal + 1250 Iron\n5 Amethyst + 1000 Gold\n150 Sapphire + 100 Emerald + 300 Diamond\n20 Opal + 25 Jade + 50 Ruby\n5 Onyx + 10 Topaz + 5 Amethyst\n1 of every single gem\n1 of every single gem\n1 of every single gem\n1 Invisible Crystal"

  # creating pillow image of text
  img = PIL.Image.new(mode="RGBA", size=(800, 480), color=(0, 0, 0, 0))
  font = ImageFont.truetype("whitneymedium.otf", 24)
  font2 = ImageFont.truetype("whitneybold.otf", 28)
  draw = ImageDraw.Draw(img)
  draw.text((5, 0), "Pickaxe:", (220, 221, 222), font=font2)
  draw.text((325, 0), "Total Price:", (220, 221, 222), font=font2)
  draw.text((5, 30), items_name.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
  draw.text((325, 30), items_price.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
  with BytesIO() as image_binary:
    img.save(image_binary, 'PNG')
    image_binary.seek(0)
    file = discord.File(fp=image_binary, filename='image.png')
  embed.set_image(url="attachment://image.png")
  embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
  await ctx.send(file=file, embed=embed)

# shows the cost of upgrading any pickaxe under PX-GEM
@bot.command(name='upgrade_cost')
async def upgrade_cost(ctx, item=None):

  # key = base pickaxe name, value = cost of reforges
  cheap_upgrades = {
    "PX-IR": ["20 Iron", "25 Iron", "33 Iron", "40 Iron", "50 Iron", "200 Iron"],
    "PX-GO": ["10 Gold", "12 Gold", "16 Gold", "20 Gold", "25 Gold", "100 Gold"],
    "PX-DI": ["10 Diamond", "12 Diamond", "16 Diamond", "20 Diamond", "25 Diamond", "100 Diamond"],
    "PX-EM": ["6 Emerald", "8 Emerald", "12 Emerald", "15 Emerald", "18 Emerald", "75 Emerald"],
    "PX-SA": ["4 Sapphire", "5 Sapphire", "6 Sapphire", "8 Sapphire", "10 Sapphire", "40 Sapphire"],
    "PX-RU": ["125 Iron", "150 Iron", "200 Iron", "250 Iron", "300 Iron", "1250 Iron"],
    "PX-JA": ["200 Iron", "250 Iron", "333 Iron", "400 Iron", "500 Iron", "2000 Iron"],
  }
  
  # key = base pickaxe name, value = cost of reforges, including additional reforge "Perfect"
  expensive_upgrades = {
    "PX-OP": ["100 Gold", "125 Gold", "166 Gold", "200 Gold", "250 Gold", "1000 Gold", "10 Opal"],
    "PX-AM": ["200 Gold", "250 Gold", "333 Gold", "400 Gold", "500 Gold", "2000 Gold", "10 Amethyst"],
    "PX-TO": ["125 Diamond", "155 Diamond", "208 Diamond", "250 Diamond", "312 Diamond", "1250 Diamond", "6 Topaz"],
    "PX-ON": ["250 Diamond", "312 Diamond", "416 Diamond", "500 Diamond", "625 Diamond", "2500 Diamond", "5 Onyx"], 
    "PX-IC": ["250 Emerald", "312 Emerald", "416 Emerald", "200 Sapphire", "250 Sapphire", "1000 Sapphire", "1 Invisible Crystal"]
  }

  if item == None or not (item in cheap_upgrades.keys() or item in expensive_upgrades.keys()):
    embed = discord.Embed(
        title="Missing or Invalid Argument!",
        description="**Try:** $upgrade_cost (*specific_pickaxe*)\n**Arguments:** *PX-IR, PX-GO, PX-DI, PX-EM, PX-SA, PX-RU, PX-JA, PX-OP, PX-AM, PX-TO, PX-ON, PX-IC*\nThe additional percentage would be a multiple of the base percentage + base pickaxe percentage.\nFor example: Equipping a GOOD-PX-IR would increase your iron chance from 0.25 to 0.25x2x1.5 = 0.75, where maximum chance is 1.",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return

  if item in cheap_upgrades.keys():
    l = cheap_upgrades[item]
    embed = discord.Embed(
      title=f"Upgrade Costs for {item}",
      description=f"Good [+50%]: {l[0]}\nProper [+60%]: {l[1]}\nDecent [+70%]: {l[2]}\nStrong [+80%]: {l[3]}\nPolished [+90%]: {l[4]}\nRefined [+100%]: {l[5]}",
      color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return 

  if item in expensive_upgrades.keys():
    l = expensive_upgrades[item]
    embed = discord.Embed(
      title=f"Upgrade Costs for {item}",
      description=f"Good [+50%]: {l[0]}\nProper [+60%]: {l[1]}\nDecent [+70%]: {l[2]}\nStrong [+80%]: {l[3]}\nPolished [+90%]: {l[4]}\nRefined [+100%]: {l[5]}\nPerfect [+200%]: {l[6]}",
      color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    
# inventory that shows number of tokens and list of items owned
@bot.command()
async def inv(ctx, member: discord.Member = None):
  # get original or specified user info
  user = str(ctx.author.id)
  if member == None:
    member = ctx.author
  else:
    user = str(member.id)

  if user not in db["item"].keys():
    embed = discord.Embed(
        title="Empty Inventory!",
        description="**Oh no!** *You need to own at least 1 pickaxe to access your inventory!*",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return

  # add all user's items into a string 
  string = ""
  for i in db["item"][user]:
    string += i + "\n"

  # include number of tokens in inventory
  token_count = db["gemstone"][user][12]
  
  embed = discord.Embed(
      title=f"{member}'s Inventory:",
      description=f"*This list shows everything you currently own! The first item is your equipped item.*\n**Tokens: {token_count}**\n{string}",
      color=discord.Color.red())
  embed.set_thumbnail(url=member.avatar)
  embed.set_image(url="attachment://image.png")
  embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
  await ctx.send(embed=embed)

# an item is equipped when it is the user's first item in the item database at index 0
@bot.command()
async def equip(ctx, item=None):
  if item == None:
    embed = discord.Embed(
        title="Missing Argument!",
        description="**Try:** $equip (*specific_item*) \n *Please check your inventory for available items to equip using $inv.*",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return

  # get user relevant information from database
  user = str(ctx.author.id)
  user_items = []
  if user in db["item"].keys():
    user_items = db["item"][user]
    
  if item not in user_items:
    await ctx.channel.send("**You do not have this item!**")
    return
  else:
    # find index of item and swap it with the currently equipped item
    index = db["item"][user].index(item)
    db["item"][user][0], db["item"][user][index] = db["item"][user][index], db["item"][user][0]
    await ctx.channel.send("**You have successfully equipped this item!**")

# taking data from gemstone database and forming a temporary leaderboard
def leaderboard(gem_index):
  tempdatabase = {}
  for key, value in db["gemstone"].items():
    tempdatabase[key] = value[gem_index]
  # sample return [(user1, 1000), (user2, 500), (user3, 100), (user4, 25), (user5, 0)]
  return sorted(tempdatabase.items(), key=lambda item: item[1], reverse=True)

# produces a leaderboard for total networth or a specific gem
@bot.command(name='lb')
async def lb(ctx, arg=None):
  # key = name of gem, value = its index in gemstone database under any user
  name_index = {
      "iron": 11,
      "gold": 10,
      "diamond": 9,
      "emerald": 8,
      "sapphire": 7,
      "ruby": 6,
      "jade": 5,
      "opal": 4,
      "amethyst": 3,
      "topaz": 2,
      "onyx": 1,
      "ic": 0
  }
  
  if arg == None or not (arg in name_index.keys() or arg == "nw"):
    embed = discord.Embed(
        title="Missing or Invalid Argument!",
        description=
        "**Try:** $lb (*specific_leaderboard*) \n **Arguments:** *nw, iron, gold, diamond, emerald, sapphire, ruby, jade, opal, amethyst, topaz, onyx, ic*",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return
    
  # if the argument is a gemstone
  if arg in name_index.keys():
    # string formatting for ugly shortened name
    title = arg.title()
    if arg == "ic":
      title = "Invisible Crystal"

    # tempdb is a list of tuples of users and the amount of the specific gem they own
    tempdb = leaderboard(name_index[arg])
    
    if tempdb[0][1] == 0:
      embed = discord.Embed(
          title="Empty Leaderboard!",
          description="**Wow!** *There is no one here! Obtain the item you searched for and be the first one on this leaderboard!*",
          color=discord.Color.red())
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
      return

    # adding users from the leaderboard to relevant strings to display in pillow image
    usernames, amount = "", ""

    # only want users in the top 10 or less that have at least 1 of the required gem 
    for user in range(min(10, len(tempdb))):
      if tempdb[user][1] != 0:
        usernames += str(bot.get_user(int(tempdb[user][0]))) + "\n"
        amount += str(tempdb[user][1]) + "\n"
        
    # displaying image of the leaderboard 
    embed = discord.Embed(
        title=f"**{title} Leaderboard:**",
        description=f"*This leaderboard shows the users with the most amount of {title}!*",
        color=discord.Color.red())
    img = PIL.Image.new(mode="RGBA", size=(800, 315), color=(0, 0, 0, 0))
    font = ImageFont.truetype("whitneymedium.otf", 24)
    font2 = ImageFont.truetype("whitneybold.otf", 28)
    draw = ImageDraw.Draw(img)
    draw.text((5, 0), "User:", (220, 221, 222), font=font2)
    draw.text((575, 0), "Amount:", (220, 221, 222), font=font2)
    draw.text((5, 30), usernames.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
    draw.text((575, 30), amount.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
    with BytesIO() as image_binary:
      img.save(image_binary, 'PNG')
      image_binary.seek(0)
      file = discord.File(fp=image_binary, filename='image.png')
    embed.set_image(url="attachment://image.png")
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(file=file, embed=embed)
    return
    
  if arg == "nw":
    #calculating networth of every user and sorting it
    networth = []
    for user, user_gems in db["gemstone"].items():
      total_value = user_gems[11] * 4 + user_gems[10] * 10 + user_gems[9] * 20 + user_gems[8] * 40 + user_gems[7] * 100 + user_gems[6] * 200 + user_gems[5] * 400 + user_gems[4] * 1000 + user_gems[3] * 2000 + user_gems[2] * 4000 + user_gems[1] * 10000 + user_gems[0] * 100000
      networth.append((user, total_value))
    networth = sorted(networth, key=lambda x: x[1], reverse=True)
    
    if networth[0][1] == 0:
      embed = discord.Embed(
          title="Empty Leaderboard!",
          description="**Wow!** *There is no one here! Obtain some gems and be the first one on this leaderboard!*",
          color=discord.Color.red())
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
      return
      
    # adding users from the leaderboard to relevant strings to display in pillow image
    usernames, values = "", ""
    
    # only want users in the top 10 or less that have at a networth
    for i in range(min(10, len(networth))):
      usernames += str(bot.get_user(int(networth[i][0]))) + "\n"
      values += "$" + str(networth[i][1]) + "\n"

    # displaying image of the leaderboard 
    embed = discord.Embed(
        title=f"**Networth Leaderboard:**",
        description=f"*This leaderboard shows the users with the highest networth!*",
        color=discord.Color.red())
    img = PIL.Image.new(mode="RGBA", size=(800, 315), color=(0, 0, 0, 0))
    font = ImageFont.truetype("whitneymedium.otf", 24)
    font2 = ImageFont.truetype("whitneybold.otf", 28)
    draw = ImageDraw.Draw(img)
    draw.text((5, 0), "User:", (220, 221, 222), font=font2)
    draw.text((550, 0), "Networth:", (220, 221, 222), font=font2)
    draw.text((5, 30), usernames.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
    draw.text((550, 30), values.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
    with BytesIO() as image_binary:
      img.save(image_binary, 'PNG')
      image_binary.seek(0)
      file = discord.File(fp=image_binary, filename='image.png')
    embed.set_image(url="attachment://image.png")
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(file=file, embed=embed)
    return

# profile that shows number of each gem that a user has
@bot.command()
async def profile(ctx, member: discord.Member = None):
  # get original or specified user info
  user = str(ctx.author.id)
  if member == None:
    member = ctx.author
  else:
    user = str(member.id)

  if user not in db["gemstone"].keys():
    embed = discord.Embed(
        title="User not in database!",
        description="**Oh no!** *You need to chat and obtain at least 1 gem to be registered in the database!*",
        color=discord.Color.red())
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)
    return

  # calculating total networth of user and converting amount of each gem to string 
  user_gems = db["gemstone"][user]
  total_value = user_gems[11] * 4 + user_gems[10] * 10 + user_gems[9] * 20 + user_gems[8] * 40 + user_gems[7] * 100 + user_gems[6] * 200 + user_gems[5] * 400 + user_gems[4] * 1000 + user_gems[3] * 2000 + user_gems[2] * 4000 + user_gems[1] * 10000 + user_gems[0] * 100000

  # reverse user_gems and convert each element in user_gems to a string joined by newline without changing the original list
  temp_list = user_gems[:]
  # remove token amount
  temp_list.pop()
  temp_list.reverse()
  amount = '\n'.join(map(str, temp_list))

  # displaying image of the user's profile
  embed = discord.Embed(
      title=f"{member}'s Profile:",
      description=
      f"**Networth:** *${total_value}*\nYour networth is the sum of the values of all the gemstones you currently own!",
      color=discord.Color.red())
  gem_name = "Iron\nGold\nDiamond\nEmerald\nSapphire\nRuby\nJade\nOpal\nAmethyst\nTopaz\nOnyx\nInvisible Crystal"
  img = PIL.Image.new(mode="RGBA", size=(800, 370), color=(0, 0, 0, 0))
  font = ImageFont.truetype("whitneymedium.otf", 24)
  font2 = ImageFont.truetype("whitneybold.otf", 28)
  draw = ImageDraw.Draw(img)
  draw.text((5, 0), "Gemstone:", (220, 221, 222), font=font2)
  draw.text((500, 0), "Amount:", (220, 221, 222), font=font2)
  draw.text((5, 30), gem_name.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
  draw.text((500, 30), amount.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
  with BytesIO() as image_binary:
    img.save(image_binary, 'PNG')
    image_binary.seek(0)
    file = discord.File(fp=image_binary, filename='image.png')
  embed.set_thumbnail(url=member.avatar)
  embed.set_image(url="attachment://image.png")
  embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
  await ctx.send(file=file, embed=embed)
  return

# information on names of the gems, their values and drop chance
@bot.command()
async def gems(ctx):
  embed = discord.Embed(
      title="Gem Information:",
      description="*This list gives information for the possible gems to be obtained.*",
      color=discord.Color.red())
  gem_name = "Iron\nGold\nDiamond\nEmerald\nSapphire\nRuby\nJade\nOpal\nAmethyst\nTopaz\nOnyx\nInvisible Crystal"
  gem_value = "$4\n$10\n$20\n$40\n$100\n$200\n$400\n$1000\n$2000\n$4000\n$10000\n$100000"
  drop_chance = "25%\n10%\n5%\n2.5%\n1%\n0.5%\n0.25%\n0.1%\n0.05%\n0.025%\n0.01%\n0.001%"
  img = PIL.Image.new(mode="RGBA", size=(800, 380), color=(0, 0, 0, 0))
  font = ImageFont.truetype("whitneymedium.otf", 24)
  font2 = ImageFont.truetype("whitneybold.otf", 28)
  draw = ImageDraw.Draw(img)
  draw.text((5, 0), "Gem:", (220, 221, 222), font=font2)
  draw.text((325, 0), "Worth:", (220, 221, 222), font=font2)
  draw.text((600, 0), "Base Chance:", (220, 221, 222), font=font2)
  draw.text((5, 30), gem_name.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
  draw.text((325, 30), gem_value.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
  draw.text((600, 30), drop_chance.encode('utf-8').decode('utf-8'), (220, 221, 222), font=font)
  with BytesIO() as image_binary:
    img.save(image_binary, 'PNG')
    image_binary.seek(0)
    file = discord.File(fp=image_binary, filename='image.png')
  embed.set_image(url="attachment://image.png")
  embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
  await ctx.send(file=file, embed=embed)

# this happens everytime a message is sent
@bot.event
async def on_message(message):
  # message has to be from a user and not a bot
  if message.author.id == None or message.author == bot.user:
    return

  # process commands so that commands can work
  await bot.process_commands(message) 

  # set this as a logs channel for every single gem that is found by any user
  channel = bot.get_channel(890817521152843786) 

  # set this as channels that the bot cannot access to check for user message
  channelcheck = ["bot_commands", "server-logs", "message-logs", 
                  "member-logs", "welcome-logs", "management", "music"]
  
  # rng is the chance that will be rolled for each corresponding gem in rolled_gem when a user sends a message
  rng = [
    0.00001, 0.0001, 0.00025, 0.0005, 0.001, 0.0025, 0.005, 
    0.01, 0.025, 0.05, 0.1, 0.25, 0, 0
  ]
  rolled_gem = [
      "Invisible Crystal", "Onyx", "Topaz", "Amethyst", "Opal", "Jade", "Ruby",
      "Sapphire", "Emerald", "Diamond", "Gold", "Iron", "Token", "Double"
  ]

  # key = base name of pickaxe, value = corresponding index of gem
  pickaxe_rng_index = {
      "PX-IR": 11,
      "PX-GO": 10,
      "PX-DI": 9,
      "PX-EM": 8,
      "PX-SA": 7,
      "PX-RU": 6,
      "PX-JA": 5,
      "PX-OP": 4,
      "PX-AM": 3,
      "PX-TO": 2,
      "PX-ON": 1,
      "PX-IC": 0
  }

  # the chance of each gem to be rolled will be increased by any equipped pickaxe and its reforge will apply an additional multiplier, where the key = name of reforge and value = multiplier
  multiplier = {
      "GOOD": 1.5,
      "PROPER": 1.6,
      "DECENT": 1.7,
      "STRONG": 1.8,
      "POLISHED": 1.9,
      "REFINED": 2,
      "PERFECT": 3
  }

  user = str(message.author.id)

  # if the user has at least 1 item, set the first item to be the equipped_item
  if user in db["item"].keys():
    equipped_item = db["item"][user][0]

    # add multiplier to rng for PX-GEM
    original_name = equipped_item
    for reforge, multiply in multiplier.items():
      if reforge in equipped_item:
        # set original_name to be base pickaxe name by removing the reforge
        original_name = equipped_item[equipped_item.index("-") + 1:len(equipped_item)]
        # add the multiplier for the reforge
        rng[pickaxe_rng_index[original_name]] *= multiply
        # add the multiplier for the base pickaxe  
        rng[pickaxe_rng_index[original_name]] *= 2
        break
        
    # add multiplier to rng for special pickaxes
    if equipped_item == "PX-A":
      # increase chance to find each gem by 1.75 except tokens
      for i in range(12):
        rng[i] *= 1.75
        
    if equipped_item == "PX-X2":
      # decrease chance to find each gem by 0.75 but add 100% chance to get double drops
      for i in range(12):
        rng[i] *= 0.75
      rng[13] = 1

    elif "PX-1" in equipped_item:
      # key = letter representing gem, where A is iron and L is Invisible Crystal, value = its corresponding index in rng
      alphabetindex = {
          "A": 11,
          "B": 10,
          "C": 9,
          "D": 8,
          "E": 7,
          "F": 6,
          "G": 5,
          "H": 4,
          "I": 3,
          "J": 2,
          "K": 1,
          "L": 0
      }
      
      # apply the increased chances only if $set_gem has been used on PX-1
      if len(equipped_item) == 5:
        last_char = equipped_item[-1]
        # set pickaxe to only be able to find the specified gem, but at a higher chance
        for i in range(len(rng)):
          if i != alphabetindex[last_char]:
            rng[i] = 0
          else:
            rng[i] *= 5

    # decrease chance to find any gem to 0 but get the ability to find a token
    elif equipped_item == "PX-T":
      for i in range(12):
        rng[i] = 0
      rng[12] = 0.000025

  # carry out the rng roll if user messages in an intended channel
  if str(message.channel) not in channelcheck:
    mention = message.author.mention
    username = str(message.author)

    # run the roll for each gem from index 0 to 12
    for i in range(len(rng) - 1):
      # custom rarity text that will appear in the same channel as the message sent
      rarity_text = ""
      rarity = ["*CRAZY RARE DROP!*", "*RARE DROP*"]

      # user will get the gem being rolled if the random chance is lower than that of rng
      if random.random() < rng[i]:
        if i == 0 or i == 12:
          rarity_text = rarity[0]
        elif i >= 1 and i <= 3:
          rarity_text = rarity[1]  

        # send every gem rolled and received in the logs channel
        await channel.send(f"**{username} just found x1 {rolled_gem[i]}!**")
        update_gemstone_database(user, i, 1)

        # if gem rolled is a rare drop, announce in the channel where user sent the message
        if rarity_text != "":
          await message.channel.send(f"{rarity_text} **{mention} just found x1 {rolled_gem[i]}!**")

        # roll the double drop chance
        if random.random() < rng[13]:
          await channel.send(f"**{username} found a second {rolled_gem[i]}!**")
          await message.channel.send(f"**{mention} found a second {rolled_gem[i]}!**")
          update_gemstone_database(user, i, 1)

# make the bot alive even when no request is sent to the bot
keep_alive()

# set token in secrets and run the bot
bot.run(os.getenv('TOKEN'))
