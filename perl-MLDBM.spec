#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MLDBM
%define		pnam	MLDBM
Summary:	MLDBM - store multi-level hash structure in single level tied hash
Summary(pl):	MLDBM - przechowywanie wielopoziomowej structury haszy w jednopoziomowym haszu zwi±zanym
Name:		perl-MLDBM
Version:	2.01
Release:	2
License:	GPL
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
Modu³ Perla MLDBM mo¿e s³u¿yæ za przezroczysty interfejs do dowolnego
pakietu TIEHASH, od którego wymaga siê przechowywania dowolnych danych
perla, w³±cznie z zagnie¿d¿onymi referencjami. Zatem modu³ ten s³u¿y
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
