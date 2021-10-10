Name:           android-headers
Version:        11.0
Release:        0
Summary:        Android Platform Headers from AOSP releases
License:        Apache-2.0
Group:          Development/Libraries/Other
Url:            https://github.com/ubports/android-headers
Source0:        %{name}-%{version}.tar.xz
BuildArchitectures: noarch
BuildRequires:  fdupes
Provides:       droid-hal-devel

%description
This package provides the platform development headers for core components
of AOSP (Android Open Source Project) used for compiling user source code
against platform headers for different releases (e.g. for libhybris).

%prep
%setup -q

%build
# Empty build section, nothing to build

%install
mkdir -p %{buildroot}/%{_prefix}/include
cp -r 30 %{buildroot}/%{_prefix}/include/android

mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cat << EOF > %{buildroot}/%{_libdir}/pkgconfig/android-headers.pc
Name: Android Platform Header Files
Description: Header files needed to write applications for the Android platform
Version: 11.0.0

prefix=/usr
exec_prefix=%{_prefix}
includedir=%{_prefix}/include

Cflags: -I\${includedir}/android
EOF

mkdir -p %{buildroot}/%{_prefix}/include/droid-devel
cat << EOF > %{buildroot}/%{_prefix}/include/droid-devel/hw-release.vars
MER_HA_DEVICE=halium
MER_HA_VENDOR=halium
MER_HA_VERSION="11.0 (aarch64,devel)"
MER_HA_VERSION_ID=11.0
MER_HA_PRETTY_NAME="Halium 11.0 (aarch64,devel)"
MER_HA_SAILFISH_BUILD=1
MER_HA_SAILFISH_FLAVOUR=devel
MER_HA_HOME_URL="https://sailfishos.org/"
EOF

# Clean up
%fdupes %{buildroot}/%{_prefix}

%files
%{_prefix}/include/*
%{_libdir}/pkgconfig/android-headers.pc

%changelog
