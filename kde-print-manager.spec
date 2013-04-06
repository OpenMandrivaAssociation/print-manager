Summary:	Printer management for KDE
Name:		kde-print-manager
Version:	4.10.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
URL:		https://projects.kde.org/projects/playground/base/print-manager
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/print-manager-%{version}.tar.xz
Source1:	kde-print-manager.rpmlintrc
BuildRequires:	gettext
BuildRequires:	kdelibs4-devel
BuildRequires:	cups-devel
Requires:	kdebase4-runtime
Obsoletes:	kdeutils4-printer-applet < 4.10.0
Obsoletes:	system-config-printer-kde < 2:4.10.0
Provides:	system-config-printer-kde = 2:%{version}-%{release}

%description
Printer management for KDE.

%prep
%setup -q -n print-manager-%{version}

%build
%cmake_kde4 -DLIBEXEC_INSTALL_DIR:PATH=%{_kde_libdir}/kde4/libexec
%make

%install
%makeinstall_std -C build

%files
%{_kde_libdir}/kde4/kcm_printer_manager.so
%{_kde_libdir}/kde4/kded_printmanager.so
%{_kde_libdir}/kde4/libexec/add-printer
%{_kde_libdir}/kde4/libexec/configure-printer
%{_kde_libdir}/kde4/libexec/print-queue
%{_kde_libdir}/kde4/plasma_engine_printers.so
%{_kde_libdir}/kde4/plasma_engine_printjobs.so
%{_kde_libdir}/libkcupslib.so
%{_kde_appsdir}/plasma/plasmoids/printmanager
%{_kde_appsdir}/plasma/services/org.kde.printers.operations
%{_kde_appsdir}/plasma/services/org.kde.printjobs.operations
%{_kde_appsdir}/printmanager
%{_kde_services}/kcm_printer_manager.desktop
%{_kde_services}/kded/printmanager.desktop
%{_kde_services}/plasma-applet-printmanager.desktop
%{_kde_services}/plasma-engine-printers.desktop
%{_kde_services}/plasma-engine-printjobs.desktop
%{_datadir}/dbus-1/services/org.kde.AddPrinter.service
%{_datadir}/dbus-1/services/org.kde.ConfigurePrinter.service
%{_datadir}/dbus-1/services/org.kde.PrintQueue.service

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Mon Feb 18 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- Now it's an official KDE replacement of system-config-printer-kde
  and kdeutils4-printer-applet
- No longer ships locale files in tarball

* Fri Aug 31 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2.0-1
+ Revision: 816127
- imported package kde-print-manager

