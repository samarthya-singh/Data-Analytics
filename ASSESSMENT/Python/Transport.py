class BusReservation:

    def __init__(self):
        # Predefined routes with prices
        self.routes = {
            1: {"route": "Mumbai to Pune", "price": 500},
            2: {"route": "Delhi to Jaipur", "price": 600},
            3: {"route": "Bangalore to Chennai", "price": 550},
            4: {"route": "Kolkata to Durgapur", "price": 400}
        }

        self.tickets = {}          # ticket_id -> ticket details
        self.route_seats = {}      # route_id -> list of booked seats
        self.next_ticket_id = 1001
        self.max_seats = 40

    # ---------------- SHOW ROUTES ----------------
    def show_routes(self):
        print("\nAvailable Routes:")
        for key, value in self.routes.items():
            print(f"{key}. {value['route']} - ₹{value['price']}")

    # ---------------- BOOK TICKET ----------------
    def book_ticket(self):
        self.show_routes()

        try:
            route_choice = int(input("Select Route Number: "))
        except ValueError:
            print("❌ Invalid Route Selection!")
            return

        if route_choice not in self.routes:
            print("❌ Route Not Found!")
            return

        name = input("Enter Passenger Name: ")

        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("❌ Age must be numeric!")
            return

        mobile = input("Enter Mobile Number (10 digits): ")
        if not (mobile.isdigit() and len(mobile) == 10):
            print("❌ Invalid Mobile Number!")
            return

        # Initialize route seat list if not exists
        if route_choice not in self.route_seats:
            self.route_seats[route_choice] = []

        # Check seat availability
        if len(self.route_seats[route_choice]) >= self.max_seats:
            print("❌ Bus is Full!")
            return

        # Assign next available seat
        seat_number = len(self.route_seats[route_choice]) + 1
        self.route_seats[route_choice].append(seat_number)

        # Generate ticket ID
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": self.routes[route_choice]["route"],
            "price": self.routes[route_choice]["price"],
            "seat": seat_number
        }

        print("\n✅ Ticket Booked Successfully!")
        print("Your Ticket ID:", ticket_id)
        print("Seat Number:", seat_number)

    # ---------------- VIEW TICKET ----------------
    def view_ticket(self):
        try:
            ticket_id = int(input("Enter Ticket ID: "))
        except ValueError:
            print("❌ Invalid Ticket ID!")
            return

        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            print("\n----- Ticket Details -----")
            print("Passenger Name:", ticket["name"])
            print("Age:", ticket["age"])
            print("Mobile:", ticket["mobile"])
            print("Route:", ticket["route"])
            print("Seat Number:", ticket["seat"])
            print("Price: ₹", ticket["price"])
        else:
            print("❌ Ticket Not Found!")

    # ---------------- CANCEL TICKET ----------------
    def cancel_ticket(self):
        try:
            ticket_id = int(input("Enter Ticket ID to Cancel: "))
        except ValueError:
            print("❌ Invalid Ticket ID!")
            return

        if ticket_id in self.tickets:
            route_name = self.tickets[ticket_id]["route"]

            # Find route_id from route name
            route_id = None
            for key, value in self.routes.items():
                if value["route"] == route_name:
                    route_id = key
                    break

            seat_number = self.tickets[ticket_id]["seat"]

            # Remove seat from route
            if route_id and seat_number in self.route_seats[route_id]:
                self.route_seats[route_id].remove(seat_number)

            del self.tickets[ticket_id]

            print("✅ Ticket Cancelled Successfully!")
        else:
            print("❌ Ticket Not Found!")

    # ---------------- MENU ----------------
    def menu(self):
        while True:
            print("\n------ Bus Reservation System ------")
            print("1. Show Available Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_routes()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.view_ticket()
            elif choice == "4":
                self.cancel_ticket()
            elif choice == "5":
                print("Thank You for Using Bus Reservation System!")
                break
            else:
                print("❌ Invalid Choice!")


# -------- RUN PROGRAM --------
bus = BusReservation()
bus.menu()
