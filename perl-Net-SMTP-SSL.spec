%define modname	Net-SMTP-SSL
%define modver	1.01

Summary:	SSL support for Net::SMTP
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(Net::SMTP)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Implements the same API as Net::SMTP, but uses IO::Socket::SSL for its
network operations. Due to the nature of 'Net::SMTP''s 'new' method, it is
not overridden to make use of a default port for the SMTPS service. Perhaps
future versions will be smart like that. Port '465' is usually what you
want, and it's not a pain to specify that.

For interface documentation, please see Net::SMTP.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

