%include	/usr/lib/rpm/macros.perl
Summary:	MLDBM perl module
Summary(pl):	Modu³ perla MLDBM
Name:		perl-MLDBM
Version:	2.00
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/MLDBM/MLDBM-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Storable
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
MLDBM - store multi-level hash structure in single level tied hash.

%description -l pl
Modu³ perla MLDBM.

%prep
%setup -q -n MLDBM-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/MLDBM
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/MLDBM.pm
%{perl_sitelib}/MLDBM
%{perl_sitearch}/auto/MLDBM

%{_mandir}/man3/*
