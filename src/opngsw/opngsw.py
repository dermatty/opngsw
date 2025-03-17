import requests, configparser, sys, json, warnings
from os.path import expanduser

warnings.filterwarnings("ignore")

userhome = expanduser("~")
maindir = userhome + "/.opngsw/"
cfg_file = maindir + "config"
# read interval & weburls config
try:
    cfg = configparser.ConfigParser()
    cfg.read(cfg_file)

    api_key = cfg["api"]["key"]
    api_secret = cfg["api"]["secret"]
    url = cfg["general"]["url"]
except Exception as e:
    print("Error " + str(e) + ", exiting ...")
    sys.exit()
r = requests.get(url, verify=False, auth=(api_key, api_secret))
rj = json.loads(r.text)["rows"]

if0 = sys.argv[1]

for r0 in rj:
    if r0["disabled"] or r0["name"] != if0:
        continue

    if "online" in r0["status"].lower():
        print("online")
        sys.exit(0)
    else:
        sys.exit(1)
sys.exit(0)