spec_list = [i for i in range(1,21)]
main_list = [1,2,3,4,5]
stat=[0,1,2]
msg2="enter specialisation from 1 - 20"
msg1="enter from 1 - 5"
msg3='Enter status (0 normal / 1 urgent / 2 super urgent): '


def valid_input(msg,b):
    while 1:
        a = int(input(msg))
        try:
            assert a in b, "mother fucker retype"
            break
        except:
            print("retype please")
    return a

class Patient:
    def __init__(self, name, status):
        self.name, self.status = name, status

    def __str__(self):
        return f'Patient: {self.name} is {self.status}'

    def __repr__(self):
        return F'Patient(name="{self.name}", status={self.status})'

   


class rules:
    def __init__(self):
        self.specializations_cnt = 20
        self.MAX_QUEUE = 10
        self.specializations = [[] for s in range(self.specializations_cnt)]
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2

    def can_add_more_patients(self,specialization):
        return (len(self.specializations[specialization]) < self.MAX_QUEUE)

    def add_patient(self, specialization, name, status):
        pat = Patient(name, status)
        obj = self.specializations[specialization]
        if status == self.NORMAL or len(obj) == 0:          #noraml case
            obj.append(pat)
        elif status == 1:  				    #urgent case
            if obj[-1].status != self.NORMAL:
                obj.append(pat)
            else:
                for idx,pati in enumerate(obj):
                    if(pati.status == self.NORMAL):
                        obj.insert(idx,pat)
                        break
        else:
            if obj[-1].status == self.SUPER_URGENT:
                obj.append(pat)
            else:
                for idx, pati in enumerate(obj):
                    if pati.status == self.NORMAL or pati.status == self.URGENT:
                        obj.insert(idx,pat)
                        break

    def patients_info(self):
        for i in range(self.specializations_cnt):
            if(not self.specializations[i]):
                    continue
            l = len(self.specializations[i])
            print(f"specialization {str(i+1)} there are {l} patients")
            for i2 in range(l):
                print("Patient: "+self.specializations[i][i2].__str__())

    def get_next_patients(self, specialization):
        if len(self.specializations[specialization]) == 0:
            return None
        return self.specializations[specialization].pop(0)

    def remove_patient(self, spec , name):      #didn't use the ticket he bought just decided to leave due to latency or other issues
        spec_ = self.specializations[spec]
        for idx, patient in enumerate(spec_):
            if patient.name == name:
                del spec_[idx]
                return True
        return False



class secretary_of_hospital(rules):
    def __init__(self):
        super(secretary_of_hospital,self).__init__()
        self.inp_menu = None


    def menu(self):
        print('\nProgram Options:')
        messages = [
            '1 Add new patient',
            '2 Print all patients',
            '3 Get next patient',
            '4 Remove a leaving patient',
            '5 End the program'
        ]
        print('\n'.join(messages)+'\n')
        self.inp_menu = valid_input(msg1,main_list)



    def run(self):
        while True:
            self.menu()
            if self.inp_menu == 1:
                inp_spec = valid_input(msg2,spec_list) - 1
                if rules.can_add_more_patients(self,inp_spec):
                    name = input('Enter patient name: ')
                    status = valid_input(msg3,stat)
                    self.add_patient(inp_spec,name,status)
                else:
                    print("Sorry we can't add more patients for this specialization at the moment.")

            elif self.inp_menu == 2:
                rules.patients_info(self)

            elif self.inp_menu == 3:
                spec = valid_input(msg2,spec_list) -1
                patient_ = rules.get_next_patients(self,spec)
                if patient_ is None:
                    print('No patients at the moment. Have rest, Dr')
                else:
                    print(f'{patient_.name}, Please go with the Dr')

            elif self.inp_menu == 4:
                spec = valid_input(msg2,spec_list) - 1
                name = input('Enter patient name: ')
                if not rules.remove_patient(self,spec,name):
                    print('No patient with such a name in this specialization!')
            else:
                break

if __name__ == '__main__':
    app = secretary_of_hospital()
    app.run()
