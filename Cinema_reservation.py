# Indexierung der Sitzplätze:  Sitzplatznummern bei 1 beginnen zu lassen und die Anpassung in der Methode set_seat_status
# Fehlerprüfung in set_seat_status: Überprüfung dass übergebenen Sitznummern gültig sind (z.B. dass sie nicht größer als total_seats sind).
# Vermeidung von Off-by-One-Fehlern: Die Methode set_seat_status fügt 1 zu jedem Index hinzu (i+1), was zu einem Off-by-One-Fehler führen kann.
# Direkte Zuweisung der Sitzplätze im Konstruktor: Anstelle einer Schleife im Konstruktor von Room könntest du ein Dictionary Comprehension verwenden, um den Code kompakter und Python-typischer zu gestalten.


class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Room:
    def __init__(self,room_number, total_seats):
        self.room_number = room_number
        self.total_seats = total_seats
        self.seats = {}
        for i in range(self.total_seats):
            self.seats[i] = "Free"
       
    def set_seat_status(self, numbers):
        for i in numbers:
            self.seats[i+1] = "Reserved" 

cinema1 = Cinema("Cineplex", "Munich")
room1 = Room(1,20)

reserve = 12, 14, 15
room1.set_seat_status(reserve)
print(room1.seats)



