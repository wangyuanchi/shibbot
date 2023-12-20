import discord 
import io
import os
import PIL
import random
import requests
from discord.ext import commands
from io import BytesIO
from keep_alive import keep_alive
from PIL import Image,ImageFont, ImageDraw
from replit import db


#setting up the bot
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

#backup (last backup = 28 Nov 2021)
#db["backup"]

#resetting gemstones database
#db["gems"] = []

#resetting items database
#db["items"] = []

#resetting token database
#db["token"] = []

#updating items database
def update_itemsdatabase(user, item):
  new = [user]
  if "items" in db.keys():
    items = db["items"]
    position = 0
    added_user = 0
    for x in items:
      if x[0] == user:
        items[position].append(item)
        added_user = 1
        break
      position = position + 1
    if added_user == 0:
      items.append(new)
      items[-1].append(item)
    db["items"] = items

#updating token database
def update_tokendatabase(user, value):
  new = [user, 0]
  if "token" in db.keys():
    token = db["token"]
    position = 0
    added_user = 0
    for x in token:
      if x[0] == user:
        token[position][1] = token[position][1] + value
        added_user = 1
        break
      position = position + 1
    if added_user == 0:
      token.append(new)
      token[-1][1] = token[-1][1] + value
    db["token"] = token

#extract gem data of user
def find_user_gems(user):
  wanteduser = []
  gems = db["gems"]
  for x in gems:
    if x[0] == user:
      wanteduser = x
      break
  return wanteduser

#extract items data of user
def find_user_items(user):
  wanteduser = []
  items = db["items"]
  for x in items:
    if x[0] == user:
      wanteduser = x
      break
  return wanteduser

