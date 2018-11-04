import csv, random, math

#unused if counter function isn't used
from collections import Counter

millnames = ['',' Thousand',' Million',' Billion',' Trillion']
winningPercent = 0
winCount = 0
gambleCount = 0
winnings = 2_000_000

#by default we want to print out our progress every 1 million attempts
log_every_n = 1_000_000

#uses randrange to generate a 5 index list with numbers ranging from 1 to 69
def generate_mm_numbers():
    #create a list
    generated_nums = list()
    # iterate 5 times
    for x in range(0, 5):
        #add a random number between 1 and 70
        generated_nums.append(random.randrange(1, 71))
    return generated_nums

#uses randint to generate a number between 1 and 25
def generate_mm_special_num():
    return random.randrange(1, 26)

# #reads all winning numbers from a CSV file and adds them to a list
# def read_mm_numbers():
    # with open("mm_numbers.csv", "r") as fin:
        # csvreader = csv.reader(fin)
        # winner_list = list()
        # for x in csvreader:
            # for num in x:
                # winner_list.append(int(num))
        # #uncomment the following two lines to find the 5 most common numbers in the winners list
        # #most_common = Counter(winner_list).most_common(5)
        # #print(most_common)

        # #reduces the list to a set (including unique values only) then converts back to a list
        # winner_list = list(set(winner_list))
    # return winner_list

def print_gamble_stats(winCount, gambleCount, winnings):
    winningPercent = (( winCount / gambleCount ) * 100.00 )
    print("Number of wins: "+str(winCount))
    print("Winnings: "+str(millify(winnings)))
    print("Number of tries: "+str(millify(gambleCount)))
    print("Winning percent: "+str(winningPercent))
    print("\n\n")

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

#uncomment the following line to read the winning numbers from CSV
#winner_set = read_mm_numbers()

running_list = list()
running_special_list = list()
most_common_list = list()

while winnings > 0.00:
    random_set = generate_mm_numbers()
    random_special_num = generate_mm_special_num()
    matchingNum = 0
    matchingspecial = False
    winnings -= 2.00
    gambleCount += 1
    if gambleCount == 1:
        #option 1, interactive user input used to choose Mega Million numbers
        #chosen_nums = [int(x) for x in input("Enter five numbers between 1 and 69 separate each number by a space, then press enter:").split()]
        #chosen_special_num = input("Enter a number between 1 and 25, then press enter:")

        #option 2, randomly select Mega Million numbers
        #chosen_nums = [int(random.randrange(1, 69)) for x in range(0, 5)]
        #chosen_special_num = int(random.randint(1, 26))

        #option 3, hardcode your chosen Mega Millions numbers as a list
        chosen_nums = [2, 20, 11, 31, 17] #chosen because they appear on winning tickets more often
        chosen_special_num = 6

    for choice in random_set:
        running_list.append(choice)
        if choice in chosen_nums:
            matchingNum += 1
        if chosen_special_num == random_special_num:
            matchingspecial = True
            running_special_list.append(random_special_num)
        else:
            matchingspecial = False

    # winnings of $500 or more count as a win
    if matchingNum > 3:
        if matchingNum == 4 and not matchingspecial:
            winnings += 500.00
        elif matchingNum == 4 and matchingspecial:
            winnings += 10_000.00
            #print("you won 10,000 dollars!")
            #print("\n\n")
        elif matchingNum == 5 and not matchingspecial:
            winnings += 1_000_000.00
            print("you won 1,000,000 dollars!")
            print("\n\n")
        elif matchingNum == 5 and matchingspecial:
            winnings += 1_600_000_000.00
            print("you won the jackpot!!!!")
            print(random_set, random_special_num)
            print("\n\n")
            print_gamble_stats(winCount, gambleCount, winnings)
            exit()
        winCount += 1
    #simple correction process. looks at the last 100,000 winning numbers, and changes chosen_nums to that list of numbers.
    # also resets the chosen_special_num based on which number was most commonly found in the past 100,00 iterations
    if len(running_list) > 100_000:
        mc_list = Counter(running_list).most_common(5)
        for item in mc_list:
            most_common_list.append(item[0])
        chosen_nums = most_common_list
        chosen_special_num = mc_list = Counter(running_special_list).most_common(1)[0]
        running_list = list()
        most_common_list = list()

    if (gambleCount % log_every_n) == 0:
        print_gamble_stats(winCount, gambleCount, winnings)

print_gamble_stats(winCount, gambleCount, winnings)
