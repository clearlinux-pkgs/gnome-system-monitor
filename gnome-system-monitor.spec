#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-system-monitor
Version  : 42.0
Release  : 20
URL      : https://download.gnome.org/sources/gnome-system-monitor/42/gnome-system-monitor-42.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-system-monitor/42/gnome-system-monitor-42.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-system-monitor-bin = %{version}-%{release}
Requires: gnome-system-monitor-data = %{version}-%{release}
Requires: gnome-system-monitor-libexec = %{version}-%{release}
Requires: gnome-system-monitor-license = %{version}-%{release}
Requires: gnome-system-monitor-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : glibmm-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : gtkmm3-dev
BuildRequires : librsvg-dev
BuildRequires : pkgconfig(giomm-2.4)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(libgtop-2.0)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(librsvg-2.0)

%description
# System Monitor
GNOME System Monitor is a GNOME process viewer and system monitor with an attractive,
easy-to-use interface, It has features, such as a tree view for process dependencies,
icons for processes, the ability to hide processes that you don't want to see,
graphical time histories of CPU/memory/swap usage,
the ability to kill/renice processes needing root access,
as well as the standard features that you might expect from a process viewer.

%package bin
Summary: bin components for the gnome-system-monitor package.
Group: Binaries
Requires: gnome-system-monitor-data = %{version}-%{release}
Requires: gnome-system-monitor-libexec = %{version}-%{release}
Requires: gnome-system-monitor-license = %{version}-%{release}

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


%package libexec
Summary: libexec components for the gnome-system-monitor package.
Group: Default
Requires: gnome-system-monitor-license = %{version}-%{release}

