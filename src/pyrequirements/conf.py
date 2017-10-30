import os
try:
    from ConfigParser import ConfigParser
except:
    from configparser import ConfigParser

class Conf(object):

    def __init__(self):
        self.get_config()
        self.index = {}

    def get_config():
        config_path = os.path.join(os.curdir, "requirements.ini")
        config = ConfigParser()
        with open(config_path) as fp:
            config.readfp(fp)
        for section_name in config.sections():
            index = self.index_name(sections_name)

    def index_name(self, rulestr):
        for rule in rulestr.split(";"):
            k, v = rule.split(":", maxsplit=1)
            self.index[k]
