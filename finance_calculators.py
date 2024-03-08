"""
    This program allows user to access two different financial
    calculators: investment and home loan calculator The program
    outputs calculation based on the choice of the user from the
    menu and compute based on the inputs of the user.
 """

import math # importing libraries for math function
import os # importing libraries for clear screen function

choice = False
while not choice:
    Menu = (
    "\ninvestment - to calculate the amount of interest you'll earn on"
    " your investment"
    "\nbond       - to calculate the amount you'll have to pay on a"
    "home loan"
    "\nquit       - to exit the program"
)
    
    os.system('cls')
    title = " FINANCE CALCULATOR "
    print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
    print("\n")
    print(Menu)
    print()
    print("=" * 80)

    menu = input("\n\nEnter either 'investment'or 'bond' from the menu above to"
                 " proceed and 'q' to exit the program: ").lower()
    
    os.system('cls') # clears the screen
   
    # user chooses investment, it calculates interest earn in simple or 
    # compound interest.
    if  menu == "investment":
        title = " INVESTMENT CALCULATOR "
        print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
        print("\n")

        try:            
            amount_money = float(
                    input("\nEnter amount of money to be deposited:\t\t £")
            )
            
            interest_rate = float(
                    input("Enter interest rate. (e.g. 8):\t\t\t %")
            )

            number_year = int(input("Enter number of years to invest:\t\t  "))
            interest = input(
                "Enter type of interest rate (simple/compound):\t "
            ).lower()

            choice1 = "simple"
            choice2 = "compound"
            if interest == choice1:
                percentage_rate = interest_rate / 100
                simple_computation = (
                    amount_money * (1 + percentage_rate * number_year )
                )

                print(
                    f"Your investment would be worth:"
                    f" \t\t £{simple_computation:0.2f}\n"
                )

            elif interest == choice2:
                percentage_rate = interest_rate / 100
                compound_computation = (
                    amount_money * math.pow((1 + percentage_rate), number_year)
                )

                print(f"Your investment would be worth:"
                      f" \t\t {compound_computation:0.2f}\t\t\n"
                )

            else:
                print("\nMake sure to enter simple or compound only!")
                    
            repeat = input("\nWould you like to go back to the main menu? (Y/N): ")
            os.system('cls')
            if repeat.lower() == 'y':
                continue
            else:
                choice = True

        except ValueError:
            print("Invalid input!")
            repeat = input("\nWould you like to go back to the main menu? (Y/N): ")
            os.system('cls')

            if repeat.lower() == 'y':
                continue
            else:
                choice = True
                 
    # user chooses 'bond', it calculates the payment for the home loan
    elif menu == "bond":
            title = " BOND CALCULATOR "
            print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
            print("\n")
            
            try:
                value_of_home = float(
                        input("\nEnter present value of the house"
                              " (e.g. 100000):\t\t £")
                )
                
                interest_rate = float(
                    input("Enter interest rate (e.g. 7):\t\t\t\t %")
                )

                number_month = int(
                    input("Enter number of months to pay the bond."
                          " (e.g. 120):\t  ")
                )

                percentage_rate = (interest_rate / 100) / 12
                repayment = (
                            (percentage_rate * value_of_home) / 
                            (1 - (1 + percentage_rate) ** (-number_month))
                )
                print(f"Your monthly payment is: \t\t\t\t £{repayment:0.2f}\n")
                repeat = input("Would you like to go back to the main menu? (Y/N) ")
                os.system('cls')
                if repeat.lower() == 'y':
                    continue
                else:
                    choice = True
            
            except ValueError:
                print("Invalid input")
                repeat = input("\nWould you like to go back to the main menu? (Y/N): ")
                os.system('cls')
                if repeat.lower() == 'y':
                    continue
                else:
                    choice = True

  
    elif menu == 'q':
        choice = True

    else:
        print("\033[5mYour input is not recognized. Choose only from"
              " the given option\033[0m.\n")
       
       
