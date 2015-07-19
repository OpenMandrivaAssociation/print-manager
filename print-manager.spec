Summary:	Printer management for KDE
Name:		print-manager
Version:	15.04.3
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://projects.kde.org/projects/playground/base/print-manager
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/print-manager-%{version}.tar.xz
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
BuildRequires:	kdelibs-devel
BuildRequires:	cups-devel
Requires:	kde-runtime
Obsoletes:	kdeutils4-printer-applet < 4.10.0
Obsoletes:	system-config-printer-kde < 2:4.10.0
Provides:	system-config-printer-kde = 2:%{version}-%{release}

%description
Printer management for KDE.

%files
%{_bindir}/configure-printer
%{_bindir}/kde-add-printer
%{_bindir}/kde-print-queue
%{_libdir}/libkcupslib.so
%{_libdir}/qt5/plugins/kcm_printer_manager.so
%{_libdir}/qt5/plugins/kded_printmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/libprintmanager.so
%{_libdir}/qt5/qml/org/kde/plasma/printmanager/qmldir
%{_datadir}/applications/org.kde.AddPrinter.desktop
%{_datadir}/applications/org.kde.ConfigurePrinter.desktop
%{_datadir}/applications/org.kde.PrintQueue.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/kded/printmanager.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/*.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/config/*.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/contents/ui/*.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager/metadata.desktop
%{_datadir}/printmanager/printmanager.notifyrc

#----------------------------------------------------------------------------

%prep
%setup -q -n print-manager-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
