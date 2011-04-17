%define upstream_name    Net-SMTP-SSL
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    SSL support for Net::SMTP
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(Net::SMTP)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Implements the same API as Net::SMTP, but uses IO::Socket::SSL for its
network operations. Due to the nature of 'Net::SMTP''s 'new' method, it is
not overridden to make use of a default port for the SMTPS service. Perhaps
future versions will be smart like that. Port '465' is usually what you
want, and it's not a pain to specify that.

For interface documentation, please see Net::SMTP.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


