from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

def save(transaction):
    sql = "INSERT INTO transactions (tag_id, merchant_id, amount) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.tag.id, transaction.merchant.id, transaction.amount]
    results = run_sql(sql, values)
    transaction.id  = results[0]['id']
    return transaction