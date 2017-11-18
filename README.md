# PyRequirements

PyRequirements is requirement packages version management.

If you have a large python progress, you will face to manage python
library requirement.
Keep these third part library newest and without conflict are
hard work.
PyRequirements aim to automatic generate requirement infomation,
check up mostly requirement conflict

## Install and Usage

1. `./setup.py install`
1. `pyrequirements install` this command help to generate requirements.ini
1. Edit requirements.ini. You should write name of your progress relied, rather then package stay in environment.
1. `pyrequirements show` Test version infomation
1. Edit your ./setup.py

        from pyrequirements import get_requirements
        # ... other code

        setup(
            # ... other arguments
            version = versioneer.get_version(),
            # ... other agruments
        )


## TODO
1. Requirements of required install package conflict check
1. Install package module and python package conflict check
1. Auto Update


