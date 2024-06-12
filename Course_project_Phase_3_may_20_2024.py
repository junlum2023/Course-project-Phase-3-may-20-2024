#Jun lum

def GetEmpNames():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter Start date (mm/dd/yyyy): ")
    todate = input("Enter End date (mm/dd/yyyy): ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input("Enter amount of hours worked: "))
    return hours

def GetHourlyrate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    GrossPay = hours * hourlyrate
    incometax = GrossPay * taxrate
    netpay = GrossPay - incometax 
    return GrossPay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
      
        GrossPay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.1%}", f"{hourlyrate:,.2f}", f"{GrossPay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += GrossPay
        TotTax += incometax
        TotNetPay += netpay
        
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay
        
def PrintTotals(Emptotals):
    print()
    print(f"Total number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['Tothrs']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"total Income tax: {EmpTotals['Tottax']:,.2f}")
    print(f"Total Net Pay: {EmpTotals['TotNetpay']:,.2f}")
    
def WriteEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5]))

def GetFromdate():
    valid = False
    fromdate = ""
    
    while not valid:
        fromdate = input("Enter From Date (mm/dd/yyyy): ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid date format")
            
        else:
            valid = True
        
    return fromdate

def ReadEmployeeInfomation(fromdate):
    EmpDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    condition = True
    
    if fromdate.upper() == 'All':
        condition = False
        
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]

        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromdate == employee[0]:
               EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList    

if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        empname = GetEmpNames()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyrate()
        taxrate = GetTaxRate()
        
        print()
        
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        WriteEmployeeInformation(EmpDetail)
    print()
    print()
    fromdate = GetFromdate()
    
    EmpDetailList = ReadEmployeeInfomation(fromdate)
    
    print()
    PrintTotals(EmpTotals)
    
    
                            
          
        
        
                   
