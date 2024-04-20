import re

priorities = {
    "HardWare": { "BrowsingExperience": 1, "Extensions": 4, "Tabs": 3, "Ram": 2},
    "category2": { "qst1": 2, "qst2": 3, "qst3": 1},
    "category3": { "qst1": 3, "qst2": 1, "qst3": 2},
}


class Agenda:

    def __init__(self, category):
        self.priority_dict = priorities.get(category, None)
        
    def get_priority(self, fact):
        match = re.match(r'^(\w+)', fact)
        if match:
            predicate = match.group(1)
            if predicate in self.priority_dict:
                return self.priority_dict[predicate]
        return float('inf')
         
    def perform_sort(self, facts):
        try:
            return sorted(facts, key=lambda x: self.get_priority(x))
        except Exception as e:
            raise e

