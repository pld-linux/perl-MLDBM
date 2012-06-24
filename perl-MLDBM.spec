#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MLDBM
%define		pnam	MLDBM
Summary:	MLDBM - store multi-level hash structure in single level tied hash
Summary(pl):	MLDBM - przechowywanie wielopoziomowej structury haszy w jednopoziomowym haszu zwi�zanym
Name:		perl-MLDBM
Version:	2.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	99550ae2cffbc0bb3eb0358631077c10
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Storable
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLDBM Perl module can serve as a transparent interface to any TIEHASH
package that is required to store arbitrary perl data, including
nested references. Thus, this module can be used for storing
references and other arbitrary data within DBM databases.

%description
Modu� Perla MLDBM mo�e s�u�y� za przezroczysty interfejs do dowolnego
pakietu TIEHASH, od kt�rego wymaga si� przechowywania dowolnych danych
perla, w��cznie z zagnie�d�onymi referencjami. Zatem modu� ten s�u�y
do przychowywania referencji oraz innych dowolnych danych w bazach
DBM.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MLDBM.pm
%{perl_vendorlib}/MLDBM
%{_mandir}/man3/*
