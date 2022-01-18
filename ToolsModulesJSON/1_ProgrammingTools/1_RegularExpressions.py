import re #Import regular expressions 

str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et  dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation jordan@test.com ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla  pariatur. chase@yahoo Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia tiffany@example.com deserunt mollit anim id est laborum'

match = re.search(r'[a-zA-Z0-9]+@[a-zA-Z0-9_]+\.[a-zA-Z]+',str)
if match:
    print(match.group())
 
print('----Example END---- \n') 
matches = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9_]+\.[a-zA-Z]+',str)
for match in matches:
    print(match)
 
print('----Example END---- \n')    
#Different code that will bring chase@yahoo Excepteur 
#Period looks for everything 
#Including slash will help to escape special character allowing you to match it. 
matchesDiff = re.findall(r'[a-zA-Z0-9]+@[a-zA-Z0-9_]+.[a-zA-Z]+',str)
for match in matchesDiff:
    print(match)
