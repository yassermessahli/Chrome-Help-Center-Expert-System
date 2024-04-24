import re

priorities = {
  "Performance": {
    "Tabs": 4,
    "Extensions": 3,
    "Cpu": 2,
    "ChromeVersion": 1,
    "Ram": 6,
    "Glitches": 7,
    "GraphicsCard": 5,
    "HardwareAcceleration": 8,
    "BrowsingExperience": 9,
    "Antivirus": 10,
    "AntivirusRealTimeScanning": 11,
    "NewTabs": 12,
    "BackgroundProcesses": 13
  },
  "Security": {
    "EmailReceived": 3,
    "Link": 2,
    "EmailFiltering": 1,
    "Popups": 6,
    "SoftwareDownloaded": 4,
    "Antivirus": 7,
    "PasswordLeakNotification": 5,
    "PasswordChangeSuggestions": 8
  },
  "Installation": {
    "InstallationError": 2,
    "SoftwareDownloaded": 4,
    "SystemRequirements": 1,
    "Antivirus": 5,
    "ChromeVersion": 3,
    "PermissionsErrors": 6,
    "LoggedIn": 7,
    "SwitchAccount": 8
  },
  "Web Content Problems": {
    "WebsiteNotLoading": 1,
    "PageRefreshed": 2,
    "InternetConnection": 6,
    "WebsiteContent": 4,
    "WebsiteUpdateInfo": 3,
    "TextDisplay": 7,
    "Browser": 5,
    "MediaLoadingProblem": 8,
    "WebsiteFunctionality": 9
  },
  "Sync Issues": {
    "SyncIssue": 1,
    "SameGoogleAccount": 2,
    "BrowserData": 4,
    "Extensions": 3,
    "SyncErrors": 5,
    "DiskSpace": 7,
    "RecentNewDeviceLogin": 6,
    "IntermittentSyncIssues": 8,
    "Antivirus": 9,
    "ExclusionPossible": 10
  },
  "Appearence and Themes": {
    "UnexpectedAppearanceChanges": 1,
    "Chromeversion": 4,
    "Extensions": 3,
    "Restart": 2,
    "Os": 5,
    "SettingChanges": 6,
    "SoftwareDownloaded": 7,
  },
  "Search Problems": {
    "DifficultyFindingSearchResults": 1,
    "SearchQuery": 2,
    "SearchEngine": 5,
    "SettingChanges": 4,
    "SafeSearch": 3,
    "Browser": 6,
    "InternetConnection": 7
  }
}


class Agenda:
    """The agenda class. Used to resolve conflict between fired rules. by sorting the facts based on their priority."""

    def __init__(self, category):
        self.priority_dict = priorities.get(category, None)
        
    def get_priority(self, fact: str):
        match = re.match(r'^(\w+)', fact)
        if match:
            predicate = match.group(1)
            if predicate in self.priority_dict:
                return self.priority_dict[predicate]
        return float('inf')
         
    def perform_sort(self, facts: list):
        try:
            return sorted(facts, key=lambda x: self.get_priority(x))
        except Exception as e:
            raise e

