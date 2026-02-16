class SchoolManagement:

    def __init__(self):
        self.students = {}   # Store student data
        self.next_id = 1     # Auto increment student ID

    # ---------------- VALIDATION METHODS ----------------

    def validate_age(self, age):
        return 5 <= age <= 18

    def validate_mobile(self, mobile):
        return mobile.isdigit() and len(mobile) == 10

    # ---------------- NEW ADMISSION ----------------

    def new_admission(self):
        name = input("Enter Student Name: ")

        try:
            age = int(input("Enter Age (5-18): "))
        except ValueError:
            print("❌ Age must be a number!")
            return

        if not self.validate_age(age):
            print("❌ Age must be between 5 and 18!")
            return

        try:
            student_class = int(input("Enter Class (1-12): "))
        except ValueError:
            print("❌ Class must be a number!")
            return

        if not (1 <= student_class <= 12):
            print("❌ Class must be between 1 and 12!")
            return

        mobile = input("Enter Guardian Mobile (10 digits): ")

        if not self.validate_mobile(mobile):
            print("❌ Mobile number must be exactly 10 digits!")
            return

        # Assign unique student ID
        student_id = self.next_id
        self.next_id += 1

        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }

        print(f"✅ Admission Successful! Student ID is: {student_id}")

    # ---------------- VIEW STUDENT ----------------

    def view_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("❌ Invalid ID!")
            return

        if student_id in self.students:
            student = self.students[student_id]
            print("\n--- Student Details ---")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Class:", student["class"])
            print("Guardian Mobile:", student["mobile"])
        else:
            print("❌ Student Not Found!")

    # ---------------- UPDATE STUDENT ----------------

    def update_student(self):
        try:
            student_id = int(input("Enter Student ID to Update: "))
        except ValueError:
            print("❌ Invalid ID!")
            return

        if student_id not in self.students:
            print("❌ Student Not Found!")
            return

        print("1. Update Class")
        print("2. Update Mobile Number")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                new_class = int(input("Enter New Class (1-12): "))
                if 1 <= new_class <= 12:
                    self.students[student_id]["class"] = new_class
                    print("✅ Class Updated Successfully!")
                else:
                    print("❌ Invalid Class!")
            except ValueError:
                print("❌ Invalid Input!")

        elif choice == "2":
            new_mobile = input("Enter New Mobile Number (10 digits): ")
            if self.validate_mobile(new_mobile):
                self.students[student_id]["mobile"] = new_mobile
                print("✅ Mobile Updated Successfully!")
            else:
                print("❌ Invalid Mobile Number!")

        else:
            print("❌ Invalid Choice!")

    # ---------------- REMOVE STUDENT ----------------

    def remove_student(self):
        try:
            student_id = int(input("Enter Student ID to Remove: "))
        except ValueError:
            print("❌ Invalid ID!")
            return

        if student_id in self.students:
            del self.students[student_id]
            print("✅ Student Record Removed Successfully!")
        else:
            print("❌ Student Not Found!")

    # ---------------- MENU ----------------

    def menu(self):
        while True:
            print("\n----- School Management System -----")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.new_admission()
            elif choice == "2":
                self.view_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.remove_student()
            elif choice == "5":
                print("Thank You! Exiting System.")
                break
            else:
                print("❌ Invalid Choice!")


# ----------- RUN PROGRAM -----------
school = SchoolManagement()
school.menu()
