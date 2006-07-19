%define		_plugin	secure_login
%define		mversion	1.2.8
Summary:	Plugin to turn on SSL during login
Summary(pl):	Wtyczka w³±czaj±ca SSL na czas logowania
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	73d2c111579e2fad17c289f62e0be855
URL:		http://www.squirrelmail.org/plugin_view.php?id=61
Requires:	squirrelmail >= 1.4.6-1
Requires:	squirrelmail-compatibility-2.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
Plugin to automatically turn on SSL security during login.

Primarily this plugin is intended to prevent plain text passwords and
email contents being transmitted over the internet after people
manually enter their server URL without including https://...

%description -l pl
Wtyczka automatycznie w³±czaj±ca szyfrowanie SSL w czasie logowania.

G³ównym celem tej wtyczki jest zapobieganie przesy³aniu hase³ i tre¶ci
maili otwartym tekstem je¿eli u¿ytkownik wpisze URL bez https://...

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
mv config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
