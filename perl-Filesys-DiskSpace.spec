%include	/usr/lib/rpm/macros.perl
Summary:	Filesys-DiskSpace perl module
Summary(pl):	Modu³ perla Filesys-DiskSpace
Name:		perl-Filesys-DiskSpace
Version:	0.05
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Filesys/Filesys-DiskSpace-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys-DiskSpace - Perl df.

%description -l pl
Filesys-DiskSpace - 'df' dla perla.

%prep
%setup -q -n Filesys-DiskSpace-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Filesys/DiskSpace.pm
%{_mandir}/man3/*
