bank_transactions_repo/
│
├── bank_transactions.py       # Main banking logic and command processor
├── test_bank.py               # Unit tests written using pytest
├── input.txt                  # Sample input command file 
└── README.md  





create_account()	Creates a new account with a zero balance
deposit_amount(account, amount)	Adds money to an account
withdraw_amount(account, amount)	Withdraws money with balance checks
display_balance(account)	Prints account balance
display_bank_balance()	Prints total balance across all accounts
process_bank_command(line)	Parses and executes commands from file
main(filename)	Reads command file and processes each line



Steps i followed after creating Repository in Github 

git clone https://github.com/<your-username>/<repo-name>.git 
https://github.com/PrasannaGurram2505/bank_transactions_repo.git
cd <repo-name>

git status

after cloning the repo ,i started with the problem statement Coding ,adding Test cases and readme files 

After coding , i pushed the script files to the repo by following : 

git add . (make sures that all the files are pushed to the staging area or else we can add mentionning each file)

git add bank_transactions.py test_bank.py 

git commit -m "Added bank script and tests"

git push origin feature/bank-script


How i ran the script locally ? 

python3 filename input file name

 python3 bank_transactions.py input_file.txt

 

