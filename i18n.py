#!/usr/bin/python3

# Update translations in po files and prepare the paths for packaging

import os
import glob


PROJECT = 'mga3prepo'

os.system("xgettext -L Python --keyword=_ --output=po/{0}.pot {1}".format(PROJECT, PROJECT))
for item in glob.glob1("po", "*.po"):
    print("Updating {0}...".format(item))
    os.system("msgmerge --update --backup=off --no-wrap --sort-by-file po/{0} po/{1}.pot".format(item, PROJECT))

for po_file in glob.glob1("po", "*.po"):
    lang = po_file[:-3]
    try:
        os.makedirs('po/usr/share/locale/{0}/LC_MESSAGES/'.format(lang))
    except:
        print('Directory allready exist')
    print("Installing {0} translations...".format(lang))
    os.system("msgfmt po/{0}.po -o po/usr/share/locale/{1}/LC_MESSAGES/{2}.mo".format(lang, lang, PROJECT))
