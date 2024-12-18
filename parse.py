import re


def parse_sql(query):
    parsed_data = {
        'fields': [],
        'table': '',
        'where': {},
        'order_by': {},
        'limit': 0
    }

    query = query.strip().lower()

    select_match = re.search(r"select (.*?) from", query)
    if select_match:
        fields = select_match.group(1).strip()
        parsed_data['fields'] = [field.strip() for field in fields.split(',')]

    from_match = re.search(r"from (\w+)", query)
    if from_match:
        parsed_data['table'] = from_match.group(1).strip()

    where_match = re.search(r"where (.+?)", query)
    if where_match:
        where_clause = where_match.group(1).strip()
        where_parts = where_clause.split('=')
        if len(where_parts) == 2:
            field = where_parts[0].strip()
            value = where_parts[1].strip().strip("'")
            parsed_data['where'] = {field: value}

    order_by_match = re.search(r"order by (\w+) (asc|desc)", query)
    if order_by_match:
        parsed_data['order_by'] = {
            'field': order_by_match.group(1),
            'order': order_by_match.group(2).upper()
        }

    limit_match = re.search(r"limit (\d+)", query)
    if limit_match:
        parsed_data['limit'] = int(limit_match.group(1))

    return parsed_data


query1 = '''SELECT name, make, model, price FROM Products WHERE price = 49.99 ORDER BY price DESC LIMIT 5'''
print(parse_sql(query1))

query2 = 'SELECT * FROM Customers'
print(parse_sql(query2))

query3 = "SELECT first_name, last_name, email FROM Cohorts WHERE first_name='John'"
print(parse_sql(query3))

query4 = "SELECT city, state from Customers where state='UT' ORDER BY city ASC"
print(parse_sql(query4))

query5 = "SELECT * FROM Courses ORDER BY name ASC LIMIT 20"
print(parse_sql(query5))
