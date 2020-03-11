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


BuildRequires:  python%{python3_pkgversion}-devel

#Provides: %{name}-static = %{version}-%{release}
#%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description
Avogadro Nanocar Plugin. Build a nanocar molecule by picking molecular wheels and chassis in Avogadro2.

How to build a Nanocar? || Avogadro 2 nanocar builder plug-in tutorial
https://www.youtube.com/watch?v=bNmIEJaXltg



%prep
%setup -q -n nanocar-avogadro-master


%build
echo "build"

%install
python3 install_plugin.py %{buildroot}%{python3_sitearch}/avogadro2/scripts




%files
%{python3_sitearch}/avogadro2/scripts



%changelog
* Sun Mar 08 2020 Gen Kawamura <gen.kawamura@cern.ch> - 1.0.0-1
- Initial package
- Using master branch on GitHub (427abb2bca83d7ff160d2983dafe1754e79c32e4)
