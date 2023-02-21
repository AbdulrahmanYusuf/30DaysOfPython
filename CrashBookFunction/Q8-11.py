
def show_messages(short_messages):
    
    for l in short_messages:
        change_message.append(l)
    return change_message
change_message = []
short_messages = ['i love python', 'I would like to improve', 'Yea I got it']
print(show_messages(short_messages[:]))
print(short_messages)