#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-yaml
Version  : 2.3.8
Release  : 95
URL      : https://cran.r-project.org/src/contrib/yaml_2.3.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/yaml_2.3.8.tar.gz
Summary  : Methods to Convert R Data to YAML and Back
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-yaml-lib = %{version}-%{release}
Requires: R-yaml-license = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-yaml package.
Group: Libraries
Requires: R-yaml-license = %{version}-%{release}

%description lib
lib components for the R-yaml package.


%package license
Summary: license components for the R-yaml package.
Group: Default

%description license
license components for the R-yaml package.


%prep
%setup -q -n yaml
pushd ..
cp -a yaml buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702961583

%install
export SOURCE_DATE_EPOCH=1702961583
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-yaml
cp %{_builddir}/yaml/COPYING %{buildroot}/usr/share/package-licenses/R-yaml/3476e3fc26cf5478584727491080dae1c4e057e4 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-yaml/3476e3fc26cf5478584727491080dae1c4e057e4
