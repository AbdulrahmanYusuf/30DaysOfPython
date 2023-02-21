def make_album(artist_name, album_title, songs = None):
    person = {'name':artist_name, 'album':album_title}
    if songs != None:
        person['song'] = songs
        print(person)
    else:
        print(person)
    return person


make_album('Gwanja', 'War', 10)
make_album('Alah', 'Sardaunan Kaao')
make_album('Khamilu', 'Ruwa Baba', 5)


