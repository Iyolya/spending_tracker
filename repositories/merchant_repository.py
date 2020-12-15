from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants name VALUES %s RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id 
    return merchant

def select_all(merchant):
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

