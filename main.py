#####################################################################################################
# ALGORITHM
#
# Game Database Query System
#
# This project uses 10 function and a main function. It answers the user search queries by finding
# appropriate games from the database. The ten functions used are as follows:
# open_file(): This function opens the entered filename, be it a game file or a discount file 
# and then returns a filer pointer for the file opened
# read_file(): This function reads the games file and returns a games dictionary with the 
# game names as the keys and a list of game attributes as the corresponding values
# read_discount(): This function reads the discount file and returns a dictionary with game names 
# as the keys and the corresponding discount percentage as values
# in_year(): using .items(), this function filters out games released in a specific year. It then 
# returns a list of game names sorted alphabetically.
# by_genre(): This function filters out games of a specific genre. It then returns a list of game
# names sorted by percentage positive reviews in descending order.
# by_dev(): This function filters out games created by a specific developer. Ir returns a list of 
# game names sorted fromlatest to oldest released games
# per_discount (): This function figures out if a game has discount available or not. If discount
# available then this function calculates the discounted price. finally it returns a list of prices
# containing discounted prices (if calculated) or original prices of games. 
# by_dev_year(): This function is filters out games created by a specific developer in a specific year.
# It returns a list of game names sorted from cheapest to most expensive.
# by_genre_no_disc(): Thiis function filters out games of a specific genre that offer no discount.
# It returns a list of game names sorted from cheapest to most expensive.
# by_dev_disc(): This function filters out games created by a specific developer that offer a discount.
# It returns a list of game names sorted from cheapest to most expensive.
# 
# Fianlly, the main function interacts with the user and prompts them with 7 options to choose from.
# It provides the functionality to use the program again and again until QUIT option selected.
# It performs the desired filterations by calling one of the above 10 mentioned functions. 
# And then it outputs the game names in the desired order. Lastly displays thank you message 
# when the user quits the program. 
#######################################################################################################

import csv
from operator import itemgetter


MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''
 
        
def open_file(s):
    '''
    This function asks the user to enter a filename. It keeps prompting the 
    user for a filename until the file is found. It then opens the file and
    returns the file pointer
    '''

    #while loop to keep prompting the user for a filename until file found
    while True:
    
        #prompt the user to enter the file to open
        filename = input('\nEnter {} file: '.format(s))

        try:
            fp = open(filename, encoding ='UTF-8')     #open file if found
            return fp   
        except FileNotFoundError:
            print('\nNo Such file')     #display error message if file not found


def read_file(fp_games):
    ''' 
    This function is used to read through the games file. It skips the header line
    and iterates over other rows in the file. It returns a dictionary with the
    games as the keys and a list of corresponding data as the corresponding values.
    '''
    reader = csv.reader(fp_games)
    result_dictt = {}
    next(reader)    #skip header line

    #for loop to iterate over each row in the given csv file
    for row in reader:

        #assign the required elements a variable name accoring to their index
        date = row[1]
        developer_list = row[2].split(';')
        genres_list = row[3].split(';')
        player_modes_list = row[4].split(';')

        #set player mode to 0 if it is a multiplayer game, otherwise set it to 1
        if player_modes_list[0].lower() == "multi-player":
            mode = 0
        else:
            mode = 1

        #try-except suite to convert price (if valid) from inr to usd
        try:
            price = row[5]
            price = price.replace(',','')
            price = float(price)
            price = price*0.012
        except ValueError:
            price = 0.0

        overall_reviews = row[6]
        reviews = int(row[7])
        percent_positive = row[8].strip("%")
        percent_positive = int(percent_positive)

        support = []    #creating an empty list to store support
        if row[9] == '1':
            support.append('win_support')
        if row[10] == '1':
            support.append('mac_support')
        if row[11] == '1':
            support.append('lin_support')

        #append each variable to a list that represents the values of the main dictionary
        each_list =  [date, developer_list, genres_list, mode, price, overall_reviews,reviews, percent_positive, support]      

        result_dictt[row[0]] = each_list    #set games as keys and each list as the corresponding value
    return result_dictt


def read_discount(fp_discount):
    '''
    The function will read the discount file and create a dictionary with key as the game name
    and value as the corresponding discount
    '''
    reader = csv.reader(fp_discount)
    result_dictt = {}
    next(reader)    #skip header line
    for row in reader:
        name = row[0]
        discount = row[1]
        discount = round(float(discount),2)    #convert to float and round to 2 decimals
        result_dictt[name] = discount       #set game names as keys and discounts as corresponding values
    return result_dictt


def in_year(master_D,year):
    ''' 
    This function filters out the games that were released in a particular
    year from the games dictionary. It then returns a list of game names 
    sorted alphabetically.
    '''
    results_list = []

    #for loop to check if input year is equal to the year in which each game was released
    for key,val in master_D.items():
        if int(val[0][-4:]) == year:
            results_list.append(key)    #appending game name to the return list
    results_list.sort()
    return results_list


