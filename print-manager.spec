%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Printer management for KDE
Name:		print-manager
Version:	23.04.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://projects.kde.org/projects/playground/base/print-manager
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/print-manager-%{version}.tar.xz
Source1:	print-manager.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	gettext
BuildRequires:	cups-devel
BuildRequires:	samba-client
Requires:	samba-client
Obsoletes:	kdeutils4-printer-applet < 4.10.0
Obsoletes:	system-config-printer-kde < 2:4.10.0
Provides:	system-config-printer-kde = 2:%{version}-%{release}
# For driver auto-detection
Requires:	system-config-printer-gui

%description
Printer management for KDE.

%files -f all.lang
%{_bindir}/configure-printer
%{_bindir}/kde-add-printer
%{_bindir}/kde-print-queue
%{_libdir}/libkcupslib.so
%{_libdir}/qt5/plugins/kf5/kded/printmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/libprintmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/qmldir
%{_datadir}/applications/kcm_printer_manager.desktop
%{_datadir}/applications/org.kde.kde-add-printer.desktop
%{_datadir}/applications/org.kde.ConfigurePrinter.desktop
%{_datadir}/applications/org.kde.PrintQueue.desktop
%{_datadir}/metainfo/org.kde.plasma.printmanager.appdata.xml
%{_datadir}/metainfo/org.kde.print-manager.metainfo.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/*.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/*.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/metadata.json
%{_datadir}/knotifications5/printmanager.notifyrc
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_printer_manager.so


#----------------------------------------------------------------------------

%prep
%autosetup

# (tpg) adjust path for CUPS backends
sed -i -e 's#/usr/lib#%{_libdir}#g' cmake/modules/FindCupsSmb.cmake

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang plasma_applet_org.kde.plasma.printmanager
%find_lang print-manager
cat *.lang >all.lang
