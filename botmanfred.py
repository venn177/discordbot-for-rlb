# coding=utf8

import dataset
import discord
import importlib
import os
import random
import re
import sys
import time
from datetime import datetime
from glob import glob
from pymarkovchain import MarkovChain
from random import randint

bot = discord.Client()
bot.login('', '')

#db = dataset.connect('sqlite:///rlb.db')

#importlib.import_module("plugins")
mc = MarkovChain()
currentDirectory = sys.path[0] + "\\"
try:
	with open(currentDirectory + "logpruned.txt", 'r',  encoding="utf8") as log:
		thelog = log.read()
	mc.generateDatabase(thelog)
except Exception as e:
	print("Issue with markov database: {0}".format(e))

db = dataset.connect('sqlite:///rlb.db')
userTable = db['users']

#for plugin in glob("C:/Python35/discordbot/plugins/[!_]*.py"):
#	module = 'plugins.' + plugin[31:-3]
#	print(module)
#	print(plugin)
#	try:
#		importlib.import_module(module)
#	except Exception as e:
#		print('Failed to import {0}: {1}'.format(plugin, e))

@bot.event
def on_message(message):
	currentTime = '[' + str(datetime.now().strftime("%H:%M:%S")) + '] '
	print(currentTime + str(message.author) + ': ' + message.content)
	botUserCheck = str(bot.user)
	if message.author == bot.user:
		return
	if message.content.startswith('/shrug'):
		bot.delete_message(message)
		bot.send_message('rlb', "¯\_(ツ)_/¯")
		return
	with open(currentDirectory + "log.txt", "a", encoding="utf8") as myfile:
		myfile.write(currentTime + str(message.author) + ': ' + message.content + '\n')
	with open(currentDirectory + "logpruned.txt", "a", encoding="utf8") as myfile:
		myfile.write(message.content + ' ')
#	add_experience(message.author)
	messageCheck = message.content.lower()
	if message.content.startswith('!roll'):
		roll(messageCheck, message)
	if message.content.startswith('!dustydice'):
		dustydice(messageCheck, message)
	if message.content.startswith('!kidsjoke'):
		line = random.choice(open(currentDirectory + "jokes.txt").readlines())
		question, answer = map(str, line.split('? '))
		bot.send_message(message.channel, question + '?')
		time.sleep(6)
		bot.send_message(message.channel, answer)
	if message.content.startswith('!pp'):
		nameSearch = str(message.content[4:])
		if nameSearch == "":
			user = userTable.find_one(username = message.author)
		else:
			user = userTable.find_one(username = nameSearch)
		if user != None:
			bot.send_message(message.channel, nameSearch + " has **" + str(user['total_points']) + "** PP.")
		else:
			bot.send_message(message.channel, "Name not found, try again. Make sure you use correct capilization.")
	if "mike trout" in messageCheck:
		bot.send_message(message.channel, "THAT'S THE G.O.A.T. TO YOU, {}!".format(message.author))
	if "ayy lmao" in messageCheck:
		ayyrandom = random.choice(('http://i.imgur.com/YSTLdza.jpg', 'http://i.imgur.com/V0V2B95.png', 'http://i.imgur.com/5zXv7VW.jpg', 'http://i.imgur.com/m3xtlO5.gif', 'http://i.imgur.com/7qM5R1g.png', 'http://i.imgur.com/JcOhXAp.gif', 'http://i.imgur.com/FMyZRBF.png', 'http://i.imgur.com/cMfMs7C.png', 'http://i.imgur.com/DTZpeZw.jpg', 'http://i.imgur.com/A59LSFx.png', 'http://i.imgur.com/OMxngaL.gif', 'http://i.imgur.com/Q9FMeEq.gif', 'http://i.imgur.com/oTg6iX7.gif', 'http://i.imgur.com/JcOhXAp.gif', 'http://i.imgur.com/QJLAFJW.gif', 'http://i.imgur.com/Yg5cJrY.png', 'http://i.imgur.com/AcnGuxb.png', 'http://i.imgur.com/RFw4wKS.png', 'http://i.imgur.com/ndl6i6q.png', 'http://i.imgur.com/2onOSUg.png', 'http://i.imgur.com/6Toewfr.png', 'http://i.imgur.com/BWToRIa.png', 'http://i.imgur.com/K9K7Co2.png', 'http://i.imgur.com/BPVmCph.png', 'http://i.imgur.com/FG7oxbz.png', 'http://i.imgur.com/KzIJxxs.png', 'http://i.imgur.com/wT8NgZT.png'))
		bot.send_message(message.channel, ayyrandom)
	if "doot doot" in messageCheck:
		skeltalrandom = random.choice(('http://i.imgur.com/TyR727g.jpg', 'https://41.media.tumblr.com/fd40ee2298e9200ff0850c430fcb9197/tumblr_nihhr7F1ZJ1tlpu2to3_540.jpg', 'Watch out fuccboi! https://i.imgur.com/S9fEydK.gif', 'http://i.imgur.com/kSl51gS.jpg', 'http://i.imgur.com/5w26yNa.jpg', 'http://i.imgur.com/3KudVwC.gif', 'http://i.imgur.com/dBUcXxW.gif', 'http://i.imgur.com/YeBSRwv.png', 'http://i.imgur.com/sXSvQGp.jpg', 'UNACCEPTABLE: http://i.imgur.com/UtOPvpF.jpg', 'https://33.media.tumblr.com/6dfdbb8dc857d55f04ee9c50e32e1ecd/tumblr_nd69kiE8Gb1qiz7imo1_500.gif', 'I am doot. http://i.imgur.com/uTzeLBz.jpg', 'http://i.imgur.com/q1iFS6P.jpg', 'http://i.imgur.com/KsLo7yM.png', 'http://i.imgur.com/CaEnKGu.png', 'http://i.imgur.com/6uNAzI3.jpg', 'http://i.imgur.com/wwdKB6a.png', 'http://i.imgur.com/98CqQj2.gif', 'TFW No Calcium: https://i.imgur.com/B92ZjT3.gif', 'http://i.imgur.com/x29nKdO.jpg', 'http://i.imgur.com/9pPcILj.jpg', 'http://i.imgur.com/KpY8R92.jpg', 'http://i.imgur.com/9PMdnoL.jpg', 'http://i.imgur.com/rQOsadt.png', 'http://i.imgur.com/ujNM6Dp.jpg', 'http://i.imgur.com/735CLv5.jpg', 'http://i.imgur.com/Nm9hWOt.jpg', 'http://i.imgur.com/8wMO5cS.jpg', 'http://i.imgur.com/nN49tnJ.png', 'http://i.imgur.com/t8IyHAB.gif'))
		bot.send_message(message.channel, skeltalrandom)
	if "38 bucks" in messageCheck:
		_38var = random.choice(('http://i.imgur.com/EpJNnSb.jpg', 'http://i.imgur.com/dRFEB9y.png', 'http://i.imgur.com/58zYhxl.png', 'http://i.imgur.com/HywGed2.png'))
		bot.send_message(message.channel, _38var)
	if "fuck the emps" in messageCheck:
		empirefuck = random.choice(('DAE RBIs > OPS??', 'I make Harold Reynolds look like he knows what he\'s talking about!', 'Triple crown = auto MVP, who needs to think??', 'Jon Lester is shit because he didn\'t get the Athletics into the playoffs against the Royals. He might as well kill himself! Despite the OVERWHELMING evidence that he was more useful to the team down the stretch than Yoenis Cespedes, the Athletics completely gimped their future and playoff chances by acquiring a better player!'))
		bot.send_message(message.channel, empirefuck)
	thenumber = randint(1,51)
	if botUserCheck.lower() in messageCheck:
		thenumber = randint(1,2)
		if thenumber == 1:
			time.sleep(randint(1,4))
			print("Markov time!")
			bot.send_message(message.channel, mc.generateString())
			return
	elif thenumber < 4:
		print("Markov time!")
		time.sleep(randint(1,4))
		bot.send_message(message.channel, mc.generateString())

