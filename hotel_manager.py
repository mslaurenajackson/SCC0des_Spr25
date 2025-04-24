class Hotel:
    def __init__(self):
        self.rooms = {
            '1': {'101': ['George Jefferson', 'Wheezy Jefferson'], '102': []},
            '2': {'237': ['Jack Torrance', 'Wendy Torrance'], '238': []},
            '3': {'333': ['Neo', 'Trinity', 'Morpheus'], '334': []}
        }

    def add_occupants(self, floor, room):
        if floor in self.rooms and room in self.rooms[floor]:
            num_guests = int(input("How many in your party? (Max: 6) "))
            if num_guests > 6:
                print("Sorry, we can only accommodate up to 6 guests.")
                return
            
            guests = [input(f"Enter name of guest {i+1}: ") for i in range(num_guests)]
            self.rooms[floor][room] = guests
            print(f"{', '.join(guests)} have been checked into room {room} on floor {floor}.")
        else:
            print("Invalid floor/room selection.")

    def show_available_rooms(self, floor):
        if floor in self.rooms:
            available_rooms = [room for room in self.rooms[floor] if not self.rooms[floor][room]]
            if available_rooms:
                print(f"Available rooms on floor {floor}: {', '.join(available_rooms)}")
            else:
                print("No available rooms on this floor.")
        else:
            print("Floor does not exist.")

    def checkin_or_checkout(self):
        action = input("Would you like to check in or check out? (in/out): ")
        floor = input("Which floor? ")
        room = input("Which room number? ")

        if floor in self.rooms and room in self.rooms[floor]:
            if action == "in":
                self.add_occupants(floor, room)
            elif action == "out":
                if self.rooms[floor][room]:
                    print(f"Checking out of room {room} on floor {floor}.")
                    self.rooms[floor][room] = []
                else:
                    print("The room is already empty.")
            else:
                print("Invalid option. Please enter 'in' or 'out'.")
        else:
            print("Room not found. Please check your reservation.")

# Create hotel instance and run the function
my_hotel = Hotel()
my_hotel.checkin_or_checkout()
floor_check = input("Enter floor number to check for available rooms: ")
my_hotel.show_available_rooms(floor_check)
