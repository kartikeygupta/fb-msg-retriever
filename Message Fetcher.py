###facepy developed by Johannes Gorset (@jgorset)
from facepy import GraphAPI
from facepy import exceptions

def get_names():
    chat_list = []
    for chat in messages['data']:
        try:
            chat_list.append(chat['to']['data'][0]['name'])
        except KeyError:
            chat_list.append("***Unknown Facebook User***")
    return chat_list
        
def print_transcript(chat):
    for message in chat:
        try:
            print('From : ' + message['from']['name'])
        except KeyError:
            print('From : Unknown Facebook User')
        try:
            print('>>> ' + message['message'])
        except UnicodeEncodeError:
            print("***Message contains emoji. Can't display.***")
        except KeyError:
            print("***" + message['from']['name'] + " sent a like.***")
        print()
        
        
def menu(chat_list):
    print('The following chats are available - ')
    i = 1
    for name in chat_list:
        print(str(i) + ' : ' + name)
        i += 1
    print(str(i) + ' : Exit')
    print('Enter the number corresponding to the chat that you wish to open : ', end = '')
    choice = int(input())
    print('\n\n')
    return choice
        
access = input('Enter Access Token : ')

graph = GraphAPI(access)
try:
    messages = graph.get('me/inbox')
except exceptions.OAuthError:
    print("\nUmm...your Access Token doesn't have the 'read_mailbox' permission. Call Kartikey. He'll know what to do. Probably. Hopefully. Maybe. Program's gonna terminate.")
else:    
    chat_list = get_names()
    choice = 0
    close = len(chat_list)
    enter = False
    while enter == False or choice!=close+1:
        if enter and choice!=close+1:
            print_transcript(messages['data'][choice-1]['comments']['data'])
        else:
            enter = True
        choice = menu(chat_list)
    print('You have successfully exited.')
