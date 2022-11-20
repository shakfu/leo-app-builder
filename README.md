# leo-app-builder

A python script to build [leo-editor](https://www.leoeditor.com) as a macOS `.app` bundle using [py2app](https://github.com/ronaldoussoren/py2app).

This script arose out of a brief but fruitful [discussion](https://github.com/leo-editor/leo-editor/issues/2966) with Thomas Passin on the [leo-editor repo](https://github.com/leo-editor/leo-editor).

## Usage

It's pretty simple:

```bash

python3 create_leo_app.py

```

This will create a virtualenv called `leonv`, and after it concludes you should find `LeoApp.app` in `leonv/dist`.


## TODO

- [ ] turn it into a class
- [ ] test test test
- [ ] add plugins incrementally



## Licensing

The contents of this repo are placed in the public domain.
