from rich.table import Table
from rich.console import Console
mylist = []
print("How many entries do you want to add? \n")
print("\n")

TotalEntries = int(input())

for i in range (1,TotalEntries+1):
   
    print("spending ? \n")
    spending = int(input())
    print("\n")

     
    print("date? \n")
    date = input()
    print("\n")


   
    print("Where did you spend it ? \n")
    remarks = input()
    print("\n")

    mydict = {
            "amount" : spending,
            "date"   : date,
            "remarks"  : remarks
            }
    mylist.append(mydict) 

 
table = Table()
console = Console()
table.add_column("amount spent")
table.add_column("date")
table.add_column("remarks")
for entry in mylist:
    
    v1 = str(entry["amount"])
    v2 = entry["date"]
    v3 = entry["remarks"]
    table.add_row(v1,v2,v3)

console.print(table)

print("thank you for using")