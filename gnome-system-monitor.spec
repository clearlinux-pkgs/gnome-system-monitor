#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-system-monitor
Version  : 3.30.0
Release  : 7
URL      : https://download.gnome.org/sources/gnome-system-monitor/3.30/gnome-system-monitor-3.30.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-system-monitor/3.30/gnome-system-monitor-3.30.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-system-monitor-bin
Requires: gnome-system-monitor-data
Requires: gnome-system-monitor-license
Requires: gnome-system-monitor-locales
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : gsettings-desktop-schemas
BuildRequires : pkgconfig(giomm-2.4)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(libgtop-2.0)
BuildRequires : pkgconfig(librsvg-2.0)

%description
System-Monitor
=============
Optional dependencies :
- libgksu2 - recommended
- libgnomesu
- libselinux
- lsb_release in PATH - recommended on linux

%package bin
Summary: bin components for the gnome-system-monitor package.
Group: Binaries
Requires: gnome-system-monitor-data
Requires: gnome-system-monitor-license

%description bin
bin components for the gnome-system-monitor package.


%package data
Summary: data components for the gnome-system-monitor package.
Group: Data

%description data
data components for the gnome-system-monitor package.


%package doc
Summary: doc components for the gnome-system-monitor package.
Group: Documentation

%description doc
doc components for the gnome-system-monitor package.


%package license
Summary: license components for the gnome-system-monitor package.
Group: Default

%description license
license components for the gnome-system-monitor package.


%package locales
Summary: locales components for the gnome-system-monitor package.
Group: Default

%description locales
locales components for the gnome-system-monitor package.


