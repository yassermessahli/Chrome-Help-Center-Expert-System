
rules = {
# Performance issues
"Performance" : [
'Tabs(High) & BrowsingExperience(Slow) ==> Potential(MemoryOverload)' ,
'Potential(MemoryOverload) & Extensions(High) ==> ProblemType(ExtensionRelatedSlowdown)',
'Potential(MemoryOverload) & Ram(Low) ==> ProblemType(ResourceLimitation)',  # Alternative Inference 
'BrowsingExperience(Slow) & Glitches(Graphical) & GraphicsCard(Dedicated) ==> Potential(HardwareAccelerationConflict)' , # E2 (new)
'Potential(HardwareAccelerationConflict) & HardwareAcceleration(Enabled) ==> ProblemType(HardwareAcceleration)',  # F2 (new)
'BrowsingExperience(Slow) & Content(Heavy) & Antivirus(Activated) ==> Potential(AntivirusInterference)', # E3 (new)
'Potential(Potential) & ExclusionPossible(Chrome) ==> ProblemType(AntivirusInterference)',  # F3 (new)
'BrowsingExperience(Slow) & NewTabs(Slow) & Cpu(High) ==> Potential(ResourceContention)',  # E4 (new)
'Potential(ResourceContention) & BackgroundProcesses(High) ==> ProblemType(BackgroundProcessesImpact)'] , # F4 (new)





#Security
"Security" : [  

'EmailReceived(Suspicious)& Link(Clicked) ==> Potential(PhishingAttempt)',
'Potential(PhishingAttempt) & EmailFiltering(Disabled) ==> ProblemType(PhishingAttempt)',
'BrowserBehavior(Unexpected)==> Potential(MalwareInfection)',
'Popups(Unusual) & SoftwareDownloaded(Untrusted) ==> Potential(MalwareInfection)',
'Potential(MalwareInfection) & Antivirus(Activated) ==> ProblemType(AntivirusDetectionLimitations)',
'Potential(MalwareInfection) & Antivirus(Disactivated) ==> ProblemType(Vulnerability)',
'PasswordLeakNotification(Received) ==> Potential(CompromisedPassword)',
'Potential(CompromisedPassword) & PasswordChangeSuggestions(Disabled) ==> ProblemType(CompromisedPasswordRisk)'] ,


# Fixing Web Content Problems :

"Web Content Problems" : [

'WebsiteNotLoading(Specific)' ,
'WebsiteNotLoading(Specific) & PageRefreshed(Yes) ==> Potential(WebsiteIssue) ' ,
'WebsiteNotLoading(Specific) & PageRefreshed(Yes) ==>  Potential(UserSideProblem)' ,
'Potential(WebsiteIssue) & InternetConnection(High) ==> ProblemType(Website-side problem)' ,
'(Potential(UserSideProblem)) & InternetConnection(Low) ==> ProblemType(NetworkConnectivityIssue)' ,
'WebsiteContent(Outdated) ==> Potential(ContentUpdate)' ,
'Potential(ContentUpdate) & WebsiteUpdateInfoChecked(Checked) ==> ProblemType(WebsiteContentOutdated)' ,
'TextDisplay(Garbled) ==> Potential(TextEncodingIssue)' ,
'Potential(TextEncodingIssue) & Browser(Different) ==> ProblemType(Website-side problem)' ,
'Potential(Potential) & Browser(Chrome) ==> ProblemType(ChromeIssue)' ,
'MediaLoadingProblem(Yes) & InternetConnection(High) ==> Potential(MediaIssue)' ,
'Potential(MediaIssue) & InternetConnection(High) ==> ProblemType(Website-side problem)' ,
'Potential(MediaIssue) & InternetConnection(Low) ==> ProblemType(NetworkConnectivityIssue)' ,
'WebsiteFunctionality(Broken) ==> Potential(WebsiteBug)' ,
'WebsiteFunctionality(Broken) ==> Potential(BrowserIncompatibility)' ,
'(Potential(WebsiteBug)& Potential(BrowserIncompatibility)) & Browser(Different) ==> ProblemType(website-side problem)' ,
'(Browser(Chrome) & WebsiteFunctionality(Broken)  ==> ProblemType(ChromeIssue)' ,

],

# Sync problems
"Sync Issues" : [
'SyncIssue(Reported) & SameGoogleAccount(Alldevices) ==> Potential(SyncTechnicalIssue)',
'SyncIssue(Reported) & SameGoogleAccount(Alldevices) ==> Potential(SyncConflict)' ,
'Potential(SyncConflict) & Extensions(High) & BrowserData[Changed] ==> ProblemType(SyncConflict)',
'Potential(SyncTechnicalIssue) & Extensions(Low) & BrowserData[NotChanged]==> ProblemType(ChromeIssue)',
'SyncErrors(Reported) & DiskSpace(Low) ==> ProblemType(StorageLimitSyncIssue)',
'SyncErrors(Reported) ==> Potential(ConflictingLogin)',
'Potential(ConflictingLogin) & RecentNewDeviceLogin(NotConfirmed) ==> ProblemType(SuspiciousLogin)',
'Potential(ConflictingLogin) & RecentNewDeviceLogin(Confirmed) ==> ProblemType(AccidentalLogin)',
'IntermittentSyncIssues(Reported) & Antivirus(Activated) ==> Potential(AntivirusSoftwareInterference)',
'Potential(AntivirusSoftwareInterference) & ExclusionPossible(Chrome) ==> ProblemType(AntivirusSoftwareInterference)',

]   ,
# Chrome installation problem :
"Installation" : [
'InstallationError(Reported) ==> Potential(InstallerIssue)',
'Potential(InstallerIssue) & SoftwareDownloaded(Trusted) ==> Potential(CorruptedInstaller)',
'Potential(InstallerIssue) & SoftwareDownloaded(UnTrusted) ==> ProblemType(CorruptedInstaller)',
'Potential(InstallerIssue) & SoftwareDownloaded(Trusted) & SystemRequirements(Low) ==> ProblemType(ResourceLimitation)',
'Potential(InstallerIssue) & SoftwareDownloaded(Trusted) & SystemRequirements(High) & Antivirus(Activated) ==> ProblemType(SoftwareConflictIssue)',
'InstallationError(Reported) & ChromeVersion(Outdated) ==> ProblemType(ChromeIssue)',
'InstallationError(Reported) & ChromeVersion(Latest) ==> ProblemType(CorruptedInstallationFile)',
'InstallationError(Reported) ==> Potential(InsufficientPermissions)',
'Potential(InsufficientPermissions) & PermissionsErrors(True) & LoggedIn(Administrator) ==>  ProblemType(TemporarySystemGlitch)',
'Potential(InsufficientPermissions) & LoggedIn(StandardUser) ==> ProblemType(InsufficientPermissions)',
] ,

# Appearance changes
"Appearence and Themes" : [

'UnexpectedAppearanceChanges(Reported) ==> Potential(ChromeSettingsIssue)',
'Potential(ChromeSettingsIssue) & SettingChanges(NoIntentional) & Restart(True) ==> ProblemType(BrowserHijacking)',
'Potential(ChromeSettingsIssue) & Extensions(High) & Restart(True) & Os(Windows) ==> ProblemType(ExtensionsHijacking)',
'Potential(ChromeSettingsIssue) &  SettingChanges(Intentional) ==> ProblemType(UnintendedChromeSettingsChanges)',
'Potential(ChromeSettingsIssue) & Chromeversion(Low) & SoftwareDownloaded(Trusted) ==> ProblemType(CompatibilityIssue)',
'Potential(ChromeSettingsIssue) & Extensions(High) ==> ProblemType(ExtensionConflict)',
'Potential(ChromeSettingsIssue) & Chromeversion(Low) & SoftwareDownloaded(Untrusted) ==> ProblemType(IncompatibleOrMaliciousTheme)',



] ,




# search
"Search Problems" : [

'DifficultyFindingSearchResults(Reported) & SearchQuery(Bad) ==> ProblemType(PoorSearchQuery)',
'DifficultyFindingSearchResults(Reported) & SearchQuery(Good) &  ==> Potential(SearchEngineProblem)',
'Potential(SearchEngineProblem) & SettingChanges(Intentional) & SearchEngine(NotDefault) ==> ProblemType(ChromeConflicts)',
'Potential(SearchEngineProblem) & SafeSearch(Activated) ==> ProblemType(SuspiciousSearchResults)',
'Potential(SearchEngineProblem) & SafeSearch(Deactivated) &  InternetConnection(High) & Browser(NotChrome)  ==> ProblemType(SearchResultsIssue)',
'Potential(SearchEngineProblem) & SafeSearch(Deactivated) &  InternetConnection(High) & Browser(Chrome)  ==> ProblemType(SearchResultsIssue)',

]
}