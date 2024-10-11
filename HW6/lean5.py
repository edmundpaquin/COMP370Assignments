# # get all the sales data by product type
# book_sales_2022 = load("data/book_sales_2022.csv")
# book_sales_2023 = load("data/book_sales_2023.csv")
# book_sales_2024 = load("data/book_sales_2024.csv")

# game_sales_2022 = load("data/game_sales_2022.csv")
# game_sales_2023 = load("data/game_sales_2023.csv")
# game_sales_2024 = load("data/game_sales_2024.csv")

# # calculate the total sales for each year
# total_sales_2022 = sum_sales(book_sales_2022, game_sales_2022)
# total_sales_2023 = sum_sales(book_sales_2023, game_sales_2023)
# total_sales_2024 = sum_sales(book_sales_2024, game_sales_2024)

book_sales = {}
game_sales = {}
total_sales = {}
years = [i for i in range(2022, 2025)]

for i in years:
    book_sales[i] = load("data/book_sales_" + str(i) + ".csv")
    game_sales[i] = load("data/game_sales_" + str(i) + ".csv")
    total_sales[i] = book_sales[i] + game_sales[i]

