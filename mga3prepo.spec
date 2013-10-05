Name:		mga3prepo
Version:	0.9.5
Release:	%mkrel 1
Summary:	A script to search packages in extra repositories
Summary(fr_FR):	Un script pour rechercher des paquets dans les dépôts supplémentaires
License:	GPLv3
Group:		System/Packaging
Url:		https://github.com/dglent/mga3prepo
Source0:	http://glenbox.free.fr/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	python3-setuptools

Requires:	python3
Requires:	wget
Requires:	gzip
Requires:	xz

%description
A script in Python3 to search package from extra (unofficial or not) 
repositories.
Launch the script as 'mga3prepo' or with the name of the package 
as an argument.

%description -l fr_FR
Un script en python3 pour rechercher des paquets dans les dépôts 
supplémentaires (non officiels ou pas).
Lancez le script de 'mga3prepo' ou avec le nom du paquet comme argument.

%prep
%setup -q

%build
%{__python3} i18n.py
%{__python3} setup.py build


%install
%{__python3} ./setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_bindir}

install -D -m 755 %{name} \
	 %{buildroot}%{_bindir}/
	 
chmod +x %{buildroot}%{_bindir}/


### Install translations ###
pushd ./po
for f in *.po
do
		poname=${f:0:2}
		mkdir -p %buildroot%{_datadir}/locale/$poname/LC_MESSAGES
		install -m 644 usr/share/locale/$poname/LC_MESSAGES/%{name}.mo \
		"%{buildroot}%{_datadir}/locale/$poname/LC_MESSAGES/"
done
popd
#############################

%find_lang %{name} --with-html


%files -f %{name}.lang
%doc README
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%py3ver.egg-info

%changelog
* Sat Oct 05 2013 dimitrios (MLO Team) <dimitrios> 0.9.5-1.mga3
- Fix crash in 'search updates'

* Fri Oct 04 2013 dimitrios (MLO Team) <dimitrios> 0.9.4-1.mga3
- Fix bug of 0.9.3 code in 'Search updates'

* Thu Oct 03 2013 dimitrios (MLO Team) <dimitrios> 0.9.3-1.mga3
- Fix bug of 0.9.2 code in 'Search updates'

* Tue Oct 01 2013 dimitrios (MLO Team) <dimitrios> 0.9.2-1.mga3
- Fix bug in comparing versions between rpm in 3rd repositories 
  (fix 0.9.1 code)

* Mon Sep 30 2013 dimitrios (MLO Team) <dimitrios> 0.9.1-1.mga3
- Fix bug in comparing versions between rpm in 3rd repositories

* Sat Sep 28 2013 dimitrios (MLO Team) <dimitrios> 0.9-1.mga3
- New version 0.9
- Add feature 'search for updates'

* Sun Sep 22 2013 dimitrios (MLO Team) <dimitrios> 0.8-1.mga3
- Code improvement

* Fri May 10 2013 dimitrios (MLO Team) <dimitrios> 0.7-1.mga3
- Make searchs faster after downloading once the media
  when searching packages from the main menu.
- Fix some minor bugs (wrongly displayed messages)

* Sat May 04 2013 dimitrios (MLO Team) <dimitrios> 0.6-1.mga3
+ New version: 0.6
- add french translations
- add french language in %%description and %%Summary
- change license to GPLv3

