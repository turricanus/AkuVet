# from qtpy import QtCore
# import pyside2


# uic.compileUiDir("ui")


import pyqt5ac


def main():
    pyqt5ac.main(uicOptions='--from-imports', force=False, initPackage=True, ioPaths=[
        ['ui/*.ui', 'ui/%%FILENAME%%_ui.py'],
        ['ui/resources/*.qrc', 'ui/%%FILENAME%%_rc.py'],
        ['modules/*/*.ui', '%%DIRNAME%%/ui/%%FILENAME%%_ui.py'],
        ['modules/*/resources/*.qrc', '%%DIRNAME%%/ui/%%FILENAME%%_rc.py']
    ])


if __name__ == '__main__':
    main()
