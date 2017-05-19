'''
Script Name: digraph.py
Version: 1
Revised Date: 09/12/2014
Python Version: 2
Description: A digraph plotter for sequential byte visualization
Copyright: 2015 Mike Felch <mike@linux.edu> 
URL: http://www.forensicpy.com/
--
- ChangeLog -
v1 - [09-12-2014]: Wrote original code
'''

import array, sys

if len(sys.argv) > 1:
  filename = str(sys.argv[1])
else:
  sys.exit('Requires a filename.\nexample: ' + str(sys.argv[0]) + ' test.png\n')

def Hex(byte):
  b = ''.join(["%02X"% ord(h) for h in byte]).strip()
  b = '0x{0}'.format(b)
  return int(b,16)

def PrintMatrix(matrix):
  for row in matrix:
    if any('x' in e for e in row):
      print ''.join(str(x) for x in row)

def Process(file):
  matrix = [[' ' for x in xrange(256)] for x in xrange(256)]
  ba = open(filename, 'rb').read()
  
  with open('plot.out','wb') as out:
    old = 0
    for new in xrange(0,len(ba),1):
      b1 = Hex(ba[old])
      b2 = Hex(ba[new])
      old = new
      
      if (b1 < 127) and (b2 < 127):
        matrix[b1][b2] = 'x'
      out.write(str(b1) + ',' + str(b2) + '\n')

  return matrix

PrintMatrix(Process(filename))

