#!/usr/bin/env python3

"""create_leo_app.py

A proof-of-concept script to create a minimal leo macos .app bundle
using py2app.

"""

PLUGINS = [
    "__init__.py",
    "contextmenu.py",
    "mod_scripting.py",
    "nav_qt.py",
    "nodetags.py",
    "plugins_menu.py",
    "quicksearch.py",
    "todo.py",
    "viewrendered.py",
]


LEOAPP_PY = """
import re
import sys
from leo.core.runLeo import run
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\\.pyw|\\.exe)?$', '', sys.argv[0])
    sys.exit(run())
"""

INCLUDES = [
    "PyQt5",
    "PyQtWebEngine",
]

EXCLUDES = [
    "asttokens",
    "black",
    "build",
    "docutils",
    "flexx",
    "jupyter",
    "meta",
    "nbformat",
    "pyenchant",
    "pyflakes",
    "pylint",
    "pyshortcuts",
    "sphinx",
    "sphinx",
    "tk",
]

SETUP_REQUIRES = ["py2app", "leo", "PyQt5"]

SETUP_PY = """
from setuptools import setup
setup(
    app=['{app}'],
    data_files={data_files},
    options=dict(py2app={options}),
    setup_requires={setup_requires}
)
"""

import os
import shutil
import sysconfig


class LeoAppBuilder:
    def __init__(self, app, **options):
        self.app = app
        self.venv = options.get("venv", "leoenv")
        self.plugins = options.get("plugins", PLUGINS)
        self.includes = options.get("includes", INCLUDES)
        self.excludes = options.get("excludes", EXCLUDES)
        self.setup_requires = options.get("setup_requires", SETUP_REQUIRES)
        self.py_ver = sysconfig.get_config_var("py_version_short")

    def cmd(self, shellcmd, *args, **kwds):
        os.system(shellcmd.format(*args, **kwds))

    def vcmds(self, shellcmds, *args, **kwds):
        shellcmd = " && ".join(shellcmds)
        os.system(shellcmd)

    def remove_extra_plugins(self, pluginsdir):
        assert os.path.exists(pluginsdir)
        for p in os.listdir(pluginsdir):
            if p not in self.plugins:
                target = os.path.join(pluginsdir, p)
                if os.path.isfile(target):
                    os.remove(target)
                    print('removed file:', target)
                else:
                    shutil.rmtree(target)
                    print('removed dir:', target)

    def create_launcher(self, path):
        with open(path, "w") as f:
            f.write(LEOAPP_PY)

    def create_setup(self, path):
        setup_py = SETUP_PY.format(
            app=self.app,
            data_files=[],
            options=dict(
                includes=self.includes,
                excludes=self.excludes,
            ),
            setup_requires=self.setup_requires,
        )
        with open(path, "w") as f:
            f.write(setup_py)

    def build(self):
        self.vcmds(
            [
                f"virtualenv {self.venv}",
                f"source {self.venv}/bin/activate",
                "pip install leo py2app",
            ]
        )
        self.create_launcher(f"{self.venv}/{self.app}")
        self.remove_extra_plugins(
            f"{self.venv}/lib/python{self.py_ver}/site-packages/leo/plugins"
        )
        self.create_setup(f"{self.venv}/setup.py")
        self.vcmds(
            [
                f"source {self.venv}/bin/activate",
                f"cd {self.venv}",
                f"python setup.py py2app --iconfile lib/python{self.py_ver}/site-packages/leo/Icons/LeoApp.ico",
            ]
        )
        print("DONE")


if __name__ == "__main__":
    builder = LeoAppBuilder(app="LeoApp.py")
    builder.build()
