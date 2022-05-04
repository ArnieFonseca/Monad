"""Import either package"""
from functional.either import Either

### Data
developers = [
    {"developer":{"name":"Arnie"}},
    {"developer":{"name":"Leon","skill":{"language":"Python"}}}
]

### Helper Lambdas
getName = lambda x : x['developer']['name']
getSkill = lambda x : x['developer']['skill']
getLanguage = lambda x : x['language']

def getDeveloper(name:str)->Either:
    """Retrive the Either Developer -> Pure Function"""

    get_data = lambda :list(filter(lambda x : getName(x) == name,developers))[0]
    return  Either.tryCatch(get_data)

def getDeveloperSkill(developer)->Either:
    """Retrive the Either Developer Skill -> Pure Function"""

    get_data = lambda : getSkill(developer)
    return  Either.tryCatch(get_data)

def main(lst:list)->None:
    """Entry Point -> Inpure Function"""

    for item in lst:

        developer:Either = getDeveloper(item)
        skill:Either = developer.bind(getDeveloperSkill)

        developer_name:str = developer.match(lambda x: getName(x), lambda x: x)
        
        skill_name:str = skill.match(lambda x: getLanguage(x), lambda x: x)

        (print)(developer_name, 
            "Main Skill", 
            skill_name if skill.is_right() else None)

if __name__ == "__main__":
    developers_names = ["Jose","Leon", "Arnie"]
    main(developers_names)
