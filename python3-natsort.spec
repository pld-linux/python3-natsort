# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests

%define		module	natsort
Summary:	Simple yet flexible natural sorting in Python
Summary(pl.UTF-8):	-
# Name must match the python module/package name (as on pypi or in 'import' statement)
Name:		python3-%{module}
Version:	7.1.1
Release:	1
License:	MIT
Group:		Libraries/Python
# if pypi:
#Source0Download: https://pypi.org/simple/MODULE/
Source0:	https://pypi.debian.net/natsort/%{module}-%{version}.tar.gz
# Source0-md5:	585f58381542884f2cc9c4d73962a08f
URL:		https://pypi.org/project/natsort/
BuildRequires:	python3-modules >= 1:3.2
#BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	python3-
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
# replace with other requires if defined in setup.py
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple yet flexible natural sorting in Python.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif

%if %{with doc}
%{_bindir}/tox -e docs
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.rst
%attr(755,root,root) %{_bindir}/natsort
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%dir %{py3_sitescriptdir}/%{module}/compat
%{py3_sitescriptdir}/%{module}/compat/*.py
%{py3_sitescriptdir}/%{module}/compat/__pycache__

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
