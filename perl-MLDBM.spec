#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MLDBM
%define		pnam	MLDBM
Summary:	MLDBM Perl module
Summary(cs):	Modul MLDBM pro Perl
Summary(da):	Perlmodul MLDBM
Summary(de):	MLDBM Perl Modul
Summary(es):	Módulo de Perl MLDBM
Summary(fr):	Module Perl MLDBM
Summary(it):	Modulo di Perl MLDBM
Summary(ja):	MLDBM Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	MLDBM ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul MLDBM
Summary(pl):	Modu³ Perla MLDBM
Summary(pt):	Módulo de Perl MLDBM
Summary(pt_BR):	Módulo Perl MLDBM
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl MLDBM
Summary(sv):	MLDBM Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl MLDBM
Summary(zh_CN):	MLDBM Perl Ä£¿é
Name:		perl-MLDBM
Version:	2.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Storable
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLDBM - store multi-level hash structure in single level tied hash.

%description -l pl
Modu³ perla MLDBM.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/MLDBM.pm
%{perl_sitelib}/MLDBM
%{_mandir}/man3/*
