 # import modules we will need
import random
import time

# take password from the user
password = int(input("Enter an integer password: "))

start_time = time.time() # start counting

guess_numbers = []  # we put the numbers to compare with the users password
password_numbers = []  # the user's password
for i in str(password): # take the str from the input and append them to the password_numbers list as integers
    password_numbers.append(int(i))

for i in range(0,len(password_numbers)): # add am many zeros as integers in password_numbers list to guess_numbers list
    guess_numbers.append(0)

numbers = [0,1,2,3,4,5,6,7,8,9] # possible input numbers
nums = [] # the integers from the numbers list that are used in the user's input


for i in numbers:  # integers from the numbers list that are used in the user's input added to nums list
    if i in password_numbers:
        #a = password_numbers.count(i)
        #for b in range(0,a):
        nums.append(i)

while True:
    guess = random.choice(nums) # take a random number from the nums list
    g = nums.count(guess) # see how many times that numbers is in the list nums
    indexes = [] # the places in the list that the guess takes place
    index = 0
    # Loop through the list and check each value
    for value in password_numbers:
        if value == guess:
            indexes.append(index)
        index += 1  # Increase the counter
    for e in range(0,len(indexes)):  # as many times as the guess exists in the nums list, we add it to the correct place in the guess_numbers list
        guess_numbers[indexes[e]] = guess

    print(guess_numbers)  # prints current (wrong or correct) guessed_numbers list

    if guess_numbers == password_numbers: # checks if we found the password and then it prints it
        print(password_numbers)
        print("I found your password!!")
        break # stops the loop and move one to stop time counting

end_time = time.time() # end counting
print(f"It took {end_time - start_time} 's to find your password")  # print the time it took to crack  the code
