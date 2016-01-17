import json

CONFIG_FILE="./config.json"
CONFIG={}

def readConfig(filename) :
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def main() :
    global CONFIG_FILE
    global CONFIG
    CONFIG = readConfig(CONFIG_FILE)

    repos = CONFIG['snapshot']['repos']
    userid = CONFIG['snapshot']['userid']
    pw = CONFIG['snapshot']['passwd']

    print ("repos value : " + repos)
    print ("userid value : " + userid)
    print ("pw value : " + pw)



if __name__ == "__main__":
    main()
