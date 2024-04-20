from expert_system.engine import run


def main():
    answers = [
        "Tabs(High)",
        "Extensions(High)",
        "Cpu(High)",
        "ChromeVersion(Outdated)",
        "Ram(Low)",
        "Glitches(No)",
        "GraphicsCard(Integrated)",
        "HardwareAcceleration(Disabled)",
        "BrowsingExperience(Slow)",
        "Antivirus(Notinstalled)",
        "AntivirusRealTimeScanning(Disabled)",
        "NewTabs(Fast)",
        "BackgroundProcesses(Low)",
    ]

    restult, explanation = run("Performance", answers)

    print()  # ExtensionRelatedSlowdown

    print(
        list(explanation.values())
    )  # Extensions are causing the slowdown. Try disabling some extensions to improve performance.


if __name__ == "__main__":
    main()




