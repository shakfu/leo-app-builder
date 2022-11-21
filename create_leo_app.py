#!/usr/bin/env python3

"""create_leo_app.py

A proof-of-concept script to create a minimal leo macos .app bundle
using py2app.

"""

PLUGINS = [
    "contextmenu.py",
    "editpane",
    "free_layout.py",
    "mod_scripting.py",
    "nav_qt.py",
    "nested_splitter.py",
    "nodetags.py",
    "plugins_menu.py",
    "QNCalendarWidget.py",
    "qt_commands.py",
    "qt_events.py",
    "qt_frame.py",
    "qt_gui.py",
    "qt_idle_time.py",
    "qt_quicksearch.py",
    "qt_quicksearch.ui",
    "qt_quicksearch_sub.py",
    "qt_quicksearch_sub.ui",
    "qt_text.py",
    "qt_tree.py",
    "quicksearch.py",
    "threadutil.py",
    "todo.py",
    "ToDo.ui",
    "viewrendered.py",
]

PLUGINS_EXCLUDED = [
    "Backlink.ui",
    "FileActions.py",
    "GraphCanvas",
    "ScrolledMessage.ui",
    "active_path.py",
    "add_directives.py",
    "anki.py",
    "at_folder.py",
    "at_produce.py",
    "at_view.py",
    "attrib_edit.py",
    "auto_colorize2_0.py",
    "backlink.py",
    "baseNativeTree.py",
    "bibtex.py",
    "bigdash.py",
    "bookmarks.py",
    "bzr_qcommands.py",
    "chapter_hoist.py",
    "cke_template.html",
    "colorize_headlines.py",
    "ctagscompleter.py",
    "cursesGui.py",
    "cursesGui2.py",
    "datenodes.py",
    "debugger_pudb.py",
    "demo.py",
    "dragdropgoodies.py",
    "dtest.py",
    "dump_globals.py",
    "empty_leo_file.py",
    "enable_gc.py",
    "example_rst_filter.py",
    "examples",
    "expfolder.py",
    "footprints.ini",
    "free_layout.py",
    "freewin.py",
    "ftp.py",
    "geotag.py",
    "gitarchive.py",
    "graphcanvas.py",
    "history_tracer.py",
    "import_cisco_config.py",
    "importers",
    "initinclass.py",
    "interact.py",
    "jinjarender.py",
    "keys.css",
    "leoGuiPluginsRef.leo",
    "leoOPML.py",
    "leoPluginNotes.txt",
    "leo_babel",
    "leo_cloud.py",
    "leo_cloud_server.py",
    "leo_interface.py",
    "leo_pdf.py",
    "leo_to_html.ini",
    "leo_to_html.py",
    "leo_to_rtf.ini",
    "leo_to_rtf.py",
    "leocursor.py",
    "leofeeds.py",
    "leoflexx.py",
    "leofts.py",
    "leomail.py",
    "leomylyn.py",
    "leoremote.py",
    "leoscreen.py",
    "lineNumbers.py",
    "line_numbering.py",
    "livecode.py",
    "macros.py",
    "markup_inline.py",
    "maximizeNewWindows.py",
    "md_docer.py",
    "mime.py",
    "mnplugins.py",
    "mod_autosave.py",
    "mod_framesize.py",
    "mod_http.py",
    "mod_leo2ascd.py",
    "mod_leo2ascd.txt",
    "mod_read_dir_outline.py",
    "mod_speedups.py",
    "mod_timestamp.py",
    "multifile.py",
    "niceNosent.py",
    "nodeActions.py",
    "nodediff.py",
    "nodewatch.py",
    "notebook.py",
    "obsolete",
    "open_shell.py",
    "outline_export.py",
    "pane_commands.py",
    "paste_as_headlines.py",
    "patch_python_colorizer.py",
    "picture_viewer.py",
    "pluginsManager.txt",
    "pluginsNotes.txt",
    "plugins_menu.py",
    "projectwizard.py",
    "pygeotag",
    "pyplot_backend.py",
    "python_terminal.py",
    "qmlnb",
    "qtGui.py",
    "qtNotes.txt",
    "qt_main.py",
    "qt_main.ui",
    "qt_main_2.ui",
    "qt_main_hardyheron.ui",
    "qt_quickheadlines.py",
    "quickMove.py",
    "quit_leo.py",
    "read_only_nodes.py",
    "redirect_to_log.py",
    "remove_duplicate_pictures.py",
    "richtext.py",
    "rss.py",
    "runGtkDialogs.py.txt",
    "run_nodes.py",
    "screen_capture.py",
    "screencast.py",
    "screenshots.py",
    "script_io_to_body.py",
    "setHomeDirectory.py",
    "settings_finder.py",
    "sftp.py",
    "slideshow.py",
    "spydershell.py",
    "startfile.py",
    "stickynotes.py",
    "stickynotes_plus.py",
    "systray.py",
    "tables.py",
    "test",
    "testRegisterCommand.py",
    "textnode.py",
    "timestamp.py",
    "tomboy_import.py",
    "trace_gc_plugin.py",
    "trace_tags.py",
    "valuespace.py",
    "viewrendered3",
    "viewrendered3.py",
    "vim.py",
    "wikiview.py",
    "word_count.py",
    "word_export.ini",
    "word_export.py",
    "writers",
    "xdb_pane.py",
    "xemacs.py",
    "xml_edit.py",
    "xsltWithNodes.py",
    "zenity_file_dialogs.py",
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
    "flexx",
    "docutils",
]

EXCLUDES = [
    "asttokens",
    "black",
    "build",
    # "docutils",
    # "flexx",
    "jupyter",
    "meta",
    "nbformat",
    "pyenchant",
    "pyflakes",
    "pylint",
    "pyshortcuts",
    "sphinx", # including this causes ImportError: No module named 'sphinxcontrib'
    "tk",
]

SETUP_REQUIRES = [
    "py2app",
    "leo",
    "PyQt5"
]

SETUP_EXTRA = [
    "docutils",
    "jinja2",
    "markdown",
    "nbformat",
    "nbconvert",
    "pyperclip",
    "matplotlib",
]

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
    def __init__(self, app: str, **options):
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
            if p == '__init__.py':
                continue
            if p not in self.plugins:
                target = os.path.join(pluginsdir, p)
                if os.path.isfile(target):
                    os.remove(target)
                    print('removed file:', target)
                else:
                    shutil.rmtree(target)
                    print('removed dir:', target)

    def remove_tests(self, testdir):
        shutil.rmtree(testdir)
        print('removed testdir:', testdir)

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
        self.remove_tests(
            f"{self.venv}/lib/python{self.py_ver}/site-packages/leo/unittests"
        )
        self.create_setup(f"{self.venv}/setup.py")
        self.vcmds(
            [
                f"source {self.venv}/bin/activate",
                f"cd {self.venv}",
                f"python setup.py py2app --iconfile lib/python{self.py_ver}/site-packages/leo/Icons/LeoApp.ico",
            ]
        )


if __name__ == "__main__":
    builder = LeoAppBuilder(app="LeoApp.py")
    builder.build()
