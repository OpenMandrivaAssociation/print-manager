%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	Printer management for KDE
Name:		print-manager
Version:	19.11.90
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://projects.kde.org/projects/playground/base/print-manager
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/print-manager-%{version}.tar.xz
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
Obsoletes:	kdeutils4-printer-applet < 4.10.0
Obsoletes:	system-config-printer-kde < 2:4.10.0
Provides:	system-config-printer-kde = 2:%{version}-%{release}
# For driver auto-detection
Recommends:	system-config-printer

%description
Printer management for KDE.

%files -f all.lang
%{_bindir}/configure-printer
%{_bindir}/kde-add-printer
%{_bindir}/kde-print-queue
%{_libdir}/libkcupslib.so
%{_libdir}/qt5/plugins/kcm_printer_manager.so
%{_libdir}/qt5/plugins/kded_printmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/libprintmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/qmldir
%{_datadir}/applications/org.kde.kde-add-printer.desktop
%{_datadir}/applications/org.kde.ConfigurePrinter.desktop
%{_datadir}/applications/org.kde.PrintQueue.desktop
%{_datadir}/metainfo/org.kde.plasma.printmanager.appdata.xml
%{_datadir}/metainfo/org.kde.print-manager.metainfo.xml
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/kded/printmanager.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/*.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/*.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/*.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/metadata.json
%{_datadir}/knotifications5/printmanager.notifyrc

#----------------------------------------------------------------------------

%prep
%setup -q -n print-manager-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang plasma_applet_org.kde.plasma.printmanager
%find_lang print-manager
cat *.lang >all.lang
