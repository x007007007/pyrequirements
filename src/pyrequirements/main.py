import sys
import os
import pkg_resources

def install():
    config_path = os.path.join(os.curdir, "requirements.ini")
    if not os.path.exists(config_path):
        with open(config_path, "w") as fp:
            fp.write(pkg_resources.resource_string("pyrequirements", "requirements.ini.tpl"))

def upgrade(name=None):
    pass


def main():
    if len(sys.argv) > 1:
        if sys.argv[1].strip() == "install":
            install()
        if sys.argv[1].strip() == "upgrade":
            if len(sys.argv) > 2:
                upgrade(sys.argv[2])
            upgrade()

