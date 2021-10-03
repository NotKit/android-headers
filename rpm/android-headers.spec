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

# Clean up
%fdupes %{buildroot}/%{_prefix}

%files
%{_prefix}/include/*
%{_libdir}/pkgconfig/android-headers.pc

%changelog
