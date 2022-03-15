# task 1
class Triangle():
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


my_triangle = Triangle(30, 60, 900)

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


# task 2
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)


happy_bday = Song(["May god bless you, ", "Have a sunshine on you,", "Happy Birthday to you !"])

happy_bday.sing_me_a_song()
