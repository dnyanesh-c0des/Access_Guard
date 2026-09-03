def design():
  print("="*105)





# Phase 1 : Data Setup & Company Info

available_tools=["Github", "AWS", "Slack", "Jira", "Production Server", "HR Portal", "Figma", "Docker"]
valid_roles=("intern", "developer", "tester", "manager", "admin")
company_info=("Infoysys", "Bengaluru", "2 July 1981", "ISO 27001 Certified")
role_based_permissions={
    "intern":["Slack","Jira"],
    "developer":["Github","Slack","Jira","AWS"],
    "tester":["Slack","Jira","Github","Docker"],
    "manager":["Github","Slack","Jira","AWS","HR Portal"],
    "admin":["Github","Slack","Jira","AWS","HR Portal","Production Server","Figma","Docker"]
                       }
employees_info={
   "E101": {
        "name":"Aarav Sharma",
        "role":"developer",
        "access list":["Slack","Jira"],
        "email":"aarav.sharma@infoysys.com"
          },
   "E102": {
        "name":"Sneha Patil",
        "role":"intern",
        "access list":["Slack","Jira"],
        "email":"sneha.patil@infoysys.com"
         }
               }
access_log=[("E101","Github","GRANTED","2026-07-15"),
            ("E102","AWS","DENIED","2026-08-02") ]

company_name, company_hq, company_est_date, company_cert=company_info

# Welcome Banner
design()
print(f"   {company_name} | HQ:{company_hq} | Est:{company_est_date}")
print(f"   Security Standard: {company_cert}")
design()
print(f"   Total tools available: {len(available_tools)}")
print(f"   Valid roles: {len(valid_roles)}")
print(f"   Employees registered: {len(employees_info)}")
design()
print()
print(f"Available Tools: {available_tools}\n")
print(f"Valid roles: {valid_roles}\n")
print(f"Role Permissions:")
print(f"   intern    --> {role_based_permissions["intern"]}")
print(f"   developer --> {role_based_permissions["developer"]}")
print(f"   tester    --> {role_based_permissions["tester"]}")
print(f"   manager   --> {role_based_permissions["manager"]}")
print(f"   admin     --> {role_based_permissions["admin"]}")
print(f"\n Existing Employees:")
print(f"   E101 | {employees_info["E101"]["name"]} | {employees_info["E101"]["role"]} | {employees_info["E101"]["access list"]} | {employees_info["E101"]["email"]} |")
print(f"   E102 | {employees_info["E102"]["name"]}  | {employees_info["E102"]["role"]}    | {employees_info["E102"]["access list"]} | {employees_info["E102"]["email"]}  |")
print(f"\n Access Log:")
print(f"   {access_log[0]}")
print(f"   {access_log[1]}")
design()



# Phase 2 : Onboard a new employee

#Getting user's name
employee_name=input("Enter your full name in the form Donald Trump:").strip().title()
employee_name=employee_name.split()
first_name=employee_name[0]
last_name=employee_name[-1]
full_name=" ".join(employee_name)

if(first_name.isalpha() and last_name.isalpha()):
  print(f"Name accepted: {full_name}")
else:
  print("Incorrect form of name")

#Getting Employee ID
employee_id=input("Enter your employee id starting with E in correct format:")
employee_id=employee_id.upper()
if not (employee_id.startswith("E")):
  print("Employee ID should start with E")
elif not (employee_id[1:].isdigit()):
  print("The last 3 characters should be digit")
elif not (len(employee_id)==4):
  print("Length should be 4")
else:
  print(f"Valid Employee ID : {employee_id}")

#Getting role
employee_role=input("Enter your role:")
employee_role=employee_role.lower()

if(employee_role in valid_roles):
  print("Your role:", employee_role)
else:
  print("Enter a role from the following only:",valid_roles)


employee_email=first_name.lower() + "." + last_name.lower() + "@" + company_name.lower() + "." + "com"
print(f"Your email: {employee_email}")

employee_password=first_name[:3].lower()+employee_id[1:]+"@TN"
print(f"Your password is {employee_password}")

years_of_exp=int(input("Enter your number of years of experience in integer:"))
print(f"Your years of experience is: {years_of_exp}")

employee_access=["Slack","Jira"]

employees_info[employee_id]={
    "name":full_name,
    "role":employee_role,
    "access list":employee_access,
    "email":employee_email
}

onboarding_record=(employee_id,full_name,employee_role,"2026-08-11")


