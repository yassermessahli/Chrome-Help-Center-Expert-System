from engine import run

# simple test


answers = ['Extensions(High)',
           'Ram(Slow)',
           'BrowsingExperience(Slow)',
           'Tabs(High)']

result, explanation = run("HardWare", answers)

print("result:")
print(result)
print("explanation:")
print(explanation)
