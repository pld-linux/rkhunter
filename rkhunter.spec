Summary:	Rootkit Hunter is a Rootkit Hunter :) _FIXMEEE_
Summary(pl):	_FIXMEEE_
Name:		rkhunter
Version:	1.1.1
Release:	0.9
License:	GPL
Group:		Applications
Source0:	http://downloads.rootkit.nl/%{name}-%{version}.tar.gz
# Source0-md5:	89b588aecf35ce34fa5cb737890e37c8
Source1:	%{name}.cron
URL:		http://www.rootkit.nl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Rootkit scanner is scanning tool to ensure you for about 99.9%% you're
clean of nasty tools. This tool scans for rootkits, backdoors and
local exploits by running tests like:
        - MD5 hash compare
        - Look for default files used by rootkits
        - Wrong file permissions for binaries
        - Look for suspected strings in LKM and KLD modules
        - Look for hidden files
        - Optional scan within plaintext and binary files

Rootkit Hunter is released as GPL licensed project and free for
everyone to use.

%description -l pl
_FIXMEEEE_

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}/cron.daily,%{_libdir}/%{name}/scripts,%{_var}/rkhunter/{db,tmp}}

install files/rkhunter $RPM_BUILD_ROOT%{_sbindir}
install files/*.dat $RPM_BUILD_ROOT%{_var}/rkhunter/db
install files/*.pl $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts
install files/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc files/CHANGELOG files/README files/WISHLIST
%attr(750,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%attr(750,root,root) %{_sysconfdir}/cron.daily/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/scripts
%attr(750,root,root) %{_libdir}/%{name}/scripts/*.pl
%dir %{_var}/rkhunter
%dir %{_var}/rkhunter/db
%dir %{_var}/rkhunter/tmp
%attr(640,root,root) %{_var}/rkhunter/db/*.dat
