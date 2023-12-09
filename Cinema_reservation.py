# Indexierung der Sitzplätze:  Sitzplatznummern bei 1 beginnen zu lassen und die Anpassung in der Methode set_seat_status
# Fehlerprüfung in set_seat_status: Überprüfung dass übergebenen Sitznummern gültig sind (z.B. dass sie nicht größer als total_seats sind).
# Vermeidung von Off-by-One-Fehlern: Die Methode set_seat_status fügt 1 zu jedem Index hinzu (i+1), was zu einem Off-by-One-Fehler führen kann.
# Direkte Zuweisung der Sitzplätze im Konstruktor: Anstelle einer Schleife im Konstruktor von Room könntest du ein Dictionary Comprehension verwenden, um den Code kompakter und Python-typischer zu gestalten.
# Sitzplatzkategorien und verschiedene Preise für Sitzplätze. Reservierung ergibt Gesamtsumme. 
# Uhrzeiten für Filme
# Kundenkonto für Karten und Zahlvorgänge + validierung bspw. Kreditkarte
# Führe eine Sitzplatzklasse ein, in der es normale und Premiumsitze gibt, die verschieden Kosten.
# Implementiere in der Kino-Klasse eine Methode __str__, die eine formatierte Darstellung des Kinos zurückgibt.


class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def __str__(self):
        return f"Cinema: {self.name}\nLocation: {self.location}"

class Room:
    def __init__(self,room_number, total_seats, cinema):
        self.room_number = room_number
        self.cinema = cinema
        self.total_seats = total_seats
        self.seats = {}
        for i in range(self.total_seats):
            self.seats[i] = "Free"
       
    def set_seat_status(self, numbers):
        for i in numbers:
            self.seats[i+1] = "Reserved" 

class Seat:
    def __init__(self, number, category, room):
        self.number = number
        self.category = category
        self.room = room
        self.status = "Free"


cineplex_muc = Cinema("Cineplex", "Munich")
cineplex_muc_room1 = Room(1,20, cineplex_muc)

seat_1_normal_room1_cineplex_muc = Seat(1, "normal", cineplex_muc_room1)
seat_2_normal_room1_cineplex_muc = Seat(2, "normal", cineplex_muc_room1)
seat_3_normal_room1_cineplex_muc = Seat(3, "normal", cineplex_muc_room1)
seat_4_normal_room1_cineplex_muc = Seat(4, "normal", cineplex_muc_room1)
seat_5_normal_room1_cineplex_muc = Seat(5, "normal", cineplex_muc_room1)
seat_6_normal_room1_cineplex_muc = Seat(6, "normal", cineplex_muc_room1)
seat_7_normal_room1_cineplex_muc = Seat(7, "normal", cineplex_muc_room1)
seat_8_normal_room1_cineplex_muc = Seat(8, "normal", cineplex_muc_room1)
seat_9_normal_room1_cineplex_muc = Seat(9, "normal", cineplex_muc_room1)
seat_10_normal_room1_cineplex_muc = Seat(10, "normal", cineplex_muc_room1)
seat_11_premium_room1_cineplex_muc = Seat(11, "premium", cineplex_muc_room1)
seat_12_premium_room1_cineplex_muc = Seat(12, "premium", cineplex_muc_room1)
seat_13_premium_room1_cineplex_muc = Seat(13, "premium", cineplex_muc_room1)
seat_14_premium_room1_cineplex_muc = Seat(14, "premium", cineplex_muc_room1)
seat_15_premium_room1_cineplex_muc = Seat(15, "premium", cineplex_muc_room1)



# reserve = 12, 14, 15
# cineplex_muc_room1.set_seat_status(reserve)
# print(cineplex_muc_room1.seats)



