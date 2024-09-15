from graphene import Schema, ObjectType, String, Int, Field, List, NonNull
from json import dumps

student = [
{
    "name": "John Doe",
    "age": 19,
    "gender": 'Male',
    "subjects": ['Math', 'Science', 'English']
},
{
    "name": "Harry Potter",
    "age": 18,
    "gender": "Male",
    "subjects": ['Math', 'Science']
}
]

class Student(ObjectType):
    name = Field(NonNull(String), description="The name of the student")
    age = Field(NonNull(Int), description="The age of the student")
    gender = Field(NonNull(String), description="The gender of the student")
    subjects = Field(List(String), description="The subjects of the student")

    def resolve_name(student, info):
        return f"{student[0].name}"
    




my_schema = Schema(
    query=Student
)

# print(my_schema)

query_student = '''
query student {
    name
}    
'''
result = my_schema.execute(query_student)
print(dumps(result.data, indent=2))
# query_string = 'query whoIsMyBestFriend { myBestFriend { lastName } }'
# my_schema.execute(query_string)