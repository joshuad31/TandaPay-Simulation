# account.py

'''
An example template of a user account instance
'''


class UserAccount:
    
    def __init__(self, bundling: int = 0):
        self.bundling = bundling

        self.generate_accounts()

    def generate_accounts(self) -> None:
        ''' Generates the accounts a user needs based on bundling 
        This could also be in a dict format:
        self.account = {
            "wallet": 0,
            "savings": 0,
            "m_0": 0,
            ...
        }
        '''
        self.bundling = self.bundling
        self.wallet = 0
        self.savings = 0
        self.month_accounts = [0] * self.bundling + 1
        # dict comprehension
        # self.month_accounts = {f'm_{n}': 0 for n in range(self.bundling)}

    def transaction(self, source: str, dest: str, amount: int) -> bool:
        ''' Conducts a transaction and returns success/failure '''
        # validate balances

        # transfer
        dest += amount
        source -= amount
        return True

    def transfer_month_accounts(self) -> None:
        '''Move month account balances to next, send to wallet if overflow'''

    def pay_premium(self, premium: int) -> bool:
        '''Transfers premium amount from wallet to m_0 account'''
        # validate balances
        # transfer from wallet to m_0
        # transfer month accounts so balances move down the line
        