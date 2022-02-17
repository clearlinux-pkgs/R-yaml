#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-yaml
Version  : 2.3.4
Release  : 80
URL      : https://cran.r-project.org/src/contrib/yaml_2.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/yaml_2.3.4.tar.gz
Summary  : Methods to Convert R Data to YAML and Back
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-yaml-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-yaml package.
Group: Libraries

%description lib
lib components for the R-yaml package.


%prep
%setup -q -c -n yaml
cd %{_builddir}/yaml

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645132371

%install
export SOURCE_DATE_EPOCH=1645132371
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library yaml
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library yaml
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library yaml
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc yaml || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/yaml/CHANGELOG
/usr/lib64/R/library/yaml/DESCRIPTION
/usr/lib64/R/library/yaml/INDEX
/usr/lib64/R/library/yaml/LICENSE
/usr/lib64/R/library/yaml/Meta/Rd.rds
/usr/lib64/R/library/yaml/Meta/features.rds
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
/usr/lib64/R/library/yaml/tests/RUnit.R
/usr/lib64/R/library/yaml/tests/files/merge.yml
/usr/lib64/R/library/yaml/tests/files/test.yml
/usr/lib64/R/library/yaml/tests/test_as_yaml.R
/usr/lib64/R/library/yaml/tests/test_read_yaml.R
/usr/lib64/R/library/yaml/tests/test_write_yaml.R
/usr/lib64/R/library/yaml/tests/test_yaml_load.R
/usr/lib64/R/library/yaml/tests/test_yaml_load_file.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/yaml/libs/yaml.so
/usr/lib64/R/library/yaml/libs/yaml.so.avx2
/usr/lib64/R/library/yaml/libs/yaml.so.avx512
