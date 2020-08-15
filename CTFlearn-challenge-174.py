# https://ctflearn.com/challenge/174
# I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! 
# Here is the file: https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys

# actually, not needed to use regular expression at all. the list.count function is perfect enough, 
# but as i used and learnt regular expression, let me post it here:

import re

file = open("/home/ubuntu/Downloads/data.dat","r")
contents = file.read()
#print(contents)

Counter = 0

CoList = contents.split("\n")

for i in CoList:
        if i:
                Counter += 1

print("the number of lines:", Counter)


def reg_exp():
        pattern1 = '1'
        pattern0 = '0'
        infile = open('/home/ubuntu/Downloads/data.dat', 'r')
        match_count = 0
        lines = 0
        threeZeros = 0
        for line in infile:
                match_count1 = re.findall(pattern1,line)
                match_count0 = re.findall(pattern0,line)
                #if match:
                #       match_count += 1
                lines += 1
                linematchcount1 = match_count1.count('1')
                linematchcount0 = match_count0.count('0')
                if (linematchcount1 % 2 == 0) or (linematchcount0 % 3 == 0):
                        threeZeros += 1
                print("count,linematchcount0,linematchcount1,linenumber,line,threeZeros",match_count,linematchcount0,linematchcount1,lines,line,threeZeros)
        return (lines, match_count)

if __name__ == "__main__":
        lines, match_count = reg_exp()
        print("lines:", lines)
        print("matches:", match_count)


Sample Run:
--------------------
<droped lots of lines>
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 11 7 9992 100101100001000101
 6657
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 7 7 9993 10010011011001
 6657
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 8 8 9994 0110011001110100
 6658
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 13 5 9995 010001001001100000
 6658
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 9 4 9996 0011000110000
 6659
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 8 7 9997 010000001111110
 6659
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 9 8 9998 00001001110110101
 6660
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 9 6 9999 101000011101000
 6661
count,linematchcount0,linematchcount1,linenumber,line,threeZeros 0 6 4 10000 0100001011
 6662
lines: 10000
matches: 0
ubuntu@sekar:~/python-test$ 


Soooo, the answer is: 6662
