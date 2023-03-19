def lyrics(ly):
    if "99" in ly:
        for i in reversed(range(0,100)):
            print(ly.replace("99",str(i)))
song="""99 bottles of beer on the wall,99 bottles of beer.Take one down,pass it around,"""
lyrics(song)