# Displaying onboarding summary
print("\n\n\n\n\n\n")
design()
print("   ONBOARDING COMPLETE \n ")
print("   Name      : ",full_name)
print("   ID        : ",employee_id)
print("   Role      : ",employee_role)
print("   Email     : ",employee_email)
print("   Password  : ",employee_password)
print("   Access    : ",employee_access)
design()
print("   Permanent Record: ",onboarding_record)
print("   Record type: ",type(onboarding_record))
design()
print("   Your experience: ")
if(years_of_exp==0):
  print("   Fresher detected.Mentor will be assigned.")
elif(3>=years_of_exp>=1):
  print("   Junior level")
elif(7>=years_of_exp>=4):
  print("   Mid level")
elif(years_of_exp>=8):
  print("   Senior level")
else:
  print("   Experience cannot be negative.")
design()




# Phase 3: Access Request Portal

design()
var5555="ACCESS REQUEST PORTAL"
print(var5555.center(105,"-"))
design()
print(f"\nRegistered Employee ID's: {employees_info.keys()}")

requested_employee_id=input("Enter your employee ID:").upper().strip()
emp= employees_info.get(requested_employee_id)
print(emp)

design()
if emp is None:
  print("No employee found with ID : ", requested_employee_id)
else:
  print(f"\nWelcome {emp["name"]}!")
  print(f"Current role: {emp["role"].title()}")
  print(f"Current access: {emp["access list"]}")
design()
print(f"\nAll company tools: {available_tools}")
requested_tool=input("Which tool  you need to access? :").strip()
design()
if(requested_tool not in available_tools):
  print(f"{requested_tool} is not in {available_tools}")

elif(requested_tool in emp["access list"]):
  print(f"{requested_tool} is already in your access list.")
  print(f"Index no. of which is {emp["access list"].index(requested_tool)}")

elif(requested_tool not in role_based_permissions.get(emp["role"],[])):
  print(f"<<< ACCESS DENIED >>>\n")
  print(f"   {emp["role"].title()} are not allowed to use {requested_tool}.")
  print(f"   Your role allows: {role_based_permissions[emp["role"]]}")

  log1=(requested_employee_id,requested_tool,"DENIED","2026-08-13")
  access_log.append(log1)
  print(f"   Your denied request is stored in log:{log1}")

else:
  emp["access list"].append(requested_tool)
  log2=(requested_employee_id,requested_tool,"GRANTED","2026-08-13")
  access_log.append(log2)

  print(f"<<< ACCESS GRANTED >>>\n")
  print(f"   Access to {requested_tool} granted to {emp["name"]}.")
  print(f"   Updated Access: {emp["access list"]}")
  print(f"   Total number of tools access to employee= {len(emp["access list"])}")
  print(f"   Your granted request is stored in log:{log2}")

design()

print(f"All employee's data: {employees_info.values()}")

design()




#Phase 4: Tool Audit And Comparison
#I'm giving Aarav his roles to execute the program more nicely, at last Aarav's access list becomes original one.

var55=employees_info["E101"]["access list"]
employees_info["E101"]["access list"]= ["Slack","Jira","Github","AWS"]

Aarav_access_set=set(employees_info["E101"]["access list"])
Sneha_access_set=set(employees_info["E102"]["access list"])
tools_set=set(available_tools)

design()
var4444="INFOYSYS AUDIT AND COMPARISON"
print(var4444.center(105,"~"))
design()

print(f"Aarav's access set: {Aarav_access_set}")
print(f"Sneha's access set: {Sneha_access_set}")
print(f"Total available tools set: {tools_set}")

design()

union=Aarav_access_set | Sneha_access_set
unused=tools_set-union

print(f"   Common tools shared between both Aarav and Sneha are: {Aarav_access_set & Sneha_access_set}")
print(f"   Tools which only Aarav has are                      : {Aarav_access_set - Sneha_access_set}")
print(f"   Tools which only Sneha has are                      : {Sneha_access_set - Aarav_access_set}")
print(f"   Total tools which are used in combine of both are   : {Aarav_access_set | Sneha_access_set}")
print(f"   Tools only one of them have (Exclusive tools) are   : {Aarav_access_set ^ Sneha_access_set}")
print(f"   Total UNUSED tools which no one uses are            : {tools_set-union}")

print(f"        Company is paying for {len(unused)} unused tool(s)!\n")

if (Sneha_access_set.issubset(Aarav_access_set)==True):
  print(f"   Sneha's access list is SUBSET of Aarav's access list.")
else:
  print(f"   Aarav's access list is SUBSET of Sneha's access list.")


if (Sneha_access_set.issuperset(Aarav_access_set)==True):
  print(f"   Sneha's access list is SUPERSET of Aarav's access list.")
else:
  print(f"   Aarav's access list is SUPERSET of Sneha's access list.")
  
