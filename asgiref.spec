#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : asgiref
Version  : 3.4.1
Release  : 22
URL      : https://files.pythonhosted.org/packages/07/93/3618b68b4ba6b54bc97b5fd7d90e4981471edfaf51c8321a29a3c76cf47c/asgiref-3.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/07/93/3618b68b4ba6b54bc97b5fd7d90e4981471edfaf51c8321a29a3c76cf47c/asgiref-3.4.1.tar.gz
Summary  : ASGI specs, helper code, and adapters
Group    : Development/Tools
License  : BSD-3-Clause
Requires: asgiref-license = %{version}-%{release}
Requires: asgiref-python = %{version}-%{release}
Requires: asgiref-python3 = %{version}-%{release}
Requires: mypy
Requires: typing_extensions
BuildRequires : buildreq-distutils3
BuildRequires : mypy

%description
asgiref
=======
.. image:: https://api.travis-ci.org/django/asgiref.svg
:target: https://travis-ci.org/django/asgiref

%package license
Summary: license components for the asgiref package.
Group: Default

%description license
license components for the asgiref package.


%package python
Summary: python components for the asgiref package.
Group: Default
Requires: asgiref-python3 = %{version}-%{release}

%description python
python components for the asgiref package.


%package python3
Summary: python3 components for the asgiref package.
Group: Default
Requires: python3-core
Provides: pypi(asgiref)

%description python3
python3 components for the asgiref package.


%prep
%setup -q -n asgiref-3.4.1
cd %{_builddir}/asgiref-3.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625580943
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/asgiref
cp %{_builddir}/asgiref-3.4.1/LICENSE %{buildroot}/usr/share/package-licenses/asgiref/baf11129ce63c4eef654f39a360b31cfc7d1ac67
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/asgiref/baf11129ce63c4eef654f39a360b31cfc7d1ac67

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
