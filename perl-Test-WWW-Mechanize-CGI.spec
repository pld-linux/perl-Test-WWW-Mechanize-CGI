#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Test
%define		pnam	WWW-Mechanize-CGI
Summary:	Test::WWW::Mechanize::CGI - Test CGI applications with Test::WWW::Mechanize
Name:		perl-Test-WWW-Mechanize-CGI
Version:	0.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	55fea6cdaa85433060c3d55a4982272e
URL:		http://search.cpan.org/dist/Test-WWW-Mechanize-CGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-WWW-Mechanize
BuildRequires:	perl-WWW-Mechanize-CGI >= 0.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a convenient way of testing CGI applications without a
external daemon.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/WWW/Mechanize/CGI.pm
%{_mandir}/man3/*
