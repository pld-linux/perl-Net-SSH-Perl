#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Net
%define		pnam	SSH-Perl
Summary:	Net::SSH::Perl - Perl client Interface to SSH
Summary(pl.UTF-8):	Net::SSH::Perl - perlowy interfejs kliencki do SSH
Name:		perl-Net-SSH-Perl
Version:	2.144
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/B/BD/BDFOY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	219bba3277b40cc4df4cbd7d74ee0777
URL:		http://search.cpan.org/dist/Net-SSH-Perl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-Curve25519 >= 0.05
BuildRequires:	perl-Crypt-IDEA
BuildRequires:	perl-CryptX >= 0.032
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-File-HomeDir
BuildRequires:	perl-Math-GMP >= 1.04
BuildRequires:	perl-String-CRC32 >= 1.2
%endif
Requires:	perl-Crypt-Curve25519 >= 0.05
Requires:	perl-Crypt-IDEA
Requires:	perl-CryptX >= 0.032
Requires:	perl-Digest-BubbleBabble
Requires:	perl-Digest-MD5
Requires:	perl-File-HomeDir
Requires:	perl-Math-GMP >= 1.04
Requires:	perl-String-CRC32 >= 1.2
# rsa1 key generation only
Suggests:	perl-Crypt-RSA
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
PERL_MM_USE_DEFAULT=1 %{__perl} Makefile.PL \
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
%dir %{perl_vendorarch}/auto/Net/SSH
%dir %{perl_vendorarch}/auto/Net/SSH/Perl
%dir %{perl_vendorarch}/Net/SSH
%attr(755,root,root) %{perl_vendorarch}/auto/Net/SSH/Perl/Perl.so
%{perl_vendorarch}/Net/SSH/*.pm
%{perl_vendorarch}/Net/SSH/Perl
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
