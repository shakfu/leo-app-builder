#!/usr/bin/env python3

"""create_leo_app.py

A proof-of-concept script to create a minimal leo macos .app bundle
using py2app.

"""

PLUGINS = [
    '__init__.py',
    'contextmenu.py',
    'mod_scripting.py',
    'nav_qt.py',
    'nodetags.py',
    'plugins_menu.py',
    'quicksearch.py',
    'todo.py',
    'viewrendered.py',
]


LEOAPP_PY = """
import re
import sys
from leo.core.runLeo import run
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\\.pyw|\\.exe)?$', '', sys.argv[0])
    sys.exit(run())
"""

SETUP_PY = """

from setuptools import setup


APP = ['LeoApp.py']
DATA_FILES = []
OPTIONS = {
    'includes': [
        'PyQt5',
        'PyQtWebEngine',
    ],

    'excludes': [
        'asttokens',
        'build',
        'flexx',
        'meta',
        'jupyter',
        'nbformat',
        'pyflakes',
        'pyshortcuts',
        'black',
        'sphinx',
        'pyenchant',
        'pylint',
        'tk',
        'sphinx',
        'docutils',
    ],
}



setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=[
        'py2app',
        'leo',
        'PyQt5',
    ],
)
"""

import os, shutil, sysconfig

PY_VER = sysconfig.get_config_var('py_version_short')


def cmd(shellcmd, *args, **kwds):
    os.system(shellcmd.format(*args, **kwds))

def vcmds(shellcmds, *args, **kwds):
    shellcmd = " && ".join(shellcmds)
    os.system(shellcmd)

def remove_extra_plugins(pluginsdir):
    assert os.path.exists(pluginsdir)

    for p in os.listdir(pluginsdir):
        if p not in PLUGINS:
            print('removing', p)
            target = os.path.join(pluginsdir, p)
            shutil.rmtree(target, ignore_errors=True)

def create_launcher(path):
    with open(path, 'w') as f:
        f.write(LEOAPP_PY)


def create_setup(path):
    with open(path, 'w') as f:
        f.write(SETUP_PY)


def create_leo_virtualenv(venv='leonv', app='LeoApp.py'):

    vcmds([
        f'virtualenv {venv}', 
        f'source {venv}/bin/activate',
        'pip install leo py2app',
    ])
    create_launcher(f'{venv}/{app}')
    remove_extra_plugins(f'leonv/lib/python{PY_VER}/site-packages/leo/plugins')
    create_setup(f'{venv}/setup.py')
    vcmds([
        f'source {venv}/bin/activate',
        f'cd {venv}',
        f'python setup.py py2app --iconfile lib/python{PY_VER}/site-packages/leo/Icons/LeoApp.ico',
    ])
    print("DONE")

if __name__ == '__main__':
    create_leo_virtualenv()

