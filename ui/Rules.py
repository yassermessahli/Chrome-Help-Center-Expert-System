from aima3.logic import *

kb = FolKB()

from aima3.logic import *

# Define a knowledge base
chrome_kb = FolKB()

# Stage 1: Identify Root Cause
chrome_kb.tell(expr('BrowsingExperience(slow)'))  # Fact A: Slow browsing experience
chrome_kb.tell(expr('Tabs(high)'))  # Fact B: Large number of tabs

# Inference rule - Potential memory overload due to tabs
chrome_kb.tell(expr('Tabs(high) & BrowsingExperience(slow) ==> MemoryOverload(Potential)'))  # E1

# Stage 2: Refine Solution
chrome_kb.tell(expr('Extensions(high)'))  # Fact D: Many extensions installed

# Inference rule - Potential extension-related slowdown
chrome_kb.tell(expr('MemoryOverload(Potential) & Extensions(high) ==> ProblemType(ExtensionRelatedSlowdown)'))  # F1

# Alternative rules for resource limitation (not shown in the example)
chrome_kb.tell(expr('Ram(slow) ==> MemoryOverload(Potential)'))
chrome_kb.tell(expr('MemoryOverload(Potential) & Ram(slow) ==> ProblemType(ResourceLimitation)'))  # Alternative Inference 





# Inference rule - Potential memory overload due to tabs (unchanged)
chrome_kb.tell(expr('Tabs(high) & BrowsingExperience(slow) ==> MemoryOverload(Potential)'))  # E1 (unchanged)

# Inference rule - Potential hardware acceleration conflict (new)
chrome_kb.tell(expr('BrowsingExperience(slow) & Glitches(graphical) & GraphicsCard(dedicated) ==> HardwareAccelerationConflict(Potential)'))  # E2 (new)


# Stage 2: Refine Solution - Hardware Acceleration Issues
chrome_kb.tell(expr('HardwareAccelerationConflict(Potential) & HardwareAcceleration(enabled) ==> ProblemType(HardwareAcceleration)'))  # F2 (new)






chrome_kb.tell(expr('BrowsingExperience(slow) & Content(heavy) & Antivirus(real_time_scanning) ==> AntivirusInterference(Potential)'))  # E3 (new)

chrome_kb.tell(expr('AntivirusInterference(Potential) & ExclusionPossible(Chrome) ==> ProblemType(AntivirusSoftwareInterference)'))  # F3 (new)



chrome_kb.tell(expr('BrowsingExperience(Slow) & NewTabOpening(Slow) & Cpu(High_usage) ==> ResourceContention(Potential)'))  # E4 (new)

chrome_kb.tell(expr('ResourceContention(Potential) & BackgroundProcesses(high_cpu) ==> ProblemType(BackgroundProcessesImpact)'))  # F4 (new)




chrome_kb.tell(expr('EmailReceived(Suspicious)& LinkClicked(Email) ==> PhishingAttempt(Potential)'))


chrome_kb.tell(expr('PhishingAttempt(Potential) & EmailFiltering(Disabled) ==> ProblemType(PhishingAttempt)'))



chrome_kb.tell(expr('BrowserBehavior(Unexpected)==> MalwareInfection(Potential)'))


chrome_kb.tell(expr('Popups(Frequent) & SoftwareDownloaded(Untrusted_source) ==> MalwareInfection(Potential)'))



chrome_kb.tell(expr('MalwareInfection(Potential) & Antivirus(Installed) ==> ProblemType(AntivirusDetectionLimitations)'))

chrome_kb.tell(expr('MalwareInfection(Potential) & Antivirus(Notinstalled) ==> ProblemType(Vulnerability)'))





chrome_kb.tell(expr('PasswordLeakNotification(Received) ==> CompromisedPassword(Potential)'))


chrome_kb.tell(expr('CompromisedPassword(Potential) & PasswordChangeSuggestions(Disabled) ==> ProblemType(CompromisedPasswordRisk)'))



chrome_kb.tell(expr('WebsiteNotLoading(specific)'))


chrome_kb.tell(expr('WebsiteNotLoading(specific) & PageRefreshed(Yes) ==> WebsiteIssue(Potential) '))
chrome_kb.tell(expr('WebsiteNotLoading(specific) & PageRefreshed(Yes) ==>  UserSideProblem(Potential)'))
# Stage 2: Refine Solution


chrome_kb.tell(expr('WebsiteIssue(Potential) & InternetConnection(Good) ==> ProblemType(WebsiteIssue)'))


chrome_kb.tell(expr('(UserSideProblem(Potential)) & InternetConnection(Bad) ==> ProblemType(NetworkConnectivityIssue)'))





