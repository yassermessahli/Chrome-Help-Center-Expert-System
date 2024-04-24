from expert_system.engine import run

# simple test


example_of_responses = ['Tabs(High)', 
                        'Extensions(Low)', 
                        'Cpu(Low)', 
                        'ChromeVersion(Outdated)', 
                        'Ram(Low)', 
                        'Glitches(No)', 
                        'GraphicsCard(Dedicated)',
                        'HardwareAcceleration(Disabled)', 
                        'BrowsingExperience(Slow)', 
                        'Antivirus(Notinstalled)',
                        'AntivirusRealTimeScanning(Disabled)', 
                        'NewTabs(Slow)', 
                        'BackgroundProcesses(Low)']

category = 'Performance'
explanation = []

result = run(category, example_of_responses, explanation)

print("="*10, "RESULT", "="*10)
print(result)
print("="*10, "EXPLANATION", "="*10)
print(explanation)
