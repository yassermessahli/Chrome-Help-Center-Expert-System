from engine import run

# simple test


a = ['Tabs(High)', 'Extensions(Low)', 'Cpu(Low)', 'ChromeVersion(Outdated)', 'Ram(Low)', 'Glitches(No)', 'GraphicsCard(Dedicated)', 'HardwareAcceleration(Disabled)', 'BrowsingExperience(Slow)', 'Antivirus(Notinstalled)', 'AntivirusRealTimeScanning(Disabled)', 'NewTabs(Slow)', 'BackgroundProcesses(Low)']

result, explanation = run("Performance", a)

print("result:")
print(result)
print("explanation:")
print(explanation)
