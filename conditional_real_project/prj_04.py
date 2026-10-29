# Student Scholarship Eligibility

from colorama  import Fore,Back,Style,init
init()


stud_name=input("Enter Student Name:").strip().title()
if stud_name=='':
    print("Student name cannot be empty")

else:
    percentage=input("Enter your percentage: ").strip()
    fam_income=input("Enter your annual income:").strip()
    attendance_per=input("Enter your attendance percentage:").strip()
    
    # input validation
    if percentage=='' or fam_income==''or  attendance_per=='':
        print("All fields are  compulsory")
    
    elif  percentage.isdigit()  and fam_income.isdigit() and attendance_per.isdigit():
        percentage=int(percentage)
        fam_income=int(fam_income)
        attendance_per=int(attendance_per)
        
        # basic eligibility conditions
 
        if percentage>=75 and fam_income<=400000 and attendance_per>=75:
            if percentage>=90:
                eligibility_status="Eligible"
                scholarship_category = "Full Scholarship"
                
            else:
                eligibility_status="Eligible"
                scholarship_category="Parial Scholarship"
            reason="All condition satisfied"
        else:
            eligibility_status='Not Eligible'
            scholarship_category="No Scholarship"
            
            # rejetion reason
            if percentage<75:
                reason="Percentage must be at least 75%"
            elif fam_income>400000:
                reason="Annual family income must be rs 4,00,0000 or less"
            else:
                reason='Attendance must be least 75%'
        
        # final output
        # Final Output
        print("\n========== SCHOLARSHIP DETAILS ==========")
        print("Student Name:", stud_name)
        print("Percentage:", percentage, "%")
        print("Annual Family Income: ₹", fam_income)
        print("Attendance:", attendance_per, "%")
        print("Eligibility Status:", eligibility_status)
        print("Scholarship Category:", scholarship_category)
        print("Reason:", reason)

    else:
        print("Please enter valid numeric values")