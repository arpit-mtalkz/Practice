class RailwayForm():
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
applicationForm=RailwayForm()
applicationForm.name=input("Enter your name :")
applicationForm.train=input("Enter Train name :")
applicationForm.printData()