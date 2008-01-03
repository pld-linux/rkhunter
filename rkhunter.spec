Summary:	Rootkit Hunter
Summary(pl.UTF-8):	Program do poszukiwania rootkitów
Name:		rkhunter
Version:	1.3.0
Release:	1
License:	GPL
Group:		Applications
#OLD Source0:	http://downloads.rootkit.nl/%{name}-%{version}.tar.gz
Source0:	http://switch.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	89a4628c6378fdf3331d5a43b975d967
Source1:	%{name}.cron
Source2:	%{name}.conf
URL:		http://www.rootkit.nl/projects/rootkit_hunter.html
Requires:	binutils
Requires:	coreutils
Requires:	diffutils
Requires:	e2fsprogs
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Skaner antyrootkitowy to narzędzie skanujące, aby upewnić się na
99.9%%, że jesteśmy wolni od brzydkich narzędzi. To narzędzie
poszukuje rootkitów, backdoorów i lokalnych eksploitów wykonując testy
w rodzaju:
 - porównywanie skrótów MD5
 - poszukiwanie plików domyślnie używanych przez rootkity
 - poszukiwanie niepoprawnych uprawnień dla binarek
 - poszukiwanie podejrzanych łańcuchów w modułach LKM i KLD
 - poszukiwanie ukrytych plików
 - opcjonalne przeszukiwanie plików tekstowych i binarnych

Rootkit Hunter jest wydany na licencji GPL i darmowy do używania przez
wszystkich.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/cron.daily,%{_datadir}/%{name}/scripts,%{_var}/lib/%{name}/{db,tmp},%{_var}/lib/%{name}/db/i18n}

install files/rkhunter $RPM_BUILD_ROOT%{_sbindir}
install files/i18n/* $RPM_BUILD_ROOT%{_var}/lib/%{name}/db/i18n
install files/*.dat $RPM_BUILD_ROOT%{_var}/lib/%{name}/db
install files/*.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts
install files/check_update.sh $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc files/CHANGELOG files/README files/WISHLIST
%attr(750,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(750,root,root) /etc/cron.daily/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/scripts
%attr(750,root,root) %{_datadir}/%{name}/scripts/*
%dir %{_var}/lib/%{name}
%dir %{_var}/lib/%{name}/db
%dir %{_var}/lib/%{name}/db/i18n
%attr(770,root,root) %dir %{_var}/lib/%{name}/tmp
%attr(640,root,root) %verify(not md5 mtime size) %{_var}/lib/%{name}/db/*.dat
%attr(640,root,root) %verify(not md5 mtime size) %{_var}/lib/%{name}/db/i18n/*
