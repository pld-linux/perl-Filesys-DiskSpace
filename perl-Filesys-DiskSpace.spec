%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	DiskSpace
Summary:	Filesys::DiskSpace perl module
Summary(pl):	Modu³ perla Filesys::DiskSpace
Name:		perl-Filesys-DiskSpace
Version:	0.05
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys::DiskSpace - Perl df.

%description -l pl
Filesys::DiskSpace - 'df' dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Filesys/DiskSpace.pm
%{_mandir}/man3/*
