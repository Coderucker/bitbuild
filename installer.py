from BitBuild.installer.InstallerWindow import InstallerWindow
from BitBuild.installer.installation import installation
from BitBuild.installer.utils.repair import repair
from BitBuild.installer.utils.uninstall import uninstall

InstallerWindow(installation, repair, uninstall)