#  Create a dictionary for a bot
bot = {
    'speed': 70,
    'reaction': 50,
    'stamina': 100,
    'health': 100,
    'name': 'pesky',
}

#  Create 100 bots
hundred_bots = []
for bots in range(0, 100):
    hundred_bots.append(bot.copy())

#  Change a few bots
hundred_bots[3]['health']=45
hundred_bots[6]['name']='head of the bots'

for b in hundred_bots:
    print(b)