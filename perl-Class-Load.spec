#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Load
Version  : 0.25
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-0.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-0.25.tar.gz
Summary  : 'A working (require "Class::Name") and more'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-Load-license = %{version}-%{release}
Requires: perl-Class-Load-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Class-Load,
version 0.25:
A working (require "Class::Name") and more

%package dev
Summary: dev components for the perl-Class-Load package.
Group: Development
Provides: perl-Class-Load-devel = %{version}-%{release}
Requires: perl-Class-Load = %{version}-%{release}

%description dev
dev components for the perl-Class-Load package.


%package license
Summary: license components for the perl-Class-Load package.
Group: Default

%description license
license components for the perl-Class-Load package.


%package perl
Summary: perl components for the perl-Class-Load package.
Group: Default
Requires: perl-Class-Load = %{version}-%{release}

%description perl
perl components for the perl-Class-Load package.


%prep
%setup -q -n Class-Load-0.25
cd %{_builddir}/Class-Load-0.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Load
cp %{_builddir}/Class-Load-0.25/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Load/02baa9a7c1e8cd4e565c56a6af13a63d650805ef
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Load.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Load/02baa9a7c1e8cd4e565c56a6af13a63d650805ef

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
