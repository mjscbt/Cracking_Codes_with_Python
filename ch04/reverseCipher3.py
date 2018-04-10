# Reverse Cipher
# http://www.nostarch.com/Crackingcodes (BSD Licensed)

# input only works for Python 3, we'll use raw_input() instead
#message = input('Enter message: ') 
message = raw_input('Enter message: ')

translated = ''

i = len(message) - 1
while  i >= 0:
	translated = translated + message[i]
	i = i - 1

print(translated)

