
# Hospital system

- There are 20 different specialization (e.g. Children, Surgery, etc)
- For each specialization, there are only 10 available spots (queue)
- The program keeps showing this menu of options
program options:

'1 Add new patient',

'2 Print all patients',

'3 Get next patient',

'4 Remove a leaving patient',

'5 End the program'

---

To add a patient: provide which specialization, name and status
- Specialization: 1-based integer (e.g. 1 to 20)
- Status is 0 (normal), 1 (urgent) and 2 (super urgent)
- Normal patient is added to the end of the current queue of this specialization
- Urgent patient is added after current urgents patients & before normal patients
- Super-urgent patient is added after current super-urgent patients & before urgent/normal patients
- Read the requested specialization [1-20].
- Read his name and status (0 = regular, 1 urgent)
- If 10 patients exist in this specialization, apologize and don’t accept

---
Get next patient
- Given a specialization, return the top patient of the queue
   And remove from the queue
- If no patient: just inform the Dr about that

---

Remove a leaving patient
- A patient may decide to leave before seeing a doctor
- Provide specialization and name
- If no such a person: inform about that





## Usage/Examples

```python

class secretary_of_hospital(rules):
    def __init__(self):
        super(secretary_of_hospital,self).__init__()
        self.inp_menu = None

    def __str__(self):
        return 'this class will be the high level of applying the rules of hospital and who Rx applications and the patients to check in depending on their condition whether to wait or to enter the intensive care.'


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
 
```


## Installation

it is just a one folder project that you can run the main file through bash shell

```bash
  [mahmood79@server ~]#python hospital.py
  or 
  [mahmood79@server ~]#./hospital.py
``` 
    