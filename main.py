import random

MAX_LINES = 3  # global constant  - does not change
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "♡": 2,
    "♤": 4,
    "♢": 6,
    "♧": 8
}

symbol_value = {
    "♡": 5,
    "♤": 4,
    "♢": 3,
    "♧": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    # randomly pick number of rows from each column
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            # _ 'underscore' anonymous variable -> whenever you need to loop through something, but you don't care about the counter that iteration value.
            # this is so that you don't have an unused variable anymore.
            all_symbols.append(symbol)

    columns = []  # nested list
    for _ in range(cols):  # generates column
        column = []
        current_symbols = all_symbols[:]  # [:] slice operator -> makes a copy of 'all_symbols'
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        column.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:  # length of col minus 1 is the max index, to access an element in cols list.
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():  # collect the user input
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet}")


slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
print_slot_machine(slots)
winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
print(f"You won ${winnings}.")
print(f"You won on lines:", *winning_lines)

main()
