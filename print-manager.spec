%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240223
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Print manager for Plasma 6
Name:		print-manager
Version:	6.4.4
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/print-manager
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/print-manager/-/archive/%{gitbranch}/print-manager-%{gitbranchd}.tar.bz2#/print-manager-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/print-manager-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(KF6Kirigami) >= 5.246.0
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	%mklibname -d KF6IconWidgets
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	pkgconfig(Qt6QuickControls2)
BuildRequires:	pkgconfig(cups)
Requires:	cups
# print-manager relies on the s-c-p DBus service to configure printers
# without extra authentication
Requires:	system-config-printer
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-05-03
%rename plasma6-print-manager

%description
Print manager for Plasma 6

%prep -a
# Make sure gzipped ppd files (that are handled by cups and packaged
# accordingly) are shown in the PPD selector dialog
sed -i -e 's,(\*\.ppd),(*.ppd *.ppd.gz),g' src/kcm/ui/MakeModel.qml po/*/kcm_printer_manager.po

%files -f %{name}.lang
%{_bindir}/configure-printer
%{_bindir}/kde-print-queue
%{_libdir}/libkcupslib.so*
%{_qtdir}/plugins/kf6/kded/printmanager.so
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_printer_manager.so
%{_qtdir}/qml/org/kde/plasma/printmanager
%{_datadir}/applications/kcm_printer_manager.desktop
%{_datadir}/applications/org.kde.ConfigurePrinter.desktop
%{_datadir}/applications/org.kde.PrintQueue.desktop
%{_datadir}/knotifications6/printmanager.notifyrc
%{_datadir}/metainfo/org.kde.plasma.printmanager.appdata.xml
%{_datadir}/metainfo/org.kde.print-manager.metainfo.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.printmanager
%{_datadir}/qlogging-categories6/pmlogs.categories
