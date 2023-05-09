# check disabled to avoid circular dependencies
%bcond_with check
%global debug_package %{nil}

%global crate indexmap

Name:           rust-%{crate}
Version:        1.9.3
Release:        1
Summary:        Hash table with consistent order and fast iteration

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/indexmap
Source:         %{crates_source}
Patch0:		indexmap-1.9.3-build.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Hash table with consistent order and fast iteration.
The indexmap is a hash
table where the iteration order of the key-value pairs is independent of the
hash values of the keys. It has the usual hash table functionality, it
preserves insertion order except after removals, and it allows lookup of its
elements by either hash table key or numerical index. A corresponding hash set
type is also provided.
This crate was initially published under the name
ordermap, but it was renamed to indexmap.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages
which use "rayon" feature of "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-1-devel %{_description}

This package contains library source intended for building other packages
which use "serde-1" feature of "%{crate}" crate.

%files       -n %{name}+serde-1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test_debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test_debug-devel %{_description}

This package contains library source intended for building other packages
which use "test_debug" feature of "%{crate}" crate.

%files       -n %{name}+test_debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test_low_transition_point-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test_low_transition_point-devel %{_description}

This package contains library source intended for building other packages
which use "test_low_transition_point" feature of "%{crate}" crate.

%files       -n %{name}+test_low_transition_point-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
