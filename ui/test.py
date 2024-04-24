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

    # print(f"Result: {restult}")


# if __name__ == "__main__":
#     main()