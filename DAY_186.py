class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"Movie Name : {self.title}\nTime : {self.duration} mins"

    def __len__(self):
        return self.duration


movie = Movie("Interstellar", 169)

print(movie)
print(len(movie))