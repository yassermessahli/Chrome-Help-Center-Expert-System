# import the necessary packages
from aima3.utils import expr
from aima3.logic import FolKB
from krb import rules
from forward_chaining import ask
from utils import Agenda



# the main function to run the inference engine
def run(category: str, answers: list):
    # STEPS:
    
    # 1. based on the category, get the appropriate rules
    rules_base = rules[category]
    
    # based on agenda's program sort the facts (for conflict resolution)
    agenda = Agenda(category)
    facts_base = agenda.perform_sort(answers)
    
    # run the forward chaining algorithm with the rules and the facts based on the agenda
    result = []
    firable_facts = []
    while not result and facts_base:
        firable_facts.append(facts_base.pop(0))
        goal_expr = expr('ProblemType(x)')
        explanation_unit = {}
        result = list(ask(rules_base, firable_facts, goal_expr, explanation_unit))
    
    try:
        return result[0], explanation_unit
    except Exception:
        return None, explanation_unit
