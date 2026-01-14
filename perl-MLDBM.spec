#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	MLDBM
%define		pnam	MLDBM
Summary:	MLDBM - store multi-level hash structure in single level tied hash
Summary(pl.UTF-8):	MLDBM - przechowywanie wielopoziomowej struktury haszy w jednopoziomowym haszu związanym
Name:		perl-MLDBM
Version:	2.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/MLDBM/%{pnam}-%{version}.tar.gz
# Source0-md5:	9b7ec37bfc36b0e83db9323be92beb50
URL:		https://metacpan.org/dist/MLDBM
BuildRequires:	perl(Data::Dumper) >= 2.08
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-FreezeThaw
%{?with_tests:BuildRequires:	perl-Test-Simple}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLDBM Perl module can serve as a transparent interface to any TIEHASH
package that is required to store arbitrary perl data, including
nested references. Thus, this module can be used for storing
references and other arbitrary data within DBM databases.

%description -l pl.UTF-8
Moduł Perla MLDBM może służyć za przezroczysty interfejs do dowolnego
pakietu TIEHASH, od którego wymaga się przechowywania dowolnych danych
perla, włącznie z zagnieżdżonymi referencjami. Zatem moduł ten służy
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MLDBM.pm
%{perl_vendorlib}/MLDBM
%{_mandir}/man3/MLDBM.3pm*
