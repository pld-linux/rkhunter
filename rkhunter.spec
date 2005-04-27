Summary:	Rootkit Hunter
Summary(pl):	Program do poszukiwania rootkitów
Name:		rkhunter
Version:	1.2.4
Release:	2
License:	GPL
Group:		Applications
Source0:	http://downloads.rootkit.nl/%{name}-%{version}.tar.gz
# Source0-md5:	d3f653233376af34bcdd2837cff56a3a
Source1:	%{name}.cron
Source2:	%{name}.conf
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-appversion.patch
Patch2:		%{name}-CAN-2005-1270.patch
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

%description -l pl
Skaner antyrootkitowy to narzêdzie skanuj±ce, aby upewniæ siê na
99.9%%, ¿e jeste¶my wolni od brzydkich narzêdzi. To narzêdzie poszukuje
rootkitów, backdoorów i lokalnych eksploitów wykonuj±c testy w rodzaju:
 - porównywanie skrótów MD5
 - poszukiwanie plików domy¶lnie u¿ywanych przez rootkity
 - poszukiwanie niepoprawnych uprawnieñ dla binarek
 - poszukiwanie podejrzanych ³añcuchów w modu³ach LKM i KLD
 - poszukiwanie ukrytych plików
 - opcjonalne przeszukiwanie plików tekstowych i binarnych

Rootkit Hunter jest wydany na licencji GPL i darmowy do u¿ywania przez
wszystkich.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/cron.daily,%{_datadir}/%{name}/scripts,%{_var}/lib/%{name}/{db,tmp}}

install files/rkhunter $RPM_BUILD_ROOT%{_sbindir}
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
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%attr(750,root,root) /etc/cron.daily/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/scripts
%attr(750,root,root) %{_datadir}/%{name}/scripts/*
%dir %{_var}/lib/%{name}
%dir %{_var}/lib/%{name}/db
%attr(770,root,root) %dir %{_var}/lib/%{name}/tmp
%attr(640,root,root) %verify(not size mtime md5) %{_var}/lib/%{name}/db/*.dat
