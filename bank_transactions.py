#!/usr/bin/env python3

accounts = {}
next_account_number = 1


def create_account():
    """
    Creates a new bank account, initializes its balance to 0,
    assigns a unique account number, and prints confirmation.
    """
    global next_account_number
    accounts[next_account_number] = 0
    print(f"New account created with account number {next_account_number}")
    next_account_number += 1


def deposit_amount(account_number, amount):
    """
    Deposits the given amount into the specified account.
    If the account does not exist, prints an error message.
    """
    if account_number not in accounts:
        print(f"Account number {account_number} not found")
        return
    accounts[account_number] += amount
    print(f"{amount} deposited to account number {account_number}")


def withdraw_amount(account_number, amount):
    """
    Withdraws the given amount from the specified account.
    Checks:
      - If the account exists
      - If sufficient balance is available
    Prints the related success or error messages.
    """
    if account_number not in accounts:
        print(f"Account number {account_number} not found")
        return

    if amount > accounts[account_number]:
        print("Withdrawal limit exceeded")
        return

    accounts[account_number] -= amount
    print(f"{amount} withdrawn from account number {account_number}")


def display_balance(account_number):
    """
    Prints the balance of the specified account.
    If the account does not exist, prints an error message.
    """
    if account_number not in accounts:
        print(f"Account number {account_number} not found")
        return
    print(f"Balance for account number {account_number}: {accounts[account_number]}")


def display_bank_balance():
    """
    Calculates and prints the total balance across all accounts.
    """
    total = sum(accounts.values())
    print(f"Total bank balance: {total}")


def process_bank_command(cmd_line):
    tokens = cmd_line.strip().split()
    if not tokens:
        return

    cmd = tokens[0]

    if cmd == "create_account":
        create_account()

    elif cmd == "deposit":
        deposit_amount(int(tokens[1]), int(tokens[2]))

    elif cmd == "withdraw":
        withdraw_amount(int(tokens[1]), int(tokens[2]))

    elif cmd == "display_balance":
        display_balance(int(tokens[1]))

    elif cmd == "display_bank_balance":
        display_bank_balance()

    else:
        print(f"Invalid command: {cmd}")


def main(filename):
    """
    Reads the input file line-by-line and processes each banking command.
    """
    with open(filename, 'r') as f:
        for cmd_line in f:
            process_bank_command(cmd_line)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("python3 bank_transactions.py <input_file>")
        sys.exit(1)
    main(sys.argv[1])
