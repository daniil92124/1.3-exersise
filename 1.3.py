#!/usr/bin/env python3
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12


# calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value
choice = "y"
# Does the math for monthly investment
while choice.lower() == "y":
    choicetwo = 0
    choicethree = 0
    choiceone = 0
    while choiceone == 0:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment < 1:
            print("Entry must be greater than 0. Please try again")
        else:
            choiceone += 1

#Does the math for yearly intrest rate
    while choicetwo == 0:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate < 1 or yearly_interest_rate > 15:
            print("Entry must be greater than 0 and less than or equal to 15. Please try again")
        else:
            choicetwo += 1

#Does the math for the numbers of years
    while choicethree == 0:
        years = int(input("Enter number of years:\t\t"))
        if years < 1 or years > 50:
            print("Entry must be greater than 0 and less than or equal to 50. Please try again")
        else:
            choicethree += 1

        # get and display future value
    future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)


    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    continue
    print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