if (Aarav_access_set.isdisjoint(Sneha_access_set)==True):
  print(f"   Their access lists do not overlap.")
else:
  print(f"   Their access lists overlap.\n")

design()

tools_set.add("Kubernetes")
tools_set.add("Slack")

print(tools_set)
print("Kubernetes and Slack were added in the set but if slack is already present then the set does not repeats same thing.\n")

tools_set.discard("Figma")
tools_set.discard("Miro")
print(tools_set)
print("Figma and Miro were removed from the set using .discard() function but Miro was not in the set and no error was generated,")
print("As discard function does'nt gives error when item which is not in the set is removed.\n")

tools_set.remove("HR Portal")
print(tools_set)
print("HR Portal was removed from the set using .remove() function but if we tried this function on item which is not in set then it will give us error.\n")

tools_set.pop()
print(tools_set)
print(".pop() function was used(its random removal in sets).\n")

tools_set.clear()
print(tools_set)
print("Set was cleared using .clear() function.\n")

design()

Buggy_list=["Slack","Jira","Slack","Github","AWS","Figma","AWS","AWS"]
print(f"\nBuggy list : {Buggy_list}")
print(f"Length of list before coverting to set= {len(Buggy_list)}\n")

Buggy_list_set=set(Buggy_list)

Cleaned_list=list(Buggy_list_set)
print(f"Cleaned list: {Cleaned_list}")
print(f"Length of list after converting back to list from set= {len(Cleaned_list)}\n")

design()

employees_info["E101"]["access list"]=var55





#Phase 5: Revoke Access and Log Analysis
print(f"{"Revoke Access":^105}")
revoke_employee_id=input("Enter employee ID:").strip().title()

checking1=employees_info.get(revoke_employee_id)

if(checking1==None):
  print(f"Enter a valid Employee Id among these :{employees_info.keys()}")
else:
  revoke_tool=input("Enter tool which you want to revoke:").strip().title()
  # Corrected logical condition: use 'not in' for clarity and accuracy
  if revoke_tool not in employees_info[revoke_employee_id]["access list"]:
    print(f"WARNING!!! You don't have the access to {revoke_tool}")
  else:
    var3333=employees_info[revoke_employee_id]["access list"].index(revoke_tool)
    print(f"Position of tool which is being revoked is: {var3333 + 1}")
    employees_info[revoke_employee_id]["access list"].remove(revoke_tool)

    log3=(revoke_employee_id,revoke_tool,"REVOKED","2026-08-14")
    access_log.append(log3)
    print(f"{revoke_tool} access revoked from {employees_info[revoke_employee_id]["name"]}.")
    print(f"   Updated access: {employees_info[revoke_employee_id]["access list"]}")
    print(f"   Revocation logged: {log3}\n")

    print(f"Access Log :{access_log}")

design()
var6666="Access Log Analysis"
print(var6666.center(105,"-"))
design()

print(f"\nTotal log entries  : {len(access_log)}")
print(f"First entry        : {access_log[0]}")
print(f"Last entry         : {access_log[-1]}")
print(f"Recent 3 entries   : {access_log[-3:]}") # Corrected: use slice notation [-3:]
print(f"Sorted log         : {sorted(access_log)}") # Corrected: use built-in sorted() function
print(f"Reversed log       : {list(reversed(access_log.copy()))}") # Corrected: get a reversed copy
# Note: access_log.pop() modifies the list. If you want to show it without modifying,
# consider access_log[-1] or deepcopy before pop if further use of full log is needed.
popped_entry = access_log.pop() # Pop the last entry and store it
print(f"Popped entry       : {popped_entry}")
access_log.insert(0,("SYSTEM","AUDIT","STARTED","2026-08-27"))
print(f"After insert       : {access_log}")







#Phase 6: Update Employee Record

update_employee_id=input("Enter employee ID: ").strip().title()

checking2=employees_info.get(update_employee_id)
design()

if(checking2==None):
  print(f"Enter a valid Employee Id among these :{employees_info.keys()}")
