from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

def save(transaction):
    sql = "INSERT INTO transactions (tag_id, merchant_id, amount) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.tag.id, transaction.merchant.id, transaction.amount]
    results = run_sql(sql, values)
    transaction.id  = results[0]['id']
    return transaction

def select_all():
    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(merchant, tag, result['amount'], result["id"])
        transactions.append(transaction)
    return transactions