
import pickle,tabulate
class vechile_details:
  #list of keys of the attributes of the vehicle.
  _keyList = ["id","ownerName","vendor","model","type","registrationNumber","engineNumber","mileage"]
  #creating a dictionary with the keys and values as None.
  _dataBase = dict.fromkeys(_keyList, None)

class Vehicles(vechile_details):
  #list which will save the dictionary of every vehicles
  __listOfVehicles = list()
  __id = 0
  def addEntries(self):
    option = 1
    while option==1:
      self.__id = self.__id + 1
      entryList = list()
      entryList.append(self.__id)
      entryList.append(input("Owner Name : "))
      entryList.append(input("Name of the Vendor : "))
      entryList.append(input("Model Name : "))
      entryList.append(input("Type of Vehicle : "))
      entryList.append(int(input("Registration Number : ")))
      entryList.append(int(input("Engine Number : ")))
      entryList.append(float(input("Vehicle Mileage : ")))
      
      for i,key in zip(entryList,self._dataBase):
        self._dataBase[key] = i
      self.__listOfVehicles.append(self._dataBase.copy())
      option = int(input("Press 1 to Add more entries\nPress 2 to exit "))

  def deleteEntries(self):
    found = False
    searchKey = int(input("Enter your ID : "))
    for i in range(len(self.__listOfVehicles)):
      if self.__listOfVehicles[i]['id']==searchKey:
        found = True
        del self.__listOfVehicles[i]
        break
    if(not found):
      print("Invalid Id")
  
  def modify(self):
    found = False
    searchKey = int(input("Enter your ID : "))
    for i in self.__listOfVehicles:
      if i['id']==searchKey:
        found = True
        print("Choose the attribute you want to modify")
        print("1.Owner Name\n2.vendor\n3.Model Name")
        print("4.Type of Vehicle \n5.Registration Number\n6.Engine Number")
        print("7.Mileage")
        option = int(input())
        if option==1:
          i['ownerName'] = input("Owner Name : ")
        elif option==2:
          i['vendor'] = input("vendor : ")
        elif option==3:
          i['model'] = input("Model Name : ")   
        elif option==4:
          i['type'] = input("Type : ")
        elif option==5:
          i['registrationNumber'] = int(input("Registration Number : "))    
        elif option==6:
          i['engineNumber'] = int(input("Engine Number : "))
        elif option==7:
          i['mileage'] = float(input("Mileage : "))
    if(not found):
      print("Invalid Key")

  def display(self,*args):
    header = ['Id','Owner','Vendor','Model','Type','Registration Number','Engine Number','Mileage']
    if(len(args)==0):
      rows =  [x.values() for x in self.__listOfVehicles]
      print(tabulate.tabulate(rows, header,tablefmt='grid'))
    elif (len(args)==2):
      print("\n",args[0])
      rows = [x.values() for x in args[1]]
      print(tabulate.tabulate(rows, header,tablefmt='grid'))

  def mileage_sort(self):
    sortedList = sorted(self.__listOfVehicles,key = lambda i:i['mileage'])
    self.display("Sorted Mileage List",sortedList)

  def list_of_vehicles(self):
    pickle.dump(self.__listOfVehicles,open("vehicleDetails.pkl","wb"))

  def sort_attributes(self):
    print("Choose the attribute which you want to sort\n1.Owner Name")
    print("2.Vendor\n3.Model Name\n4.Type\n5.Mileage")
    option = int(input("Option : "))
    sortedList = list()
    if(option==1):
      sortKey = (input("Enter the name you want to sort"))
      sortedList = [i for i in self.__listOfVehicles if i['ownerName']== sortKey]
      self.display("sorted List",sortedList)
    elif (option==2):
      sortKey = (input("Enter the name you want to sort"))
      sortedList = [i for i in self.__listOfVehicles if i['vendor']== sortKey]
      self.display("sorted List",sortedList)
    elif (option==3):
      sortKey = (input("Enter the name you want to sort"))
      sortedList = [i for i in self.__listOfVehicles if i['model']== sortKey]
      self.display("sorted List",sortedList)
    elif (option==4):
      sortKey = (input("Enter the name you want to sort"))
      sortedList = [i for i in self.__listOfVehicles if i['type']== sortKey]
      self.display("sorted List",sortedList)
    elif(option==5):
      sortKey = float(input("Enter the name you want to sort"))
      sortedList = [i for i in self.__listOfVehicles if i['mileage']== sortKey]
      self.display("sorted List",sortedList)
  def loadFile(self,filePath):
    self.__listOfVehicles = pickle.load(open(filePath,"rb"))
    idList = [self.__listOfVehicles[i]['id'] for i in range(len(self.__listOfVehicles))]
    self.__id = max(idList)

def main():
  vehicleObject = Vehicles()
  mainLoopOption= 'y'
  if(int(input("Press 1 to Add new Entries \nPress 2 to Save report "))==1):
    vehicleObject.addEntries()  
  else:
    filePath = input("Enter the file name : ")
    vehicleObject.loadFile(filePath)
  vehicleObject.display()
  
  if( mainLoopOption=='y'):
    print("1.Add Entries\n2.Modify Attributes\n3.Delete Attributes\n4.Display Entries")
    print("5.Sort According to Mileage\n6.sort Attributes\n7.Create Pdf File\n8.Exit")
    choice = int(input())
    if choice==1:
      vehicleObject.addEntries()
    elif choice==2:
      vehicleObject.modify()
    elif choice==3:
      vehicleObject.deleteEntries()
    elif choice==4:
      vehicleObject.display()
    elif choice==5:
      vehicleObject.mileage_sort()
    elif choice==6:
      vehicleObject.sort_attributes()
    elif choice==7:
      vehicleObject.list_of_vehicles()
    elif choice==8:
      print("Thank you")
  mainLoopOption = input("\nDo you Want to continue ?(y/n) ")

if __name__=="__main__":
  main()
