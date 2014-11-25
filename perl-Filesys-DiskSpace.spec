#
# Conditional build:
%bcond_with	tests	# perform crappy "make test"

%define		pdir	Filesys
%define		pnam	DiskSpace
%include	/usr/lib/rpm/macros.perl
Summary:	Filesys::DiskSpace - Perl df
Summary(pl.UTF-8):	Filesys::DiskSpace - df w Perlu
Name:		perl-Filesys-DiskSpace
Version:	0.05
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b95651483e0234db33561a53708e007d
URL:		http://search.cpan.org/dist/Filesys-DiskSpace/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Filesys::DiskSpace Perl module is used for displaying information
of a file system such as its type, the amount of disk space occupied,
the total disk space and the number of inodes.

%description -l pl.UTF-8
Moduł Perla Filesys::DiskSpace służy do wypisywania takich informacji
o systemie plików, jak jego typ, ilość zajętego miejsca na dysku,
łączna pojemność dysku i liczba i-węzłów.

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
