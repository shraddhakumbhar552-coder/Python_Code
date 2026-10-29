# online shopping checkout

from colorama import Fore,Back,Style,init
init()

customer_name=input("Enter your customer name:")

if customer_name=='':
    
    print(Fore.RED+"Customer name cannot be empty")

else:
    print(f"Customer Name {customer_name}")
    
    purchase_amount=input("Enter your amount:").strip() 
    discount=0
    # prurchase amount validation
    if purchase_amount.replace(".", "", 1).isdigit() or purchase_amount.startswith("-") and purchase_amount[1:].replace(".", "", 1).isdigit():
        purchase_amount=float(purchase_amount)
        if purchase_amount>0:
            # print("valid purchase amount")
            print("Your purchased amount:",purchase_amount)
         # Regular discount calculation
        
            if purchase_amount>=5000:
                discount = purchase_amount * 20 / 100
            elif purchase_amount>=3000 and purchase_amount<5000:
                discount=purchase_amount*10/100
            elif purchase_amount>=1000 and purchase_amount<3000:
                discount=purchase_amount*5/100
            else:
                discount=0
                print("There will be no regular discount below 1000")
            print("Regular Discount:",discount)
            
            # amount after purchase 
            amount_after_discount=purchase_amount-discount
            customer_type=input("Enter a customer type (Premiun or Regular): ").strip() .lower()
            
            if customer_type=='':
                print(Fore.RED+ "Customer type cannot be empty")
            
            elif customer_type=="premium":
                premium_discount=amount_after_discount*5/100
                final_amount=amount_after_discount-premium_discount
                print("Premium Discount:",premium_discount)
            
            elif customer_type=="regular":
                premium_discount=0
                final_amount=amount_after_discount
                print("Regular Discount:",premium_discount)
            
            else:
                print(Fore.RED + "Invalid customer type")
            
            if customer_type=="premium" or customer_type=='regular':
                 
                if final_amount>2000:
                    delivery_charge=0
                    print("You get a free delivery")
                    
                else:
                    delivery_charge=100
                    print("Delivery Charges:100")
                final_payable_amount=final_amount+delivery_charge
                print("Final Amount:", final_amount)
                print("Your Final Payable Amount:", final_payable_amount)  
        else:
            print(Fore.RED + "Amount must be greater than zero")
                     
    else:
        print(Fore.RED + "Please enter a valid amount")
            
            
      

    
                 
             
                
            
            
            


            