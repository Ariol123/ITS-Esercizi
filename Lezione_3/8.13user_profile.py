'''
Build a profile of yourself by calling
 build_profile(), using your first and last names and three other key-value pairs that describe you. All the values 
 must be passed to the function as parameters. 
 The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
'''
person = {"firs_name": "Arjol" , "last_name":"Spirollari", "age":42, "lungezza":185 }
def build_profile(name, last_name, **kwargs):
    s = ""
    for key,value in person.items():
        s += f"{key}, {value} "
    return s
    
    
s = build_profile("arjol", "spirollari", age = 42, lunghezza = 185)
print(s)

