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

def lines_too_long(filename):
    for line in fileinput.input([filename]):
        if len(line):
            fileinput.close()
            return True
    return False

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    parser.add_argument('--len', dest='length', default=120, type=int, help='max line length')
    args = parser.parse_args(argv)
    text_files = [f for f in args.filenames if is_textfile(f)]
    files_with_too_long_lines = [f for f in text_files if lines_too_long(f)]
    for file in files_with_too_long_lines:
        print('File has lines that are too long: {0}'.format(file))
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
