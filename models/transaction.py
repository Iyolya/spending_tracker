class Transaction:

    def __init__(self, tag, merchant, amount, id = None):
        self.tag = tag
        self.merchant = merchant
        self.amount = amount
        self.id = id