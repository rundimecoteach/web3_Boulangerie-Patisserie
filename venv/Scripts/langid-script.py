#!C:\Users\Dylan\PycharmProjects\TPScrapping\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'langid==1.1.6','console_scripts','langid'
__requires__ = 'langid==1.1.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('langid==1.1.6', 'console_scripts', 'langid')()
    )
