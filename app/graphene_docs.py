from graphene import ObjectType, Field, String, Schema, NonNull, List
from json import dumps

class Human(ObjectType):
    name = Field(NonNull(String), description="The name of the human")
    age = Field(NonNull(String), description="The age of the human")
    gender = Field(NonNull(String), description="The gender of the human")
    hobbies = Field(List(String), description="The hobbies of the human (nullable list)")

class Query(ObjectType):
    human_by_name = Field(NonNull(Human), name=NonNull(String))

    def resolve_human_by_name(self, info, name):
        return get_human(name=name)


def get_human(name):
    humans = [
        {
            "name": "John Doe",
            "age": "30",
            "gender": "Male",
            "hobbies": ['Reading', 'Swimming', 'Cycling']
        },
        {
            "name": "Jane Smith",
            "age": "25",
            "gender": "Female",
            "hobbies": None
        }
    ]
    for human in humans:
        # h = dict(**human)
        # print(h)
        if human["name"] == name:
            return Human(**human)
    return None

# Create the schema
schema = Schema(query=Query)

# Example usage (you can run this part in your Python script to test the schema)
query = '''
{ 
    humanByName(name: "John Doe") 
    {
        name 
        age 
        gender 
        hobbies
    } 
}
'''
result = schema.execute(query)
print(dumps(result.data, indent=2))
    