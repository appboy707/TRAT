poetry run pyinstaller -w -F --name TRAT -i resources/images/logo.ico trat/__main__.py --add-data ".env:."