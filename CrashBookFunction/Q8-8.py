def make_album(artist_name, album_title):
    person = {'name':artist_name, 'album':album_title}
    
    return person
print("(enter 'q' at any time to quit)")

while True:   
        artist_name = input('enter artist name: ')
        if  artist_name == 'q':
            break;
        album_title = input('enter the album title: ')
        if  album_title == 'q':
            break;
        print(make_album(artist_name=artist_name, album_title=album_title))      
