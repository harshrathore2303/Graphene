import json
from graphene import ObjectType, String, Int, Field, Schema
import os

"""
{
    name: "John Doe",
    age: 30,
}
"""

class Query(ObjectType):
    name = String(value = String(default_value="Harry Potter"), name="_name")
    age = Int()

    def resolve_name(root, info, value):
        # return "John Doe"
        return value

    def resolve_age(root, info):
        return 30
    

schema = Schema(query=Query)
print(schema)

# graphql_query

# for single query
# query_graphql = 'query myFirstQuery { user_name: name(value: "Harshit") user_age: age }'

# for multiple query
query_graphql = '''
query myFirstQuery {
    user_name: _name(value: "Harshit")
    user_age: age
}
'''
result = schema.execute(query_graphql)
# print(result.data)
print(json.dumps(result.data, indent=2))