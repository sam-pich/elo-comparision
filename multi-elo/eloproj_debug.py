import math
import itertools

# read the text file
data_file = open('data.txt', 'r')

# constant for the ELO equation
K = 400
Ra = 0
Rb = 0

d = 0

# sets up an array for the text in the file
file_text = []
# sets up an array for the elo ranking for each item in the file
elo_ranking = []
# counter to organize the array
counterlist = []
# basic counter to use in the for loop
count = 0
comb_counter = 0

# reads all the individual lines at once, and sets it a varible
datum = data_file.readlines()

# for every line
for line in datum:
    #counter goes up, append the counter with the text to the file_text array and append an elo of 400 to the elo array
    count += 1
    file_text.append(str(count) + '. ' + line.title().strip())
    print(file_text)
    elo_ranking.append(1000)
    print(elo_ranking)
    counterlist.append(count)
    print(counterlist)

# Function to calculate the Probability
def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

'''
    Title: Elo Rating Algorithm
    Author: Smitha Dinesh Semwal 
    Date: May 21, 2022
    Availability: https://www.geeksforgeeks.org/elo-rating-algorithm/
'''

# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(Ra, Rb, K, d):
    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)

    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)

    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (d == 1):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)


    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)

    # Updates the elo score
    elo_ranking[(comb[0]-1)] = Ra
    elo_ranking[(comb[1]-1)] = Rb

    print("Updated Ratings:-")
    print("Ra =", round(Ra, 6), " Rb =", round(Rb, 6))


# Ra and Rb are current ELO ratings

print("------------")



for comb in itertools.combinations(counterlist, 2):

    # print the combo we will try now
    print(comb)

    # sets Ra/Rb to whatever combo the comb function makes in each iteration, minus one because of lists
    Ra = elo_ranking[(comb[0]-1)]
    Rb = elo_ranking[(comb[1]-1)]

    # asks the user to input which option they like better, sets the input to an int and runs it through the victory check
    print('Do you like option 1 or 2 better (Please input 1/2):', end=' ')
    one_two = int(input())

    if one_two == 1:
        d = 1

    if one_two == 2:
        d = 2

    # elo rating function
    EloRating(Ra, Rb, K, d)

    # print the valuables of RA RB
    print(Ra)
    print(Rb)

    print('--------')

    # print the list again
    print(elo_ranking)
