import importlib
import bank_transactions as bank


def setup_function():
    
  
    importlib.reload(bank)
    bank.accounts = {}
    bank.next_account_number = 1


def test_create_account():
    bank.create_account()
    assert bank.accounts[1] == 0
    assert bank.next_account_number == 2


def test_deposit_amount():
    bank.create_account()
    bank.deposit_amount(1, 500)
    assert bank.accounts[1] == 500


def test_deposit_invalid_account():
    bank.deposit_amount(2, 500)
    assert 2 not in bank.accounts


def test_withdraw_amount_success():
    bank.create_account()
    bank.deposit_amount(1, 1000)
    bank.withdraw_amount(1, 500)
    assert bank.accounts[1] == 500


def test_withdraw_insufficient_balance():
    bank.create_account()
    bank.deposit_amount(1, 200)
    bank.withdraw_amount(1, 500)
