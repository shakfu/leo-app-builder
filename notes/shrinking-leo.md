# notes on shrinking leo to a minimum

## Dependency mgmt

These in leo's `setup.py` file:

```
install_requires = [
    'PyQt5 >= 5.15',  # #2884: reuire v5.15. #1217: require v5.12+.
    'PyQtWebEngine',  # #1202 QtWebKit needs to be installed separately starting Qt 5.6
    'asttokens',  # abstract syntax tree text parsing
    'build >= 0.6.0',  # simple PEP 517 package builder
    'docutils',  # used by Sphinx, rST plugin
    'flexx',  # for LeoWapp browser gui
    'meta',  # for livecode.py plugin, which is enabled by default
    'nbformat',  # for Jupyter notebook integration
    'pylint', 'pyflakes', 'black',  # coding syntax standards
    'pyenchant',  # The spell tab.
    'pyshortcuts >= 1.7',  # desktop integration (#1243)
    'sphinx',  # rST plugin
    'tk',  # tkinter.
    'windows-curses; platform_system=="Windows"',  # for console mode on Windows
]
```

- asstoken: module
- 


## These are in `leoenv/lib/python3.10/site-packages`
```
224.8	PyQt5/Qt5/lib/QtWebEngineCore.framework
4.9		PyQt5/Qt5/lib/QtDesigner.framework
4.7		PyQt5/Qt5/lib/QtQml.framework
2.1		PyQt5/Qt5/lib/QtLocation.framework
2.1		PyQt5/Qt5/lib/QtQuickTemplates2.framework
1.6		PyQt5/Qt5/lib/QtNetwork.framework
0.67	PyQt5/Qt5/lib/QtBluetooth.framework
0.50	PyQt5/Qt5/lib/QtWebEngine.framework
0.34	PyQt5/Qt5/lib/QtWebEngineWidgets.framework
		PyQt5/Qt5/lib/QtQuick.framework


23.1	PyQt5/Qt5/qml

7.3		PyQt5/Qt5/plugins/geoservices

0.9		PyQt5/Qt5/QtQuick.abi3.so
0.9		PyQt5/Qt5/QtNetwork.abi3.so
0.9		PyQt5/Qt5/QtQml.abi3.so
0.4		PyQt5/Qt5/QtBluetooth.abi3.so
0.4		PyQt5/Qt5/QtDesigner.abi3.so
0.4		PyQt5/Qt5/QtSql.abi3.so
0.3		PyQt5/Qt5/QtWebEngineWidgets.abi3.so
0.2		PyQt5/Qt5/QtWebEngineCore.abi3.so

```


