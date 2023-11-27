
# Hospital system

### Detailed description of how the program function

- There are 20 different specialization (e.g. Children, Surgery, etc)
- For each specialization, there are only 10 available spots (queue)
- The program keeps showing this menu of options
program options:

> 1 Add new patient

>2 Print all patients

> 3 Get next patient

> 4 Remove a leaving patient

> 5 End the program

---

To add a patient: provide which specialization, name and status
- Specialization: 1-based integer (e.g. 1 to 20)
- Status is 0 (normal), 1 (urgent) and 2 (super urgent)
- Normal patient is added to the end of the current queue of this specialization
- Urgent patient is added after current urgent patients & before normal patients
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



## Installation

it is just a one folder project that you can run the main file through bash shell after cloning the file to your desktop

```bash
  [mahmood79@server ~]#python hospital.py
  or 
  [mahmood79@server ~]#./hospital.py
``` 
    
