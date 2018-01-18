Summary:	Nightingale Media Player
Name:		nightingale
Version:	1.12.1
Release:	0.1
License:	GPL-2, BSD, MPL
Group:		X11/Applications/Multimedia
Source0:	https://github.com/nightingale-media-player/nightingale-hacking/archive/%{name}-%{version}.tar.gz
URL:		https://getnightingale.com/
BuildRequires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nightingale is a community based fork of the Songbird Media player
distributed under the GNU GPL and portions (XULRunner and Mozilla
libs) licensed under the Mozilla MPL/BSD license.

The goal of Nightingale is to create a Media Player, which will
eventually use only system libraries to conserve space. Currently,
some libraries are still bundled, but progress is being made to change
this fact.

This git tree is the Songbird trunk, rebranded for Nightingale. It's a
reflection of what our Xul 6+ releases will be like.

%prep
%setup -qc
mv nightingale-hacking-nightingale-%{version}/* .

%build
bash -x ./build.sh

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
