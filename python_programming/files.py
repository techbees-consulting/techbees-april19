# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:28:23 2019

@author: ak
"""

"""
Python, a file operation takes place in the following order.

1. Open a file
2. Read or write (perform operation)
3. Close the file
"""

#os is python builtin library to work on directories and file systems
import os
#list of os operations
os.getcwd()
os.chdir()
os.listdir()
os.rename('file1','file2')
os.system('cmd') #copy file1 file2

f = open("test_fileio.txt","w")



    

"""
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode. (while working with image/audio/video data)
'+'	Open a file for updating (reading and writing)
"""

f.write('first line \n')
f.write('second line')
f.close()

f = open("test_fileio.txt","r")
f.read()
f1 = open("C:/Users/ak/Desktop/techbees/batch-02/code/python_programming/test_fileio.txt",'a')

f1.write('\nthird line')

f1.close()

fr = open("test_fileio.txt","r")
fr.read(4)
fr.seek(0)
fr.read(5)

fr.readline()
fr.seek(0)

for line in fr.readlines():
    print(line)
    
fr.close()

with open('filedata.txt','w') as fd:
          fd.write('writing a line \n')
          fd.write('using WITH \n')
          fd.write('you don\'t need to close file explicitly')

fr.tell()
fr.seek(0)
fr.close()

with open('test_fileio.txt') as fr:
    a=fr.readlines()
    print(a)

for line in open('test_fileio.txt'):
    print(line)