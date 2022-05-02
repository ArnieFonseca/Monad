"""Import maybe package"""
from functional.maybe import Maybe,tryCatch

### Data
developers = [
    {"developer":{"name":"Arnie"}},
    {"developer":{"name":"Leon","skill":{"language":"Python"}}}
]

### Helper Lambdas
getName = lambda x : x['developer']['name']
getSkill = lambda x : x['developer']['skill']
getLanguage = lambda x : x['language']

def getDeveloper(name:str)->Maybe:
    """Retrive the Maybe Developer -> Pure Function"""

    get_data = lambda :list(filter(lambda x : getName(x) == name,developers))[0]
    return  tryCatch(get_data)

def getDeveloperSkill(developer)->Maybe:
    """Retrive the Maybe Developer Skill -> Pure Function"""

    get_data = lambda : getSkill(developer)
    return  tryCatch(get_data)

def main(lst:list)->None:
    """Entry Point -> Inpure Function"""

    for item in lst:

        developer:Maybe = getDeveloper(item)
        skill:Maybe = developer.bind(getDeveloperSkill)

        developer_name:str = developer.match(lambda x: getName(x), lambda x: "No Developer")
        skill_name:str = skill.match(lambda x: getLanguage(x), lambda x: "No Skill")

        (print)(developer_name, skill_name)

if __name__ == "__main__":
    developers_names = ["Leon", "Arnie", "Jose"]
    main(developers_names)
