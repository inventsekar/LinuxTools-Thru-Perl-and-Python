"""
#!/usr/bin/perl -w
# invent sekar  - 3/5/2014 - wednesday
# Perl implementation of Linux wc command, using a while loop and of course, the great regex ;).
"""

#!/usr/bin/python3
# inventsekar - 7th Aug 2020 Friday
# Python implementation of Linux WC Command, learning the great regex once again:


"""
print "Please enter line1:\n";
my $line1=<STDIN>;
chomp $line1;

$line2="A quiet bubble floating on a sea of noise. - The god of small things - Arundhati Roy";
$line3="Hello how are you";
"""

print("Please enter the line1:\n")
line1 = input()

line2="A quiet bubble floating on a sea of noise. - The god of small things - Arundhati Roy";
line3="Hello how are you";

print("\n line1, line2, line3 are:\n %s \n %s \n %s" % (line1,line2,line3))



"""

################################
# Finding number of words: wc -w
#################################
print "Finding numer of words: wc -w\n";
print "---------------------------------\n";
$nWords=0;

while ($line1 =~ /\b\w+\b/g){ $nWords++; }
print "line1 is $line1\n";
print "\$line1 contains $nWords words\n";

$nWords=0;
while ($line2 =~ /\b\w+\b/g){ $nWords++; }
print "line2 is $line2\n";
print "\$line2 contains $nWords words\n";

$nWords=0;
while ($line3 =~ /\b\w+\b/g){ $nWords++; }
print "line3 is $line3\n";
print "\$line3 contains $nWords words\n\n";

"""

import re

print(" \n Finding numer of words: wc -w\n")
print("---------------------------------\n")
nWords1=0
nWords2=0
nWords3=0

nWords1 = re.findall('\w+',line1)
nWords1 = len(nWords1)

nWords2 = re.findall('\w+',line2)
nWords2 = len(nWords2)

nWords3 = re.findall('\w+',line3)
nWords3 = len(nWords3)


print("\n line1 is:\n",line1)
print("line1 contains %s words\n", nWords1)

print("line2 is:\n",line2)
print("line2 contains %s words\n", nWords2)

print("line3 is:\n",line3)
print("line3 contains %s words\n", nWords3)



"""

################################
# Finding number of characters: wc -m
#################################
print "Finding numer of characters : wc -m\n";
print "---------------------------------\n";

$nChar=0;
while($line1 =~ /./g){$nChar++;}
print "line1 is $line1\n";
print "\$line1 contains $nChar characters\n";

$nChar=0;
while($line2 =~ /./g){$nChar++;}
print "line2 is $line2\n";
print "\$line2 contains $nChar characters\n";

$nChar=0;
while($line3 =~ /./g){$nChar++;}
print "line3 is $line3\n";
print "\$line3 contains $nChar characters\n";
"""