def roll(messageCheck, message):
	dice = messageCheck[6:]
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		bot.send_message(message.channel, 'Format has to be in XdY!')
		return

	if rolls > 100 or limit > 100:
		bot.send_message(message.channel, "Jesus fucking christ, that's too much rolling you spamming motherfucker.")
		return

	dicerolls = []
	result = ""

	for n in range(0, rolls):
		dicerolls.append(randint(1, limit))

	result += " = %s" % sum(dicerolls)

	bot.send_message(message.channel, str(dicerolls) + result)
	return

def dustydice(messageCheck, message):
	player = ["", "", "", "", "", "", "", "", ""]
	position = ["C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH"]
	dustydice = message.content[11:]
	i = 0
	result = ""
	try:
		player[0], player[1], player[2], player[3], player[4], player[5], player[6], player[7], player[8] = map(str, dustydice.split(', '))
	except Exception:
		bot.send_message(message.channel, 'I need exactly 9 names, separated by a comma, like so: De Mesquites, Rickard, Etc.')
		return

	while i != 9:
		i += 1
		randPlayer = randint(0,len(player) - 1)
		randPos = randint(0,len(position) - 1)
		result += str(i) + ". " + position[randPos] + " " + player[randPlayer] + " "
		player.pop(randPlayer)
		position.pop(randPos)
	bot.send_message(message.channel, result)
	return

#def add_scores(xpUsername):
#	user = db['users'].find_one(username = xpUsername)
#	if user != None:
#		new_points = user['total_experience'] + points
#		data = dict(id = user['id'], total_points = new_points)
#	else:
#		data = dict(username = xpUsername, total_points = points)
#		db['users'].insert(data)


@bot.event
def on_ready():
	print('Logged in as ' + str(bot.user.name) + ' (' + bot.user.id + ')')

def main():
	while True:
		try:
			bot.run()
		except Exception as e:
			print('Unhandled exception: {}'.format(e))
			pass

if __name__ == "__main__":
	main()