%prep
%setup -q -n gnome-system-monitor-3.30.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536128688
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/gnome-system-monitor
cp COPYING %{buildroot}/usr/share/doc/gnome-system-monitor/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-system-monitor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-system-monitor
/usr/libexec/gnome-system-monitor/gsm-kill
/usr/libexec/gnome-system-monitor/gsm-renice

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-system-monitor-kde.desktop
/usr/share/applications/gnome-system-monitor.desktop
/usr/share/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
/usr/share/gnome-system-monitor/gsm.gresource
/usr/share/icons/hicolor/16x16/apps/gnome-system-monitor.png
/usr/share/icons/hicolor/22x22/apps/gnome-system-monitor.png
/usr/share/icons/hicolor/24x24/apps/gnome-system-monitor.png
/usr/share/icons/hicolor/32x32/apps/gnome-system-monitor.png
/usr/share/icons/hicolor/48x48/apps/gnome-system-monitor.png
/usr/share/icons/hicolor/512x512/apps/gnome-system-monitor.png
/usr/share/icons/hicolor/symbolic/apps/gnome-system-monitor-symbolic.svg
/usr/share/metainfo/gnome-system-monitor.appdata.xml
/usr/share/polkit-1/actions/org.gnome.gnome-system-monitor.policy

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-system-monitor/commandline.page
/usr/share/help/C/gnome-system-monitor/cpu-check.page
/usr/share/help/C/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/C/gnome-system-monitor/cpu-multicore.page
/usr/share/help/C/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/C/gnome-system-monitor/fs-device.page
/usr/share/help/C/gnome-system-monitor/fs-diskusage.page
/usr/share/help/C/gnome-system-monitor/fs-info.page
/usr/share/help/C/gnome-system-monitor/fs-showall.page
/usr/share/help/C/gnome-system-monitor/index.page
/usr/share/help/C/gnome-system-monitor/legal.xml
/usr/share/help/C/gnome-system-monitor/mem-check.page
/usr/share/help/C/gnome-system-monitor/mem-swap.page
/usr/share/help/C/gnome-system-monitor/memory-map-use.page
/usr/share/help/C/gnome-system-monitor/net-bits.page
/usr/share/help/C/gnome-system-monitor/process-explain.page
/usr/share/help/C/gnome-system-monitor/process-files.page
/usr/share/help/C/gnome-system-monitor/process-identify-file.page
/usr/share/help/C/gnome-system-monitor/process-identify-hog.page
/usr/share/help/C/gnome-system-monitor/process-kill.page
/usr/share/help/C/gnome-system-monitor/process-many.page
/usr/share/help/C/gnome-system-monitor/process-priority-change.page
/usr/share/help/C/gnome-system-monitor/process-status.page
/usr/share/help/C/gnome-system-monitor/process-update-speed.page
/usr/share/help/C/gnome-system-monitor/solaris-mode.page
/usr/share/help/C/gnome-system-monitor/units.page
/usr/share/help/cs/gnome-system-monitor/commandline.page
/usr/share/help/cs/gnome-system-monitor/cpu-check.page
/usr/share/help/cs/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/cs/gnome-system-monitor/cpu-multicore.page
/usr/share/help/cs/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/cs/gnome-system-monitor/fs-device.page
/usr/share/help/cs/gnome-system-monitor/fs-diskusage.page
/usr/share/help/cs/gnome-system-monitor/fs-info.page
/usr/share/help/cs/gnome-system-monitor/fs-showall.page
/usr/share/help/cs/gnome-system-monitor/index.page
/usr/share/help/cs/gnome-system-monitor/legal.xml
/usr/share/help/cs/gnome-system-monitor/mem-check.page
/usr/share/help/cs/gnome-system-monitor/mem-swap.page
/usr/share/help/cs/gnome-system-monitor/memory-map-use.page
/usr/share/help/cs/gnome-system-monitor/net-bits.page
/usr/share/help/cs/gnome-system-monitor/process-explain.page
/usr/share/help/cs/gnome-system-monitor/process-files.page
/usr/share/help/cs/gnome-system-monitor/process-identify-file.page
/usr/share/help/cs/gnome-system-monitor/process-identify-hog.page
/usr/share/help/cs/gnome-system-monitor/process-kill.page
/usr/share/help/cs/gnome-system-monitor/process-many.page
/usr/share/help/cs/gnome-system-monitor/process-priority-change.page
/usr/share/help/cs/gnome-system-monitor/process-status.page
/usr/share/help/cs/gnome-system-monitor/process-update-speed.page
/usr/share/help/cs/gnome-system-monitor/solaris-mode.page
/usr/share/help/cs/gnome-system-monitor/units.page
/usr/share/help/de/gnome-system-monitor/commandline.page
/usr/share/help/de/gnome-system-monitor/cpu-check.page
/usr/share/help/de/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/de/gnome-system-monitor/cpu-multicore.page
/usr/share/help/de/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/de/gnome-system-monitor/fs-device.page
/usr/share/help/de/gnome-system-monitor/fs-diskusage.page
/usr/share/help/de/gnome-system-monitor/fs-info.page
/usr/share/help/de/gnome-system-monitor/fs-showall.page
/usr/share/help/de/gnome-system-monitor/index.page
/usr/share/help/de/gnome-system-monitor/legal.xml
/usr/share/help/de/gnome-system-monitor/mem-check.page
/usr/share/help/de/gnome-system-monitor/mem-swap.page
/usr/share/help/de/gnome-system-monitor/memory-map-use.page
/usr/share/help/de/gnome-system-monitor/net-bits.page
/usr/share/help/de/gnome-system-monitor/process-explain.page
/usr/share/help/de/gnome-system-monitor/process-files.page
/usr/share/help/de/gnome-system-monitor/process-identify-file.page
/usr/share/help/de/gnome-system-monitor/process-identify-hog.page
/usr/share/help/de/gnome-system-monitor/process-kill.page
/usr/share/help/de/gnome-system-monitor/process-many.page
/usr/share/help/de/gnome-system-monitor/process-priority-change.page
/usr/share/help/de/gnome-system-monitor/process-status.page
/usr/share/help/de/gnome-system-monitor/process-update-speed.page
/usr/share/help/de/gnome-system-monitor/solaris-mode.page
/usr/share/help/de/gnome-system-monitor/units.page
/usr/share/help/el/gnome-system-monitor/commandline.page
/usr/share/help/el/gnome-system-monitor/cpu-check.page
/usr/share/help/el/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/el/gnome-system-monitor/cpu-multicore.page
/usr/share/help/el/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/el/gnome-system-monitor/fs-device.page
/usr/share/help/el/gnome-system-monitor/fs-diskusage.page
/usr/share/help/el/gnome-system-monitor/fs-info.page
/usr/share/help/el/gnome-system-monitor/fs-showall.page
/usr/share/help/el/gnome-system-monitor/index.page
/usr/share/help/el/gnome-system-monitor/legal.xml
/usr/share/help/el/gnome-system-monitor/mem-check.page
/usr/share/help/el/gnome-system-monitor/mem-swap.page
/usr/share/help/el/gnome-system-monitor/memory-map-use.page
/usr/share/help/el/gnome-system-monitor/net-bits.page
/usr/share/help/el/gnome-system-monitor/process-explain.page
/usr/share/help/el/gnome-system-monitor/process-files.page
/usr/share/help/el/gnome-system-monitor/process-identify-file.page
/usr/share/help/el/gnome-system-monitor/process-identify-hog.page
/usr/share/help/el/gnome-system-monitor/process-kill.page
/usr/share/help/el/gnome-system-monitor/process-many.page
/usr/share/help/el/gnome-system-monitor/process-priority-change.page
/usr/share/help/el/gnome-system-monitor/process-status.page
/usr/share/help/el/gnome-system-monitor/process-update-speed.page
/usr/share/help/el/gnome-system-monitor/solaris-mode.page
/usr/share/help/el/gnome-system-monitor/units.page
/usr/share/help/es/gnome-system-monitor/commandline.page
/usr/share/help/es/gnome-system-monitor/cpu-check.page
/usr/share/help/es/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/es/gnome-system-monitor/cpu-multicore.page
/usr/share/help/es/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/es/gnome-system-monitor/fs-device.page
/usr/share/help/es/gnome-system-monitor/fs-diskusage.page
/usr/share/help/es/gnome-system-monitor/fs-info.page
/usr/share/help/es/gnome-system-monitor/fs-showall.page
/usr/share/help/es/gnome-system-monitor/index.page
/usr/share/help/es/gnome-system-monitor/legal.xml
/usr/share/help/es/gnome-system-monitor/mem-check.page
/usr/share/help/es/gnome-system-monitor/mem-swap.page
/usr/share/help/es/gnome-system-monitor/memory-map-use.page
/usr/share/help/es/gnome-system-monitor/net-bits.page
/usr/share/help/es/gnome-system-monitor/process-explain.page
/usr/share/help/es/gnome-system-monitor/process-files.page
/usr/share/help/es/gnome-system-monitor/process-identify-file.page
/usr/share/help/es/gnome-system-monitor/process-identify-hog.page
/usr/share/help/es/gnome-system-monitor/process-kill.page
/usr/share/help/es/gnome-system-monitor/process-many.page
/usr/share/help/es/gnome-system-monitor/process-priority-change.page
/usr/share/help/es/gnome-system-monitor/process-status.page
/usr/share/help/es/gnome-system-monitor/process-update-speed.page
/usr/share/help/es/gnome-system-monitor/solaris-mode.page
/usr/share/help/es/gnome-system-monitor/units.page
/usr/share/help/fr/gnome-system-monitor/commandline.page
/usr/share/help/fr/gnome-system-monitor/cpu-check.page
/usr/share/help/fr/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/fr/gnome-system-monitor/cpu-multicore.page
/usr/share/help/fr/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/fr/gnome-system-monitor/fs-device.page
/usr/share/help/fr/gnome-system-monitor/fs-diskusage.page
/usr/share/help/fr/gnome-system-monitor/fs-info.page
/usr/share/help/fr/gnome-system-monitor/fs-showall.page
/usr/share/help/fr/gnome-system-monitor/index.page
/usr/share/help/fr/gnome-system-monitor/legal.xml
/usr/share/help/fr/gnome-system-monitor/mem-check.page
/usr/share/help/fr/gnome-system-monitor/mem-swap.page
/usr/share/help/fr/gnome-system-monitor/memory-map-use.page
/usr/share/help/fr/gnome-system-monitor/net-bits.page
/usr/share/help/fr/gnome-system-monitor/process-explain.page
/usr/share/help/fr/gnome-system-monitor/process-files.page
/usr/share/help/fr/gnome-system-monitor/process-identify-file.page
/usr/share/help/fr/gnome-system-monitor/process-identify-hog.page
/usr/share/help/fr/gnome-system-monitor/process-kill.page
/usr/share/help/fr/gnome-system-monitor/process-many.page
/usr/share/help/fr/gnome-system-monitor/process-priority-change.page
/usr/share/help/fr/gnome-system-monitor/process-status.page
/usr/share/help/fr/gnome-system-monitor/process-update-speed.page
/usr/share/help/fr/gnome-system-monitor/solaris-mode.page
/usr/share/help/fr/gnome-system-monitor/units.page
/usr/share/help/hu/gnome-system-monitor/commandline.page
/usr/share/help/hu/gnome-system-monitor/cpu-check.page
/usr/share/help/hu/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/hu/gnome-system-monitor/cpu-multicore.page
/usr/share/help/hu/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/hu/gnome-system-monitor/fs-device.page
/usr/share/help/hu/gnome-system-monitor/fs-diskusage.page
/usr/share/help/hu/gnome-system-monitor/fs-info.page
/usr/share/help/hu/gnome-system-monitor/fs-showall.page
/usr/share/help/hu/gnome-system-monitor/index.page
/usr/share/help/hu/gnome-system-monitor/legal.xml
/usr/share/help/hu/gnome-system-monitor/mem-check.page
/usr/share/help/hu/gnome-system-monitor/mem-swap.page
/usr/share/help/hu/gnome-system-monitor/memory-map-use.page
/usr/share/help/hu/gnome-system-monitor/net-bits.page
/usr/share/help/hu/gnome-system-monitor/process-explain.page
/usr/share/help/hu/gnome-system-monitor/process-files.page
/usr/share/help/hu/gnome-system-monitor/process-identify-file.page
/usr/share/help/hu/gnome-system-monitor/process-identify-hog.page
/usr/share/help/hu/gnome-system-monitor/process-kill.page
/usr/share/help/hu/gnome-system-monitor/process-many.page
/usr/share/help/hu/gnome-system-monitor/process-priority-change.page
/usr/share/help/hu/gnome-system-monitor/process-status.page
/usr/share/help/hu/gnome-system-monitor/process-update-speed.page
/usr/share/help/hu/gnome-system-monitor/solaris-mode.page
/usr/share/help/hu/gnome-system-monitor/units.page
/usr/share/help/ko/gnome-system-monitor/commandline.page
/usr/share/help/ko/gnome-system-monitor/cpu-check.page
/usr/share/help/ko/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/ko/gnome-system-monitor/cpu-multicore.page
/usr/share/help/ko/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/ko/gnome-system-monitor/fs-device.page
/usr/share/help/ko/gnome-system-monitor/fs-diskusage.page
/usr/share/help/ko/gnome-system-monitor/fs-info.page
/usr/share/help/ko/gnome-system-monitor/fs-showall.page
/usr/share/help/ko/gnome-system-monitor/index.page
/usr/share/help/ko/gnome-system-monitor/legal.xml
/usr/share/help/ko/gnome-system-monitor/mem-check.page
/usr/share/help/ko/gnome-system-monitor/mem-swap.page
/usr/share/help/ko/gnome-system-monitor/memory-map-use.page
/usr/share/help/ko/gnome-system-monitor/net-bits.page
/usr/share/help/ko/gnome-system-monitor/process-explain.page
/usr/share/help/ko/gnome-system-monitor/process-files.page
/usr/share/help/ko/gnome-system-monitor/process-identify-file.page
/usr/share/help/ko/gnome-system-monitor/process-identify-hog.page
/usr/share/help/ko/gnome-system-monitor/process-kill.page
/usr/share/help/ko/gnome-system-monitor/process-many.page
/usr/share/help/ko/gnome-system-monitor/process-priority-change.page
/usr/share/help/ko/gnome-system-monitor/process-status.page
/usr/share/help/ko/gnome-system-monitor/process-update-speed.page
/usr/share/help/ko/gnome-system-monitor/solaris-mode.page
/usr/share/help/ko/gnome-system-monitor/units.page
/usr/share/help/pl/gnome-system-monitor/commandline.page
/usr/share/help/pl/gnome-system-monitor/cpu-check.page
/usr/share/help/pl/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/pl/gnome-system-monitor/cpu-multicore.page
/usr/share/help/pl/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/pl/gnome-system-monitor/fs-device.page
/usr/share/help/pl/gnome-system-monitor/fs-diskusage.page
/usr/share/help/pl/gnome-system-monitor/fs-info.page
/usr/share/help/pl/gnome-system-monitor/fs-showall.page
/usr/share/help/pl/gnome-system-monitor/index.page
/usr/share/help/pl/gnome-system-monitor/legal.xml
/usr/share/help/pl/gnome-system-monitor/mem-check.page
/usr/share/help/pl/gnome-system-monitor/mem-swap.page
/usr/share/help/pl/gnome-system-monitor/memory-map-use.page
/usr/share/help/pl/gnome-system-monitor/net-bits.page
/usr/share/help/pl/gnome-system-monitor/process-explain.page
/usr/share/help/pl/gnome-system-monitor/process-files.page
/usr/share/help/pl/gnome-system-monitor/process-identify-file.page
/usr/share/help/pl/gnome-system-monitor/process-identify-hog.page
/usr/share/help/pl/gnome-system-monitor/process-kill.page
/usr/share/help/pl/gnome-system-monitor/process-many.page
/usr/share/help/pl/gnome-system-monitor/process-priority-change.page
/usr/share/help/pl/gnome-system-monitor/process-status.page
/usr/share/help/pl/gnome-system-monitor/process-update-speed.page
/usr/share/help/pl/gnome-system-monitor/solaris-mode.page
/usr/share/help/pl/gnome-system-monitor/units.page
/usr/share/help/pt/gnome-system-monitor/commandline.page
/usr/share/help/pt/gnome-system-monitor/cpu-check.page
/usr/share/help/pt/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/pt/gnome-system-monitor/cpu-multicore.page
/usr/share/help/pt/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/pt/gnome-system-monitor/fs-device.page
/usr/share/help/pt/gnome-system-monitor/fs-diskusage.page
/usr/share/help/pt/gnome-system-monitor/fs-info.page
/usr/share/help/pt/gnome-system-monitor/fs-showall.page
/usr/share/help/pt/gnome-system-monitor/index.page
/usr/share/help/pt/gnome-system-monitor/legal.xml
/usr/share/help/pt/gnome-system-monitor/mem-check.page
/usr/share/help/pt/gnome-system-monitor/mem-swap.page
/usr/share/help/pt/gnome-system-monitor/memory-map-use.page
/usr/share/help/pt/gnome-system-monitor/net-bits.page
/usr/share/help/pt/gnome-system-monitor/process-explain.page
/usr/share/help/pt/gnome-system-monitor/process-files.page
/usr/share/help/pt/gnome-system-monitor/process-identify-file.page
/usr/share/help/pt/gnome-system-monitor/process-identify-hog.page
/usr/share/help/pt/gnome-system-monitor/process-kill.page
/usr/share/help/pt/gnome-system-monitor/process-many.page
/usr/share/help/pt/gnome-system-monitor/process-priority-change.page
/usr/share/help/pt/gnome-system-monitor/process-status.page
/usr/share/help/pt/gnome-system-monitor/process-update-speed.page
/usr/share/help/pt/gnome-system-monitor/solaris-mode.page
/usr/share/help/pt/gnome-system-monitor/units.page
/usr/share/help/pt_BR/gnome-system-monitor/commandline.page
/usr/share/help/pt_BR/gnome-system-monitor/cpu-check.page
/usr/share/help/pt_BR/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/pt_BR/gnome-system-monitor/cpu-multicore.page
/usr/share/help/pt_BR/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/pt_BR/gnome-system-monitor/fs-device.page
/usr/share/help/pt_BR/gnome-system-monitor/fs-diskusage.page
/usr/share/help/pt_BR/gnome-system-monitor/fs-info.page
/usr/share/help/pt_BR/gnome-system-monitor/fs-showall.page
/usr/share/help/pt_BR/gnome-system-monitor/index.page
/usr/share/help/pt_BR/gnome-system-monitor/legal.xml
/usr/share/help/pt_BR/gnome-system-monitor/mem-check.page
/usr/share/help/pt_BR/gnome-system-monitor/mem-swap.page
/usr/share/help/pt_BR/gnome-system-monitor/memory-map-use.page
/usr/share/help/pt_BR/gnome-system-monitor/net-bits.page
/usr/share/help/pt_BR/gnome-system-monitor/process-explain.page
/usr/share/help/pt_BR/gnome-system-monitor/process-files.page
/usr/share/help/pt_BR/gnome-system-monitor/process-identify-file.page
/usr/share/help/pt_BR/gnome-system-monitor/process-identify-hog.page
/usr/share/help/pt_BR/gnome-system-monitor/process-kill.page
/usr/share/help/pt_BR/gnome-system-monitor/process-many.page
/usr/share/help/pt_BR/gnome-system-monitor/process-priority-change.page
/usr/share/help/pt_BR/gnome-system-monitor/process-status.page
/usr/share/help/pt_BR/gnome-system-monitor/process-update-speed.page
/usr/share/help/pt_BR/gnome-system-monitor/solaris-mode.page
/usr/share/help/pt_BR/gnome-system-monitor/units.page
/usr/share/help/ro/gnome-system-monitor/commandline.page
/usr/share/help/ro/gnome-system-monitor/cpu-check.page
/usr/share/help/ro/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/ro/gnome-system-monitor/cpu-multicore.page
/usr/share/help/ro/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/ro/gnome-system-monitor/fs-device.page
/usr/share/help/ro/gnome-system-monitor/fs-diskusage.page
/usr/share/help/ro/gnome-system-monitor/fs-info.page
/usr/share/help/ro/gnome-system-monitor/fs-showall.page
/usr/share/help/ro/gnome-system-monitor/index.page
/usr/share/help/ro/gnome-system-monitor/legal.xml
/usr/share/help/ro/gnome-system-monitor/mem-check.page
/usr/share/help/ro/gnome-system-monitor/mem-swap.page
/usr/share/help/ro/gnome-system-monitor/memory-map-use.page
/usr/share/help/ro/gnome-system-monitor/net-bits.page
/usr/share/help/ro/gnome-system-monitor/process-explain.page
/usr/share/help/ro/gnome-system-monitor/process-files.page
/usr/share/help/ro/gnome-system-monitor/process-identify-file.page
/usr/share/help/ro/gnome-system-monitor/process-identify-hog.page
/usr/share/help/ro/gnome-system-monitor/process-kill.page
/usr/share/help/ro/gnome-system-monitor/process-many.page
/usr/share/help/ro/gnome-system-monitor/process-priority-change.page
/usr/share/help/ro/gnome-system-monitor/process-status.page
/usr/share/help/ro/gnome-system-monitor/process-update-speed.page
/usr/share/help/ro/gnome-system-monitor/solaris-mode.page
/usr/share/help/ro/gnome-system-monitor/units.page
/usr/share/help/sv/gnome-system-monitor/commandline.page
/usr/share/help/sv/gnome-system-monitor/cpu-check.page
/usr/share/help/sv/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/sv/gnome-system-monitor/cpu-multicore.page
/usr/share/help/sv/gnome-system-monitor/figures/monitorlogo.png
/usr/share/help/sv/gnome-system-monitor/fs-device.page
/usr/share/help/sv/gnome-system-monitor/fs-diskusage.page
/usr/share/help/sv/gnome-system-monitor/fs-info.page
/usr/share/help/sv/gnome-system-monitor/fs-showall.page
/usr/share/help/sv/gnome-system-monitor/index.page
/usr/share/help/sv/gnome-system-monitor/legal.xml
/usr/share/help/sv/gnome-system-monitor/mem-check.page
/usr/share/help/sv/gnome-system-monitor/mem-swap.page
/usr/share/help/sv/gnome-system-monitor/memory-map-use.page
/usr/share/help/sv/gnome-system-monitor/net-bits.page
/usr/share/help/sv/gnome-system-monitor/process-explain.page
/usr/share/help/sv/gnome-system-monitor/process-files.page
/usr/share/help/sv/gnome-system-monitor/process-identify-file.page
/usr/share/help/sv/gnome-system-monitor/process-identify-hog.page
/usr/share/help/sv/gnome-system-monitor/process-kill.page
/usr/share/help/sv/gnome-system-monitor/process-many.page
/usr/share/help/sv/gnome-system-monitor/process-priority-change.page
/usr/share/help/sv/gnome-system-monitor/process-status.page
/usr/share/help/sv/gnome-system-monitor/process-update-speed.page
/usr/share/help/sv/gnome-system-monitor/solaris-mode.page
/usr/share/help/sv/gnome-system-monitor/units.page

%files license
%defattr(-,root,root,-)
/usr/share/doc/gnome-system-monitor/COPYING

%files locales -f gnome-system-monitor.lang
%defattr(-,root,root,-)

