#! python3
#Password Locker

import sys, pyperclip

passwords = {'email': 'rgr99fdjirw3lKLW(jisa9',
             'accountOne': 'Dswsd2SAD23SADfddf3',
             'accountTwo': 'saddSA23DSasd43sdfa'
             }

#Checks if a command line argument has been entered 
if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

accountRequested = sys.argv[1] 

if accountRequested in passwords:
    pyperclip.copy(passwords[accountRequested])
    print('Password for ' + accountRequested + ' copied to clipboard.')
else:
    print('There is no account named ' + accountRequested)
