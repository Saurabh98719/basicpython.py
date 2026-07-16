#create a student class with attributes: Name, roll Number,Marks(3subject) method:
#get_data() , display_data(),calculate_percentage()

class student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

        def get_data(self):
            self.name = input("enter student name: ")
            self.roll_number = input("enter roll number: ")
            self.marks = []
            for i in range(3):
                mark = float(input(f"enter marks for subject {i+1}: "))
                self.marks.append(mark)

                def display_data(self):
                    print(f"Name: {self.name}")
                    print(f"Roll Number: {self.roll_number}")
                    print(f"Marks: {self.marks}")

                    def calculate_percentage(self):
                        total_marks = sum(self.marks)
                        percentage = (total_marks / (len(self.marks) * 100)) * 100
                        return percentage
                    
