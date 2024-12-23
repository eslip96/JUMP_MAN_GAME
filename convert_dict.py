def to_sql(sql_dict):
    sql_query = f"SELECT {', '.join(sql_dict['fields'])} FROM {sql_dict['table']}"

    if 'where' in sql_dict and sql_dict['where']:
        where_conditions = []
        for cond in sql_dict['where'].get('AND', []):
            value = cond['value']
            if isinstance(value, str):
                value = f"'{value}'"
            where_conditions.append(f"{cond['field']} {'=' if cond['operator'] == 'equals' else cond['operator']} {value}")
        if where_conditions:
            sql_query += f" WHERE {' AND '.join(where_conditions)}"

    if 'order_by' in sql_dict:
        sql_query += f" ORDER BY {sql_dict['order_by']['field']} {sql_dict['order_by'].get('order', 'ASC')}"

    if 'limit' in sql_dict and sql_dict['limit'] > 0:
        sql_query += f" LIMIT {sql_dict['limit']}"

    return sql_query


sql_dict = {
    'fields': ['name', 'model', 'price'],
    'table': 'Products',
    'where': {
        'AND': [
           {'field': 'make', 'value': 'Apple', 'operator': 'LIKE'},
           {'field': 'price', 'value': 1100.00, 'operator': 'lessthan'}
        ]
    },
    'order_by': {'field': 'price', 'order': 'DESC'},
    'limit': 0
}

query = to_sql(sql_dict)
print(query)
