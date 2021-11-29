Summary:	Client for PPP+SSL VPN tunnel services
Name:		openfortivpn
Version:	1.17.1
Release:	1
License:	GPLv3+
Group:		Networking/Other
URL:		https://github.com/adrienverge/%{name}
Source0:	https://github.com/adrienverge/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(systemd)

Requires:		ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.

It is compatible with Fortinet VPNs.

%files
%license LICENSE LICENSE.OpenSSL
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}@.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/openfortivpn/config

#--------------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#autoreconf -fi
%configure

%make_build

%install
%make_install

