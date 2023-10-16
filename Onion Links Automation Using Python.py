Import requests
Import random
Import re

def scrape (newdata):
	yourquery = newdata

	if " " in yourquery:
		yourquery = yourquery. replace(" ", "+")
url = "https://ahmia.fi/search/?q={}".format(yourquery)
request = requests.get(url)
content = request.text
regexquery = "\w+\.onion"
mineddata = re.findall (regexquery, content)

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

newdata=input(" [*]Please Enter Your Query: ")
scrape (newdata)