chrome_kb.tell(expr('WebsiteContent(outdated) ==> Potential(ContentUpdate)'))




chrome_kb.tell(expr('Potential(ContentUpdate) & WebsiteUpdateInfoChecked(yes) ==> ProblemType(WebsiteContentOutdated)'))



chrome_kb.tell(expr('TextDisplay(garbled) ==> TextEncodingIssue(Potential)'))


chrome_kb.tell(expr('TextEncodingIssue(Potential) & TriedDifferentBrowser(yes) ==> ProblemType(ChromeIssue)'))


chrome_kb.tell(expr('TriedDifferentBrowser(no)'))  # Optional fact, negation of TriedDifferentBrowser(yes)


chrome_kb.tell(expr('TextEncodingIssue(Potential) & TriedDifferentBrowser(no) ==> ProblemType(WebsiteIssue)'))




chrome_kb.tell(expr('MediaLoading(problematic)'))

# Fact B: User has a stable internet connection
chrome_kb.tell(expr('InternetConnection(stable)'))

# Inference rule - Potential issues with website or user settings (E1)
chrome_kb.tell(expr('MediaLoading(Yes) & InternetConnection(Stable) ==> MediaIssue(Potential)'))

chrome_kb.tell(expr('MediaIssue(Potential) & InternetSpeed(High) ==> ProblemType(website-side problem)'))


chrome_kb.tell(expr('MediaIssue(Potential) & InternetSpeed(Low) ==> ProblemType(NetworkConnectivityIssue)'))



chrome_kb.tell(expr('WebsiteFunctionality(broken) ==> WebsiteBug(Potential)'))
chrome_kb.tell(expr('WebsiteFunctionality(broken) ==> BrowserIncompatibility(Potential)'))


chrome_kb.tell(expr('(WebsiteBug(Potential) | BrowserIncompatibility(Potential)) & TriedDifferentBrowser(yes) ==> ProblemType(website-side problem)'))

chrome_kb.tell(expr('(TriedDifferentBrowser(Yes) & WebsiteFunctionality(NotBroken)  ==> ProblemType(ChromeIssue)'))  # Refine inference as browser incompatibility is less likely across browsers





chrome_kb.tell(expr('SameGoogleAccount(Alldevices)'))

# Inference rule - Potential sync conflict or technical issue (E1)
chrome_kb.tell(expr('SyncIssue(Reported) & SameGoogleAccount(Alldevices) ==> SyncTechnicalIssue(Potential)'))

