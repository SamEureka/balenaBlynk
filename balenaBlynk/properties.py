import configparser as CFG
import json
import os

# Init the config parser
config = CFG.ConfigParser()
config.optionxform = lambda option: option
config['blynk'] = {}

with open('blynk.json') as b:
  blynkvars = json.load(b)
def vConf (balena_d,ini_d,section_d,default_d):
  def bConf(balena_d, default_d):
    return os.environ[balena_d] if balena_d in os.environ else default_d
  config[section_d][ini_d] = bConf(balena_d, default_d)
for blynk in blynkvars['variables']:
  vConf(blynk['balena'], blynk['ini'], blynk['section'], blynk['default'])
with open('server.properties', 'w') as configfile:
  config.write(configfile)

