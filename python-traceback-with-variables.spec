Name:		python-traceback-with-variables
Version:	2.2.1
Release:	1
Summary:	Adds variables to python traceback. Simple, lightweight, controllable.
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/traceback-with-variables/
Source0:	traceback_with_variables-2.2.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Adds variables to python traceback. Simple, lightweight, controllable..

%files
%{py_sitedir}/*
%{_bindir}/*