chrome_kb.tell(expr('SyncIssue(Reported) & SameGoogleAccount(Alldevices) ==> SyncConflict(Potential)')
# Stage 2: Refine Solution


chrome_kb.tell(expr('SyncConflict(Potential) & Extensions(High) ==> ProblemType(SyncConflict)'))
chrome_kb.tell(expr('SyncTechnicalIssue(Potential) & Extensions(Low) ==> ProblemType(ChromeIssue)'))




chrome_kb.tell(expr('DiskSpace(Low)'))

# Inference rule - Potential storage impacting sync (E1)
chrome_kb.tell(expr('SyncErrors(Reported) & DiskSpace(Low) ==> ProblemType(StorageLimitSyncIssue)'))




chrome_kb.tell(expr('SyncIssue(reported) & SuspiciousLogin(suspected) ==> ConflictingLogin(Potential)'))

chrome_kb.tell(expr('ConflictingLogin(Potential) & NoRecentNewDeviceLogin(confirmed) ==> ProblemType(SuspiciousLogin)'))

chrome_kb.tell(expr('ConflictingLogin(Potential) & LoggedInNewDevice(acknowledged) & UnintendedSync(acknowledged) ==> ProblemType(AccidentalLogin)'))




chrome_kb.tell(expr('IntermittentSyncIssues(reported)'))

# Fact B: User has antivirus with real-time scanning
chrome_kb.tell(expr('AntivirusSoftware(active)'))
chrome_kb.tell(expr('AntivirusRealTimeScanning(enabled)'))

# Inference rule - Potential antivirus software interference (E1)
chrome_kb.tell(expr('IntermittentSyncIssues(reported) & AntivirusSoftware(active) & AntivirusRealTimeScanning(enabled) ==> AntivirusSoftwareInterference(Potential)'))


chrome_kb.tell(expr('AntivirusExclusionList(available)'))

# Inference rule - Antivirus interrupting Chrome sync (F1)
chrome_kb.tell(expr('AntivirusSoftwareInterference(Potential) & AntivirusExclusionList(Enabled) ==> ProblemType(AntivirusSoftwareInterference)'))




chrome_kb.tell(expr('InstallationError(Reported) ==> InstallerIssue(Potential)'))


chrome_kb.tell(expr('InstallerIssue(potential) & DownloadedFromOfficialWebsite(confirmed) ==> CorruptedInstaller(Potential)'))


chrome_kb.tell(expr('InstallerIssue(potential) & DownloadedFromThirdPartyWebsite(confirmed) ==> ProblemType(CorruptedInstaller)'))



chrome_kb.tell(expr('InstallerIssue(potential) & DownloadedFromOfficialWebsite(confirmed) & SystemRequirements(Low) ==> ProblemType(ResourceLimitation)'))


# Inference rule - Potential software conflict (F4)
chrome_kb.tell(expr('InstallerIssue(potential) & DownloadedFromOfficialWebsite(confirmed) & SystemRequirementsMet(confirmed) & SuspectsSoftwareConflict(possible) ==> ProblemType(SoftwareConflictIssue)'))




chrome_kb.tell(expr('InstallationError(Reported) & ChromeVersion(Outdated) ==> ProblemType(ChromeIssue)'))



chrome_kb.tell(expr('InstallationError(reported) & ChromeVersion(Latest) ==> ProblemType(CorruptedInstallationFile)'))




chrome_kb.tell(expr('InstallationError(Reported) ==> InsufficientPermissions(potential)'))


chrome_kb.tell(expr('InsufficientPermissions(potential) & LoggedIn(Administrator) ==>  ProblemType(TemporarySystemGlitch)'))


chrome_kb.tell(expr('InsufficientPermissions(potential) & LoggedIn(StandardUser) ==> ProblemType(InsufficientPermissions)'))




chrome_kb.tell(expr('UnexpectedAppearanceChanges(Reported) ==> ChromeSettingsIssue(Potential)'))


chrome_kb.tell(expr('ChromeSettingsIssue(Potential) & SettingChanges(NoIntentional) ==> ProblemType(BrowserHijacking)'))


chrome_kb.tell(expr('ChromeSettingsIssue(Potential) & Extensions(High) ==> ProblemType(ExtensionsHijacking)'))




chrome_kb.tell(expr('ChromeSettingsIssue(Potential) &  SettingChanges(Intentional) ==> ProblemType(UnintendedChromeSettingsChanges)'))









# Inference rule - Theme compatibility or browser extensions (F1)
chrome_kb.tell(expr('ThemeIssue(Reported)& Chromeversion(Low) & DownloadedFrom(Official) ==> ProblemType(CompatibilityIssue)))

# Question 1: Installed new extensions?
chrome_kb.tell(expr('AskUserAboutNewExtensions(necessary)'))

# Inference rule - Potential interference from a recently installed extension (F2)
chrome_kb.tell(expr('ThemeIssue(Reported) & Extensions(High) ==> ProblemType(ExtensionConflict)'))


chrome_kb.tell(expr('ThemeIssue(Reported)& Chromeversion(Low) & DownloadedFrom(ThirdPartyWebsite) ==> ProblemType(IncompatibleOrMaliciousTheme)'))










chrome_kb.tell(expr('DifficultyFindingSearchResults(reported) ==> PoorSearchQuery | SearchEngineIssue | ChromeSettingsIssue | NetworkConnectivityIssue'))


chrome_kb.tell(expr('PoorSearchQuery | SearchEngineIssue | ChromeSettingsIssue | NetworkConnectivityIssue & ClearAndSpecificSearchQueries(confirmed) ==> SearchEngineIssue | ChromeSettingsIssue | NetworkConnectivityIssue'))


chrome_kb.tell(expr('SearchEngineIssue & AskUserAboutDefaultSearchEngine(necessary) & NotUsingDefaultSearchEngine(confirmed) ==> PotentialNonStandardSearchEngineIssue'))



# Inference rule - Potential conflict with Chrome settings (F3)
chrome_kb.tell(expr('ChromeSettingsIssue & AskUserAboutRecentChromeSettingsChanges(necessary) & MadeRecentChromeSettingsChanges(confirmed) ==> PotentialChromeSettingsConflict'))


chrome_kb.tell(expr('NetworkConnectivityIssue & ~PotentialNonStandardSearchEngineIssue & ~PotentialChromeSettingsConflict ==> AskUserAboutOtherWebsiteAccess(necessary)'))

# Inference rule - Potential network connectivity issue (F4)
chrome_kb.tell(expr('NetworkConnectivityIssue & ~PotentialNonStandardSearchEngineIssue & ~PotentialChromeSettingsConflict & CanAccessOtherWebsites(confirmed) ==> PotentialNetworkConnectivityIssue'))
