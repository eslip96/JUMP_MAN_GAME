def parse_sql(sql_query):
    result = {
        'fields': [],
        'table': '',
        'where': {},
        'order_by': {},
        'limit': 0
    }

    query = sql_query.strip()
    query_upper = query.upper()

    select_start = query_upper.find("SELECT") + len("SELECT")
    from_start = query_upper.find("FROM")
    fields = query[select_start:from_start].strip()
    result['fields'] = [field.strip() for field in fields.split(",")]

    from_end = from_start + len("FROM")
    where_start = query_upper.find("WHERE")
    table = query[from_end:where_start].strip() if where_start != -1 else query[from_end:].strip()
    order_start = query_upper.find("ORDER BY")
    limit_start = query_upper.find("LIMIT")
    if order_start != -1:
        table = query[from_end:order_start].strip()
    elif limit_start != -1:
        table = query[from_end:limit_start].strip()
    result['table'] = table

    if where_start != -1:
        where_end = order_start if order_start != -1 else (limit_start if limit_start != -1 else len(query))
        where_clause = query[where_start + len("WHERE"):where_end].strip()
        if "=" in where_clause:
            field, value = map(str.strip, where_clause.split("=", 1))
            value = value.strip("'").strip('"')
            result['where'] = {field: float(value) if value.replace('.', '', 1).isdigit() else value}

    if order_start != -1:
        order_end = limit_start if limit_start != -1 else len(query)
        order_clause = query[order_start + len("ORDER BY"):order_end].strip()
        if "DESC" in order_clause.upper():
            field, order = order_clause.rsplit(" ", 1)
            result['order_by'] = {'field': field.strip(), 'order': 'DESC'}
        elif "ASC" in order_clause.upper():
            field, order = order_clause.rsplit(" ", 1)
            result['order_by'] = {'field': field.strip(), 'order': 'ASC'}

    if limit_start != -1:
        limit_clause = query[limit_start + len("LIMIT"):].strip()
        result['limit'] = int(limit_clause)

    return result


query1 = "SELECT * FROM Customers"
query2 = "SELECT name, model FROM Products WHERE make = 'Apple'"
query3 = "SELECT name, make, model, price FROM Products WHERE price = 49.99 ORDER BY price DESC LIMIT 5"

print(parse_sql(query1))
print(parse_sql(query2))
print(parse_sql(query3))
