class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there!"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shell"])

hey_jude = Song(["Hey jude",
                 "don't make it bad",
                 "take a sad song and make it better"])


bulls_on_parade.sing_me_a_song()

hey_jude.sing_me_a_song()

happy_bday.sing_me_a_song()

foo = Song(happy_bday.lyrics)
foo.sing_me_a_song()
