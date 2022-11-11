
#turn a song list into a string
def string_maker(filename):
    str='' #create a empty string
    file = open(filename, "r") #open the file in read mode
    str= file.read() # this will turn the file into a single strinb
    return str
    file.close()

#turn the string into a dictionary with key as the song and value as the style
def dictionary_maker(string):
    song_dictionary={} #empty dictionary
    song_list = string.split('\n') #split the string in a list of each lines
    for song in song_list[:-1]: #iterate through each line to slit them again
        song_list2 = song.split('-') # - seperate the song and the style
        style = song_list2[1].split('/')# seperate each substyle
        for i in range(len(style)): #keep track of case and spaces
            style[i]= style[i].lower() #case
            style[i]=style[i].strip(' ') #spaces
        song_dictionary[song_list2[0]] = style #add on to the dictionary where the value is a list of the two potential substyle
    return song_dictionary

def song_selcter(dictionary):
    playlist_song = [] # create a list to store the selected songs
    while True: # loop until the list is complet
        try:# Error handling
            while playlist_song == []: # loop to keep promping the user until the user gives a valid style
                print("Hi, I'm here to make you a Playlist\nSelect a muscic style from the list below:")
                user_choice = input("-Pop\n-Rock\n-Country\n-Hip Hop\n-Rap\n-Classical\n-Grunge\n-Reggae\n-Dance\n-Soul\n-R&B\n-Jazz\n-Blues\n-Alternative\n-Indie\n-Afropop\n-Kpop\n:" )
                user_choice = user_choice.lower() #account for case
                user_choice = user_choice.strip(' ') #spaces
                for song,style in dictionary.items(): # iterate through the song and style
                    if user_choice in style: # select each songs that as the same syle as user choice
                        playlist_song.append(song)
                if playlist_song == []: # Error handling
                    print("Sorry, this style doesn't exist in our catalog:)")
            break
        except: # if the input is invalid and it created and error
            print("Sorry that not a vaild style, try again:")
    return playlist_song

def write_playlistf(dict, outputname='playlist.txt'): #take in a dictionary and a file name
    playlistf = open(outputname,'w') #open the file to write in it
    for song in dict: # iterate through the dictionary to create the file
        playlistf.write(song+'\n') # create the formate
    playlistf.close() #close the file
    return playlistf

''

songs_string = string_maker("song.txt")
songs_dictionary = dictionary_maker(songs_string)

playlist_dict =song_selcter(songs_dictionary)
# print(playlist_dict)

playlist_file = write_playlistf(playlist_dict)
print('Here is your playlist:')
print(' ')

for song in playlist_dict:
    print(song)

print(' ')
print('You can also find a file attached with your playlist')
print('Thank you for using my sevrice')