%description libexec
libexec components for the gnome-system-monitor package.


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
%setup -q -n gnome-system-monitor-42.0
cd %{_builddir}/gnome-system-monitor-42.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647724752
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-system-monitor
cp %{_builddir}/gnome-system-monitor-42.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-system-monitor/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-system-monitor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-system-monitor

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-system-monitor-kde.desktop
/usr/share/applications/gnome-system-monitor.desktop
/usr/share/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
/usr/share/gnome-system-monitor/gsm.gresource
/usr/share/icons/hicolor/scalable/apps/org.gnome.SystemMonitor.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.SystemMonitor.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.SystemMonitor-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/speedometer-symbolic.svg
/usr/share/metainfo/gnome-system-monitor.appdata.xml
/usr/share/polkit-1/actions/org.gnome.gnome-system-monitor.policy

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-system-monitor/commandline.page
/usr/share/help/C/gnome-system-monitor/cpu-check.page
/usr/share/help/C/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/C/gnome-system-monitor/cpu-multicore.page
/usr/share/help/C/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/C/gnome-system-monitor/fs-device.page
/usr/share/help/C/gnome-system-monitor/fs-diskusage.page
/usr/share/help/C/gnome-system-monitor/fs-info.page
/usr/share/help/C/gnome-system-monitor/fs-showall.page
/usr/share/help/C/gnome-system-monitor/index.page
/usr/share/help/C/gnome-system-monitor/legal.xml
/usr/share/help/C/gnome-system-monitor/mem-check.page
/usr/share/help/C/gnome-system-monitor/mem-swap.page
/usr/share/help/C/gnome-system-monitor/memory-map-use.page
/usr/share/help/C/gnome-system-monitor/memory-map-what.page
/usr/share/help/C/gnome-system-monitor/net-bits.page
/usr/share/help/C/gnome-system-monitor/process-explain.page
/usr/share/help/C/gnome-system-monitor/process-files.page
/usr/share/help/C/gnome-system-monitor/process-identify-file.page
/usr/share/help/C/gnome-system-monitor/process-identify-hog.page
/usr/share/help/C/gnome-system-monitor/process-kill.page
/usr/share/help/C/gnome-system-monitor/process-many.page
/usr/share/help/C/gnome-system-monitor/process-priority-change.page
/usr/share/help/C/gnome-system-monitor/process-priority-what.page
/usr/share/help/C/gnome-system-monitor/process-status.page
/usr/share/help/C/gnome-system-monitor/process-update-speed.page
/usr/share/help/C/gnome-system-monitor/solaris-mode.page
/usr/share/help/C/gnome-system-monitor/units.page
/usr/share/help/ca/gnome-system-monitor/commandline.page
/usr/share/help/ca/gnome-system-monitor/cpu-check.page
/usr/share/help/ca/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/ca/gnome-system-monitor/cpu-multicore.page
/usr/share/help/ca/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/ca/gnome-system-monitor/fs-device.page
/usr/share/help/ca/gnome-system-monitor/fs-diskusage.page
/usr/share/help/ca/gnome-system-monitor/fs-info.page
/usr/share/help/ca/gnome-system-monitor/fs-showall.page
/usr/share/help/ca/gnome-system-monitor/index.page
/usr/share/help/ca/gnome-system-monitor/legal.xml
/usr/share/help/ca/gnome-system-monitor/mem-check.page
/usr/share/help/ca/gnome-system-monitor/mem-swap.page
/usr/share/help/ca/gnome-system-monitor/memory-map-use.page
/usr/share/help/ca/gnome-system-monitor/memory-map-what.page
/usr/share/help/ca/gnome-system-monitor/net-bits.page
/usr/share/help/ca/gnome-system-monitor/process-explain.page
/usr/share/help/ca/gnome-system-monitor/process-files.page
/usr/share/help/ca/gnome-system-monitor/process-identify-file.page
/usr/share/help/ca/gnome-system-monitor/process-identify-hog.page
/usr/share/help/ca/gnome-system-monitor/process-kill.page
/usr/share/help/ca/gnome-system-monitor/process-many.page
/usr/share/help/ca/gnome-system-monitor/process-priority-change.page
/usr/share/help/ca/gnome-system-monitor/process-priority-what.page
/usr/share/help/ca/gnome-system-monitor/process-status.page
/usr/share/help/ca/gnome-system-monitor/process-update-speed.page
/usr/share/help/ca/gnome-system-monitor/solaris-mode.page
/usr/share/help/ca/gnome-system-monitor/units.page
/usr/share/help/cs/gnome-system-monitor/commandline.page
/usr/share/help/cs/gnome-system-monitor/cpu-check.page
/usr/share/help/cs/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/cs/gnome-system-monitor/cpu-multicore.page
/usr/share/help/cs/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/cs/gnome-system-monitor/fs-device.page
/usr/share/help/cs/gnome-system-monitor/fs-diskusage.page
/usr/share/help/cs/gnome-system-monitor/fs-info.page
/usr/share/help/cs/gnome-system-monitor/fs-showall.page
/usr/share/help/cs/gnome-system-monitor/index.page
/usr/share/help/cs/gnome-system-monitor/legal.xml
/usr/share/help/cs/gnome-system-monitor/mem-check.page
/usr/share/help/cs/gnome-system-monitor/mem-swap.page
/usr/share/help/cs/gnome-system-monitor/memory-map-use.page
/usr/share/help/cs/gnome-system-monitor/memory-map-what.page
/usr/share/help/cs/gnome-system-monitor/net-bits.page
/usr/share/help/cs/gnome-system-monitor/process-explain.page
/usr/share/help/cs/gnome-system-monitor/process-files.page
/usr/share/help/cs/gnome-system-monitor/process-identify-file.page
/usr/share/help/cs/gnome-system-monitor/process-identify-hog.page
/usr/share/help/cs/gnome-system-monitor/process-kill.page
/usr/share/help/cs/gnome-system-monitor/process-many.page
/usr/share/help/cs/gnome-system-monitor/process-priority-change.page
/usr/share/help/cs/gnome-system-monitor/process-priority-what.page
/usr/share/help/cs/gnome-system-monitor/process-status.page
/usr/share/help/cs/gnome-system-monitor/process-update-speed.page
/usr/share/help/cs/gnome-system-monitor/solaris-mode.page
/usr/share/help/cs/gnome-system-monitor/units.page
/usr/share/help/da/gnome-system-monitor/commandline.page
/usr/share/help/da/gnome-system-monitor/cpu-check.page
/usr/share/help/da/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/da/gnome-system-monitor/cpu-multicore.page
/usr/share/help/da/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/da/gnome-system-monitor/fs-device.page
/usr/share/help/da/gnome-system-monitor/fs-diskusage.page
/usr/share/help/da/gnome-system-monitor/fs-info.page
/usr/share/help/da/gnome-system-monitor/fs-showall.page
/usr/share/help/da/gnome-system-monitor/index.page
/usr/share/help/da/gnome-system-monitor/legal.xml
/usr/share/help/da/gnome-system-monitor/mem-check.page
/usr/share/help/da/gnome-system-monitor/mem-swap.page
/usr/share/help/da/gnome-system-monitor/memory-map-use.page
/usr/share/help/da/gnome-system-monitor/memory-map-what.page
/usr/share/help/da/gnome-system-monitor/net-bits.page
/usr/share/help/da/gnome-system-monitor/process-explain.page
/usr/share/help/da/gnome-system-monitor/process-files.page
/usr/share/help/da/gnome-system-monitor/process-identify-file.page
/usr/share/help/da/gnome-system-monitor/process-identify-hog.page
/usr/share/help/da/gnome-system-monitor/process-kill.page
/usr/share/help/da/gnome-system-monitor/process-many.page
/usr/share/help/da/gnome-system-monitor/process-priority-change.page
/usr/share/help/da/gnome-system-monitor/process-priority-what.page
/usr/share/help/da/gnome-system-monitor/process-status.page
/usr/share/help/da/gnome-system-monitor/process-update-speed.page
/usr/share/help/da/gnome-system-monitor/solaris-mode.page
/usr/share/help/da/gnome-system-monitor/units.page
/usr/share/help/de/gnome-system-monitor/commandline.page
/usr/share/help/de/gnome-system-monitor/cpu-check.page
/usr/share/help/de/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/de/gnome-system-monitor/cpu-multicore.page
/usr/share/help/de/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/de/gnome-system-monitor/fs-device.page
/usr/share/help/de/gnome-system-monitor/fs-diskusage.page
/usr/share/help/de/gnome-system-monitor/fs-info.page
/usr/share/help/de/gnome-system-monitor/fs-showall.page
/usr/share/help/de/gnome-system-monitor/index.page
/usr/share/help/de/gnome-system-monitor/legal.xml
/usr/share/help/de/gnome-system-monitor/mem-check.page
/usr/share/help/de/gnome-system-monitor/mem-swap.page
/usr/share/help/de/gnome-system-monitor/memory-map-use.page
/usr/share/help/de/gnome-system-monitor/memory-map-what.page
/usr/share/help/de/gnome-system-monitor/net-bits.page
/usr/share/help/de/gnome-system-monitor/process-explain.page
/usr/share/help/de/gnome-system-monitor/process-files.page
/usr/share/help/de/gnome-system-monitor/process-identify-file.page
/usr/share/help/de/gnome-system-monitor/process-identify-hog.page
/usr/share/help/de/gnome-system-monitor/process-kill.page
/usr/share/help/de/gnome-system-monitor/process-many.page
/usr/share/help/de/gnome-system-monitor/process-priority-change.page
/usr/share/help/de/gnome-system-monitor/process-priority-what.page
/usr/share/help/de/gnome-system-monitor/process-status.page
/usr/share/help/de/gnome-system-monitor/process-update-speed.page
/usr/share/help/de/gnome-system-monitor/solaris-mode.page
/usr/share/help/de/gnome-system-monitor/units.page
/usr/share/help/el/gnome-system-monitor/commandline.page
/usr/share/help/el/gnome-system-monitor/cpu-check.page
/usr/share/help/el/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/el/gnome-system-monitor/cpu-multicore.page
/usr/share/help/el/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/el/gnome-system-monitor/fs-device.page
/usr/share/help/el/gnome-system-monitor/fs-diskusage.page
/usr/share/help/el/gnome-system-monitor/fs-info.page
/usr/share/help/el/gnome-system-monitor/fs-showall.page
/usr/share/help/el/gnome-system-monitor/index.page
/usr/share/help/el/gnome-system-monitor/legal.xml
/usr/share/help/el/gnome-system-monitor/mem-check.page
/usr/share/help/el/gnome-system-monitor/mem-swap.page
/usr/share/help/el/gnome-system-monitor/memory-map-use.page
/usr/share/help/el/gnome-system-monitor/memory-map-what.page
/usr/share/help/el/gnome-system-monitor/net-bits.page
/usr/share/help/el/gnome-system-monitor/process-explain.page
/usr/share/help/el/gnome-system-monitor/process-files.page
/usr/share/help/el/gnome-system-monitor/process-identify-file.page
/usr/share/help/el/gnome-system-monitor/process-identify-hog.page
/usr/share/help/el/gnome-system-monitor/process-kill.page
/usr/share/help/el/gnome-system-monitor/process-many.page
/usr/share/help/el/gnome-system-monitor/process-priority-change.page
/usr/share/help/el/gnome-system-monitor/process-priority-what.page
/usr/share/help/el/gnome-system-monitor/process-status.page
/usr/share/help/el/gnome-system-monitor/process-update-speed.page
/usr/share/help/el/gnome-system-monitor/solaris-mode.page
/usr/share/help/el/gnome-system-monitor/units.page
/usr/share/help/es/gnome-system-monitor/commandline.page
/usr/share/help/es/gnome-system-monitor/cpu-check.page
/usr/share/help/es/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/es/gnome-system-monitor/cpu-multicore.page
/usr/share/help/es/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/es/gnome-system-monitor/fs-device.page
/usr/share/help/es/gnome-system-monitor/fs-diskusage.page
/usr/share/help/es/gnome-system-monitor/fs-info.page
/usr/share/help/es/gnome-system-monitor/fs-showall.page
/usr/share/help/es/gnome-system-monitor/index.page
/usr/share/help/es/gnome-system-monitor/legal.xml
/usr/share/help/es/gnome-system-monitor/mem-check.page
/usr/share/help/es/gnome-system-monitor/mem-swap.page
/usr/share/help/es/gnome-system-monitor/memory-map-use.page
/usr/share/help/es/gnome-system-monitor/memory-map-what.page
/usr/share/help/es/gnome-system-monitor/net-bits.page
/usr/share/help/es/gnome-system-monitor/process-explain.page
/usr/share/help/es/gnome-system-monitor/process-files.page
/usr/share/help/es/gnome-system-monitor/process-identify-file.page
/usr/share/help/es/gnome-system-monitor/process-identify-hog.page
/usr/share/help/es/gnome-system-monitor/process-kill.page
/usr/share/help/es/gnome-system-monitor/process-many.page
/usr/share/help/es/gnome-system-monitor/process-priority-change.page
/usr/share/help/es/gnome-system-monitor/process-priority-what.page
/usr/share/help/es/gnome-system-monitor/process-status.page
/usr/share/help/es/gnome-system-monitor/process-update-speed.page
/usr/share/help/es/gnome-system-monitor/solaris-mode.page
/usr/share/help/es/gnome-system-monitor/units.page
/usr/share/help/eu/gnome-system-monitor/commandline.page
/usr/share/help/eu/gnome-system-monitor/cpu-check.page
/usr/share/help/eu/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/eu/gnome-system-monitor/cpu-multicore.page
/usr/share/help/eu/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/eu/gnome-system-monitor/fs-device.page
/usr/share/help/eu/gnome-system-monitor/fs-diskusage.page
/usr/share/help/eu/gnome-system-monitor/fs-info.page
/usr/share/help/eu/gnome-system-monitor/fs-showall.page
/usr/share/help/eu/gnome-system-monitor/index.page
/usr/share/help/eu/gnome-system-monitor/legal.xml
/usr/share/help/eu/gnome-system-monitor/mem-check.page
/usr/share/help/eu/gnome-system-monitor/mem-swap.page
/usr/share/help/eu/gnome-system-monitor/memory-map-use.page
/usr/share/help/eu/gnome-system-monitor/memory-map-what.page
/usr/share/help/eu/gnome-system-monitor/net-bits.page
/usr/share/help/eu/gnome-system-monitor/process-explain.page
/usr/share/help/eu/gnome-system-monitor/process-files.page
/usr/share/help/eu/gnome-system-monitor/process-identify-file.page
/usr/share/help/eu/gnome-system-monitor/process-identify-hog.page
/usr/share/help/eu/gnome-system-monitor/process-kill.page
/usr/share/help/eu/gnome-system-monitor/process-many.page
/usr/share/help/eu/gnome-system-monitor/process-priority-change.page
/usr/share/help/eu/gnome-system-monitor/process-priority-what.page
/usr/share/help/eu/gnome-system-monitor/process-status.page
/usr/share/help/eu/gnome-system-monitor/process-update-speed.page
/usr/share/help/eu/gnome-system-monitor/solaris-mode.page
/usr/share/help/eu/gnome-system-monitor/units.page
/usr/share/help/fr/gnome-system-monitor/commandline.page
/usr/share/help/fr/gnome-system-monitor/cpu-check.page
/usr/share/help/fr/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/fr/gnome-system-monitor/cpu-multicore.page
/usr/share/help/fr/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/fr/gnome-system-monitor/fs-device.page
/usr/share/help/fr/gnome-system-monitor/fs-diskusage.page
/usr/share/help/fr/gnome-system-monitor/fs-info.page
/usr/share/help/fr/gnome-system-monitor/fs-showall.page
/usr/share/help/fr/gnome-system-monitor/index.page
/usr/share/help/fr/gnome-system-monitor/legal.xml
/usr/share/help/fr/gnome-system-monitor/mem-check.page
/usr/share/help/fr/gnome-system-monitor/mem-swap.page
/usr/share/help/fr/gnome-system-monitor/memory-map-use.page
/usr/share/help/fr/gnome-system-monitor/memory-map-what.page
/usr/share/help/fr/gnome-system-monitor/net-bits.page
/usr/share/help/fr/gnome-system-monitor/process-explain.page
/usr/share/help/fr/gnome-system-monitor/process-files.page
/usr/share/help/fr/gnome-system-monitor/process-identify-file.page
/usr/share/help/fr/gnome-system-monitor/process-identify-hog.page
/usr/share/help/fr/gnome-system-monitor/process-kill.page
/usr/share/help/fr/gnome-system-monitor/process-many.page
/usr/share/help/fr/gnome-system-monitor/process-priority-change.page
/usr/share/help/fr/gnome-system-monitor/process-priority-what.page
/usr/share/help/fr/gnome-system-monitor/process-status.page
/usr/share/help/fr/gnome-system-monitor/process-update-speed.page
/usr/share/help/fr/gnome-system-monitor/solaris-mode.page
/usr/share/help/fr/gnome-system-monitor/units.page
/usr/share/help/gl/gnome-system-monitor/commandline.page
/usr/share/help/gl/gnome-system-monitor/cpu-check.page
/usr/share/help/gl/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/gl/gnome-system-monitor/cpu-multicore.page
/usr/share/help/gl/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/gl/gnome-system-monitor/fs-device.page
/usr/share/help/gl/gnome-system-monitor/fs-diskusage.page
/usr/share/help/gl/gnome-system-monitor/fs-info.page
/usr/share/help/gl/gnome-system-monitor/fs-showall.page
/usr/share/help/gl/gnome-system-monitor/index.page
/usr/share/help/gl/gnome-system-monitor/legal.xml
/usr/share/help/gl/gnome-system-monitor/mem-check.page
/usr/share/help/gl/gnome-system-monitor/mem-swap.page
/usr/share/help/gl/gnome-system-monitor/memory-map-use.page
/usr/share/help/gl/gnome-system-monitor/memory-map-what.page
/usr/share/help/gl/gnome-system-monitor/net-bits.page
/usr/share/help/gl/gnome-system-monitor/process-explain.page
/usr/share/help/gl/gnome-system-monitor/process-files.page
/usr/share/help/gl/gnome-system-monitor/process-identify-file.page
/usr/share/help/gl/gnome-system-monitor/process-identify-hog.page
/usr/share/help/gl/gnome-system-monitor/process-kill.page
/usr/share/help/gl/gnome-system-monitor/process-many.page
/usr/share/help/gl/gnome-system-monitor/process-priority-change.page
/usr/share/help/gl/gnome-system-monitor/process-priority-what.page
/usr/share/help/gl/gnome-system-monitor/process-status.page
/usr/share/help/gl/gnome-system-monitor/process-update-speed.page
/usr/share/help/gl/gnome-system-monitor/solaris-mode.page
/usr/share/help/gl/gnome-system-monitor/units.page
/usr/share/help/hu/gnome-system-monitor/commandline.page
/usr/share/help/hu/gnome-system-monitor/cpu-check.page
/usr/share/help/hu/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/hu/gnome-system-monitor/cpu-multicore.page
/usr/share/help/hu/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/hu/gnome-system-monitor/fs-device.page
/usr/share/help/hu/gnome-system-monitor/fs-diskusage.page
/usr/share/help/hu/gnome-system-monitor/fs-info.page
/usr/share/help/hu/gnome-system-monitor/fs-showall.page
/usr/share/help/hu/gnome-system-monitor/index.page
/usr/share/help/hu/gnome-system-monitor/legal.xml
/usr/share/help/hu/gnome-system-monitor/mem-check.page
/usr/share/help/hu/gnome-system-monitor/mem-swap.page
/usr/share/help/hu/gnome-system-monitor/memory-map-use.page
/usr/share/help/hu/gnome-system-monitor/memory-map-what.page
/usr/share/help/hu/gnome-system-monitor/net-bits.page
/usr/share/help/hu/gnome-system-monitor/process-explain.page
/usr/share/help/hu/gnome-system-monitor/process-files.page
/usr/share/help/hu/gnome-system-monitor/process-identify-file.page
/usr/share/help/hu/gnome-system-monitor/process-identify-hog.page
/usr/share/help/hu/gnome-system-monitor/process-kill.page
/usr/share/help/hu/gnome-system-monitor/process-many.page
/usr/share/help/hu/gnome-system-monitor/process-priority-change.page
/usr/share/help/hu/gnome-system-monitor/process-priority-what.page
/usr/share/help/hu/gnome-system-monitor/process-status.page
/usr/share/help/hu/gnome-system-monitor/process-update-speed.page
/usr/share/help/hu/gnome-system-monitor/solaris-mode.page
/usr/share/help/hu/gnome-system-monitor/units.page
/usr/share/help/id/gnome-system-monitor/commandline.page
/usr/share/help/id/gnome-system-monitor/cpu-check.page
/usr/share/help/id/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/id/gnome-system-monitor/cpu-multicore.page
/usr/share/help/id/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/id/gnome-system-monitor/fs-device.page
/usr/share/help/id/gnome-system-monitor/fs-diskusage.page
/usr/share/help/id/gnome-system-monitor/fs-info.page
/usr/share/help/id/gnome-system-monitor/fs-showall.page
/usr/share/help/id/gnome-system-monitor/index.page
/usr/share/help/id/gnome-system-monitor/legal.xml
/usr/share/help/id/gnome-system-monitor/mem-check.page
/usr/share/help/id/gnome-system-monitor/mem-swap.page
/usr/share/help/id/gnome-system-monitor/memory-map-use.page
/usr/share/help/id/gnome-system-monitor/memory-map-what.page
/usr/share/help/id/gnome-system-monitor/net-bits.page
/usr/share/help/id/gnome-system-monitor/process-explain.page
/usr/share/help/id/gnome-system-monitor/process-files.page
/usr/share/help/id/gnome-system-monitor/process-identify-file.page
/usr/share/help/id/gnome-system-monitor/process-identify-hog.page
/usr/share/help/id/gnome-system-monitor/process-kill.page
/usr/share/help/id/gnome-system-monitor/process-many.page
/usr/share/help/id/gnome-system-monitor/process-priority-change.page
/usr/share/help/id/gnome-system-monitor/process-priority-what.page
/usr/share/help/id/gnome-system-monitor/process-status.page
/usr/share/help/id/gnome-system-monitor/process-update-speed.page
/usr/share/help/id/gnome-system-monitor/solaris-mode.page
/usr/share/help/id/gnome-system-monitor/units.page
/usr/share/help/ko/gnome-system-monitor/commandline.page
/usr/share/help/ko/gnome-system-monitor/cpu-check.page
/usr/share/help/ko/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/ko/gnome-system-monitor/cpu-multicore.page
/usr/share/help/ko/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/ko/gnome-system-monitor/fs-device.page
/usr/share/help/ko/gnome-system-monitor/fs-diskusage.page
/usr/share/help/ko/gnome-system-monitor/fs-info.page
/usr/share/help/ko/gnome-system-monitor/fs-showall.page
/usr/share/help/ko/gnome-system-monitor/index.page
/usr/share/help/ko/gnome-system-monitor/legal.xml
/usr/share/help/ko/gnome-system-monitor/mem-check.page
/usr/share/help/ko/gnome-system-monitor/mem-swap.page
/usr/share/help/ko/gnome-system-monitor/memory-map-use.page
/usr/share/help/ko/gnome-system-monitor/memory-map-what.page
/usr/share/help/ko/gnome-system-monitor/net-bits.page
/usr/share/help/ko/gnome-system-monitor/process-explain.page
/usr/share/help/ko/gnome-system-monitor/process-files.page
/usr/share/help/ko/gnome-system-monitor/process-identify-file.page
/usr/share/help/ko/gnome-system-monitor/process-identify-hog.page
/usr/share/help/ko/gnome-system-monitor/process-kill.page
/usr/share/help/ko/gnome-system-monitor/process-many.page
/usr/share/help/ko/gnome-system-monitor/process-priority-change.page
/usr/share/help/ko/gnome-system-monitor/process-priority-what.page
/usr/share/help/ko/gnome-system-monitor/process-status.page
/usr/share/help/ko/gnome-system-monitor/process-update-speed.page
/usr/share/help/ko/gnome-system-monitor/solaris-mode.page
/usr/share/help/ko/gnome-system-monitor/units.page
/usr/share/help/pl/gnome-system-monitor/commandline.page
/usr/share/help/pl/gnome-system-monitor/cpu-check.page
/usr/share/help/pl/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/pl/gnome-system-monitor/cpu-multicore.page
/usr/share/help/pl/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/pl/gnome-system-monitor/fs-device.page
/usr/share/help/pl/gnome-system-monitor/fs-diskusage.page
/usr/share/help/pl/gnome-system-monitor/fs-info.page
/usr/share/help/pl/gnome-system-monitor/fs-showall.page
/usr/share/help/pl/gnome-system-monitor/index.page
/usr/share/help/pl/gnome-system-monitor/legal.xml
/usr/share/help/pl/gnome-system-monitor/mem-check.page
/usr/share/help/pl/gnome-system-monitor/mem-swap.page
/usr/share/help/pl/gnome-system-monitor/memory-map-use.page
/usr/share/help/pl/gnome-system-monitor/memory-map-what.page
/usr/share/help/pl/gnome-system-monitor/net-bits.page
/usr/share/help/pl/gnome-system-monitor/process-explain.page
/usr/share/help/pl/gnome-system-monitor/process-files.page
/usr/share/help/pl/gnome-system-monitor/process-identify-file.page
/usr/share/help/pl/gnome-system-monitor/process-identify-hog.page
/usr/share/help/pl/gnome-system-monitor/process-kill.page
/usr/share/help/pl/gnome-system-monitor/process-many.page
/usr/share/help/pl/gnome-system-monitor/process-priority-change.page
/usr/share/help/pl/gnome-system-monitor/process-priority-what.page
/usr/share/help/pl/gnome-system-monitor/process-status.page
/usr/share/help/pl/gnome-system-monitor/process-update-speed.page
/usr/share/help/pl/gnome-system-monitor/solaris-mode.page
/usr/share/help/pl/gnome-system-monitor/units.page
/usr/share/help/pt/gnome-system-monitor/commandline.page
/usr/share/help/pt/gnome-system-monitor/cpu-check.page
/usr/share/help/pt/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/pt/gnome-system-monitor/cpu-multicore.page
/usr/share/help/pt/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/pt/gnome-system-monitor/fs-device.page
/usr/share/help/pt/gnome-system-monitor/fs-diskusage.page
/usr/share/help/pt/gnome-system-monitor/fs-info.page
/usr/share/help/pt/gnome-system-monitor/fs-showall.page
/usr/share/help/pt/gnome-system-monitor/index.page
/usr/share/help/pt/gnome-system-monitor/legal.xml
/usr/share/help/pt/gnome-system-monitor/mem-check.page
/usr/share/help/pt/gnome-system-monitor/mem-swap.page
/usr/share/help/pt/gnome-system-monitor/memory-map-use.page
/usr/share/help/pt/gnome-system-monitor/memory-map-what.page
/usr/share/help/pt/gnome-system-monitor/net-bits.page
/usr/share/help/pt/gnome-system-monitor/process-explain.page
/usr/share/help/pt/gnome-system-monitor/process-files.page
/usr/share/help/pt/gnome-system-monitor/process-identify-file.page
/usr/share/help/pt/gnome-system-monitor/process-identify-hog.page
/usr/share/help/pt/gnome-system-monitor/process-kill.page
/usr/share/help/pt/gnome-system-monitor/process-many.page
/usr/share/help/pt/gnome-system-monitor/process-priority-change.page
/usr/share/help/pt/gnome-system-monitor/process-priority-what.page
/usr/share/help/pt/gnome-system-monitor/process-status.page
/usr/share/help/pt/gnome-system-monitor/process-update-speed.page
/usr/share/help/pt/gnome-system-monitor/solaris-mode.page
/usr/share/help/pt/gnome-system-monitor/units.page
/usr/share/help/pt_BR/gnome-system-monitor/commandline.page
/usr/share/help/pt_BR/gnome-system-monitor/cpu-check.page
/usr/share/help/pt_BR/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/pt_BR/gnome-system-monitor/cpu-multicore.page
/usr/share/help/pt_BR/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/pt_BR/gnome-system-monitor/fs-device.page
/usr/share/help/pt_BR/gnome-system-monitor/fs-diskusage.page
/usr/share/help/pt_BR/gnome-system-monitor/fs-info.page
/usr/share/help/pt_BR/gnome-system-monitor/fs-showall.page
/usr/share/help/pt_BR/gnome-system-monitor/index.page
/usr/share/help/pt_BR/gnome-system-monitor/legal.xml
/usr/share/help/pt_BR/gnome-system-monitor/mem-check.page
/usr/share/help/pt_BR/gnome-system-monitor/mem-swap.page
/usr/share/help/pt_BR/gnome-system-monitor/memory-map-use.page
/usr/share/help/pt_BR/gnome-system-monitor/memory-map-what.page
/usr/share/help/pt_BR/gnome-system-monitor/net-bits.page
/usr/share/help/pt_BR/gnome-system-monitor/process-explain.page
/usr/share/help/pt_BR/gnome-system-monitor/process-files.page
/usr/share/help/pt_BR/gnome-system-monitor/process-identify-file.page
/usr/share/help/pt_BR/gnome-system-monitor/process-identify-hog.page
/usr/share/help/pt_BR/gnome-system-monitor/process-kill.page
/usr/share/help/pt_BR/gnome-system-monitor/process-many.page
/usr/share/help/pt_BR/gnome-system-monitor/process-priority-change.page
/usr/share/help/pt_BR/gnome-system-monitor/process-priority-what.page
/usr/share/help/pt_BR/gnome-system-monitor/process-status.page
/usr/share/help/pt_BR/gnome-system-monitor/process-update-speed.page
/usr/share/help/pt_BR/gnome-system-monitor/solaris-mode.page
/usr/share/help/pt_BR/gnome-system-monitor/units.page
/usr/share/help/ro/gnome-system-monitor/commandline.page
/usr/share/help/ro/gnome-system-monitor/cpu-check.page
/usr/share/help/ro/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/ro/gnome-system-monitor/cpu-multicore.page
/usr/share/help/ro/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/ro/gnome-system-monitor/fs-device.page
/usr/share/help/ro/gnome-system-monitor/fs-diskusage.page
/usr/share/help/ro/gnome-system-monitor/fs-info.page
/usr/share/help/ro/gnome-system-monitor/fs-showall.page
/usr/share/help/ro/gnome-system-monitor/index.page
/usr/share/help/ro/gnome-system-monitor/legal.xml
/usr/share/help/ro/gnome-system-monitor/mem-check.page
/usr/share/help/ro/gnome-system-monitor/mem-swap.page
/usr/share/help/ro/gnome-system-monitor/memory-map-use.page
/usr/share/help/ro/gnome-system-monitor/memory-map-what.page
/usr/share/help/ro/gnome-system-monitor/net-bits.page
/usr/share/help/ro/gnome-system-monitor/process-explain.page
/usr/share/help/ro/gnome-system-monitor/process-files.page
/usr/share/help/ro/gnome-system-monitor/process-identify-file.page
/usr/share/help/ro/gnome-system-monitor/process-identify-hog.page
/usr/share/help/ro/gnome-system-monitor/process-kill.page
/usr/share/help/ro/gnome-system-monitor/process-many.page
/usr/share/help/ro/gnome-system-monitor/process-priority-change.page
/usr/share/help/ro/gnome-system-monitor/process-priority-what.page
/usr/share/help/ro/gnome-system-monitor/process-status.page
/usr/share/help/ro/gnome-system-monitor/process-update-speed.page
/usr/share/help/ro/gnome-system-monitor/solaris-mode.page
/usr/share/help/ro/gnome-system-monitor/units.page
/usr/share/help/ru/gnome-system-monitor/commandline.page
/usr/share/help/ru/gnome-system-monitor/cpu-check.page
/usr/share/help/ru/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/ru/gnome-system-monitor/cpu-multicore.page
/usr/share/help/ru/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/ru/gnome-system-monitor/fs-device.page
/usr/share/help/ru/gnome-system-monitor/fs-diskusage.page
/usr/share/help/ru/gnome-system-monitor/fs-info.page
/usr/share/help/ru/gnome-system-monitor/fs-showall.page
/usr/share/help/ru/gnome-system-monitor/index.page
/usr/share/help/ru/gnome-system-monitor/legal.xml
/usr/share/help/ru/gnome-system-monitor/mem-check.page
/usr/share/help/ru/gnome-system-monitor/mem-swap.page
/usr/share/help/ru/gnome-system-monitor/memory-map-use.page
/usr/share/help/ru/gnome-system-monitor/memory-map-what.page
/usr/share/help/ru/gnome-system-monitor/net-bits.page
/usr/share/help/ru/gnome-system-monitor/process-explain.page
/usr/share/help/ru/gnome-system-monitor/process-files.page
/usr/share/help/ru/gnome-system-monitor/process-identify-file.page
/usr/share/help/ru/gnome-system-monitor/process-identify-hog.page
/usr/share/help/ru/gnome-system-monitor/process-kill.page
/usr/share/help/ru/gnome-system-monitor/process-many.page
/usr/share/help/ru/gnome-system-monitor/process-priority-change.page
/usr/share/help/ru/gnome-system-monitor/process-priority-what.page
/usr/share/help/ru/gnome-system-monitor/process-status.page
/usr/share/help/ru/gnome-system-monitor/process-update-speed.page
/usr/share/help/ru/gnome-system-monitor/solaris-mode.page
/usr/share/help/ru/gnome-system-monitor/units.page
/usr/share/help/sv/gnome-system-monitor/commandline.page
/usr/share/help/sv/gnome-system-monitor/cpu-check.page
/usr/share/help/sv/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/sv/gnome-system-monitor/cpu-multicore.page
/usr/share/help/sv/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/sv/gnome-system-monitor/fs-device.page
/usr/share/help/sv/gnome-system-monitor/fs-diskusage.page
/usr/share/help/sv/gnome-system-monitor/fs-info.page
/usr/share/help/sv/gnome-system-monitor/fs-showall.page
/usr/share/help/sv/gnome-system-monitor/index.page
/usr/share/help/sv/gnome-system-monitor/legal.xml
/usr/share/help/sv/gnome-system-monitor/mem-check.page
/usr/share/help/sv/gnome-system-monitor/mem-swap.page
/usr/share/help/sv/gnome-system-monitor/memory-map-use.page
/usr/share/help/sv/gnome-system-monitor/memory-map-what.page
/usr/share/help/sv/gnome-system-monitor/net-bits.page
/usr/share/help/sv/gnome-system-monitor/process-explain.page
/usr/share/help/sv/gnome-system-monitor/process-files.page
/usr/share/help/sv/gnome-system-monitor/process-identify-file.page
/usr/share/help/sv/gnome-system-monitor/process-identify-hog.page
/usr/share/help/sv/gnome-system-monitor/process-kill.page
/usr/share/help/sv/gnome-system-monitor/process-many.page
/usr/share/help/sv/gnome-system-monitor/process-priority-change.page
/usr/share/help/sv/gnome-system-monitor/process-priority-what.page
/usr/share/help/sv/gnome-system-monitor/process-status.page
/usr/share/help/sv/gnome-system-monitor/process-update-speed.page
/usr/share/help/sv/gnome-system-monitor/solaris-mode.page
/usr/share/help/sv/gnome-system-monitor/units.page
/usr/share/help/uk/gnome-system-monitor/commandline.page
/usr/share/help/uk/gnome-system-monitor/cpu-check.page
/usr/share/help/uk/gnome-system-monitor/cpu-mem-normal.page
/usr/share/help/uk/gnome-system-monitor/cpu-multicore.page
/usr/share/help/uk/gnome-system-monitor/figures/org.gnome.SystemMonitor.svg
/usr/share/help/uk/gnome-system-monitor/fs-device.page
/usr/share/help/uk/gnome-system-monitor/fs-diskusage.page
/usr/share/help/uk/gnome-system-monitor/fs-info.page
/usr/share/help/uk/gnome-system-monitor/fs-showall.page
/usr/share/help/uk/gnome-system-monitor/index.page
/usr/share/help/uk/gnome-system-monitor/legal.xml
/usr/share/help/uk/gnome-system-monitor/mem-check.page
/usr/share/help/uk/gnome-system-monitor/mem-swap.page
/usr/share/help/uk/gnome-system-monitor/memory-map-use.page
/usr/share/help/uk/gnome-system-monitor/memory-map-what.page
/usr/share/help/uk/gnome-system-monitor/net-bits.page
/usr/share/help/uk/gnome-system-monitor/process-explain.page
/usr/share/help/uk/gnome-system-monitor/process-files.page
/usr/share/help/uk/gnome-system-monitor/process-identify-file.page
/usr/share/help/uk/gnome-system-monitor/process-identify-hog.page
/usr/share/help/uk/gnome-system-monitor/process-kill.page
/usr/share/help/uk/gnome-system-monitor/process-many.page
/usr/share/help/uk/gnome-system-monitor/process-priority-change.page
/usr/share/help/uk/gnome-system-monitor/process-priority-what.page
/usr/share/help/uk/gnome-system-monitor/process-status.page
/usr/share/help/uk/gnome-system-monitor/process-update-speed.page
/usr/share/help/uk/gnome-system-monitor/solaris-mode.page
/usr/share/help/uk/gnome-system-monitor/units.page

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-system-monitor/gsm-kill
/usr/libexec/gnome-system-monitor/gsm-renice
/usr/libexec/gnome-system-monitor/gsm-taskset

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-system-monitor/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files locales -f gnome-system-monitor.lang
%defattr(-,root,root,-)

