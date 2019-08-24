#!/usr/bin/python3
#
# Copyright (C) 2013 Dimitrios Glentadakis <dglent@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Update translations in po files and prepare the paths for packaging

import os
import glob


PROJECT = 'mga3prepo'

os.system(
    "xgettext -L Python --keyword=_ --output=po/{0}.pot {0}".format(PROJECT)
)
for item in glob.glob1("po", "*.po"):
    print("Updating {0}...".format(item))
    os.system(
        "msgmerge --update --backup=off --no-wrap --sort-by-file po/{0} po/{1}.pot".format(item, PROJECT)
    )

for po_file in glob.glob1("po", "*.po"):
    lang = po_file[:-3]
    try:
        os.makedirs('po/usr/share/locale/{0}/LC_MESSAGES/'.format(lang))
    except:
        print('Directory allready exist')
    print("Installing {0} translations...".format(lang))
    os.system(
        "msgfmt po/{0}.po -o po/usr/share/locale/{0}/LC_MESSAGES/{1}.mo".format(lang, PROJECT)
    )
