class Patient(object):
    def __init__(self, idnum, name, allergies):
        self.idnum = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = "None"


class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.beds = []
        for vals in range(capacity):
            self.beds.append(False)
        self.next_patient_id = 1

    def admit(self, name, allergies):
        if len(self.patients) == self.capacity:             # check to make sure there's room
            print "Sorry, we're all full. Good luck with that!"
            return self
        for bed in range(len(self.beds)):                   # Find the first empty bed in the beds list
            if not self.beds[bed]:
                self.beds[bed] = True                       # mark it as occupied in the list
                new_bed = bed                               # store the newly occupied bed number for assignment to the patient
                break
        new_patient = Patient(self.next_patient_id, name, allergies)    # Create new patient record, passing new_bed in as patient's bednum
        new_patient.bednum = new_bed
        self.next_patient_id += 1
        self.patients.append(new_patient)
        print "Congratulations, {}, you've been admitted and placed in bed #{}.".format(new_patient.name, new_patient.bednum)
        return self

    def discharge(self, query_name):
        for num in range(len(self.patients)):
            if self.patients[num].name == query_name:
                self.beds[self.patients[num].bednum] = False
                print "Get outta here, {}!".format(self.patients[num].name)
                del self.patients[num]
                break
        for patient in self.patients:
            print patient.name
        print self.beds
        return self


tough_luck_ch = Hospital("Tough Luck County Hospital", 10)
tough_luck_ch.admit("Charlie Brown", "Peauts")
tough_luck_ch.admit("Sally", "Peanuts")
tough_luck_ch.admit("Linus", "Peanuts")
tough_luck_ch.admit("Peppermint Pattie", "Peanuts")
tough_luck_ch.admit("Marcie", "Peanuts")
tough_luck_ch.admit("Lucy", "Peanuts")
tough_luck_ch.admit("Franklin", "Peanuts")
tough_luck_ch.admit("Pig Pen", "Peanuts")
tough_luck_ch.admit("Violet", "Peanuts")
tough_luck_ch.admit("Little Red-haired Girl", "Peanuts")
tough_luck_ch.admit("Teacher", "Peanuts")
tough_luck_ch.discharge("Peppermint Pattie")
tough_luck_ch.admit("Teacher", "Peanuts")
