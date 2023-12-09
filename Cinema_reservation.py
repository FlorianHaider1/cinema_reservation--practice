# Fehlerprüfung in set_seat_status: Überprüfung dass übergebenen Sitznummern gültig sind (z.B. dass sie nicht größer als total_seats sind).
# Direkte Zuweisung der Sitzplätze im Konstruktor: Anstelle einer Schleife im Konstruktor von Room könntest du ein Dictionary Comprehension verwenden, um den Code kompakter und Python-typischer zu gestalten.
# Uhrzeiten für Filme
# Kundenkonto für Karten und Zahlvorgänge + validierung bspw. Kreditkarte. Einkaufswagen mit Einzelposten und Gesamtsumme

class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = {}
      
    def add_room(self, room):
        self.rooms[room.room_number] = room
    
    def __str__(self):
        return f"Cinema: {self.name}\nLocation: {self.location}"
    
    def view_rooms(self):
        return "\n".join(str(room)for room in self.rooms.values())  

class Room:
    def __init__(self,room_number, cinema, normal_seats, premium_seats):
        self.room_number = room_number
        self.cinema = cinema
        self.seats = {i: Seat_normal(i, self) for i in range(normal_seats+1)}
        self.seats.update({i: Seat_premium(i, self) for i in range(normal_seats +1, normal_seats +1 + premium_seats)})

    def list_seats(self):
        return "\n".join(str(seat) for seat in self.seats.values())
 
    def __str__(self):
        return f"Room number {self.room_number}"

class Seat:
    def __init__(self, seat, room):
        self.seat_number = seat
        self.room = room
        self.status = "Free"
    
    def __str__(self):
        return f"{self.category} Seat number {self.seat_number:02d}: {self.status}"

class Seat_normal(Seat):
    def __init__(self, seat, room):
        super().__init__(seat, room)
        self.room = room
        self.category = "Normal"
        self.price = 14.50

class Seat_premium(Seat):
    def __init__(self, seat, room):
        super().__init__(seat, room)
        self.room = room
        self.category = "Premium"
        self.price = 16.99

class Movie:
    def __init__(self, name):
        self.name = name

cineplex_muc = Cinema("Cineplex", "Munich")
cineplex_muc_room1 = Room(1, cineplex_muc, normal_seats= 35, premium_seats = 15)
cineplex_muc_room2 = Room(2, cineplex_muc, normal_seats= 40, premium_seats = 10)
palast_ber = Cinema("Filmpalast", "Berlin")
palast_ber_room1 = Room(1, palast_ber, normal_seats = 25, premium_seats = 15)
palast_ber_room2 = Room(2, palast_ber, normal_seats = 50, premium_seats = 20)                          

action_movie = Movie("The Punishifinator 3D")
romance_movie = Movie("The love is love")
comedy_movie = Movie("Funny laughing 3")

cineplex_muc.add_room(cineplex_muc_room1)
cineplex_muc.add_room(cineplex_muc_room2)

print(cineplex_muc_room1.list_seats())
    

# reserve = 12, 14, 15
# cineplex_muc_room1.set_seat_status(reserve)
# print(cineplex_muc_room1.seats)



