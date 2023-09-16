# Project Description: Game Database Query System in Python

## Introduction
The "Game Database Query System" is a Python project designed to provide users with a tool to search and filter a game database based on specific criteria. The system utilizes 10 functions and a main function to facilitate user interactions and process search queries. It allows users to filter games by various parameters, including release year, developer, genre, and discounts. This description provides an in-depth overview of the project's purpose, function details, and implementation.

## Purpose
The purpose of this project is to create a user-friendly program that interacts with a game database, enabling users to retrieve information about games based on their preferences. By offering multiple filtering options, users can narrow down their search and find relevant games that match their desired criteria, such as release year, developer, genre, and pricing information. This project aims to enhance the user experience and provide a versatile tool for exploring the game database efficiently.

## Function Details

### 1. `open_file(filename)`
This function prompts the user to input a filename, attempts to open the specified file, and returns the file pointer if successful. If the file does not exist, it displays an error message and prompts the user again.

### 2. `read_file(fp_games)`
Reads the games file and creates a dictionary with game names as keys and corresponding attributes as values. The function processes each row of the CSV file, extracting relevant game information such as release date, developer, genres, pricing, and reviews.

### 3. `read_discount(fp_discount)`
Reads the discount file and creates a dictionary with game names as keys and the corresponding discount percentages as values. The function parses the discount file, extracts the discount information, and associates it with the respective game.

### 4. `in_year(master_D, year)`
Filters games based on the input year and returns a sorted list of game names released in that year. The function iterates through the games and checks the release year to include games that match the specified year.

### 5. `by_genre(master_D, genre)`
Filters games based on the input genre and returns a sorted list of game names, ordered by percentage of positive reviews. The function identifies games of the specified genre and sorts them by review ratings.

### 6. `by_dev(master_D, developer)`
Filters games created by a specific developer and returns a sorted list of game names, ordered from the latest to the oldest release. The function identifies games associated with the given developer and organizes them based on their release dates.

### 7. `per_discount(master_D, games, discount_D)`
Calculates the discounted prices for games with available discounts and returns a list of prices. If no discount is available, it includes the original prices in the list. The function calculates the reduced prices based on the discount percentage.

### 8. `by_dev_year(master_D, discount_D, developer, year)`
Filters games by a specific developer and a specific release year, returning a sorted list of game names based on their pricing. The function considers discounts and sorts games by price in ascending order.

### 9. `by_genre_no_disc(master_D, discount_D, genre)`
Filters games of a specific genre that do not have discounts and returns a sorted list of game names based on their pricing. The function sorts games by price in ascending order and considers the absence of discounts.

### 10. `by_dev_with_disc(master_D, discount_D, developer)`
Filters games by a specific developer that offer discounts and returns a sorted list of game names based on their pricing. The function sorts games by price in ascending order, considering the available discounts.

### 11. `main()`
Interacts with the user, allowing them to choose from various options to filter games based on their preferences. The function prompts the user for specific inputs, processes their choices, and displays the sorted game names accordingly. The program continues to prompt the user until they choose to exit, at which point a thank-you message is displayed.

## Implementation
The project is implemented in Python and utilizes CSV file processing to read game and discount information. The functions are organized to handle different filtering scenarios, ensuring flexibility in searching the game database. Exception handling is employed to validate user inputs and handle file-related errors gracefully. The main function orchestrates user interactions, calling the appropriate filtering functions based on the selected option and presenting the results to the user in an organized manner. This implementation allows users to efficiently explore the game database and obtain relevant information based on their preferences.
