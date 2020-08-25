import os

while True:
    query = input('Can you please tell me what can I do for you? ').lower()
    list_no = ['do not', "don't", 'no need', 'no']
    for i in list_no:
        if i in query:
            print('Okay, sure.')
    if 'run' in query or 'open' in query:
        if 'notepad' in query or 'edit' in query:
            os.system('notepad')
        if 'chrome' in query or 'browser' in query:
            os.system('start chrome')
        if 'media' in query or 'player' in query:
            os.chdir('C:\Program Files\VideoLAN\VLC')
            os.system('vlc')
    elif 'exit' in query or 'terminate' in query or 'stop' in query:
        break
    else:
        print('Can you please try again')