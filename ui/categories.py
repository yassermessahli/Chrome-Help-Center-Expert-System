from constants import constants

categories = [
    {
        "title": "Performance",
        "description": "Google Chrome is running slow or crashing.",
        "icon": constants.performance_icon,
        "color": constants.blue100,
        "button_color": constants.blue600,
        "questions": [
            {
                "question": "Do you currently have a large number of tabs open in Chrome? How many?",
                "options": [
                    {"text": "Usually under 5", "value": "Tabs(Low)"},
                    {"text": "Between 5 and 10", "value": "Tabs(Low)"},
                    {"text": "Between 10 and 20", "value": "Tabs(Hight)"},
                    {"text": "More than 20", "value": "Tabs(Hight)"},
                    {"text": "I don't know", "value": "Tabs(Hight)"},
                ],
            },
            {
                "question": "Have you recently installed any new extensions in Chrome? How many?",
                "options": [
                    {"text": "None", "value": "Extensions(Low)"},
                    {"text": "1 to 3", "value": "Extensions(Low)"},
                    {"text": "4 to 6", "value": "Extensions(High)"},
                    {"text": "More than 6", "value": "Extensions(High)"},
                    {"text": "I don't remember", "value": "Extensions(High)"},
                ],
            },
            {
                "question": "How is the CPU usage in your Task Manager while using Chrome?",
                "options": [
                    {"text": "Low", "value": "Cpu(Low)"},
                    {"text": "Moderate", "value": "Cpu(High)"},
                    {"text": "High", "value": "Cpu(High)"},
                ],
            },
            {
                "question": "Is your version of Google Chrome up to date?",
                "options": [
                    {
                        "text": "Yes, I just updated it",
                        "value": "ChromeVersion(Latest)",
                    },
                    {
                        "text": "No, I haven't updated it in a while",
                        "value": "ChromeVersion(Outdated)",
                    },
                    {"text": "I'm not sure", "value": "ChromeVersion(Outdated)"},
                ],
            },
            {
                "question": "Are you familiar with your computer's RAM capacity? If so, do you know how much RAM you have installed?",
                "options": [
                    {"text": "I have 4GB or less", "value": "Ram(Low)"},
                    {"text": "I have 8GB", "value": "Ram(High)"},
                    {"text": "I have 16GB or more", "value": "Ram(High)"},
                    {"text": "I'm not sure", "value": "Ram(Low)"},
                ],
            },
            {
                "question": "In addition to slow browsing, do you experience any visual glitches or distorted graphics while using Chrome?",
                "options": [
                    {
                        "text": "Yes, I've noticed visual glitches",
                        "value": "Glitches(Yes)",
                    },
                    {"text": "No, everything looks normal", "value": "Glitches(No)"},
                    {"text": "I'm not sure", "value": "Glitches(No)"},
                ],
            },
            {
                "question": "Is your graphical card integrated or dedicated?",
                "options": [
                    {"text": "Integrated", "value": "GraphicsCard(Integrated)"},
                    {"text": "Dedicated", "value": "GraphicsCard(Dedicated)"},
                    {"text": "I have both", "value": "GraphicsCard(Dedicated)"},
                    {"text": "I have no idea", "value": "GraphicsCard(Integrated)"},
                ],
            },
            {
                "question": "Have you checked hardware acceleration in Chrome settings?",
                "options": [
                    {"text": "Enabled", "value": "HardwareAcceleration(Enabled)"},
                    {"text": "Disabled", "value": "HardwareAcceleration(Disabled)"},
                    {"text": "I'm not sure", "value": "HardwareAcceleration(Disabled)"},
                ],
            },
            {
                "question": "Along with slow browsing, have you noticed any delays specifically while loading websites with heavy images, videos, or other content?",
                "options": [
                    {
                        "text": "Yes, I've noticed delays",
                        "value": "BrowsingExperience(Fast)",
                    },
                    {
                        "text": "No, websites load normally",
                        "value": "BrowsingExperience(Slow)",
                    },
                    {"text": "I'm not sure", "value": "BrowsingExperience(Slow)"},
                ],
            },
            {
                "question": "Do you have antivirus software installed on your computer?",
                "options": [
                    {
                        "text": "Yes, I have antivirus software",
                        "value": "Antivirus(Installed)",
                    },
                    {
                        "text": "No, I don't have antivirus software",
                        "value": "Antivirus(Notinstalled)",
                    },
                    {"text": "I'm not sure", "value": "Antivirus(Notinstalled)"},
                ],
            },
            {
                "question": "Does your antivirus software offer an option to exclude specific applications from real-time scanning?",
                "options": [
                    {
                        "text": "Yes, it does",
                        "value": "AntivirusRealTimeScanning(Enabled)",
                    },
                    {
                        "text": "No, it doesn't",
                        "value": "AntivirusRealTimeScanning(Disabled)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "AntivirusRealTimeScanning(Disabled)",
                    },
                ],
            },
            {
                "question": "When you experience slow browsing, particularly when opening new tabs, does your computer feel sluggish overall?",
                "options": [
                    {"text": "Yes, my computer feels sluggish", "value": "NewTabs(Slow)"},
                    {"text": "No, my computer is responsive", "value": "NewTabs(Fast)"},
                    {"text": "I'm not sure", "value": "New"},
                ],
            },
            {
                "question": "If you've used Task Manager/Activity Monitor, can you identify any specific applications or processes consuming high CPU resources alongside Chrome?",
                "options": [
                    {
                        "text": "Yes, I've identified high CPU usage",
                        "value": "BackgroundProcesses(High)",
                    },
                    {
                        "text": "No, everything looks normal",
                        "value": "BackgroundProcesses(Low)",
                    },
                    {"text": "I'm not sure", "value": "BackgroundProcesses(Low)"},
                ],
            },
        ],
    },
    {
        "title": "Security",
        "description": "Google Chrome is not secure.",
        "icon": constants.security_icon,
        "color": constants.red100,
        "button_color": constants.red600,
        "questions": [
            {
                "question": "Have you recently received emails claiming to be from legitimate companies (e.g., banks, social media)?",
                "options": [
                    {
                        "text": "Yes, they seem suspicious",
                        "value": "EmailReceived(Suspicious)",
                    },
                    {
                        "text": "No, they seem legitimate",
                        "value": "EmailReceived(NotSuspicious)",
                    },
                    {
                        "text": "I can't tell",
                        "value": "EmailReceived(Suspicious)",
                    },
                    {
                        "text": "I don't use email",
                        "value": "EmailReceived(NotSuspicious)",
                    },
                ],
            },
            {
                "question": "Do you typically click on links or open attachments within these emails?",
                "options": [
                    {"text": "Yes, I click on links", "value": "Link(Clicked)"},
                    {"text": "No, I don't click on links", "value": "Link(NotClicked)"},
                    {"text": "I'm not sure", "value": "Link(NotClicked)"},
                ],
            },
            {
                "question": "Do you have any email filtering enabled in your email provider settings (e.g., spam filter)?",
                "options": [
                    {
                        "text": "Yes, I have filtering enabled",
                        "value": "EmailFiltering(Enabled)",
                    },
                    {
                        "text": "No, I don't have filtering enabled",
                        "value": "EmailFiltering(Disabled)",
                    },
                    {"text": "I'm not sure", "value": "EmailFiltering(Disabled)"},
                ],
            },
            {
                "question": "Have you experienced any unusual pop-up ads or unexpected changes in Chrome's behavior recently?",
                "options": [
                    {
                        "text": "Yes, I've seen unusual pop-ups",
                        "value": "Popups(Unusual)",
                    },
                    {"text": "No, everything seems normal", "value": "Popups(Usual)"},
                    {"text": "I'm not sure", "value": "Popups(Usual)"},
                ],
            },
            {
                "question": "Do you typically download software from websites other than official app stores or developer websites?",
                "options": [
                    {
                        "text": "Yes, I download from untrusted sites",
                        "value": "SoftwareDownloaded(Untrusted)",
                    },
                    {
                        "text": "No, I download from trusted sources",
                        "value": "SoftwareDownloaded(Trusted)",
                    },
                    {"text": "I'm not sure", "value": "SoftwareDownloaded(Trusted)"},
                ],
            },
            {
                "question": "Do you have antivirus software installed on your computer and is it actively running?",
                "options": [
                    {
                        "text": "Yes, antivirus is activated",
                        "value": "Antivirus(Activated)",
                    },
                    {
                        "text": "No, antivirus is deactivated",
                        "value": "Antivirus(Disactivated)",
                    },
                    {"text": "I'm not sure", "value": "Antivirus(Disactivated)"},
                ],
            },
            {
                "question": "Have you recently received a notification from Chrome about a potential password leak?",
                "options": [
                    {
                        "text": "Yes, I received the notification",
                        "value": "PasswordLeakNotification(Received)",
                    },
                    {
                        "text": "No, I haven't received any notification",
                        "value": "PasswordLeakNotification(NotReceived)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "PasswordLeakNotification(NotReceived)",
                    },
                ],
            },
            {
                "question": "Do you have the option enabled in Chrome settings to recommend password changes for leaked passwords?",
                "options": [
                    {
                        "text": "Yes, I have it enabled",
                        "value": "PasswordChangeSuggestions(Enabled)",
                    },
                    {
                        "text": "No, I have it disabled",
                        "value": "PasswordChangeSuggestions(Disabled)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "PasswordChangeSuggestions(Disabled)",
                    },
                ],
            },
        ],
    },
    {
        "title": "Installation",
        "description": "You are having trouble installing Google Chrome.",
        "icon": constants.install_icon,
        "color": constants.green100,
        "button_color": constants.green600,
        "questions": [
            {
                "question": "What specific error message (if any) did you encounter during Chrome installation?",
                "options": [
                    {
                        "text": "Reported installation error",
                        "value": "InstallationError(Reported)",
                    },
                    {
                        "text": "No reported error",
                        "value": "InstallationError(NotReported)",
                    },
                    {"text": "I'm not sure", "value": "InstallationError(Reported)"},
                ],
            },
            {
                "question": "Did you download the Chrome installer from the official Google Chrome website?",
                "options": [
                    {
                        "text": "Yes, I downloaded from official site",
                        "value": "SoftwareDownloaded(Trusted)",
                    },
                    {
                        "text": "No, I downloaded from elsewhere",
                        "value": "SoftwareDownloaded(UnTrusted)",
                    },
                    {"text": "I'm not sure", "value": "SoftwareDownloaded(Trusted)"},
                ],
            },
            {
                "question": "Does your computer meet the minimum system requirements for running Chrome?",
                "options": [
                    {
                        "text": "High system requirements",
                        "value": "SystemRequirements(High)",
                    },
                    {
                        "text": "Low system requirements",
                        "value": "SystemRequirements(Low)",
                    },
                    {"text": "I'm not sure", "value": "SystemRequirements(High)"},
                ],
            },
            {
                "question": "Do you have any antivirus or security software running on your computer?",
                "options": [
                    {"text": "Antivirus is activated", "value": "Antivirus(Activated)"},
                    {
                        "text": "Antivirus is deactivated",
                        "value": "Antivirus(Disactivated)",
                    },
                    {"text": "I'm not sure", "value": "Antivirus(Disactivated)"},
                ],
            },
            {
                "question": "How long has it been since you last updated Chrome?",
                "options": [
                    {"text": "Outdated version", "value": "ChromeVersion(Outdated)"},
                    {"text": "Latest version", "value": "ChromeVersion(Latest)"},
                    {"text": "I'm not sure", "value": "ChromeVersion(Outdated)"},
                ],
            },
            {
                "question": "What specific error message did you encounter during Chrome installation?",
                "options": [
                    {
                        "text": "Permissions error reported",
                        "value": "PermissionsErrors(True)",
                    },
                    {
                        "text": "No permissions error",
                        "value": "PermissionsErrors(False)",
                    },
                    {"text": "I'm not sure", "value": "PermissionsErrors(False)"},
                ],
            },
            {
                "question": "Are you logged in with an administrator account on your computer?",
                "options": [
                    {
                        "text": "Standard user account",
                        "value": "LoggedIn(StandardUser)",
                    },
                    {"text": "Administrator account", "value": "LoggedIn(Admin)"},
                    {"text": "I'm not sure", "value": "LoggedIn(Admin)"},
                ],
            },
            {
                "question": "Is it possible for you to switch to an administrator account temporarily for the installation process?",
                "options": [
                    {
                        "text": "Yes, I can switch accounts",
                        "value": "SwitchAccount(Yes)",
                    },
                    {
                        "text": "No, I can't switch accounts",
                        "value": "SwitchAccount(No)",
                    },
                    {"text": "I'm not sure", "value": "SwitchAccount(Yes)"},
                ],
            },
        ],
    },
    {
        "title": "Web Content Problems",
        "description": "Google Chrome is not displaying web pages correctly.",
        "icon": constants.web_content_icon,
        "color": constants.orange100,
        "button_color": constants.orange600,
        "questions": [
            {
                "question": "Are you encountering an error message when trying to access a specific website or is it for all websites?",
                "options": [
                    {
                        "text": "Specific website",
                        "value": "WebsiteNotLoading(Specific)",
                    },
                    {"text": "All websites", "value": "WebsiteNotLoading(All)"},
                    {"text": "I'm not sure", "value": "WebsiteNotLoading(Specific)"},
                ],
            },
            {
                "question": "Have you tried refreshing the page multiple times?",
                "options": [
                    {
                        "text": "Yes, I've refreshed the page",
                        "value": "PageRefreshed(Yes)",
                    },
                    {
                        "text": "No, I haven't refreshed the page",
                        "value": "PageRefreshed(No)",
                    },
                    {"text": "I'm not sure", "value": "PageRefreshed(No)"},
                ],
            },
            {
                "question": "Have you confirmed your internet connection is stable and sufficient for streaming content?",
                "options": [
                    {
                        "text": "High-speed connection",
                        "value": "InternetConnection(High)",
                    },
                    {
                        "text": "Low-speed connection",
                        "value": "InternetConnection(Low)",
                    },
                    {"text": "I'm not sure", "value": "InternetConnection(High)"},
                ],
            },
            {
                "question": "Are you encountering outdated information or broken links while browsing a specific website?",
                "options": [
                    {
                        "text": "Outdated information",
                        "value": "WebsiteContent(Outdated)",
                    },
                    {
                        "text": "Up-to-date information",
                        "value": "WebsiteContent(NotOutdated)",
                    },
                    {"text": "I'm not sure", "value": "WebsiteContent(Outdated)"},
                ],
            },
            {
                "question": "Have you checked the website for any information about when the content was last updated?",
                "options": [
                    {
                        "text": "Yes, I checked the update info",
                        "value": "WebsiteUpdateInfo(Checked)",
                    },
                    {
                        "text": "No, I haven't checked the update info",
                        "value": "WebsiteUpdateInfo(NotChecked)",
                    },
                    {"text": "I'm not sure", "value": "WebsiteUpdateInfo(NotChecked)"},
                ],
            },
            {
                "question": "Are you encountering strange characters or garbled text while browsing a specific website?",
                "options": [
                    {"text": "Garbled text", "value": "TextDisplay(Garbled)"},
                    {"text": "Normal text", "value": "TextDisplay(NotGarbled)"},
                    {"text": "I'm not sure", "value": "TextDisplay(Garbled)"},
                ],
            },
            {
                "question": "Have you tried accessing the website with a different browser to see if the issue persists?",
                "options": [
                    {
                        "text": "Yes, I tried a different browser",
                        "value": "Browser(Different)",
                    },
                    {"text": "No, I only use Chrome", "value": "Browser(Chrome)"},
                    {"text": "I'm not sure", "value": "Browser(Chrome)"},
                ],
            },
            {
                "question": "Are you specifically having trouble loading images or videos on a website?",
                "options": [
                    {
                        "text": "Yes, I'm having trouble",
                        "value": "MediaLoadingProblem(Yes)",
                    },
                    {
                        "text": "No, images load fine",
                        "value": "MediaLoadingProblem(No)",
                    },
                    {"text": "I'm not sure", "value": "MediaLoadingProblem(No)"},
                ],
            },
            {
                "question": "Are you encountering specific features not working properly on a website? (e.g., login forms, buttons)",
                "options": [
                    {
                        "text": "Features are broken",
                        "value": "WebsiteFunctionality(Broken)",
                    },
                    {
                        "text": "Features work fine",
                        "value": "WebsiteFunctionality(NotBroken)",
                    },
                    {"text": "I'm not sure", "value": "WebsiteFunctionality(Broken)"},
                ],
            },
        ],
    },
    {
        "title": "Sync Issues",
        "description": "Google Chrome is not syncing your data.",
        "icon": constants.sync_icon,
        "color": constants.pink100,
        "button_color": constants.pink600,
        "questions": [
            {
                "question": "Are you experiencing issues with your bookmarks or browsing history not syncing across all your devices where you use Chrome?",
                "options": [
                    {"text": "Reported sync issues", "value": "SyncIssue(Reported)"},
                    {
                        "text": "No reported sync issues",
                        "value": "SyncIssue(NotReported)",
                    },
                    {"text": "I'm not sure", "value": "SyncIssue(Reported)"},
                ],
            },
            {
                "question": "Have you confirmed you're signed in to the same Google Account on all these devices?",
                "options": [
                    {
                        "text": "All devices are signed in",
                        "value": "SameGoogleAccount(AllDevices)",
                    },
                    {
                        "text": "Not all devices are signed in",
                        "value": "SameGoogleAccount(NotALL)",
                    },
                    {"text": "I'm not sure", "value": "SameGoogleAccount(AllDevices)"},
                ],
            },
            {
                "question": "Have you recently made any major changes to your bookmarks or browsing data on any specific device?",
                "options": [
                    {"text": "Changes were made", "value": "BrowserData(Changed)"},
                    {
                        "text": "No changes were made",
                        "value": "BrowserData(NotChanged)",
                    },
                    {"text": "I'm not sure", "value": "BrowserData(Changed)"},
                ],
            },
            {
                "question": "Have you recently installed any new extensions in Chrome that might interact with bookmarks or browsing history?",
                "options": [
                    {"text": "High number of extensions", "value": "Extensions(High)"},
                    {"text": "Low number of extensions", "value": "Extensions(Low)"},
                    {"text": "I'm not sure", "value": "Extensions(High)"},
                ],
            },
            {
                "question": "Are you encountering sync errors specifically on one device while others seem to be working properly?",
                "options": [
                    {"text": "Reported sync errors", "value": "SyncErrors(Reported)"},
                    {
                        "text": "No reported sync errors",
                        "value": "SyncErrors(NoReported)",
                    },
                    {"text": "I'm not sure", "value": "SyncErrors(Reported)"},
                ],
            },
            {
                "question": "Does the device with sync issues have very limited available storage space?",
                "options": [
                    {"text": "High storage space", "value": "DiskSpace(High)"},
                    {"text": "Low storage space", "value": "DiskSpace(Low)"},
                    {"text": "I'm not sure", "value": "DiskSpace(High)"},
                ],
            },
            {
                "question": "Have you recently signed in to your Google Account on any new devices that you don't intend to keep synced with Chrome?",
                "options": [
                    {
                        "text": "Confirmed new device sign-in",
                        "value": "RecentNewDeviceLogin(Confirmed)",
                    },
                    {
                        "text": "Not confirmed new device sign-in",
                        "value": "RecentNewDeviceLogin(NotConfirmed)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "RecentNewDeviceLogin(Confirmed)",
                    },
                ],
            },
            {
                "question": "Do you notice your sync functionality stopping and restarting occasionally, even though you haven't manually signed out?",
                "options": [
                    {
                        "text": "Reported intermittent sync issues",
                        "value": "IntermittentSyncIssues(Reported)",
                    },
                    {
                        "text": "No reported intermittent sync issues",
                        "value": "IntermittentSyncIssues(NotReported)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "IntermittentSyncIssues(Reported)",
                    },
                ],
            },
            {
                "question": "Do you have antivirus software installed on your device with real-time scanning enabled?",
                "options": [
                    {
                        "text": "Antivirus with real-time scanning",
                        "value": "Antivirus(Activated)",
                    },
                    {
                        "text": "Antivirus without real-time scanning",
                        "value": "Antivirus(Disactivated)",
                    },
                    {"text": "I'm not sure", "value": "Antivirus(Disactivated)"},
                ],
            },
            {
                "question": "Does your antivirus software offer options to exclude specific programs from real-time scanning?",
                "options": [
                    {
                        "text": "Exclusion possible for Chrome",
                        "value": "ExclusionPossible(Chrome)",
                    },
                    {
                        "text": "No exclusion possible for Chrome",
                        "value": "ExclusionPossible(NotChrome)",
                    },
                    {"text": "I'm not sure", "value": "ExclusionPossible(Chrome)"},
                ],
            },
        ],
    },
    {
        "title": "Appearence and Themes",
        "description": "Google Chrome is not looking right.",
        "icon": constants.theme_icon,
        "color": constants.light_green200,
        "button_color": constants.light_green600,
        "questions": [
            {
                "question": "Have you encountered any error messages related to the theme while using Chrome?",
                "options": [
                    {
                        "text": "Reported appearance changes",
                        "value": "UnexpectedAppearanceChanges(Reported)",
                    },
                    {
                        "text": "No reported appearance changes",
                        "value": "UnexpectedAppearanceChanges(NotReported)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "UnexpectedAppearanceChanges(Reported)",
                    },
                ],
            },
            {
                "question": "What version of Chrome are you currently using?",
                "options": [
                    {"text": "High version", "value": "Chromeversion(High)"},
                    {"text": "Low version", "value": "Chromeversion(Low)"},
                    {"text": "I'm not sure", "value": "Chromeversion(High)"},
                ],
            },
            {
                "question": "Have you recently installed any new Chrome extensions?",
                "options": [
                    {"text": "High number of extensions", "value": "Extensions(High)"},
                    {"text": "Low number of extensions", "value": "Extensions(Low)"},
                    {"text": "I'm not sure", "value": "Extensions(High)"},
                ],
            },
            {
                "question": "Have you noticed any unfamiliar toolbars or search engines appearing in Chrome, or any unexpected redirects when browsing?",
                "options": [
                    {
                        "text": "Reported appearance changes",
                        "value": "UnexpectedAppearanceChanges(Reported)",
                    },
                    {
                        "text": "No reported appearance changes",
                        "value": "UnexpectedAppearanceChanges(NotReported)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "UnexpectedAppearanceChanges(Reported)",
                    },
                ],
            },
            {
                "question": "Have you tried restarting Chrome completely?",
                "options": [
                    {"text": "Yes, I've restarted Chrome", "value": "Restart(True)"},
                    {
                        "text": "No, I haven't restarted Chrome",
                        "value": "Restart(False)",
                    },
                    {"text": "I'm not sure", "value": "Restart(True)"},
                ],
            },
            {
                "question": "Are you using Chrome on a computer running Windows, Mac, or another operating system?",
                "options": [
                    {"text": "Windows", "value": "Os(Windows)"},
                    {"text": "Linux", "value": "Os(Linux)"},
                    {"text": "Mac", "value": "Os(Mac)"},
                    {"text": "Other", "value": "Os(Windows)"},
                ],
            },
            {
                "question": "Have you made any changes in the settings?",
                "options": [
                    {
                        "text": "Intentional changes",
                        "value": "SettingChanges(Intentional)",
                    },
                    {
                        "text": "No changes made",
                        "value": "SettingChanges(NotIntentional)",
                    },
                    {"text": "I'm not sure", "value": "SettingChanges(Intentional)"},
                ],
            },
            {
                "question": "Have you downloaded the theme from the official website?",
                "options": [
                    {"text": "Trusted source", "value": "SoftwareDownloaded(Trusted)"},
                    {
                        "text": "Untrusted source",
                        "value": "SoftwareDownloaded(Untrusted)",
                    },
                    {"text": "I'm not sure", "value": "SoftwareDownloaded(Trusted)"},
                ],
            },
        ],
    },
    {
        "title": "Search Problems",
        "description": "Google Chrome is not searching correctly.",
        "icon": constants.search_icon,
        "color": constants.grey300,
        "button_color": constants.grey600,
        "questions": [
            {
                "question": "Is it difficult to find search results?",
                "options": [
                    {
                        "text": "Reported difficulty",
                        "value": "DifficultyFindingSearchResults(Reported)",
                    },
                    {
                        "text": "No reported difficulty",
                        "value": "DifficultyFindingSearchResults(NotReported)",
                    },
                    {
                        "text": "I'm not sure",
                        "value": "DifficultyFindingSearchResults(Reported)",
                    },
                ],
            },
            {
                "question": "Is your search query clear?",
                "options": [
                    {"text": "Bad search query", "value": "SearchQuery(Bad)"},
                    {"text": "Good search query", "value": "SearchQuery(Good)"},
                    {"text": "I'm not sure", "value": "SearchQuery(Good)"},
                ],
            },
            {
                "question": "Are you using the default search engine in Chrome?",
                "options": [
                    {
                        "text": "Not default search engine",
                        "value": "SearchEngine(NotDefault)",
                    },
                    {"text": "Default search engine", "value": "SearchEngine(Default)"},
                    {"text": "I'm not sure", "value": "SearchEngine(Default)"},
                ],
            },
            {
                "question": "Have you made any recent changes to Chrome settings, particularly related to search or privacy?",
                "options": [
                    {
                        "text": "Intentional changes",
                        "value": "SettingChanges(Intentional)",
                    },
                    {
                        "text": "No changes made",
                        "value": "SettingChanges(NotIntentional)",
                    },
                    {"text": "I'm not sure", "value": "SettingChanges(Intentional)"},
                ],
            },
            {
                "question": "Is the safe search activated?",
                "options": [
                    {"text": "Safe search activated", "value": "SafeSearch(Activated)"},
                    {
                        "text": "Safe search deactivated",
                        "value": "SafeSearch(Disactivated)",
                    },
                    {"text": "I'm not sure", "value": "SafeSearch(Activated)"},
                ],
            },
            {
                "question": "Have you tried using a different web browser to conduct the same search queries?",
                "options": [
                    {"text": "Chrome browser", "value": "Browser(Chrome)"},
                    {"text": "Different browser", "value": "Browser(NotChrome)"},
                    {"text": "I'm not sure", "value": "Browser(Chrome)"},
                ],
            },
            {
                "question": "How is your internet connection?",
                "options": [
                    {
                        "text": "High-speed connection",
                        "value": "InternetConnection(High)",
                    },
                    {
                        "text": "Low-speed connection",
                        "value": "InternetConnection(Low)",
                    },
                    {"text": "I'm not sure", "value": "InternetConnection(High)"},
                ],
            },
        ],
    },
]
