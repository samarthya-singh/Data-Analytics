class ClinicAppointment:

    def __init__(self):
        # Dictionary to store appointments
        # Structure:
        # {
        #   doctor_name: {
        #       time_slot: [appointment1, appointment2, appointment3]
        #   }
        # }
        self.appointments = {}
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.max_per_slot = 3

    # ---------------- BOOK APPOINTMENT ----------------
    def book_appointment(self):
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        mobile = input("Enter Mobile Number: ")
        doctor = input("Enter Preferred Doctor Name: ")

        print("\nAvailable Time Slots:")
        for slot in self.time_slots:
            print(slot)

        selected_slot = input("Select Time Slot: ")

        if selected_slot not in self.time_slots:
            print("Invalid Time Slot!")
            return

        # Create doctor if not exists
        if doctor not in self.appointments:
            self.appointments[doctor] = {}

        # Create slot if not exists
        if selected_slot not in self.appointments[doctor]:
            self.appointments[doctor][selected_slot] = []

        # Check availability
        if len(self.appointments[doctor][selected_slot]) < self.max_per_slot:
            appointment = {
                "name": name,
                "age": age,
                "mobile": mobile
            }
            self.appointments[doctor][selected_slot].append(appointment)
            print("✅ Appointment Booked Successfully!")
        else:
            print("❌ Slot Full! Please choose another time.")

    # ---------------- VIEW APPOINTMENT ----------------
    def view_appointment(self):
        mobile = input("Enter Mobile Number to View Appointment: ")

        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for patient in patients:
                    if patient["mobile"] == mobile:
                        print("\nAppointment Details:")
                        print("Doctor:", doctor)
                        print("Time:", slot)
                        print("Name:", patient["name"])
                        print("Age:", patient["age"])
                        return
        print("No Appointment Found!")

    # ---------------- CANCEL APPOINTMENT ----------------
    def cancel_appointment(self):
        mobile = input("Enter Mobile Number to Cancel Appointment: ")

        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for patient in patients:
                    if patient["mobile"] == mobile:
                        patients.remove(patient)
                        print("✅ Appointment Cancelled Successfully!")
                        return
        print("No Appointment Found!")

    # ---------------- MAIN MENU ----------------
    def menu(self):
        while True:
            print("\n---- Clinic Appointment System ----")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointment()
            elif choice == "3":
                self.cancel_appointment()
            elif choice == "4":
                print("Thank You!")
                break
            else:
                print("Invalid Choice!")


# ---------------- RUN SYSTEM ----------------
clinic = ClinicAppointment()
clinic.menu()
