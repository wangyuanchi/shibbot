# Shibbot

![bot_icon_small.png](bot_icon_small.png)

## Description
Shibbot is a simple discord bot that rewards users for being active by chatting in a server. 

* Everytime a user sends a message, there is a chance for the user to receive different gems with different rarities.

* The user can spend the gems as currency to buy and upgrade pickaxes which increase their chance to find more gems.

* There are different leaderboards for users to compare their collections and networth.

## Set up
1. Go to https://discord.com/developers/applications/, create a new discord bot and add it to a server
2. Go to https://replit.com/ and add the files to a new project
3. Generate a new discord bot token and add it as a new secret in replit
   * ` SECRET_KEY = TOKEN `
4. Go to https://uptimerobot.com/ and add the url of the web server under a new monitor
5. Change line 52 to user_id of an admin and line 712 to a logs channel in the server
   * `if ctx.author.id != 315107540138721280:`
   * `channel = bot.get_channel(890817521152843786)`
6. Create the empty databases
   * `db["gemstone"] = {}, db["item"] = {}`  
7. Ready to go!
