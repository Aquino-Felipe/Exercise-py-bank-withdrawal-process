# Print a line of 30 equal signs for visual separation
print("=" * 30)
# Print the welcome message centered within a line of 30 equal signs
print("{:^30}".format("Welcome to XYZ BANK"))
# Print another line of 30 equal signs for visual separation
print("=" * 30)

# Prompt the user to enter the amount of money they want to withdraw
n = int(input("How much money do you want to withdraw? $"))
# Initialize the total amount to be withdrawn
total = n
# Initialize the bank note value to start with $50
bank_notes = 50
# Initialize a counter for the total number of bank notes
totalnotes = 0

# Start an infinite loop to handle the withdrawal process
while True:
    # Check if the total amount is greater than or equal to the current bank note value
    if total >= bank_notes:
        # Subtract the bank note value from the total amount
        total -= bank_notes
        # Increment the counter for the total number of bank notes
        totalnotes += 1
    else:
        # If there are any bank notes to be printed, print the total number of bank notes of the current value
        if totalnotes > 0:
            print(f"Total of {totalnotes} bank notes of   ${bank_notes}")
        # Adjust the bank note value to the next lower denomination
        if bank_notes == 50:
            bank_notes = 20
        elif bank_notes == 20:
            bank_notes = 10
        elif bank_notes == 10:
            bank_notes = 1
        # Reset the counter for the total number of bank notes
        totalnotes = 0
        # If the total amount to be withdrawn is now zero, break the loop
        if total == 0:
            break
