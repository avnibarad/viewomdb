import getopt, sys
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
argumentList="avengers"
print(argumentList)
#pip install omdb

import omdb
omdb.set_default('apikey', 
"b1b6806f")
#client = omdb.OMDBClient(apikey="b1b6806f")
response= omdb.search(argumentList,tomatoes=True)
print(response)
#print(client.get(title='True Grit',tomatoes=True))
