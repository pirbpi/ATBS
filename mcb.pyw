#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword string to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip,sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    shelfKeywords = list(mcbShelf.keys())
    for i in range(len(shelfKeywords)):
        del mcbShelf[shelfKeywords[i]]
elif len(sys.argv) == 2:
    # TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
