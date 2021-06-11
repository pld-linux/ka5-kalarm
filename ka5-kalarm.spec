%define		kdeappsver	21.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kalarm
Summary:	kalarm
Name:		ka5-%{kaname}
Version:	21.04.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	aa65ad3d5f17e4957f403f8a40504e93
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-akonadi-devel >= 18.04.0
BuildRequires:	ka5-kalarmcal-devel >= %{kdeappsver}
BuildRequires:	ka5-kimap-devel >= %{kdeappsver}
BuildRequires:	ka5-mailcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kauth-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kholidays-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAlarm is a personal alarm message, command and email scheduler.

Features

• Display alarms using your own text message, the text generated by a
command, or a text or image file. • Audible alarm using a sound file •
Recurring alarm on an hours/minutes, daily, weekly, monthly or annual
basis, or set it to trigger every time you log in. • Display alarms
color and font customization • Support for multiple alarm calendars,
which for example enables you to share alarms between a laptop and
desktop computer.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/kalarm.autostart.desktop
%attr(755,root,root) %{_bindir}/kalarm
%attr(755,root,root) %{_bindir}/kalarmautostart
%{_prefix}/libexec/kauth/kalarm_helper
%{_desktopdir}/org.kde.kalarm.desktop
%{_datadir}/config.kcfg/kalarmconfig.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_iconsdir}/hicolor/128x128/apps/kalarm.png
%{_iconsdir}/hicolor/16x16/apps/kalarm.png
%{_iconsdir}/hicolor/22x22/apps/kalarm.png
%{_iconsdir}/hicolor/32x32/apps/kalarm.png
%{_iconsdir}/hicolor/48x48/apps/kalarm.png
%{_iconsdir}/hicolor/64x64/apps/kalarm.png
%{_datadir}/kalarm
%attr(755,root,root) %{_datadir}/kconf_update/kalarm-1.2.1-general.pl
%attr(755,root,root) %{_datadir}/kconf_update/kalarm-1.9.5-defaults.pl
%attr(755,root,root) %{_datadir}/kconf_update/kalarm-15.08-kickoff.sh
%attr(755,root,root) %{_datadir}/kconf_update/kalarm-2.0.2-general.pl
%attr(755,root,root) %{_datadir}/kconf_update/kalarm-2.1.5-general.pl
%attr(755,root,root) %{_datadir}/kconf_update/kalarm-version.pl
%{_datadir}/kconf_update/kalarm.upd
%dir %{_datadir}/kxmlgui5/kalarm
%{_datadir}/kxmlgui5/kalarm/kalarmui.rc
%{_datadir}/metainfo/org.kde.kalarm.appdata.xml
%{_datadir}/polkit-1/actions/org.kde.kalarm.rtcwake.policy
%{_datadir}/dbus-1/system-services/org.kde.kalarm.rtcwake.service
%{_datadir}/dbus-1/system.d/org.kde.kalarm.rtcwake.conf
%{_datadir}/qlogging-categories5/kalarm.categories
%{_datadir}/qlogging-categories5/kalarm.renamecategories
%{_datadir}/knotifications5/kalarm.notifyrc
