# import the necessary packages
from aima3.utils import expr
from aima3.logic import FolKB

from expert_system.kb import rules
from expert_system.forward_chaining import ask
from expert_system.utils import Agenda

# the main function to run the inference engine
def run(category: str, answers: list):
    """
    The inference engine run function.
    Takes the problem category and the answers to the questions. and returns the problem type and the explanation (how it infere to find the result).
    Use forward chaining algorithm
    """
    
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
    
    # retur the result and the explanation
    try:
        return result[0], explanation_unit
    except Exception:
        return None, {}
