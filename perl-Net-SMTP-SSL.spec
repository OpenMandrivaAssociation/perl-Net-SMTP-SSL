%define upstream_name    Net-SMTP-SSL
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	SSL support for Net::SMTP
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(Net::SMTP)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-4mdv2012.0
+ Revision: 765534
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2
+ Revision: 654266
- rebuild for updated spec-helper

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 497152
- import perl-Net-SMTP-SSL


* Wed Jan 27 2010 cpan2dist 1.01-1mdv
- initial mdv release, generated with cpan2dist
