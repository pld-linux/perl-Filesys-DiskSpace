#
# Conditional build:
%bcond_with	tests	# perform crappy "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	DiskSpace
Summary:	Filesys::DiskSpace - Perl df
Summary(pl):	Filesys::DiskSpace - df w Perlu
Name:		perl-Filesys-DiskSpace
Version:	0.05
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b95651483e0234db33561a53708e007d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Filesys::DiskSpace Perl module is used for displaying information
of a file system such as its type, the amount of disk space occupied,
the total disk space and the number of inodes.

%description -l pl
Modu³ Perla Filesys::DiskSpace s³u¿y do wypisywania takich informacji
o systemie plików, jak jego typ, ilo¶æ zajêtego miejsca na dysku,
³±czna pojemno¶æ dysku i liczba i-wêz³ów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc README
%{perl_vendorlib}/Filesys/DiskSpace.pm
%{_mandir}/man3/*
