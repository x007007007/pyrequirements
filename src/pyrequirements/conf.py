import os
try:
    from ConfigParser import ConfigParser
except:
    from configparser import ConfigParser
import re
from collections import OrderedDict


class Conf(object):
    def __init__(self):
        self.index = {}
        self.configs = {}

        self.get_config()

    def get_config(self):
        config_path = os.path.join(os.curdir, "requirements.ini")
        config = ConfigParser()
        with open(config_path) as fp:
            if hasattr(config, "read_file"):
                config.read_file(fp)
            else:
                config.readfp(fp)
        for section_name in config.sections():
            index = self.index_name(section_name)
            self.index[section_name] = index
            rules = self.requirements_engine(config.items(section_name))
            self.configs[section_name] = rules

    def index_name(self, rule_str):
        index = {}
        for rule in rule_str.split(";"):
            if "generate" == rule:
                return index
            if ":" in rule:
                k, v = rule.split(":", 1)
                index[k] = v.split(",")
        return index

    def requirements_engine(self, raws):
        reqs = []
        for raw_key, raw_value in raws:
            res = re.match(r"^(?:(?P<id>\d+)\.)?\s*(?P<cmd>\w+)(?:\>\s*(?P<arg>.*))?$", raw_key, re.I)
            if not res:
                raise KeyError(raw_key)
            dictres = res.groupdict()
            dictres['value'] = raw_value
            reqs.append(dictres)
        reqs.sort(lambda x, y: cmp(x.get('id', 0), y.get('id', 0)))
        return reqs

    def get_requirements(self, section_name):
        requirements = OrderedDict()
        dependence = OrderedDict()
        for config in self.configs[section_name]:
            cmd = config['cmd']
            arg = config['arg']
            value = config['value']
            if cmd == "pip":
                requirements[arg] = value
            if cmd == "git":
                dependence[arg] = value
        return requirements, dependence

    def search(self, platform=None, os=None, env=None, pyenv=None, **kwargs):
        if platform:
            kwargs['platform'] = platform
        if os:
            kwargs['os'] = os
        if env:
            kwargs['env'] = env
        if pyenv:
            kwargs['pyenv'] =pyenv
        requirement = {}
        requirement_git = {}
        search_dict = dict(self.index)
        for section_name, index in search_dict.items():
            if not section_name == "generate":
                matched = True
                for k, v in kwargs.items():
                    if k in index:
                        if v not in index[k]:
                            matched = False
                            break
                if not matched:
                    continue
            req, req_git = self.get_requirements(section_name)
            print req, req_git
            requirement.update(req)
            requirement_git.update(req_git)
        return requirement, requirement_git

