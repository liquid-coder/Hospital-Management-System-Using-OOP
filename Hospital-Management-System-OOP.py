
class Patient:
  def __init__(self,id,name,age,bg):
    self.id = id
    self.name = name
    self.age = age
    self.bg = bg
class DoublyNode:
  def __init__(self,elem,next = None,prev = None):
    self.elem = elem
    self.next = next
    self.prev =prev
class WRM:
  def __init__(self):
    self.head = DoublyNode(None)
    self.head.next = self.head
    self.head.prev = self.head
  def RegisterPatient(self,id,name,age,bg):
    add_patient = Patient(id,name,age,bg)
    new_node = DoublyNode(add_patient)
    new_node.next = self.head.next
    new_node.prev = self.head
    self.head.next.prev = new_node
    self.head.next = new_node
  def ServePatient(self):
    if self.head.next == self.head:
      print('No patients are currently in the waiting room')
      return
    patient = self.head.prev.elem
    self.head.prev.prev.next = self.head
    self.head.prev = self.head.prev.prev
    print('Serving Patient',patient.name)
  def CancelAll(self):
    self.head.next = self.head
    self.head.prev = self.head
    print('All appointments are cancelled')
  def CanDoctorGoHome(self):
    if self.head.next == self.head:
      print(f"Yes")
    else:
      print(f"No")
  def ShowAllPatient(self):
    present = self.head.next
    if present.elem == None:
       print('No patients are currently in lobby')
    else:
      while present!=self.head:
        print('Patient Name:',present.elem.name)
        present = present.next


print('Welcome To Waiting Room Management System')

patient=WRM()
while True:
  print(f'''==Choose an option==
  1.RegisterPatient
2.ServePatient
3.CancelAll
4.CanDoctorGoHome
5.ShowAllPatient
6. exit
===================''')
  pcount=int(input('Enter your choice:'))
  if pcount==6:
    print(f'Thank you for using waiting room management system\nEXITING..... ')
    break
  elif pcount==1:
    print('Executing RegisterPatient().....')
    id=int(input('Enter ID:'))
    name=input('Enter Name:')
    age=int(input('Enter Age:'))
    bloodgroup= input('Enter Bloodgroup:')

    patient.RegisterPatient(id, name, age, bloodgroup)
    print('Success in registering patient')
  elif pcount==5:
    print('Executing ShowAllPatient()....')
    patient.ShowAllPatient()
  elif pcount==2:
    patient.ServePatient()
  elif pcount==4:
    patient.CanDoctorGoHome()
  elif pcount==3:
    patient.CancelAll()
  else:
    print('There are no such option')