# In order for the totals to display as money, I need this import
import locale
import math

# Set totals to USD
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

# Global Variables: Assigned fee & taxes source:https://quickbooks.intuit.com/r/free-self-employment-tax-calculator/
transactionFee = 0.05
transactionFeePercent = transactionFee * 100
medicareTax = 0.029
socialSecurityTax = 0.124
additionalTax = 0.3  # Estimated rounded high end of additional taxes source: https://www.fundera.com/blog/small-business-tax-rate
business_deduction = 0.3963656


def main():
    # Display Start Menu for user
    print("MAIN MENU")
    print("-" * 50)
    response = input("1. Calculate Your Subscription Earnings\n"
                     '2. "How Many Subscribers Do I Need?" Calculator\n'
                     "Choose a calculator (1 or 2): ")

    if response.isnumeric() or is_float(response):
        response = int(float(response))
        if response == 1:
            calculate_totals()
        elif response == 2:
            calculate_subs()
        else:
            print("Invalid key. Try again.\n\n")
            main()
    else:
        print("Invalid key. Try again.\n\n")
        main()


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate_totals():
    # Ask user for sub info
    supporters = input("\nNumber of Supporters: ")
    if not supporters.isnumeric():
        if not is_float(supporters) == True:
            print("Invalid key. Try again.")
            calculate_totals()
    else:
        subscription_fee = input("Monthly Subscription Fee: $")

        if subscription_fee.isnumeric() or is_float(subscription_fee) == True:
            supporters = int(supporters)
            subscription_fee = float(subscription_fee)
            # All formulas needed to find subtotals, monthly total with taxes, amount paid in taxes,
            subscription_total = supporters * subscription_fee
            transaction_fee_total = subscription_total * transactionFee
            total = subscription_total - transaction_fee_total
            deduction = total * business_deduction
            total_with_deduction = total - deduction
            taxes = (total_with_deduction * medicareTax) + (total_with_deduction * socialSecurityTax) + (
                    total_with_deduction * additionalTax)
            total_with_tax = total - taxes

            # Yearly sums
            yearly_income = total * 12
            yearly_income_with_tax = total_with_tax * 12
            yearly_business_deduction = deduction * 12
            taxes_paid_yearly = taxes * 12
            transaction_fee_yearly = transaction_fee_total * 12

            # Make the totals look like money
            total = locale.currency(float(total), grouping=True)
            taxes = locale.currency(float(taxes), grouping=True)
            total_with_tax = locale.currency(float(total_with_tax), grouping=True)
            yearly_income = locale.currency(float(yearly_income), grouping=True)
            yearly_income_with_tax = locale.currency(float(yearly_income_with_tax), grouping=True)
            yearly_business_deduction = locale.currency(float(yearly_business_deduction), grouping=True)
            taxes_paid_yearly = locale.currency(float(taxes_paid_yearly), grouping=True)
            transaction_fee_yearly = locale.currency(float(transaction_fee_yearly), grouping=True)

            # Display Monthly Sums
            print("\nThe Transaction Fee is " + str(transactionFeePercent) + "%")
            print("Your Monthly Income without Tax: " + str(total))
            print("Your Monthly Income with Tax: " + str(total_with_tax))
            print("Monthly Taxes Paid: " + str(taxes))

            # Display Yearly Sums
            print("\nANNUAL TOTALS")
            print("-" * 50)
            print("Your Yearly Income without Tax: " + str(yearly_income))
            print("Your Yearly Income with Tax: " + str(yearly_income_with_tax))
            print("Your Yearly Business Deduction: " + str(yearly_business_deduction))
            print("Your Yearly Taxes (Medicare, Social Security, & Additional Taxes): " + str(taxes_paid_yearly))
            print("Your Yearly Transaction Fee: " + str(transaction_fee_yearly))
            print("\n***ALL TAXES ARE HIGH-END ESTIMATES. YOU MAY PAY LESS WHEN YOU ACTUALLY FILE YOUR TAXES***\n")

            start_over(calculate_totals)
        else:
            print("Invalid key. Try again.")
            calculate_totals()


def calculate_subs():
    # Ask user for desired income & their monthly subscription fee
    total_money = input("\nThe amount you want to make a month: $")

    # Check ValueError
    if not total_money.isnumeric or is_float(total_money) == False:
            print("Invalid key.")
            calculate_subs()
    else:
        sub_fee = input("Monthly Subscription Fee you'll charge: $")

        # Check ValueError
        if sub_fee.isnumeric() or is_float(sub_fee) == True:
            total_money = float(total_money)
            sub_fee = float(sub_fee)

            # Calculate user's answer for minimum required subscriber total amount
            total_money_with_deduction = total_money - (total_money * business_deduction)
            charges = (total_money_with_deduction * medicareTax) + \
                      (total_money_with_deduction * socialSecurityTax) + \
                      (total_money_with_deduction * transactionFee) + \
                      (total_money_with_deduction * additionalTax)

            total_money_with_tax = total_money - charges
            total_money_needed = total_money_with_tax + (charges * 2.485)
            subs = total_money_needed / sub_fee
            subs_round_up = math.ceil(subs)
            subs_round_up = int(subs_round_up)

            # Change totals into USD
            total_money = locale.currency(float(total_money), grouping=True)
            subs_round_up = ("{:,.0f}".format(subs_round_up))

            # Display subscriber calculation
            print("The Transaction fee is " + str(transactionFeePercent) + "%")
            print("You will need " + (str(subs_round_up)) + " subscribers in order to make at least " + str(
                total_money) + " a month after taxes.")
            start_over(calculate_subs)
        else:
            # ValueError catch
            print("\nInvalid key. Try again.")
            calculate_subs()


def main_menu_choice(calc):
    main_menu_answer = input("\nOkay. Go to Main Menu or just quit the program (M/Q): ")
    print("\n" * 10)
    main_menu_answer = main_menu_answer.upper()

    if not main_menu_answer.isnumeric() or is_float(main_menu_answer) == True:

        # Go to Main Menu
        if main_menu_answer == "M":
            main()

        # Quit program
        elif main_menu_answer == "Q":
            print("\nAlright. Goodbye!")

        else:
            print("Invalid key. Try again.")
            main_menu_choice(calc)

    # ValueError catch
    else:
        print("Invalid key. Try again.\n\n")
        main_menu_choice(calc)


def start_over(calc):
    # Ask user if they want to restart the calculator
    answer = input("\nNew calculation? (Y/N): ")
    print("\n")
    answer = answer.upper()

    if not answer.isnumeric() or is_float(answer) == True:

        # Restart calculator
        if answer == "Y":
            return calc()
        # Ask user if they want to quit or go back to the Main Menu
        elif answer == "N":
            main_menu_choice(calc)

        else:
            print("Invalid Key. Try again.")
            start_over(calc)
    else:
        print("Invalid key. Try again\n\n")
        return start_over(calc)


main()
