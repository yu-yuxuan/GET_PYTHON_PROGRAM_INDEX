#!/usr/bin/python3
import glob
import os, errno
import re

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured

if __name__ == '__main__':
    filename=input('Enter output file name here(may equal to searchphrase): ') or "test" # "README.org"
    silentremove(filename)
    folder=input('Enter folder  here: ') or "."
    searchphrase=input('Enter search phrase here(^\s*def): ') or "^\s*def" # get_index.py
    fileend=input('Enter file ends with here(.py): ') or ".py" # .py
    pattern = re.compile(searchphrase)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(fileend):
                print(os.path.join(root, file))
                program_file=os.path.join(root, file)
                with open(program_file, "r") as f:
                    searchlines = f.readlines()
                for i, line in enumerate(searchlines):
                    for match in re.finditer(pattern, line):
                        print(searchlines[i])

                    # if searchphrase in line:
                    #     with open(filename, "a") as myfile:
                    #         myfile.write(searchlines[i].rstrip()+'===='+program_file+ '\n')

                        # for l in searchlines[i:i+3]:print(l),


# pattern = re.compile("^def")
# for i, line in enumerate(open('test.txt')):
#     for match in re.finditer(pattern, line):
#         print 'Found on line %s: %s' % (i+1, match.groups())
