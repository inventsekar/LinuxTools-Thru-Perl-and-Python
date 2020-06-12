
ubuntu@sekar:/tmp$ more pygrep.py 

#!/usr/bin/python
# inventsekar 13th june 2020 
# python implementation of Linux tool "grep"

import re

#fileName = raw_input("Please enter the filename:")
line = "hi hello how are you, him her hi one two three"

searchStr = raw_input("Please enter the search string:")

# general search - grep searchSrt filename

results = re.findall(searchStr, line)

print("the search results are:", results)





-------------------------------------------------
ubuntu@sekar:/tmp$ python pygrep.py 
Please enter the search string:hello
('the search results are:', ['hello'])
-------------------------------------------------
ubuntu@sekar:/tmp$ python pygrep.py
Please enter the search string:hi
('the search results are:', ['hi', 'hi', 'hi'])
ubuntu@sekar:/tmp$ 
-------------------------------------------------
