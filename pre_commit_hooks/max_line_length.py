from __future__ import print_function
import argparse, fileinput, sys
import string

KNOWN_BINARY_FILE_EXT = ['.pdf']
ALLOWED_NON_PRINTABLE_THRESHOLD = 0.15

def is_textfile(filename, blocksize=512):
    if any(filename.endswith(ext) for ext in KNOWN_BINARY_FILE_EXT):
        return False
    return is_text(open(filename).read(blocksize))

def is_text(stuff):
    if "\0" in stuff:
        return False
    if not stuff:  # Empty files are considered text
        return True
    # Get the non-text characters (maps a character to itself then
    # use the 'remove' option to get rid of the text characters.)
    non_printable_chars = ''.join(c for c in stuff if c not in string.printable)
    return len(non_printable_chars) / len(stuff) < ALLOWED_NON_PRINTABLE_THRESHOLD

def lines_too_long(filename, length):
    too_long = [] 
    i = 1
    for line in fileinput.input([filename]):
        if len(line) > length:
            too_long.append(str(i))

        i += 1

    fileinput.close()
    if len(too_long) > 0:
        return too_long
    return False

def main(argv=None):
    rv = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    parser.add_argument('--len', dest='length', default=120, type=int, help='max line length')
    args = parser.parse_args(argv)
    text_files = [f for f in args.filenames if is_textfile(f)]
    for file in text_files:
        lines = lines_too_long(file, args.length)
        if lines:
            print('Line {1} too long: {0}'.format(file, ",".join(lines)))
            rv = 1
    return rv

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