def by_genre(master_D,genre): 
    ''' 
    This function filters out the games of a specific genre from the games dictionary.
    it then returns a list of game names sorted by percentage positive reviews in
    descending order.
    '''
    result_list = []
    helper_list = []    

    #for loop to crearte tuples of game names and corresponding percentage positive review values
    for key,val in master_D.items():
        if genre in val[2]:
            #list of tuples of games names and percentage positive reviews         
            helper_list.append((key,val[7]))    
    
    #sort tuples according to percentage positive reviews in descending order
    sorted_list = sorted(helper_list, key=itemgetter(1), reverse = True)

    #extract game name from each tuple of the sorted list
    for tup in sorted_list:
        result_list.append(tup[0])
    return result_list

        
def by_dev(master_D,developer): 
    ''' 
    This function filters out games that are made by a specific developer from the games
    dictionary. It then sorts the games and returns a list of game names sorted from
    latest to oldest released games. 
    '''
    result_list = []
    helper_list = []

    #for loop to create a list of tuples of game names and corresponding release years 
    for key,val in master_D.items(): 
        if developer in val[1]:
            helper_list.append((key,int(val[0][-4:])))

    #sort the tuples from latest to oldest released game names
    sorted_list = sorted(helper_list, key=itemgetter(1), reverse = True)

    #for loop to extract game name from each tuple of sorted list
    for tup in sorted_list:
        result_list.append(tup[0])
    return result_list
        

def per_discount(master_D,games,discount_D): 
    '''
    This function determines the reduced price for each game in the list of games,
    rounds it to six decimal places and returns the list. If a game has no discount 
    available, this function appends its original price to the list of prices. 
    '''
    result_list = []

    #for loop to iterate over each game in the games_list
    for game in games:
        price = master_D[game][4]
        if game in discount_D:      #condition to check if a game has an available discount
            discount = discount_D[game]
            new_price = (1-(discount/100))*price    #calculating new price based on the discount percentage available
            new_price = round(new_price,6)      #round the new price to 6 decimals
            result_list.append(new_price)
        else:
            result_list.append(price)      #if no discount available, append original price to return list
    return result_list
    

def by_dev_year(master_D,discount_D,developer,year):
    '''
    This function filters out games created by specific a developer and released in 
    a specific year. It returns a list of game names sorted in the ascending order of
    their pricing. If the game has discount, then the discounted price is taken into 
    consideration while sorting. If there is a tie, the games are sorted according to 
    their names. 
    '''
    games_list = []
    result_list = []
    helper_list = []
    price = 0.0

    #for loop to iterate over each game and its values in the games dictionary
    for key,val in master_D.items():
        if developer in val[1] and (int(val[0][-4:])) == year:
            #append each game created by specific developer and released in a aspecific year
            games_list.append(key)      

    #call the price_list function to get the price of each game based on the availability of discount
    price_list = per_discount(master_D,games_list,discount_D)
    i=0

    #for loop to iterate over each game in games_list
    for game in games_list:

        #append each game and it's corresponding price as a tuple in the helper_list
        helper_list.append((game,price_list[i]))
        i += 1      #increasing index by 1

    #sort tuples inside the helper list in the ascending order of their prices 
    sorted_list = sorted(helper_list, key=itemgetter(1), reverse = False)

    #for loop to extract game name from each tuple in the sorted list
    for tup in sorted_list:
        result_list.append(tup[0])
    return result_list  

          
def by_genre_no_disc(master_D,discount_D,genre):
    '''
    This function filters out games by a specific genre that do not offer a discount on their price. It returns
    a list of game names sorted from cheapest to most expensive. If there is a tie, the games are sorted in the 
    descending order of their percentage positive reviews.
    '''
    result_list = []
    helper_list = []

    #call by_genre function to get a filtered list of games of a specific genre
    games_list = by_genre(master_D, genre)  

    #for loop to iterate over each game in the games_list
    for game in games_list:
        if game not in discount_D:      #condition to ensure that game offers no discount
            price = master_D[game][4]
            #append tuples of game, price and percentage positive reviews to a helper list 
            helper_list.append((game,price,master_D[game][7]))

    #sort the tuples in helper_list based on price in ascending order
    sorted_list = sorted(helper_list, key=itemgetter(1))

    #for loop to extract game name from each tuple in the sorted list
    for tup in sorted_list:
        result_list.append(tup[0])
    return result_list


def by_dev_with_disc(master_D,discount_D,developer):
    '''
    This function filters out games by a specific developer. It then filters out those games that offer a
    discount. Finally, it returns a list of game names sorted from cheapest to most expensive. The original
    price is considered when sorting. If there is a tie, the games are sorted from latest to oldest released
    games. If there is a tie in the release year, games are kept in the same order as in the main dictionary
    '''
    result_list = []
    helper_list = []

    #call by_dev function to get a filtered list of games created by a particular developer
    games_list = by_dev(master_D, developer)

    #for loop to iterate over each game in the games_list
    for game in games_list: 
        if game in discount_D:      #condition to ensure that the game offers a discount
            price = master_D[game][4]
            year = int(master_D[game][0][-4:])

            #append tuple of game,price and year to a helper_list
            helper_list.append((game,price,year))

    #sort tuples by comparing first the price and then the year of each game        
    sorted_list = sorted(helper_list, key=itemgetter(1,2), reverse=False)

    #for loop to extract game name from each tuple in the sorted list
    for tup in sorted_list:
        result_list.append(tup[0])
    return result_list

             
