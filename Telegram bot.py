Import requests
Import random
Import re
Import telebot
#pip install telebot

BOT_TOKEN = '6146129471 :AAESSOHNJPNLPdJm9dLNmNWWW9dVGnFUdRg'
# BOT_Token, we can get from Telegram channel BotFather

bot = telebot.TeleBot(BOT_TOKEN)

@bot .message_handler(commands=['start', 'hello']) 
def send_welcome(message):
	bot. reply_to (message,"""Welcome to Dark Web OSINT
/darkweb (search)
Example: /darkweb credit cards
Created By CTI
				""" )

@bot.message_handLer(commands=['darkweb, 'getonions'])
def send_welcome(message):
	bot.reply_to(message,"[+] Getting Links")
	data=message.text
	newdata=data.replace('/darkweb','')
	bot.reply_to(message, scrape(newdata))
	bot.reply_to(message,"[!] You Need TOR To Access Oninon Links")

def scrape (newdata):
	yourquery = newdata
	#yourquery = "Croatia Index Of"

	if " " in yourquery:
		yourquery = yourquery. replace(" ", "+")
	url = "https://ahmia.fi/search/?q={}".format(yourquery)
	request = requests.get(url)
	content = request.text
	regexquery = "\w+\.onion"
	mineddata = re.findall(regexquery, content)

	n=random.randint(1, 9999)

	filename = "sites{}.txt".format(str (n))
	print ("Saving to …", filename)
	mineddata = list(dict.fromkeys(mineddata))

	for k in mineddata:
		with open(filename, "a") as newfile:
			k=k + "\n"
			newfile.write(k)
	print("All the files written to a text file", filename)

	with open(filename) as input_file:
		head = [next(input_file) for x in range (5)]
		contents = '\n'.join(map(str, head))
		print(contents)

	Return contents

bot.infinity_polling()
