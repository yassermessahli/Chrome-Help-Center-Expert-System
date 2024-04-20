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
                    {"text": "Yes, my computer feels sluggish", "value": "Yes"},
                    {"text": "No, my computer is responsive", "value": "No"},
                    {"text": "I'm not sure", "value": "No"},
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
        "questions": [],
    },
    {
        "title": "Installation",
        "description": "You are having trouble installing Google Chrome.",
        "icon": constants.install_icon,
        "color": constants.green100,
        "button_color": constants.green600,
        "questions": [],
    },
    {
        "title": "Web Content Problems",
        "description": "Google Chrome is not displaying web pages correctly.",
        "icon": constants.web_content_icon,
        "color": constants.orange100,
        "button_color": constants.orange600,
        "questions": [],
    },
    {
        "title": "Sync Issues",
        "description": "Google Chrome is not syncing your data.",
        "icon": constants.sync_icon,
        "color": constants.pink100,
        "button_color": constants.pink600,
        "questions": [],
    },
    {
        "title": "Appearence and Themes",
        "description": "Google Chrome is not looking right.",
        "icon": constants.theme_icon,
        "color": constants.light_green200,
        "button_color": constants.light_green600,
        "questions": [],
    },
    {
        "title": "Search Problems",
        "description": "Google Chrome is not searching correctly.",
        "icon": constants.search_icon,
        "color": constants.grey300,
        "button_color": constants.grey600,
        "questions": [],
    },
]