#upgradecost command
@bot.command(name='upgradecost')
async def upgradecost(ctx, arg=None):
  if ctx.channel.name == "bot_commands":
    if arg == None:
      embed = discord.Embed(
        title="Missing Argument!", 
        description="**Try:** $upgradecost (*specific_pickaxe*)\n**Arguments:** *PX-IR, PX-GO, PX-DI, PX-EM, PX-SA, PX-RU, PX-JA, PX-OP, PX-AM, PX-TO, PX-ON, PX-IC*\nThe additional percentage would be a multiple of the base percentage + base pickaxe percentage.\nFor example: Equipping a GOOD-PX-IR would increase your iron chance from 0.25 to 0.25x2x1.5 = 0.75, where maximum chance is 1.", 
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-IR":
      embed = discord.Embed(
        title="Upgrade Costs for PX-IR", 
        description="Good [+50%]: 20 Iron\nProper [+60%]: 25 Iron\nDecent [+70%]: 33 Iron\nStrong [+80%]: 40 Iron\nPolished [+90%]: 50 Iron\nRefined [+100%]: 200 Iron",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-GO":
      embed = discord.Embed(
        title="Upgrade Costs for PX-GO", 
        description="Good [+50%]: 10 Gold\nProper [+60%]: 12 Gold\nDecent [+70%]: 16 Gold\nStrong [+80%]: 20 Gold\nPolished [+90%]: 25 Gold\nRefined [+100%]: 100 Gold",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-DI":
      embed = discord.Embed(
        title="Upgrade Costs for PX-DI", 
        description="Good [+50%]: 10 Diamond\nProper [+60%]: 12 Diamond\nDecent [+70%]: 16 Diamond\nStrong [+80%]: 20 Diamond\nPolished [+90%]: 25 Diamond\nRefined [+100%]: 100 Diamond",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-EM":
      embed = discord.Embed(
        title="Upgrade Costs for PX-EM", 
        description="Good [+50%]: 6 Emerald\nProper [+60%]: 8 Emerald\nDecent [+70%]: 12 Emerald\nStrong [+80%]: 15 Emerald\nPolished [+90%]: 18 Emerald\nRefined [+100%]: 75 Emerald",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-SA":
      embed = discord.Embed(
        title="Upgrade Costs for PX-SA", 
        description="Good [+50%]: 4 Sapphire\nProper [+60%]: 5 Sapphire\nDecent [+70%]: 6 Sapphire\nStrong [+80%]: 8 Sapphire\nPolished [+90%]: 10 Sapphire\nRefined [+100%]: 40 Sapphire",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-RU":
      embed = discord.Embed(
        title="Upgrade Costs for PX-RU", 
        description="Good [+50%]: 125 Iron\nProper [+60%]: 150 Iron\nDecent [+70%]: 200 Iron\nStrong [+80%]: 250 Iron\nPolished [+90%]: 300 Iron\nRefined [+100%]: 1250 Iron",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-JA":
      embed = discord.Embed(
        title="Upgrade Costs for PX-JA", 
        description="Good [+50%]: 200 Iron\nProper [+60%]: 250 Iron\nDecent [+70%]: 333 Iron\nStrong [+80%]: 400 Iron\nPolished [+90%]: 500 Iron\nRefined [+100%]: 2000 Iron",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-OP":
      embed = discord.Embed(
        title="Upgrade Costs for PX-OP", 
        description="Good [+50%]: 100 Gold\nProper [+60%]: 125 Gold\nDecent [+70%]: 166 Gold\nStrong [+80%]: 200 Gold\nPolished [+90%]: 250 Gold\nRefined [+100%]: 1000 Gold\nPerfect [+200%]: 10 Opal",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-AM":
      embed = discord.Embed(
        title="Upgrade Costs for PX-AM", 
        description="Good [+50%]: 200 Gold\nProper [+60%]: 250 Gold\nDecent [+70%]: 333 Gold\nStrong [+80%]: 400 Gold\nPolished [+90%]: 500 Gold\nRefined [+100%]: 2000 Gold\nPerfect [+200%]: 10 Amethyst",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-TO":
      embed = discord.Embed(
        title="Upgrade Costs for PX-TO", 
        description="Good [+50%]: 125 Diamond\nProper [+60%]: 155 Diamond\nDecent [+70%]: 208 Diamond\nStrong [+80%]: 250 Diamond\nPolished [+90%]: 312 Diamond\nRefined [+100%]: 1250 Diamond\nPerfect [+200%]: 6 Topaz",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-ON":
      embed = discord.Embed(
        title="Upgrade Costs for PX-ON", 
        description="Good [+50%]: 250 Diamond\nProper [+60%]: 312 Diamond\nDecent [+70%]: 416 Diamond\nStrong [+80%]: 500 Diamond\nPolished [+90%]: 625 Diamond\nRefined [+100%]: 2500 Diamond\nPerfect [+200%]: 5 Onyx",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == "PX-IC":
      embed = discord.Embed(
        title="Upgrade Costs for PX-IC", 
        description="Good [+50%]: 250 Emerald\nProper [+60%]: 312 Emerald\nDecent [+70%]: 416 Emerald\nStrong [+80%]: 200 Sapphire\nPolished [+90%]: 250 Sapphire\nRefined [+100%]: 1000 Sapphire\nPerfect [+200%]: 1 Invisible Crystal",
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(
        title="Invalid Argument!", 
        description="**Try:** $upgradecost (*specific_pickaxe*)\n**Arguments:** *PX-IR, PX-GO, PX-DI, PX-EM, PX-SA, PX-RU, PX-JA, PX-OP, PX-AM, PX-TO, PX-ON, PX-IC*\nThe additional percentage would be a multiple of the base percentage + base pickaxe percentage.\nFor example: Equipping a GOOD-PX-IR would increase your iron chance from 0.25 to 0.25x2x1.5 = 0.75, where maximum chance is 1.", 
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)

#upgrade command
@bot.command(name='upgrade')
async def upgrade(ctx, arg=None):
  user = ctx.author.id
  usergems = []
  itemslist = []
  itemslist = find_user_items(user)
  usergems = find_user_gems(user)
  if ctx.channel.name == "bot_commands":
    if arg == None:
      embed = discord.Embed(
        title="Missing Argument!", 
        description="**Try:** $upgrade (*specific_pickaxe*)\n*Please check your inventory for available pickaxes to upgrade using $inv.*", 
        color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif arg == ctx.author.id:
      await ctx.channel.send("**You do not have this item!**")
    elif itemslist == []:
      await ctx.channel.send("**You do not have this item!**")
    elif arg in itemslist and "PX-" in arg:
      if "PX-IR" in arg:
        if "PX-IR" == arg:
          if usergems[12] >= 20:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 20
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IR" in str(y):
                    x[counter] = "GOOD-PX-IR"
                    await ctx.channel.send("**Successfully upgraded your PX-IR to GOOD-PX-IR! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
            await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[12] >= 25:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 25
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IR" in str(y):
                    x[counter] = "PROPER-PX-IR"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-IR to PROPER-PX-IR! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
            await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[12] >= 33:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 33
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IR" in str(y):
                    x[counter] = "DECENT-PX-IR"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-IR to DECENT-PX-IR! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
            await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[12] >= 40:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 40
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IR" in str(y):
                    x[counter] = "STRONG-PX-IR"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-IR to STRONG-PX-IR! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
            await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[12] >= 50:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 50
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IR" in str(y):
                    x[counter] = "POLISHED-PX-IR"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-IR to POLISHED-PX-IR! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
            await ctx.channel.send("**You do not have enough gems to upgrade this item!**") 
        elif "POLISHED" in arg:
          if usergems[12] >= 200:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 200
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IR" in str(y):
                    x[counter] = "REFINED-PX-IR"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-IR to REFINED-PX-IR! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
            await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**")
      if "PX-GO" in arg:
        if "PX-GO" == arg:
          if usergems[11] >= 10:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 10
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-GO" in str(y):
                    x[counter] = "GOOD-PX-GO"
                    await ctx.channel.send("**Successfully upgraded your PX-GO to GOOD-PX-GO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[11] >= 12:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 12
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-GO" in str(y):
                    x[counter] = "PROPER-PX-GO"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-GO to PROPER-PX-GO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")    
        elif "PROPER" in arg:
          if usergems[11] >= 16:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 16
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-GO" in str(y):
                    x[counter] = "DECENT-PX-GO"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-GO to DECENT-PX-GO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")     
        elif "DECENT" in arg:
          if usergems[11] >= 20:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 20
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-GO" in str(y):
                    x[counter] = "STRONG-PX-GO"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-GO to STRONG-PX-GO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[11] >= 25:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 25
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-GO" in str(y):
                    x[counter] = "POLISHED-PX-GO"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-GO to POLISHED-PX-GO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[11] >= 100:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 100
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-GO" in str(y):
                    x[counter] = "REFINED-PX-GO"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-GO to REFINED-PX-GO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**")
      if "PX-DI" in arg:
        if "PX-DI" == arg:
          if usergems[10] >= 10:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 10
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-DI" in str(y):
                    x[counter] = "GOOD-PX-DI"
                    await ctx.channel.send("**Successfully upgraded your PX-DI to GOOD-PX-DI! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[10] >= 12:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 12
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-DI" in str(y):
                    x[counter] = "PROPER-PX-DI"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-DI to PROPER-PX-DI! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[10] >= 16:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 16
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-DI" in str(y):
                    x[counter] = "DECENT-PX-DI"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-DI to DECENT-PX-DI! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[10] >= 20:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 20
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-DI" in str(y):
                    x[counter] = "STRONG-PX-DI"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-DI to STRONG-PX-DI! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[10] >= 25:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 25
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-DI" in str(y):
                    x[counter] = "POLISHED-PX-DI"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-DI to POLISHED-PX-DI! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[10] >= 100:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 100
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-DI" in str(y):
                    x[counter] = "REFINED-PX-DI"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-DI to REFINED-PX-DI! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**")
      if "PX-EM" in arg:
        if "PX-EM" == arg:
          if usergems[9] >= 6:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 6
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-EM" in str(y):
                    x[counter] = "GOOD-PX-EM"
                    await ctx.channel.send("**Successfully upgraded your PX-EM to GOOD-PX-EM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[9] >= 8:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 8
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-EM" in str(y):
                    x[counter] = "PROPER-PX-EM"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-EM to PROPER-PX-EM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[9] >= 12:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 12
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-EM" in str(y):
                    x[counter] = "DECENT-PX-EM"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-EM to DECENT-PX-EM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[9] >= 15:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 15
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-EM" in str(y):
                    x[counter] = "STRONG-PX-EM"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-EM to STRONG-PX-EM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[9] >= 18:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 18
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-EM" in str(y):
                    x[counter] = "POLISHED-PX-EM"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-EM to POLISHED-PX-EM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[9] >= 75:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 75
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-EM" in str(y):
                    x[counter] = "REFINED-PX-EM"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-EM to REFINED-PX-EM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**")
      if "PX-SA" in arg:
        if "PX-SA" == arg:
          if usergems[8] >= 4:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 4
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-SA" in str(y):
                    x[counter] = "GOOD-PX-SA"
                    await ctx.channel.send("**Successfully upgraded your PX-SA to GOOD-PX-SA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[8] >= 5:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 5
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-SA" in str(y):
                    x[counter] = "PROPER-PX-SA"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-SA to PROPER-PX-SA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[8] >= 6:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 6
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-SA" in str(y):
                    x[counter] = "DECENT-PX-SA"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-SA to DECENT-PX-SA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[8] >= 8:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 8
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-SA" in str(y):
                    x[counter] = "STRONG-PX-SA"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-SA to STRONG-PX-SA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[8] >= 10:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 10
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-SA" in str(y):
                    x[counter] = "POLISHED-PX-SA"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-SA to POLISHED-PX-SA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[8] >= 40:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 40
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-SA" in str(y):
                    x[counter] = "REFINED-PX-SA"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-SA to REFINED-PX-SA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**")
      if "PX-RU" in arg:
        if "PX-RU" == arg:
          if usergems[12] >= 125:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 125
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-RU" in str(y):
                    x[counter] = "GOOD-PX-RU"
                    await ctx.channel.send("**Successfully upgraded your PX-RU to GOOD-PX-RU! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[12] >= 150:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 150
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-RU" in str(y):
                    x[counter] = "PROPER-PX-RU"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-RU to PROPER-PX-RU! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[12] >= 200:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 200
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-RU" in str(y):
                    x[counter] = "DECENT-PX-RU"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-RU to DECENT-PX-RU! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[12] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-RU" in str(y):
                    x[counter] = "STRONG-PX-RU"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-RU to STRONG-PX-RU! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[12] >= 300:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 300
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-RU" in str(y):
                    x[counter] = "POLISHED-PX-RU"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-RU to POLISHED-PX-RU! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[12] >= 1250:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 1250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-RU" in str(y):
                    x[counter] = "REFINED-PX-RU"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-RU to REFINED-PX-RU! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**") 
      if "PX-JA" in arg:
        if "PX-JA" == arg:
          if usergems[12] >= 200:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 200
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-JA" in str(y):
                    x[counter] = "GOOD-PX-JA"
                    await ctx.channel.send("**Successfully upgraded your PX-JA to GOOD-PX-JA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[12] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-JA" in str(y):
                    x[counter] = "PROPER-PX-JA"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-JA to PROPER-PX-JA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[12] >= 333:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 333
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-JA" in str(y):
                    x[counter] = "DECENT-PX-JA"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-JA to DECENT-PX-JA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[12] >= 400:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 400
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-JA" in str(y):
                    x[counter] = "STRONG-PX-JA"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-JA to STRONG-PX-JA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[12] >= 500:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 500
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-JA" in str(y):
                    x[counter] = "POLISHED-PX-JA"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-JA to POLISHED-PX-JA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[12] >= 2000:
            for x in db["gems"]:
              if x[0] == user:
                x[12] = x[12] - 2000
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-JA" in str(y):
                    x[counter] = "REFINED-PX-JA"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-JA to REFINED-PX-JA! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**") 
      if "PX-OP" in arg:
        if "PX-OP" == arg:
          if usergems[11] >= 100:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 100
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-OP" in str(y):
                    x[counter] = "GOOD-PX-OP"
                    await ctx.channel.send("**Successfully upgraded your PX-OP to GOOD-PX-OP! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[11] >= 125:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 125
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-OP" in str(y):
                    x[counter] = "PROPER-PX-OP"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-OP to PROPER-PX-OP! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[11] >= 166:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 166
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-OP" in str(y):
                    x[counter] = "DECENT-PX-OP"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-OP to DECENT-PX-OP! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[11] >= 200:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 200
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-OP" in str(y):
                    x[counter] = "STRONG-PX-OP"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-OP to STRONG-PX-OP! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[11] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-OP" in str(y):
                    x[counter] = "POLISHED-PX-OP"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-OP to POLISHED-PX-OP! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[11] >= 1000:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 1000
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-OP" in str(y):
                    x[counter] = "REFINED-PX-OP"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-OP to REFINED-PX-OP! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "REFINED" in arg:
          if usergems[5] >= 10:
            for x in db["gems"]:
              if x[0] == user:
                x[5] = x[5] - 10
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-OP" in str(y):
                    x[counter] = "PERFECT-PX-OP"
                    await ctx.channel.send("**Successfully upgraded your REFINED-PX-OP to PERFECT-PX-OP! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**") 
      if "PX-AM" in arg:
        if "PX-AM" == arg:
          if usergems[11] >= 200:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 200
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-AM" in str(y):
                    x[counter] = "GOOD-PX-AM"
                    await ctx.channel.send("**Successfully upgraded your PX-AM to GOOD-PX-AM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[11] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-AM" in str(y):
                    x[counter] = "PROPER-PX-AM"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-AM to PROPER-PX-AM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[11] >= 333:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 333
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-AM" in str(y):
                    x[counter] = "DECENT-PX-AM"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-AM to DECENT-PX-AM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[11] >= 400:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 400
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-AM" in str(y):
                    x[counter] = "STRONG-PX-AM"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-AM to STRONG-PX-AM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[11] >= 500:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 500
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-AM" in str(y):
                    x[counter] = "POLISHED-PX-AM"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-AM to POLISHED-PX-AM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[11] >= 2000:
            for x in db["gems"]:
              if x[0] == user:
                x[11] = x[11] - 2000
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-AM" in str(y):
                    x[counter] = "REFINED-PX-AM"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-AM to REFINED-PX-AM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "REFINED" in arg:
          if usergems[4] >= 10:
            for x in db["gems"]:
              if x[0] == user:
                x[4] = x[4] - 10
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-AM" in str(y):
                    x[counter] = "PERFECT-PX-AM"
                    await ctx.channel.send("**Successfully upgraded your REFINED-PX-AM to PERFECT-PX-AM! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**")  
      if "PX-TO" in arg:
        if "PX-TO" == arg:
          if usergems[10] >= 125:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 125
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-TO" in str(y):
                    x[counter] = "GOOD-PX-TO"
                    await ctx.channel.send("**Successfully upgraded your PX-TO to GOOD-PX-TO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[10] >= 155:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 155
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-TO" in str(y):
                    x[counter] = "PROPER-PX-TO"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-TO to PROPER-PX-TO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[10] >= 208:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 208
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-TO" in str(y):
                    x[counter] = "DECENT-PX-TO"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-TO to DECENT-PX-TO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")

        elif "DECENT" in arg:
          if usergems[10] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-TO" in str(y):
                    x[counter] = "STRONG-PX-TO"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-TO to STRONG-PX-TO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[10] >= 312:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 312
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-TO" in str(y):
                    x[counter] = "POLISHED-PX-TO"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-TO to POLISHED-PX-TO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[10] >= 1250:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 1250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-TO" in str(y):
                    x[counter] = "REFINED-PX-TO"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-TO to REFINED-PX-TO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "REFINED" in arg:
          if usergems[3] >= 6:
            for x in db["gems"]:
              if x[0] == user:
                x[3] = x[3] - 6
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-TO" in str(y):
                    x[counter] = "PERFECT-PX-TO"
                    await ctx.channel.send("**Successfully upgraded your REFINED-PX-TO to PERFECT-PX-TO! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**") 
      if "PX-ON" in arg:
        if "PX-ON" == arg:
          if usergems[10] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-ON" in str(y):
                    x[counter] = "GOOD-PX-ON"
                    await ctx.channel.send("**Successfully upgraded your PX-ON to GOOD-PX-ON! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[10] >= 312:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 312
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-ON" in str(y):
                    x[counter] = "PROPER-PX-ON"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-ON to PROPER-PX-ON! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[10] >= 416:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 416
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-ON" in str(y):
                    x[counter] = "DECENT-PX-ON"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-ON to DECENT-PX-ON! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[10] >= 500:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 500
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-ON" in str(y):
                    x[counter] = "STRONG-PX-ON"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-ON to STRONG-PX-ON! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[10] >= 625:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 625
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-ON" in str(y):
                    x[counter] = "POLISHED-PX-ON"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-ON to POLISHED-PX-ON! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[10] >= 2500:
            for x in db["gems"]:
              if x[0] == user:
                x[10] = x[10] - 2500
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-ON" in str(y):
                    x[counter] = "REFINED-PX-ON"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-ON to REFINED-PX-ON! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "REFINED" in arg:
          if usergems[2] >= 5:
            for x in db["gems"]:
              if x[0] == user:
                x[2] = x[2] - 5
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-ON" in str(y):
                    x[counter] = "PERFECT-PX-ON"
                    await ctx.channel.send("**Successfully upgraded your REFINED-PX-ON to PERFECT-PX-ON! **")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else: 
          await ctx.channel.send("**You have maxed out this item!**")   
      if "PX-IC" in arg:
        if "PX-IC" == arg:
          if usergems[9] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IC" in str(y):
                    x[counter] = "GOOD-PX-IC"
                    await ctx.channel.send("**Successfully upgraded your PX-IC to GOOD-PX-IC!**")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "GOOD" in arg:
          if usergems[9] >= 312:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 312
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IC" in str(y):
                    x[counter] = "PROPER-PX-IC"
                    await ctx.channel.send("**Successfully upgraded your GOOD-PX-IC to PROPER-PX-IC!**")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "PROPER" in arg:
          if usergems[9] >= 416:
            for x in db["gems"]:
              if x[0] == user:
                x[9] = x[9] - 416
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IC" in str(y):
                    x[counter] = "DECENT-PX-IC"
                    await ctx.channel.send("**Successfully upgraded your PROPER-PX-IC to DECENT-PX-IC!**")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "DECENT" in arg:
          if usergems[8] >= 200:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 200
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IC" in str(y):
                    x[counter] = "STRONG-PX-IC"
                    await ctx.channel.send("**Successfully upgraded your DECENT-PX-IC to STRONG-PX-IC!**")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "STRONG" in arg:
          if usergems[8] >= 250:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 250
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IC" in str(y):
                    x[counter] = "POLISHED-PX-IC"
                    await ctx.channel.send("**Successfully upgraded your STRONG-PX-IC to POLISHED-PX-IC!**")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "POLISHED" in arg:
          if usergems[8] >= 1000:
            for x in db["gems"]:
              if x[0] == user:
                x[8] = x[8] - 1000
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IC" in str(y):
                    x[counter] = "REFINED-PX-IC"
                    await ctx.channel.send("**Successfully upgraded your POLISHED-PX-IC to REFINED-PX-IC!**")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        elif "REFINED" in arg:
          if usergems[1] >= 1:
            for x in db["gems"]:
              if x[0] == user:
                x[1] = x[1] - 1
                break
            for x in db["items"]:
              if x[0] == user:
                counter = 0
                for y in x:
                  if "PX-IC" in str(y):
                    x[counter] = "PERFECT-PX-IC"
                    await ctx.channel.send("**Successfully upgraded your REFINED-PX-IC to PERFECT-PX-IC!**")
                    break
                  else:
                    counter = counter + 1
                break
          else:
             await ctx.channel.send("**You do not have enough gems to upgrade this item!**")
        else:
          await ctx.channel.send("**You have maxed out this item!**")   
    else:
      await ctx.channel.send("**You either do not have this item or you cannot upgrade it!**")

#buy command
@bot.command(name='buy')
async def buy(ctx, arg=None):
  user = int(ctx.author.id)
  usergems = []
  useritems = []
  if ctx.channel.name == "bot_commands":
    usergems = find_user_gems(user)
    useritems = find_user_items(user)
    #if no argument for buy provided
    if arg == None:
      embed = discord.Embed(
      title="Missing Argument!", 
      description="**Try:** $buy (*specific_item*) \n **Arguments:** *PX-IR, PX-GO, PX-DI, PX-EM, PX-SA, PX-RU, PX-JA, PX-OP, PX-AM, PX-TO, PX-ON, PX-IC, PX-A, PX-X2, PX-1, PX-T*", 
      color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    #if argument is an item
    elif arg == "PX-IR":
      if useritems == []:
        if usergems[12] >= 200:
          for x in db["gems"]:
            if x[0] == user:
              x[12] = x[12] - 200
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-IR" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-IR" not in str(x) and str(x) == useritems[-1]:
            if usergems[12] >= 200:
              for x in db["gems"]:
                if x[0] == user:
                  x[12] = x[12] - 200
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-GO":
      if useritems == []:
        if usergems[11] >= 100:
          for x in db["gems"]:
            if x[0] == user:
              x[11] = x[11] - 100
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-GO" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-GO" not in str(x) and str(x) == useritems[-1]:
            if usergems[11] >= 100:
              for x in db["gems"]:
                if x[0] == user:
                  x[11] = x[11] - 100
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-DI":
      if useritems == []:
        if usergems[10] >= 100:
          for x in db["gems"]:
            if x[0] == user:
              x[10] = x[10] - 100
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-DI" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-DI" not in str(x) and str(x) == useritems[-1]:
            if usergems[10] >= 100:
              for x in db["gems"]:
                if x[0] == user:
                  x[10] = x[10] - 100
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-EM":
      if useritems == []:
        if usergems[9] >= 60 and usergems[12] >= 150:
          for x in db["gems"]:
            if x[0] == user:
              x[9] = x[9] - 60
              x[12] = x[12] -150
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-EM" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-EM" not in str(x) and str(x) == useritems[-1]:
            if usergems[9] >= 60 and usergems[12] >= 150:
              for x in db["gems"]:
                if x[0] == user:
                  x[9] = x[9] - 60
                  x[12] = x[12] -150
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-SA":
      if useritems == []:
        if usergems[8] >= 30 and usergems[12] >= 250:
          for x in db["gems"]:
            if x[0] == user:
              x[8] = x[8] - 30
              x[12] = x[12] - 250
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-SA" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-SA" not in str(x) and str(x) == useritems[-1]:
            if usergems[8] >= 30 and usergems[12] >= 250:
              for x in db["gems"]:
                if x[0] == user:
                  x[8] = x[8] - 30
                  x[12] = x[12] - 250
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-RU":
      if useritems == []:
        if usergems[7] >= 20 and usergems[12] >= 250:
          for x in db["gems"]:
            if x[0] == user:
              x[7] = x[7] - 20
              x[12] = x[12] - 250
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-RU" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-RU" not in str(x) and str(x) == useritems[-1]:
            if usergems[7] >= 20 and usergems[12] >= 250:
              for x in db["gems"]:
                if x[0] == user:
                  x[7] = x[7] - 20
                  x[12] = x[12] - 250
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-JA":
      if useritems == []:
        if usergems[6] >= 15 and usergems[12] >= 500:
          for x in db["gems"]:
            if x[0] == user:
              x[6] = x[6] - 15
              x[12] = x[12] - 500
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-JA" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-JA" not in str(x) and str(x) == useritems[-1]:
            if usergems[6] >= 15 and usergems[12] >= 500:
              for x in db["gems"]:
                if x[0] == user:
                  x[6] = x[6] - 15
                  x[12] = x[12] - 500
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-OP":
      if useritems == []:
        if usergems[5] >= 5 and usergems[12] >= 1250:
          for x in db["gems"]:
            if x[0] == user:
              x[5] = x[5] - 5
              x[12] = x[12] - 1250
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-OR" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-OP" not in str(x) and str(x) == useritems[-1]:
            if usergems[5] >= 5 and usergems[12] >= 1250:
              for x in db["gems"]:
                if x[0] == user:
                  x[5] = x[5] - 5
                  x[12] = x[12] - 1250
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-AM":
      if useritems == []:
        if usergems[4] >= 5 and usergems[11] >= 1000:
          for x in db["gems"]:
            if x[0] == user:
              x[4] = x[4] - 5
              x[11] = x[11] - 1000
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-AM" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-AM" not in str(x) and str(x) == useritems[-1]:
            if usergems[4] >= 5 and usergems[11] >= 1000:
              for x in db["gems"]:
                if x[0] == user:
                  x[4] = x[4] - 5
                  x[11] = x[11] - 1000
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-TO":
      if useritems == []:
        if usergems[8] >= 150 and usergems[9] >= 100 and usergems[10] >= 300:
          for x in db["gems"]:
            if x[0] == user:
              x[8] = x[8] - 150
              x[9] = x[9] - 100
              x[10] = x[10] - 300
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-TO" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-TO" not in str(x) and str(x) == useritems[-1]:
            if usergems[8] >= 150 and usergems[9] >= 100 and usergems[10] >= 300:
              for x in db["gems"]:
                if x[0] == user:
                  x[8] = x[8] - 150
                  x[9] = x[9] - 100
                  x[10] = x[10] - 300
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-ON":
      if useritems == []:
        if usergems[5] >= 20 and usergems[6] >= 25 and usergems[7] >= 50:
          for x in db["gems"]:
            if x[0] == user:
              x[5] = x[5] - 20
              x[6] = x[6] - 25
              x[7] = x[7] - 50
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-ON" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-ON" not in str(x) and str(x) == useritems[-1]:
            if usergems[5] >= 20 and usergems[6] >= 25 and usergems[7] >= 50:
              for x in db["gems"]:
                if x[0] == user:
                  x[5] = x[5] - 20
                  x[6] = x[6] - 25
                  x[7] = x[7] - 50
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-IC":
      if useritems == []:
        if usergems[2] >= 5 and usergems[3] >= 10 and usergems[4] >= 5:
          for x in db["gems"]:
            if x[0] == user:
              x[2] = x[2] - 5
              x[3] = x[3] - 10
              x[4] = x[4] - 5
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-IC" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-IC" not in str(x) and str(x) == useritems[-1]:
            if usergems[2] >= 5 and usergems[3] >= 10 and usergems[4] >= 5:
              for x in db["gems"]:
                if x[0] == user:
                  x[2] = x[2] - 5
                  x[3] = x[3] - 10
                  x[4] = x[4] - 5
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-A" or arg == "PX-X2":
      if useritems == []:
        if usergems[1] >= 1 and usergems[2] >= 1 and usergems[3] >= 1 and usergems[4] >= 1 and usergems[5] >= 1 and usergems[6] >= 1 and usergems[7] >= 1 and usergems[8] >= 1 and usergems[9] >= 1 and usergems[10] >= 1 and usergems[11] >= 1 and usergems[12] >= 1:
          for x in db["gems"]:
            if x[0] == user:
              x[1] = x[1] - 1
              x[2] = x[2] - 1
              x[3] = x[3] - 1
              x[4] = x[4] - 1
              x[5] = x[5] - 1
              x[6] = x[6] - 1
              x[7] = x[7] - 1
              x[8] = x[8] - 1
              x[9] = x[9] - 1
              x[10] = x[10] - 1
              x[11] = x[11] - 1
              x[12] = x[12] - 1
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if arg in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if arg not in str(x) and str(x) == useritems[-1]:
            if usergems[1] >= 1 and usergems[2] >= 1 and usergems[3] >= 1 and usergems[4] >= 1 and usergems[5] >= 1 and usergems[6] >= 1 and usergems[7] >= 1 and usergems[8] >= 1 and usergems[9] >= 1 and usergems[10] >= 1 and usergems[11] >= 1 and usergems[12] >= 1:
              for x in db["gems"]:
                if x[0] == user:
                  x[1] = x[1] - 1
                  x[2] = x[2] - 1
                  x[3] = x[3] - 1
                  x[4] = x[4] - 1
                  x[5] = x[5] - 1
                  x[6] = x[6] - 1
                  x[7] = x[7] - 1
                  x[8] = x[8] - 1
                  x[9] = x[9] - 1
                  x[10] = x[10] - 1
                  x[11] = x[11] - 1
                  x[12] = x[12] - 1
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-1":
      if useritems == []:
        if usergems[1] >= 1 and usergems[2] >= 1 and usergems[3] >= 1 and usergems[4] >= 1 and usergems[5] >= 1 and usergems[6] >= 1 and usergems[7] >= 1 and usergems[8] >= 1 and usergems[9] >= 1 and usergems[10] >= 1 and usergems[11] >= 1 and usergems[12] >= 1:
          for x in db["gems"]:
            if x[0] == user:
              x[1] = x[1] - 1
              x[2] = x[2] - 1
              x[3] = x[3] - 1
              x[4] = x[4] - 1
              x[5] = x[5] - 1
              x[6] = x[6] - 1
              x[7] = x[7] - 1
              x[8] = x[8] - 1
              x[9] = x[9] - 1
              x[10] = x[10] - 1
              x[11] = x[11] - 1
              x[12] = x[12] - 1
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item! Please remember to use $setgem to set the gem for the pickaxe to mine only.**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-1" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-1" not in str(x) and str(x) == useritems[-1]:
            if usergems[1] >= 1 and usergems[2] >= 1 and usergems[3] >= 1 and usergems[4] >= 1 and usergems[5] >= 1 and usergems[6] >= 1 and usergems[7] >= 1 and usergems[8] >= 1 and usergems[9] >= 1 and usergems[10] >= 1 and usergems[11] >= 1 and usergems[12] >= 1:
              for x in db["gems"]:
                if x[0] == user:
                  x[1] = x[1] - 1
                  x[2] = x[2] - 1
                  x[3] = x[3] - 1
                  x[4] = x[4] - 1
                  x[5] = x[5] - 1
                  x[6] = x[6] - 1
                  x[7] = x[7] - 1
                  x[8] = x[8] - 1
                  x[9] = x[9] - 1
                  x[10] = x[10] - 1
                  x[11] = x[11] - 1
                  x[12] = x[12] - 1
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item! Please remember to use $setgem to set the gem for the pickaxe to mine only.**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    elif arg == "PX-T":
      if useritems == []:
        if usergems[1] >= 1:
          for x in db["gems"]:
            if x[0] == user:
              x[1] = x[1] - 1
              break
          update_itemsdatabase(user, arg)
          await ctx.channel.send("**You have successfully bought the item!**")
        else: 
          await ctx.channel.send("**You do not have enough gems to buy this item!**")
      else:
        for x in useritems:
          if "PX-T" in str(x):
            await ctx.channel.send("**You already have this item!**")
            break
          if "PX-T" not in str(x) and str(x) == useritems[-1]:
            if usergems[1] >= 1:
              for x in db["gems"]:
                if x[0] == user:
                  x[1] = x[1] - 1
                  break
              update_itemsdatabase(user, arg)
              await ctx.channel.send("**You have successfully bought the item!**")
            else: 
              await ctx.channel.send("**You do not have enough gems to buy this item!**")
    #wrong buy argument
    else:
      embed = discord.Embed(
      title="Invalid Argument!", 
      description="**Try:** $buy (*specific_item*) \n **Arguments:** *PX-IR, PX-GO, PX-DI, PX-EM, PX-SA, PX-RU, PX-JA, PX-OP, PX-AM, PX-TO, PX-ON, PX-IC, PX-A, PX-X2, PX-1, PX-T*", 
      color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)

#inventory with everything a user owns
@bot.command()
async def inv(ctx, member: discord.Member = None):
  if member == None:
    user = int(ctx.author.id)
    member = ctx.author
  else:
    user = member.id
  items = db["items"]
  inventory = []
  for x in items:
    if x[0] == user:
      inventory = x
  if ctx.channel.name == "bot_commands":
    string = ""
    counter = 0
    for x in inventory:
      if counter != 0:
        string = string + x + "\n"
      else:
        counter = counter + 1
    tokencount = 0
    for a in db["token"]:
      if a[0] == user:
        tokencount = a[1]
    embed = discord.Embed(
    title=f"{member}'s Inventory:", 
    description=f"*This list shows everything you currently own! The first item is your equipped item.*\n**Tokens: {tokencount}**\n{string}", 
    color=discord.Color.red()
  )
    embed.set_thumbnail(url=member.avatar)  
    embed.set_image(url="attachment://image.png")
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)

#setting gem for PX-1
@bot.command()
async def setgem(ctx, gem=None):
  if ctx.channel.name == "bot_commands":
    itemlist = []
    itemlist = find_user_items(ctx.author.id)
    if itemlist == []:
      await ctx.channel.send("**You do not have PX-1 and cannot set a gem for it to mine!**")
    else:
      have_item = False
      for a in itemlist:
        if "PX-1" in str(a):
          have_item = True
      if have_item == False:
        await ctx.channel.send("**You do not have PX-1 and cannot set a gem for it to mine!**")
      if have_item == True:
        if gem == None:
          embed = discord.Embed(
          title="Missing Argument!", 
          description="**Try:** $setgem (*specific_gem*) \n **Arguments:** *iron, gold, diamond, emerald, sapphire, ruby, jade, opal, amethyst, topaz, onyx, ic*", 
          color=discord.Color.red()
          )
          embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
          await ctx.send(embed=embed)
        elif gem == "iron":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1A"
                  await ctx.channel.send("**Successfully set PX-1 to mine only iron! It has been renamed to PX-1A!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "gold":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1B"
                  await ctx.channel.send("**Successfully set PX-1 to mine only gold! It has been renamed to PX-1B!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "diamond":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1C"
                  await ctx.channel.send("**Successfully set PX-1 to mine only diamond! It has been renamed to PX-1C!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "emerald":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1D"
                  await ctx.channel.send("**Successfully set PX-1 to mine only emerald! It has been renamed to PX-1D!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "sapphire":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1E"
                  await ctx.channel.send("**Successfully set PX-1 to mine only sapphire! It has been renamed to PX-1E!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "ruby":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1F"
                  await ctx.channel.send("**Successfully set PX-1 to mine only ruby! It has been renamed to PX-1F!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "jade":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1G"
                  await ctx.channel.send("**Successfully set PX-1 to mine only jade! It has been renamed to PX-1G!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "opal":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1H"
                  await ctx.channel.send("**Successfully set PX-1 to mine only opal! It has been renamed to PX-1H!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "amethyst":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1I"
                  await ctx.channel.send("**Successfully set PX-1 to mine only amethyst! It has been renamed to PX-1I!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "topaz":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1J"
                  await ctx.channel.send("**Successfully set PX-1 to mine only topaz! It has been renamed to PX-1J!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "onyx":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1K"
                  await ctx.channel.send("**Successfully set PX-1 to mine only onyx! It has been renamed to PX-1K!**")
                  break
                else:
                  counter = counter + 1
              break
        elif gem == "ic":
          for x in db["items"]:
            if x[0] == ctx.author.id:
              counter = 0
              for y in x:
                if "PX-1" in str(y):
                  x[counter] = "PX-1L"
                  await ctx.channel.send("**Successfully set PX-1 to mine only Invisible Crystal! It has been renamed to PX-1L!**")
                  break
                else:
                  counter = counter + 1
              break
        else:
          embed = discord.Embed(
          title="Invalid Argument!", 
          description="**Try:** $setgem (*specific_gem*) \n **Arguments:** *iron, gold, diamond, emerald, sapphire, ruby, jade, opal, amethyst, topaz, onyx, ic*", 
          color=discord.Color.red()
          )
          embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
          await ctx.send(embed=embed)
  
#equipping an item
@bot.command()
async def equip(ctx, item=None):
  if ctx.channel.name == "bot_commands":
    itemlist = []
    itemlist = find_user_items(ctx.author.id)
    if item == None:
      embed = discord.Embed(
      title="Missing Argument!", 
      description="**Try:** $equip (*specific_item*) \n *Please check your inventory for available items to equip using $inv.*", 
      color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    elif itemlist == []:
      await ctx.channel.send("**You do not have this item!**")
    elif item == ctx.author.id:
      await ctx.channel.send("**You do not have this item!**")
    elif "PX-" in item and item in itemlist:
      position = 1
      position = itemlist.index(item)
      temp1 = ""
      temp2 = ""
      if item in itemlist:
        for x in db["items"]:
          if x[0] == ctx.author.id:
            temp1 = x[position]
            temp2 = x[1]
            x[1] = temp1
            x[position] = temp2
            break
        await ctx.channel.send("**You have successfully equipped this item!**")
    else:
      await ctx.channel.send("**You either do not have this item or you cannot equip it!**")

#updating gemstones database
def update_database(user, point):
  new = [user, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  if "gems" in db.keys():
    gems = db["gems"]
    position = 0
    added_user = 0
    for x in gems:
      if x[0] == user:
        gems[position][point] = gems[position][point] + 1
        added_user = 1
        break
      position = position + 1
    if added_user == 0:
      gems.append(new)
      gems[-1][point] = gems[-1][point] + 1
    db["gems"] = gems

#taking data from gemstone database and forming a temporary leaderboard
def leaderboard():
  my_dict = {"ID":[],"IC":[],"Onyx":[],"Topaz":[],"Amethyst":[],"Opal":[],"Jade":[],"Ruby":[],"Sapphire":[],"Emerald":[],"Diamond":[],"Gold":[],"Iron":[]};
  database = []
  if "gems" in db.keys():
    database = db["gems"]
  tempdatabase = []
  for x in database:
    my_dict["ID"].append(x[0])
    my_dict["IC"].append(x[1])
    my_dict["Onyx"].append(x[2])
    my_dict["Topaz"].append(x[3])
    my_dict["Amethyst"].append(x[4])
    my_dict["Opal"].append(x[5])
    my_dict["Jade"].append(x[6])
    my_dict["Ruby"].append(x[7])
    my_dict["Sapphire"].append(x[8])
    my_dict["Emerald"].append(x[9])
    my_dict["Diamond"].append(x[10])
    my_dict["Gold"].append(x[11])
    my_dict["Iron"].append(x[12])
    tempdatabase.append(my_dict)
    my_dict = {"ID":[],"IC":[],"Onyx":[],"Topaz":[],"Amethyst":[],"Opal":[],"Jade":[],"Ruby":[],"Sapphire":[],"Emerald":[],"Diamond":[],"Gold":[],"Iron":[]};
  return tempdatabase

#all possible commands listed in $help
@bot.command()
async def help(ctx):
  if ctx.channel.name == "bot_commands":
    embed = discord.Embed(
      title="Command List:", 
      description="**Prefix ($):** *buy, equip, gem, inv, items, lb, price, profile, setgem, upgrade, upgradecost*", 
      color=discord.Color.red()
      )
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)

#all possible items
@bot.command()
async def items(ctx):
  if ctx.channel.name == "bot_commands":
    embed = discord.Embed(
      title="Items List:", 
      description="**Pickaxes:**\n**PX-GEM:** Increase chance to find the gemstone that the pickaxe is made of by 100%.\n**PX-A:** Increase chance to find any gemstone by 75%. [cannot be upgraded]\n**PX-X2:** Decreases chance to find any gemstone by 25%, but every gem found is doubled. [cannot be upgraded]\n**PX-1:** Increase chance of set gem to be found by 500%, but doesn't find any other gems. [cannot be upgraded]\n**PX-T:** Ability to find tokens when mining. [cannot be upgraded]", 
      color=discord.Color.red()
      )
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(embed=embed)

#gem info
@bot.command()
async def gem(ctx):
  if ctx.channel.name == "bot_commands":
    embed = discord.Embed(
      title="Gem Information:", 
      description="*This list gives information for the possible gems to be obtained.*",
      color=discord.Color.red()
      )
    name1="Iron\nGold\nDiamond\nEmerald\nSapphire\nRuby\nJade\nOpal\nAmethyst\nTopaz\nOnyx\nInvisible Crystal"
    name2="$4\n$10\n$20\n$40\n$100\n$200\n$400\n$1000\n$2000\n$4000\n$10000\n$100000"
    name3="25%\n10%\n5%\n2.5%\n1%\n0.5%\n0.25%\n0.1%\n0.05%\n0.025%\n0.01%\n0.001%"
    img = PIL.Image.new(mode="RGBA", size=(800, 380), color=(0, 0, 0, 0))
    font = ImageFont.truetype("whitneymedium.otf", 24)
    font2 = ImageFont.truetype("whitneybold.otf", 28)
    draw = ImageDraw.Draw(img)
    draw.text((5,0), "Gem:", (220,221,222), font=font2)
    draw.text((325,0), "Worth:", (220,221,222), font=font2)
    draw.text((600,0), "Base Chance:", (220,221,222), font=font2)
    draw.text((5,30), str(name1).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
    draw.text((325,30), str(name2).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
    draw.text((600,30), str(name3).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
    with BytesIO() as image_binary:
      img.save(image_binary, 'PNG')
      image_binary.seek(0)
      file=discord.File(fp=image_binary, filename='image.png')
    embed.set_image(url="attachment://image.png")
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(file=file,embed=embed)

#all item price
@bot.command()
async def price(ctx):
  if ctx.channel.name == "bot_commands":
    embed = discord.Embed(
      title="Pricing List:", 
      description="*This list shows the price of items that you can potentially buy. Once bought, the gems would be deducted from your balance and your networth will also decrease accordingly. Once an item is bought, you have to equip it to use it.*",
      color=discord.Color.red()
      )
    name1="PX-IR\nPX-GO\nPX-DI\nPX-EM\nPX-SA\nPX-RU\nPX-JA\nPX-OP\nPX-AM\nPX-TO\nPX-ON\nPX-IC\nPX-A\nPX-X2\nPX-1\nPX-T"
    name2="200 Iron\n100 Gold\n100 Diamond\n60 Emerald + 150 Iron\n30 Sapphire + 250 Iron\n20 Ruby + 250 Iron\n15 Jade + 500 Iron\n5 Opal + 1250 Iron\n5 Amethyst + 1000 Gold\n150 Sapphire + 100 Emerald + 300 Diamond\n20 Opal + 25 Jade + 50 Ruby\n5 Onyx + 10 Topaz + 5 Amethyst\n1 of every single gem\n1 of every single gem\n1 of every single gem\n1 Invisible Crystal"
    img = PIL.Image.new(mode="RGBA", size=(800, 480), color=(0, 0, 0, 0))
    font = ImageFont.truetype("whitneymedium.otf", 24)
    font2 = ImageFont.truetype("whitneybold.otf", 28)
    draw = ImageDraw.Draw(img)
    draw.text((5,0), "Pickaxe:", (220,221,222), font=font2)
    draw.text((325,0), "Total Price:", (220,221,222), font=font2)
    draw.text((5,30), str(name1).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
    draw.text((325,30), str(name2).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
    with BytesIO() as image_binary:
      img.save(image_binary, 'PNG')
      image_binary.seek(0)
      file=discord.File(fp=image_binary, filename='image.png')
    embed.set_image(url="attachment://image.png")
    embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
    await ctx.send(file=file,embed=embed)
      
#leaderboard command
@bot.command(name='lb')
async def lb(ctx, arg=None):
  if ctx.channel.name == "bot_commands":
    #if no argument for leaderboard provided
    if arg == None:
      embed = discord.Embed(
      title="Missing Argument!", 
      description="**Try:** $lb (*specific_leaderboard*) \n **Arguments:** *nw, iron, gold, diamond, emerald, sapphire, ruby, jade, opal, amethyst, topaz, onyx, ic*", 
      color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
    #if argument is a gemstone
    elif arg == 'iron' or arg == 'gold' or arg == 'diamond' or arg == 'emerald' or arg == 'sapphire' or arg == "ruby" or arg == "jade" or arg == "opal" or arg == "amethyst" or arg == "topaz" or arg == "onyx" or arg == "ic":
      gem = str(arg.title())
      title = ""
      title = gem
      if arg == "ic":
        gem = "IC"
        title = "Invisible Crystal"
      tempdatabase = leaderboard()
      def myFunc(e):
        return e[gem]
      tempdatabase.sort(key=myFunc,reverse=True)
      counttoten = 0
      usernames = ""
      values = ""
      for x in tempdatabase:
        counttoten = counttoten + 1
        output = int(x["ID"][0])
        #when no one is on the leaderboard
        if x[gem][0] == 0 and counttoten == 1:
          embed = discord.Embed(
          title="Empty Leaderboard!", 
          description="**Wow!** *There is no one here! Obtain the item you searched for and be the first one on this leaderboard!*", 
          color=discord.Color.red()
      )
          embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
          await ctx.send(embed=embed)
          break
        #adding people on leaderboard to a string
        if x[gem][0] != 0:
          values = values + str(x[gem][0]) + "\n"
          usernames = usernames + str(bot.get_user(output)) + "\n"
        #printing the leaderboard once everyone required is in the string
        if x[gem][0] == 0 or x == tempdatabase[-1] or counttoten == 10:
          embed = discord.Embed(
          title=f"**{title} Leaderboard:**", 
          description=f"*This leaderboard shows the users with the most amount of {title}!*",
          color=discord.Color.red()
      )     
          img = PIL.Image.new(mode="RGBA", size=(800, 315), color=(0, 0, 0, 0))
          font = ImageFont.truetype("whitneymedium.otf", 24)
          font2 = ImageFont.truetype("whitneybold.otf", 28)
          draw = ImageDraw.Draw(img)
          draw.text((5,0), "User:", (220,221,222), font=font2)
          draw.text((575,0), "Amount:", (220,221,222), font=font2)
          draw.text((5,30), str(usernames).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
          draw.text((575,30), str(values).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
          with BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            file=discord.File(fp=image_binary, filename='image.png')
          embed.set_image(url="attachment://image.png")
          embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
          await ctx.send(file=file,embed=embed)
          break
    #when leaderboard argument is networth
    elif arg == 'nw':
      nwlb = {"ID":[],"value":[]}
      networth = []
      tempdatabase = leaderboard()
      for x in tempdatabase:
        iron = int(x["Iron"][0])
        gold = int(x["Gold"][0])
        diamond = int(x["Diamond"][0])
        emerald = int(x["Emerald"][0])
        sapphire = int(x["Sapphire"][0])
        ruby = int(x["Ruby"][0])
        jade = int(x["Jade"][0])
        opal = int(x["Opal"][0])
        amethyst = int(x["Amethyst"][0])
        topaz = int(x["Topaz"][0])
        onyx = int(x["Onyx"][0])
        ic = int(x["IC"][0])
        value = int(iron)*4 + int(gold)*10 + int(diamond)*20 + int(emerald)*40 + int(sapphire)*100 + int(ruby)*200 + int(jade)*400 + int(opal)*1000 + int(amethyst)*2000 + int(topaz)*4000 + int(onyx)*10000 + int(ic)*100000
        nwlb["ID"].append(x["ID"][0])
        nwlb["value"].append(int(value))
        networth.append(nwlb)
        nwlb = {"ID":[],"value":[]}
      def myFunc(e):
          return e["value"]
      networth.sort(key=myFunc,reverse=True)
      usernames = ""
      values = ""
      counttoten = 0
      for x in networth:
        counttoten = counttoten + 1
        output = int(x["ID"][0])
        #when no one is on the leaderboard
        if x["value"][0] == 0:
          embed = discord.Embed(
          title="Empty Leaderboard!", 
          description="**Wow!** *There is no one here! Obtain some gems and be the first one on this leaderboard!*", 
          color=discord.Color.red()
      )
          embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
          await ctx.send(embed=embed)
          break
        #adding people on leaderboard to a string
        if x["value"][0] != 0:
          values = values + "$" + str(x["value"][0]) + "\n"
          usernames = usernames + str(bot.get_user(output)) + "\n"
        #printing the leaderboard once everyone required is in the string
        if x["value"][0] == 0 or x == networth[-1] or counttoten == 10:
          embed = discord.Embed(
          title=f"**Networth Leaderboard:**", 
          description=f"*This leaderboard shows the users with the highest networth!*",
          color=discord.Color.red()
      )     
          img = PIL.Image.new(mode="RGBA", size=(800, 315), color=(0, 0, 0, 0))
          font = ImageFont.truetype("whitneymedium.otf", 24)
          font2 = ImageFont.truetype("whitneybold.otf", 28)
          draw = ImageDraw.Draw(img)
          draw.text((5,0), "User:", (220,221,222), font=font2)
          draw.text((550,0), "Networth:", (220,221,222), font=font2)
          draw.text((5,30), str(usernames).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
          draw.text((550,30), str(values).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
          with BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            file=discord.File(fp=image_binary, filename='image.png')
          embed.set_image(url="attachment://image.png")
          embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
          await ctx.send(file=file,embed=embed)
          break
    #no leaderboard argument
    else:
      embed = discord.Embed(
      title="Invalid Argument!", 
      description="**Try:** $lb (*specific_leaderboard*) \n **Arguments:** *nw, iron, gold, diamond, emerald, sapphire, ruby, jade, opal, amethyst, topaz, onyx, ic*", 
      color=discord.Color.red()
      )
      embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
      await ctx.send(embed=embed)
      
#profile with everything a user has
@bot.command()
async def profile(ctx, member: discord.Member = None):
  if member == None:
    user = int(ctx.author.id)
    member = ctx.author
  else:
    user = member.id
  if ctx.channel.name == "bot_commands":
    gemlist = ["Iron", "Gold", "Diamond", "Emerald", "Sapphire", "Ruby", "Jade", "Opal", "Amethyst", "Topaz", "Onyx", "IC"]
    gemcounter = 0
    for a in gemlist:
      def myFunc(e):
        return e[a]
      tempdatabase = leaderboard()
      tempdatabase.sort(key=myFunc,reverse=True)
      counter = 0
      for x in tempdatabase:
        counter = counter + 1
        if int(x["ID"][0]) == user and int(x[a][0] != 0):
          gemlist[gemcounter] = int(counter)
          gemcounter = gemcounter + 1
          break
        elif int(x["ID"][0]) == user and int(x[a][0] == 0):
          gemlist[gemcounter] = "None"
          gemcounter = gemcounter + 1
          break
    for x in tempdatabase:
      if int(x["ID"][0]) == user:
        iron = str(x["Iron"][0])
        gold = str(x["Gold"][0])
        diamond = str(x["Diamond"][0])
        emerald = str(x["Emerald"][0])
        sapphire = str(x["Sapphire"][0])
        ruby = str(x["Ruby"][0])
        jade = str(x["Jade"][0])
        opal = str(x["Opal"][0])
        amethyst = str(x["Amethyst"][0])
        topaz = str(x["Topaz"][0])
        onyx = str(x["Onyx"][0])
        ic = str(x["IC"][0])
        value = int(iron)*4 + int(gold)*10 + int(diamond)*20 + int(emerald)*40 + int(sapphire)*100 + int(ruby)*200 + int(jade)*400 + int(opal)*1000 + int(amethyst)*2000 + int(topaz)*4000 + int(onyx)*10000 + int(ic)*100000
        embed = discord.Embed(
        title=f"{member}'s Profile:", 
        description=f"**Networth:** *${value}*\nYour networth is the sum of the values of all the gemstones you currently own!", 
        color=discord.Color.red()
      )
        name1="Iron\nGold\nDiamond\nEmerald\nSapphire\nRuby\nJade\nOpal\nAmethyst\nTopaz\nOnyx\nInvisible Crystal"
        name2=f"{iron}\n{gold}\n{diamond}\n{emerald}\n{sapphire}\n{ruby}\n{jade}\n{opal}\n{amethyst}\n{topaz}\n{onyx}\n{ic}"
        name3=f"{gemlist[0]}\n{gemlist[1]}\n{gemlist[2]}\n{gemlist[3]}\n{gemlist[4]}\n{gemlist[5]}\n{gemlist[6]}\n{gemlist[7]}\n{gemlist[8]}\n{gemlist[9]}\n{gemlist[10]}\n{gemlist[11]}"
        img = PIL.Image.new(mode="RGBA", size=(800, 370), color=(0, 0, 0, 0))
        font = ImageFont.truetype("whitneymedium.otf", 24)
        font2 = ImageFont.truetype("whitneybold.otf", 28)
        draw = ImageDraw.Draw(img)
        draw.text((5,0), "Gemstone:", (220,221,222), font=font2)
        draw.text((250,0), "Amount:", (220,221,222), font=font2)
        draw.text((500,0), "Position:", (220,221,222), font=font2)
        draw.text((5,30), str(name1).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
        draw.text((250,30), str(name2).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
        draw.text((500,30), str(name3).encode('utf-8').decode('utf-8'), (220,221,222), font=font)
        with BytesIO() as image_binary:
          img.save(image_binary, 'PNG')
          image_binary.seek(0)
          file=discord.File(fp=image_binary, filename='image.png')
        embed.set_thumbnail(url=member.avatar)  
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
        await ctx.send(file=file,embed=embed)
        break
      #if user not in database
      elif x == tempdatabase[-1]:
        embed = discord.Embed(
        title="User not in database!", 
        description="**Oh no!** *You need to chat and obtain at least 1 gem to be registered in the database!*", 
        color=discord.Color.red()
      )
        embed.set_footer(text="Shibbot | made by: shibecaisu#8100")
        await ctx.send(embed=embed)
        break

#spawn gem command
@bot.command(name='spawn')
async def spawn(ctx,member: discord.Member=None,gemcode=None,amount=None):
  if ctx.channel.name == "bot_commands":
    if ctx.author.id != 315107540138721280:
      await ctx.channel.send("**You cannot use this command!**")
    else: 
      user = member.id
      for x in db["gems"]:
        if x[0] == user:
          x[int(gemcode)] = x[int(gemcode)] + int(amount)
          break

#on every message this happens
@bot.event
async def on_message(message):
  if message.author.id == None:
    return
  await bot.process_commands(message)
  channel = bot.get_channel(889529318974296105) #change this to logs channel!
  if message.author == bot.user:
    return
  channelcheck = ["bot_commands", "server-logs", "message-logs", "member-logs", "welcome-logs", "management", "music"]
  #if message not in unwanted channels, roll the rng
  iron_chance = 0.25
  gold_chance = 0.1
  diamond_chance = 0.05
  emerald_chance = 0.025
  sapphire_chance = 0.01
  ruby_chance =  0.005
  jade_chance = 0.0025
  opal_chance = 0.001
  amethyst_chance = 0.0005
  topaz_chance = 0.00025
  onyx_chance = 0.0001
  ic_chance = 0.00001
  double_drop_chance = 0
  token_chance = 0
  useritems = []
  useritems = find_user_items(message.author.id)
  if useritems != []:
    if "PX-IR" in useritems[1]:
      iron_chance = iron_chance*2
      if "GOOD" in useritems[1]:
        iron_chance = iron_chance*1.5
      if "PROPER" in useritems[1]:
        iron_chance = iron_chance*1.6
      if "DECENT" in useritems[1]:
        iron_chance = iron_chance*1.7
      if "STRONG" in useritems[1]:
        iron_chance = iron_chance*1.8
      if "POLISHED" in useritems[1]:
        iron_chance = iron_chance*1.9
      if "REFINED" in useritems[1]:
        iron_chance = iron_chance*2
    if "PX-GO" in useritems[1]:
      gold_chance = gold_chance*2
      if "GOOD" in useritems[1]:
        gold_chance = gold_chance*1.5
      if "PROPER" in useritems[1]:
        gold_chance = gold_chance*1.6
      if "DECENT" in useritems[1]:
        gold_chance = gold_chance*1.7
      if "STRONG" in useritems[1]:
        gold_chance = gold_chance*1.8
      if "POLISHED" in useritems[1]:
        gold_chance = gold_chance*1.9
      if "REFINED" in useritems[1]:
        gold_chance = gold_chance*2
    if "PX-DI" in useritems[1]:
      diamond_chance = diamond_chance*2
      if "GOOD" in useritems[1]:
        diamond_chance = diamond_chance*1.5
      if "PROPER" in useritems[1]:
        diamond_chance = diamond_chance*1.6
      if "DECENT" in useritems[1]:
        diamond_chance = diamond_chance*1.7
      if "STRONG" in useritems[1]:
        diamond_chance = diamond_chance*1.8
      if "POLISHED" in useritems[1]:
        diamond_chance = diamond_chance*1.9
      if "REFINED" in useritems[1]:
        diamond_chance = diamond_chance*2
    if "PX-EM" in useritems[1]:
      emerald_chance = emerald_chance*2
      if "GOOD" in useritems[1]:
        emerald_chance = emerald_chance*1.5
      if "PROPER" in useritems[1]:
        emerald_chance = emerald_chance*1.6
      if "DECENT" in useritems[1]:
        emerald_chance = emerald_chance*1.7
      if "STRONG" in useritems[1]:
        emerald_chance = emerald_chance*1.8
      if "POLISHED" in useritems[1]:
        emerald_chance = emerald_chance*1.9
      if "REFINED" in useritems[1]:
        emerald_chance = emerald_chance*2
    if "PX-SA" in useritems[1]:
      sapphire_chance = sapphire_chance*2
      if "GOOD" in useritems[1]:
        sapphire_chance = sapphire_chance*1.5
      if "PROPER" in useritems[1]:
        sapphire_chance = sapphire_chance*1.6
      if "DECENT" in useritems[1]:
        sapphire_chance = sapphire_chance*1.7
      if "STRONG" in useritems[1]:
        sapphire_chance = sapphire_chance*1.8
      if "POLISHED" in useritems[1]:
        sapphire_chance = sapphire_chance*1.9
      if "REFINED" in useritems[1]:
        sapphire_chance = sapphire_chance*2
    if "PX-RU" in useritems[1]:
      ruby_chance = ruby_chance*2
      if "GOOD" in useritems[1]:
        ruby_chance = ruby_chance*1.5
      if "PROPER" in useritems[1]:
        ruby_chance = ruby_chance*1.6
      if "DECENT" in useritems[1]:
        ruby_chance = ruby_chance*1.7
      if "STRONG" in useritems[1]:
        ruby_chance = ruby_chance*1.8
      if "POLISHED" in useritems[1]:
        ruby_chance = ruby_chance*1.9
      if "REFINED" in useritems[1]:
        ruby_chance = ruby_chance*2
    if "PX-JA" in useritems[1]:
      jade_chance = jade_chance*2
      if "GOOD" in useritems[1]:
        jade_chance = jade_chance*1.5
      if "PROPER" in useritems[1]:
        jade_chance = jade_chance*1.6
      if "DECENT" in useritems[1]:
        jade_chance = jade_chance*1.7
      if "STRONG" in useritems[1]:
        jade_chance = jade_chance*1.8
      if "POLISHED" in useritems[1]:
        jade_chance = jade_chance*1.9
      if "REFINED" in useritems[1]:
        jade_chance = jade_chance*2
    if "PX-OP" in useritems[1]:
      opal_chance = opal_chance*2
      if "GOOD" in useritems[1]:
        opal_chance = opal_chance*1.5
      if "PROPER" in useritems[1]:
        opal_chance = opal_chance*1.6
      if "DECENT" in useritems[1]:
        opal_chance = opal_chance*1.7
      if "STRONG" in useritems[1]:
        opal_chance = opal_chance*1.8
      if "POLISHED" in useritems[1]:
        opal_chance = opal_chance*1.9
      if "REFINED" in useritems[1]:
        opal_chance = opal_chance*2 
      if "PERFECT" in useritems[1]:
        opal_chance = opal_chance*3 
    if "PX-AM" in useritems[1]:
      amethyst_chance = amethyst_chance*2
      if "GOOD" in useritems[1]:
        amethyst_chance = amethyst_chance*1.5
      if "PROPER" in useritems[1]:
        amethyst_chance = amethyst_chance*1.6
      if "DECENT" in useritems[1]:
        amethyst_chance = amethyst_chance*1.7
      if "STRONG" in useritems[1]:
        amethyst_chance = amethyst_chance*1.8
      if "POLISHED" in useritems[1]:
        amethyst_chance = amethyst_chance*1.9
      if "REFINED" in useritems[1]:
        amethyst_chance = amethyst_chance*2 
      if "PERFECT" in useritems[1]:
        amethyst_chance = amethyst_chance*3 
    if "PX-TO" in useritems[1]:
      topaz_chance = topaz_chance*2
      if "GOOD" in useritems[1]:
        topaz_chance = topaz_chance*1.5
      if "PROPER" in useritems[1]:
        topaz_chance = topaz_chance*1.6
      if "DECENT" in useritems[1]:
        topaz_chance = topaz_chance*1.7
      if "STRONG" in useritems[1]:
        topaz_chance = topaz_chance*1.8
      if "POLISHED" in useritems[1]:
        topaz_chance = topaz_chance*1.9
      if "REFINED" in useritems[1]:
        topaz_chance = topaz_chance*2 
      if "PERFECT" in useritems[1]:
        topaz_chance = topaz_chance*3 
    if "PX-ON" in useritems[1]:
      onyx_chance = onyx_chance*2
      if "GOOD" in useritems[1]:
        onyx_chance = onyx_chance*1.5
      if "PROPER" in useritems[1]:
        onyx_chance = onyx_chance*1.6
      if "DECENT" in useritems[1]:
        onyx_chance = onyx_chance*1.7
      if "STRONG" in useritems[1]:
        onyx_chance = onyx_chance*1.8
      if "POLISHED" in useritems[1]:
        onyx_chance = onyx_chance*1.9
      if "REFINED" in useritems[1]:
        onyx_chance = onyx_chance*2 
      if "PERFECT" in useritems[1]:
        onyx_chance = onyx_chance*3 
    if "PX-IC" in useritems[1]:
      ic_chance = ic_chance*2
      if "GOOD" in useritems[1]:
        ic_chance = ic_chance*1.5
      if "PROPER" in useritems[1]:
        ic_chance = ic_chance*1.6
      if "DECENT" in useritems[1]:
        ic_chance = ic_chance*1.7
      if "STRONG" in useritems[1]:
        ic_chance = ic_chance*1.8
      if "POLISHED" in useritems[1]:
        ic_chance = ic_chance*1.9
      if "REFINED" in useritems[1]:
        ic_chance = ic_chance*2 
      if "PERFECT" in useritems[1]:
        ic_chance = ic_chance*3 
    if "PX-A" == useritems[1]:
      iron_chance = iron_chance*1.75
      gold_chance = gold_chance*1.75
      diamond_chance = diamond_chance*1.75
      emerald_chance = emerald_chance*1.75
      sapphire_chance = sapphire_chance*1.75
      ruby_chance =  ruby_chance*1.75
      jade_chance = jade_chance*1.75
      opal_chance = opal_chance*1.75
      amethyst_chance = amethyst_chance*1.75
      topaz_chance = topaz_chance*1.75
      onyx_chance = onyx_chance*1.75
      ic_chance = ic_chance*1.75
    if "PX-X2" == useritems[1]:
      iron_chance = iron_chance*0.75
      gold_chance = gold_chance*0.75
      diamond_chance = diamond_chance*0.75
      emerald_chance = emerald_chance*0.75
      sapphire_chance = sapphire_chance*0.75
      ruby_chance =  ruby_chance*0.75
      jade_chance = jade_chance*0.75
      opal_chance = opal_chance*0.75
      amethyst_chance = amethyst_chance*0.75
      topaz_chance = topaz_chance*0.75
      onyx_chance = onyx_chance*0.75
      ic_chance = ic_chance*0.75
      double_drop_chance = 1
    if "PX-1A" == useritems[1]:
      iron_chance = iron_chance*5
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1B" == useritems[1]:
      iron_chance = 0
      gold_chance = gold_chance*5
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1C" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = diamond_chance*5
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1D" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = emerald_chance*5
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1E" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = sapphire_chance*5
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1F" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance = ruby_chance*5
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1G" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = jade_chance*5
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1H" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = opal_chance*5
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1I" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = amethyst_chance*5
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = 0
    if "PX-1J" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = topaz_chance*5
      onyx_chance = 0
      ic_chance = 0
    if "PX-1K" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = onyx_chance*5
      ic_chance = 0
    if "PX-1L" == useritems[1]:
      iron_chance = 0
      gold_chance = 0
      diamond_chance = 0
      emerald_chance = 0
      sapphire_chance = 0
      ruby_chance =  0
      jade_chance = 0
      opal_chance = 0
      amethyst_chance = 0
      topaz_chance = 0
      onyx_chance = 0
      ic_chance = ic_chance*5
    if "PX-T" == useritems[1]:
      token_chance = 0.000025
  if str(message.channel) not in channelcheck:
    if random.random() < token_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found a token!**")
      await message.channel.send(f"*PRAY TO RNGESUS DROP!* **{mention} just found a token!**")
      user = int(message.author.id)
      update_tokendatabase(user,1)
    if random.random() < ic_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found AN INVISIBLE CRYSTAL!**")
      await message.channel.send(f"*PRAY TO RNGESUS DROP!* **{mention} just found AN INVISIBLE CRYSTAL!**")
      user = int(message.author.id)
      point = 1
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found AN INVISIBLE CRYSTAL!**")
        await message.channel.send(f"*PRAY TO RNGESUS DROP!* **{mention} just found AN INVISIBLE CRYSTAL!**")
    if random.random() < onyx_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found an Onyx!**")
      await message.channel.send(f"*CRAZY RARE DROP!* **{mention} just found an Onyx!**")
      user = int(message.author.id)
      point = 2
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found an Onyx!**")
        await message.channel.send(f"*CRAZY RARE DROP!* **{mention} just found an Onyx!**")
    if random.random() < topaz_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found a Topaz!**")
      await message.channel.send(f"*CRAZY RARE DROP!* **{mention} just found a Topaz!**")
      user = int(message.author.id)
      point = 3
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found a Topaz!**")
        await message.channel.send(f"*CRAZY RARE DROP!* **{mention} just found a Topaz!**")
    if random.random() < amethyst_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found an Amethyst!**")
      user = int(message.author.id)
      point = 4
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found an Amethyst!**")
    if random.random() < opal_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found an Opal!**")
      user = int(message.author.id)
      point = 5
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found an Opal!**")
    if random.random() < jade_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found a Jade!**")
      user = int(message.author.id)
      point = 6
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found a Jade!**")
    if random.random() < ruby_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found a Ruby!**")
      user = int(message.author.id)
      point = 7
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found a Ruby!**")
    if random.random() < sapphire_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found a Sapphire!**")
      user = int(message.author.id)
      point = 8
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found a Sapphire!**")
    if random.random() < emerald_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found an Emerald.**")
      user = int(message.author.id)
      point = 9
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found an Emerald.**")
    if random.random() < diamond_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found a Diamond.**")
      user = int(message.author.id)
      point = 10
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found a Diamond.**")
    if random.random() < gold_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found some gold.**")
      user = int(message.author.id)
      point = 11
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found some gold.**")
    if random.random() < iron_chance:
      mention = message.author.mention
      username = str(message.author)
      await channel.send(f"**{username} just found some iron.**")
      user = int(message.author.id)
      point = 12
      update_database(user, point)
      if random.random() < double_drop_chance:
        update_database(user, point)
        await channel.send(f"**{username} just found some iron.**")

#running bot forever
keep_alive()
bot.run(os.getenv('TOKEN'))