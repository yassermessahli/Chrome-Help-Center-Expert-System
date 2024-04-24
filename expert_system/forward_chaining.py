# import necessary libraries
from aima3.logic import (FolKB, 
                         unify, 
                         parse_definite_clause, 
                         subst, 
                         constant_symbols, 
                         variables)
import itertools
from aima3.utils import expr



# the main function of forward chaining
def ask(rules: list, facts: list, goal: str, entailment_process=None):
    """
    A derivation of The original forward chaining algorithm of aima3. 
    Takes a rules base, a set of facts, and a goal expression. 
    Returns all substitutions that make the goal expression true.
    """
    # initiate the knowledge base
    KB = FolKB()
    for fact in facts:
        KB.tell(expr(fact))
    for rule in rules:
        KB.tell(expr(rule))
    
    # Initialize known constant symbols
    consts = list({c for clause in KB.clauses for c in constant_symbols(clause)})

    # Define generator function to enumerate substitutions
    def enum_subst(p):
        query_vars = list({v for clause in p for v in variables(clause)})
        for assignment_list in itertools.product(consts, repeat=len(query_vars)):
            theta = {x: y for x, y in zip(query_vars, assignment_list)}
            yield theta

    # Check if we can answer without working_memory inferences
    for q in KB.clauses:
        phi = unify(q, goal, {})
        if phi is not None:
            yield phi

    # Forward chaining algorithm
    entailment_process[1] = facts
    while True:
        working_memory = []
        for rule in KB.clauses:
            p, q = parse_definite_clause(rule)
            for theta in enum_subst(p):
                if set(subst(theta, p)).issubset(set(KB.clauses)):
                    q_ = subst(theta, q)
                    if all([unify(x, q_, {}) is None for x in KB.clauses + working_memory]):
                        working_memory.append(q_)
                        phi = unify(q_, goal, {})
                        if phi is not None:
                            yield phi
        if not working_memory:
            break
        entailment_process[len(entailment_process)+1] = working_memory
        for clause in working_memory:
            KB.tell(clause)
    return None
