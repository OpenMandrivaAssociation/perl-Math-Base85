%define real_name Math-Base85

Summary:	Math::Base85 - Perl extension for base 85 numbers, as referenced by RFC 1924
Name:		perl-%{real_name}
Version:	0.2
Release: %mkrel 6
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




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-6mdv2010.0
+ Revision: 430499
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2009.0
+ Revision: 257772
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2009.0
+ Revision: 245823
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.2-2mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-2mdk
- Fix According to perl Policy
	- Source URL
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdk
- initial Mandriva package

