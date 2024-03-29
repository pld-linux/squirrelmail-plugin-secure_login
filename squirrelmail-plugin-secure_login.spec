%define		_plugin	secure_login
%define		mversion	1.2.8
Summary:	Plugin to turn on SSL during login
Summary(pl.UTF-8):	Wtyczka włączająca SSL na czas logowania
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.4
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	e511a8e78beab042b123d468ea7e0df9
URL:		http://www.squirrelmail.org/plugin_view.php?id=61
Requires:	squirrelmail >= 1.2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
Plugin to automatically turn on SSL security during login.

Primarily this plugin is intended to prevent plain text passwords and
email contents being transmitted over the internet after people
manually enter their server URL without including https://...

%description -l pl.UTF-8
Wtyczka automatycznie włączająca szyfrowanie SSL w czasie logowania.

Głównym celem tej wtyczki jest zapobieganie przesyłaniu haseł i treści
maili otwartym tekstem jeżeli użytkownik wpisze URL bez https://...

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
mv $RPM_BUILD_ROOT{%{_plugindir}/config.sample,%{_sysconfdir}/%{_plugin}_config}.php
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
