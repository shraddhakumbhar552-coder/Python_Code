# Smart Electricity Bill Calculator
from colorama import Fore, Style,Back,init
init()
customer_name=input("Enter Customer Name: ")
if customer_name=='':
    print(Fore.RED + "Customer name cannot be empty.")
else:
    print(f"Customer Name: {customer_name}")
    
    units_consumed=(input("Enter Units Consumed:"))
    if units_consumed.isdigit():
        units_consumed=int(units_consumed)
        if units_consumed>0:
            print("Total units consumed:" ,units_consumed)
        
            if units_consumed<=100:
                Energy_charge=units_consumed*3
                print("Energy Charge",Energy_charge)
            
            elif units_consumed<=200:
                Energy_charge=(100*3)+(units_consumed-100)*5
                print("Energy Charge",Energy_charge)
                
            else:
                Energy_charge=(100*3)+(100*5)+(units_consumed-200)*100
                print("Energy Charge",Energy_charge)
                 
            service_charge=150
            print("Service Charge:",service_charge)
                
            final_bill=Energy_charge+service_charge
            print("Final Bill:",final_bill)
                
            if final_bill>5000:
                print(Fore.RED+"High Usage Bill")
                 
            else:
                print(Fore.GREEN+"Normal Usage")
         
        else:
            print(Fore.RED+"Unit must be greater than zero:")           
    else:
        print(Fore.RED+"Enter a valid unit number")
           
               
                
         

