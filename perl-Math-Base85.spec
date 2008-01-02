%define real_name Math-Base85

Summary:	Math::Base85 - Perl extension for base 85 numbers, as referenced by RFC 1924
Name:		perl-%{real_name}
Version:	0.2
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/Math/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
RFC 1924 describes a compact, fixed-size representation of IPv6
addresses which uses a base 85 number system.  This module handles
some of the uglier details of it.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Math/Base85.pm
%{_mandir}/*/*


