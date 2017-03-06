#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-yaml
Version  : 2.1.14
Release  : 21
URL      : http://cran.r-project.org/src/contrib/yaml_2.1.14.tar.gz
Source0  : http://cran.r-project.org/src/contrib/yaml_2.1.14.tar.gz
Summary  : Methods to Convert R Data to YAML and Back
Group    : Development/Tools
License  : NCSA
Requires: R-yaml-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-yaml package.
Group: Libraries

%description lib
lib components for the R-yaml package.


%prep
%setup -q -c -n yaml

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484551352

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1484551352
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library yaml
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library yaml


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/yaml/CHANGELOG
/usr/lib64/R/library/yaml/DESCRIPTION
/usr/lib64/R/library/yaml/INDEX
/usr/lib64/R/library/yaml/LICENSE
/usr/lib64/R/library/yaml/Meta/Rd.rds
/usr/lib64/R/library/yaml/Meta/hsearch.rds
/usr/lib64/R/library/yaml/Meta/links.rds
/usr/lib64/R/library/yaml/Meta/nsInfo.rds
/usr/lib64/R/library/yaml/Meta/package.rds
/usr/lib64/R/library/yaml/NAMESPACE
/usr/lib64/R/library/yaml/R/yaml
/usr/lib64/R/library/yaml/R/yaml.rdb
/usr/lib64/R/library/yaml/R/yaml.rdx
/usr/lib64/R/library/yaml/THANKS
/usr/lib64/R/library/yaml/help/AnIndex
/usr/lib64/R/library/yaml/help/aliases.rds
/usr/lib64/R/library/yaml/help/paths.rds
/usr/lib64/R/library/yaml/help/yaml.rdb
/usr/lib64/R/library/yaml/help/yaml.rdx
/usr/lib64/R/library/yaml/html/00Index.html
/usr/lib64/R/library/yaml/html/R.css
/usr/lib64/R/library/yaml/implicit.re
/usr/lib64/R/library/yaml/libs/symbols.rds
/usr/lib64/R/library/yaml/tests/files/test.yml
/usr/lib64/R/library/yaml/tests/test_as_yaml.R
/usr/lib64/R/library/yaml/tests/test_yaml_load.R
/usr/lib64/R/library/yaml/tests/test_yaml_load_file.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/yaml/libs/yaml.so
