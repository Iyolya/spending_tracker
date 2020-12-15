from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING id"
    values = [tag.name]
    results = run_sql(sql, values)
    tag.id  = results[0]['id']
    return tag

def select_all(tag):
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)
    return tags