else:
  print(f"Current record for {update_employee_id}:")
  print(f"   Fields           : {employees_info[update_employee_id].items()}")
  print(f"   Availables fields: {employees_info[update_employee_id].keys()}")

  design()

  update_employee_role=input("Enter the new role of employee(you can just press Enter if u don't want new role):").lower()
  if(update_employee_role in valid_roles):
    employees_info[update_employee_id].update({"role":update_employee_role})
    employees_info[update_employee_id].update({"access list":role_based_permissions[update_employee_role]})
    print(f"Role updated to {update_employee_role}")
    print(f"   Access reset to : {employees_info[update_employee_id]["access list"]}")
  elif(update_employee_role==""):
    pass
  else:
    print("\n\n\nEnter a valid role from : ", valid_roles)
    
  design()

  employees_info[update_employee_id].setdefault("phone","Not provided")
  phone_no=input("Enter employee's phone number(Press enter if you want to skip):")
  if(len(phone_no)==10 and phone_no.isdigit()==True or phone_no==""):
    print(f"   Phone number updated: {phone_no}")

    design()

    remove_key=input("Enter a key name from 'Available fields' above to remove the item:")
    if(remove_key==""):
      pass
    elif(remove_key not in employees_info[update_employee_id].keys()):
      print("Enter a valid key")
    else:
      var2222=employees_info[update_employee_id][remove_key]
      employees_info[update_employee_id].pop(remove_key,"Field not found")

      design()

      print(f"   Removed {remove_key} was {var2222}")

      design()

    print(f"Updated record:")
    print(f"   Keys : {employees_info[update_employee_id].keys()}")
    print(f"   Values : {employees_info[update_employee_id].values()}")

  else:
    print(f"Enter correct phone number......")








 #Phase 7: Cloning An Employee's Report

design()
var1111="Cloning an Employee's data"
print(var1111.center(105,"-"))
design()

new_access_list=employees_info["E101"]["access list"].copy()
new_access_list.append("Production Server")

print(f"   Aarav's access list: {employees_info["E101"]["access list"]}")
print(f"   Riya's access list : {new_access_list}")

design()

print(f"   Memory address of Aarav's access list: {id(employees_info["E101"]["access list"])}")
print(f"   Memory address of Riya's access list: {id(new_access_list)}")
print(f"   Aarav's access list and Riya's access list are the same : {employees_info["E101"]["access list"] is new_access_list}")

design()

copy1 = list(employees_info["E101"]["access list"])
copy2 = employees_info["E101"]["access list"][:]

print(f"   Copy 1 created using list(): {copy1}")
print(f"   Copy 2 creatd using [:]    : {copy2}")
print(f"   Copy 1 and Copy 2 are the same: {copy1 is copy2}")

design()

backup_Aarav_access_list = employees_info["E101"]["access list"].copy()
backup_Aarav_access_list.append("Figma")
print(f"   To confirm original list does'nt changes when a tool is added in backup list")
print(f"   Original list: {employees_info["E101"]["access list"]}")
print(f"   Backup list: {backup_Aarav_access_list}")

design()   








#Phase 8: Final Dashboard And Report

var7777="ACCESS GUARD - FINAL REPORT"
print(var7777.center(105,"="))
var8888="Company"
print(f"{var8888.upper():>105}")

print(f"\n {"ID":<15} {"Name":<10} {"Role":>30} {"Tools":>20} {"Access list":>15}")

print("-"*105)

ID1,ID2,ID3=employees_info.keys()

print(f" {ID1:<15} {employees_info["E101"]["name"]:<10} {employees_info["E101"]["role"].upper():>33} {len(employees_info["E101"]["access list"]):>11} {" | ".join(employees_info["E101"]["access list"]):>20}")
print(f" {ID2:<15} {employees_info["E102"]["name"]:<10} {employees_info["E102"]["role"].upper():>32} {len(employees_info["E102"]["access list"]):>13} {" | ".join(employees_info["E102"]["access list"]):>20}")
print(f" {ID3:<15} {employees_info["E103"]["name"]:<10} {employees_info["E103"]["role"].upper():>26} {len(employees_info["E103"]["access list"]):>15} {" | ".join(employees_info["E103"]["access list"]):>20}")

design()

print("Total  Employees:", len(employees_info) , "   Total Tools:", len(available_tools) , "   Log Entries:" ,len(access_log) , sep=" | " , end=" | ")

var9999="ACCESS LOG"
print(f"\n\n\n\n {var9999.center(105,"-")}")

print(f"\n{"Emp ID":<15} {"Tool":<10} {"Status":>30} {"Date":>20}")
print("-"*105)
print(f"{access_log[1][0]:<15} {access_log[1][1]:<10} {access_log[1][2]:>31} {access_log[1][3]:>25}")
print(f"{access_log[2][0]:<15} {access_log[2][1]:<10} {access_log[2][2]:>31} {access_log[2][3]:>25}")
print(f"{access_log[3][0]:<15} {access_log[3][1]:<10} {access_log[3][2]:>31} {access_log[3][3]:>25}")
print("-"*105)

print("Report generated by AccessGuard v1.0".center(105))
print("Confidential - Internal Use Only".center(105))