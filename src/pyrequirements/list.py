from .conf import Conf


def get_requirements():
    conf = Conf()
    print(conf.search(platform="x86", os="Darwin"))