def main():
    '''
    This Function is reads all the files and creates the main (game) dictionary and the discount
    dictionary. It would give the users 7 different options to select from, each providing different
    service. Depending on the option selected, it would prompt the user for specific inputs and display the 
    list of sorted games as per user’s selection. This function function keeps asking the user until the
    Exit (option 7) is selected and would display a goodbye message. If the user enters none of these 
    options, an invalid option message is printed and the user is reprompted to choose an option
    '''
    fp_games = open_file("games")   #prompt user to enter game file name until valid file entered
    fp_discount = open_file("discount") #prompt user to enter discount file name unitl valid file entered
    master_D = read_file(fp_games)  #call read_file function to create the main (games) dictionary
    discount_D = read_discount(fp_discount)     #call the read_discount function to create the discounts dictionary

    option = input(MENU)    #prompt user to choose from a list of 7 options
    while True:     #main loop to keep prompting user for an option until exit (option 7) selected
        if option == "1":
            while True:     #while loop to keep promprting user until valid year is entered
                input_year = input('\nWhich year: ')
                
                #try-except suite to check if the inputyear is an integer or not
                try:   
                    input_year = int(input_year)
                    break
                except ValueError:
                    print("\nPlease enter a valid year")

            #call in year function to get a list of games released in the year entered by the user
            in_year_list = in_year(master_D,input_year)     
            in_year_list.sort()     #sortign all games in the ascending alphabetical order
            if in_year_list != []:
                print("\nGames released in {}:".format(input_year))
                print(", ".join(in_year_list))  #print filtered games seperated by commas
            else:
                print("\nNothing to print")     #if no games found after filteration, display no games found message
            option = input(MENU)   
        
        elif option == "2":
            developer = input('\nWhich developer: ')
            
            #call by_dev function to get a list of games created by a specific developer
            games_list = by_dev(master_D, developer)

            if games_list != []:
                print("\nGames made by {}:".format(developer))
                print(", ".join(games_list))    #print the filtered games seperated by commas
            else:
                print("\nNothing to print")     #print nothing to print message if no games found after filteration
            option = input(MENU)

        elif option == "3":
            genre = input('\nWhich genre: ')

            #call the by_genre function to get a filtered list of games of a specific genre
            games_list = by_genre(master_D, genre)

            if games_list != []:
                print("\nGames with {} genre:".format(genre))
                print(", ".join(games_list))    #print games seperated by commas
            else:
                print("\nNothing to print")  #print nothing to print message if no games found after filteration
            option = input(MENU)

        elif option == "4":
            developer = input('\nWhich developer: ')

            #while loop to keep prompting the user for a year until a valid year is entered
            while True:
                input_year = input('\nWhich year: ')
                try:
                    input_year = int(input_year)
                    break
                except ValueError:
                    print("\nPlease enter a valid year")

            #calling by_dev_year function to get a list of games created by a developer in a specific year
            by_dev_year_list = by_dev_year(master_D,discount_D,developer,input_year)

            if by_dev_year_list != []:
                print("\nGames made by {} and released in {}:".format(developer,input_year))    
                print(", ".join(by_dev_year_list))       #print games seperated by commas
            else:
                print("\nNothing to print")   #print nothing to print message if no games found after filteration
            option = input(MENU)

        elif option == "5":
            genre = input('\nWhich genre: ')

            #calling by_genre_no_disc fucntion to get a lis of games of a specific genre that offer no discount 
            genre_no_disc_list = by_genre_no_disc(master_D,discount_D,genre)
            if genre_no_disc_list != []:
                print("\nGames with {} genre and without a discount:".format(genre))
                print(", ".join(genre_no_disc_list))     #print games seperated by commas
            else:
                print("\nNothing to print")   #print nothing to print message if no games found after filteration
            option = input(MENU)
    
        elif option == "6":
            developer = input('\nWhich developer: ')

            #calling the developer_disc_list function to get a list of games created by a developer that offer a discount
            developer_disc_list = by_dev_with_disc(master_D,discount_D,developer)
            if developer_disc_list != []:
                print("\nGames made by {} which offer discount:".format(developer))
                print(", ".join(developer_disc_list))    #print games seperated by commas
            else:
                print("\nNothing to print")     #print nothing to print message if no games found after filteration
            option = input(MENU)

        elif option == "7":
            print("\nThank you.")   #print thank you message 
            break       #quit the program

        else:
            print("\nInvalid option") #print error message if option is invalid
            option = input(MENU)    #reprompt user to enter an option
            
if __name__ == "__main__":
    main()
