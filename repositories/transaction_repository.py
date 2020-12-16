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

def select(id):
    transaction = None

    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        tag = tag_repository.select(result['tag_id'])
        transaction = Transaction(merchant, tag, result['amount'], result['id'])
    return transaction 

def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, tag_id, amount) = (%s, %s, %s) WHERE id = %s"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount, transaction.id]
    run_sql(sql, values)

def total():
    sql = "SELECT SUM(amount) FROM transactions"
    result = run_sql(sql)

    total = result
    return total