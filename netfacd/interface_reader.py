#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library"""

import netifaces

def main():
    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ',end='')
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            print('IP: ',end='')
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            print('Could not collect adapter information')

def faces():
    for i in netifaces.interfaces():
        print(i, end='    ')
    print('\n')
    face = 'invalid'
    while face not in netifaces.interfaces():
        face = input("Select an interface: \n=======>>")
    return face

def ip_only():
    face = faces()
    print('IP: ',end=' ')
    print(netifaces.ifaddresses(face)[netifaces.AF_INET][0]['addr'])

def mac_only():
    face = faces()
    print('MAC: ',end=' ')
    print(netifaces.ifaddresses(face)[netifaces.AF_LINK][0]['addr'])

# ip_only()
mac_only()
# main()
