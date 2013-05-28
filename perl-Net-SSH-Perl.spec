#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SSH-Perl
Summary:	Net::SSH::Perl - Perl client Interface to SSH
Summary(pl.UTF-8):	Net::SSH::Perl - perlowy interfejs kliencki do SSH
Name:		perl-Net-SSH-Perl
Version:	1.34
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5b6d60e459707058e856c45c30e96e53
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Convert-PEM >= 0.05
BuildRequires:	perl-Crypt-DH >= 0.01
BuildRequires:	perl-Crypt-DSA >= 0.11
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Digest-SHA1 >= 2.10
BuildRequires:	perl-Math-GMP >= 1.04
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-String-CRC32 >= 1.2
%endif
Requires:	perl-Convert-PEM >= 0.05
Requires:	perl-Crypt-Blowfish
Requires:	perl-Crypt-DES
Requires:	perl-Crypt-DH >= 0.01
Requires:	perl-Crypt-DSA >= 0.11
Requires:	perl-Crypt-IDEA
Requires:	perl-Crypt-RSA
Requires:	perl-Digest-BubbleBabble
Requires:	perl-Digest-HMAC
Requires:	perl-Digest-MD5
Requires:	perl-Digest-SHA1 >= 2.10
Requires:	perl-Math-GMP >= 1.04
Requires:	perl-Math-Pari >= 2.001804
Requires:	perl-MIME-Base64
Requires:	perl-String-CRC32 >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SSH::Perl is an all-Perl module implementing an SSH (Secure
Shell) client. It is compatible with both the SSH-1 and SSH-2
protocols.

%description -l pl.UTF-8
Net::SSH::Perl to napisany w całości w Perlu moduł implementujący
klienta SSH (Secure Shell). Jest kompatybilny z protokołami zarówno
SSH-1 jak i SSH-2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Perl::Net::SSH::Perl")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes ToDo
%dir %{perl_vendorlib}/Net/SSH
%{perl_vendorlib}/Net/SSH/*.pm
%{perl_vendorlib}/Net/SSH/Perl
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
