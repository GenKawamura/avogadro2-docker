## This release does not compile because of current unsupported GCC version (4.8.5) on rhel7
## during compilation of bundled 'jsoncpp'.
## Error "unsupported GCC version - see https://github.com/nlohmann/json#supported-compilers"

# Use devtoolset 8
Name:           avogadro2-nanocar
Version:        1.0.0
Release:        1%{?dist}
Summary:        Avogadro2 Nanocar Plugin

# BSD is main license
License: BSD-3
URL: https://github.com/kbsezginel/nanocar-avogadro/archive/master.zip
Source0: nanocar-avogadro-master.zip
%global commit 427abb2bca83d7ff160d2983dafe1754e79c32e4

Requires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-devel


%description
Avogadro Nanocar Plugin. Build a nanocar molecule by picking molecular wheels and chassis in Avogadro2.

How to build a Nanocar? || Avogadro 2 nanocar builder plug-in tutorial
https://www.youtube.com/watch?v=bNmIEJaXltg



%prep
%setup -q -n nanocar-avogadro-master


%build

%install
mkdir -vp %{buildroot}%{_datadir}/%{name}
cp -v requirements.txt %{buildroot}%{_datadir}/%{name}
python3 install_plugin.py %{buildroot}%{_datadir}/%{name}



%post
export PIP_TARGET=%{_datadir}/%{name}
pip3 install --upgrade -r %{_datadir}/%{name}/requirements.txt

%preun
export PIP_TARGET=%{_datadir}/%{name}
pip3 uninstall -r %{_datadir}/%{name}/requirements.txt


%files
%{_datadir}/%{name}



%changelog
* Sun Mar 08 2020 Gen Kawamura <gen.kawamura@cern.ch> - 1.0.0-1
- Initial package
- Using master branch on GitHub (427abb2bca83d7ff160d2983dafe1754e79c32e4)
