%include	/usr/lib/rpm/macros.perl
Summary:	MLDBM perl module
Summary(pl):	Modu³ perla MLDBM
Name:		perl-MLDBM
Version:	2.00
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/MLDBM/MLDBM-%{version}.tar.gz
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
%setup -q -n MLDBM-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/MLDBM.pm
%{perl_sitelib}/MLDBM
%{_mandir}/man3/*
