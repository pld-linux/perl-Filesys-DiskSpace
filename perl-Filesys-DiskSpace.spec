%include	/usr/lib/rpm/macros.perl
Summary:	Filesys-DiskSpace perl module
Summary(pl):	Modu³ perla Filesys-DiskSpace
Name:		perl-Filesys-DiskSpace
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Filesys/Filesys-DiskSpace-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Filesys-DiskSpace - Perl df. 

%description -l pl
Filesys-DiskSpace - 'df' dla perla.

%prep
%setup -q -n Filesys-DiskSpace-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Filesys/DiskSpace
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Filesys/DiskSpace.pm
%{perl_sitearch}/auto/Filesys/DiskSpace

%{_mandir}/man3/*
