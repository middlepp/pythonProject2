from atm import Account

class TestAccount:


    def test_account_default_balance(self):



        new_account = Account(account_id=10, account_pin=1234)
        assert new_account.get_account_balace() == 0