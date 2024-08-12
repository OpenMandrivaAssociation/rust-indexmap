# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_with check
%global debug_package %{nil}

%global crate indexmap

Name:           rust-indexmap
Version:        2.3.0
Release:        1
Summary:        Hash table with consistent order and fast iteration
Group:          Development/Rust

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/indexmap
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(equivalent) >= 1.0.0 with crate(equivalent) < 2.0.0~)
BuildRequires:  (crate(hashbrown) >= 0.14.1 with crate(hashbrown) < 0.15.0~)
BuildRequires:  (crate(hashbrown/raw) >= 0.14.1 with crate(hashbrown/raw) < 0.15.0~)
BuildRequires:  rust >= 1.63
%if %{with check}
BuildRequires:  (crate(fnv/default) >= 1.0.0 with crate(fnv/default) < 2.0.0~)
BuildRequires:  (crate(fxhash/default) >= 0.2.1 with crate(fxhash/default) < 0.3.0~)
BuildRequires:  (crate(itertools/default) >= 0.13.0 with crate(itertools/default) < 0.14.0~)
BuildRequires:  (crate(lazy_static/default) >= 1.3.0 with crate(lazy_static/default) < 2.0.0~)
BuildRequires:  (crate(quickcheck) >= 1.0.0 with crate(quickcheck) < 2.0.0~)
BuildRequires:  (crate(rand/default) >= 0.8.0 with crate(rand/default) < 0.9.0~)
BuildRequires:  (crate(rand/small_rng) >= 0.8.0 with crate(rand/small_rng) < 0.9.0~)
BuildRequires:  (crate(serde_derive/default) >= 1.0.0 with crate(serde_derive/default) < 2.0.0~)
%endif

%global _description %{expand:
A hash table with consistent order and fast iteration.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap) = 2.3.0
Requires:       (crate(equivalent) >= 1.0.0 with crate(equivalent) < 2.0.0~)
Requires:       (crate(hashbrown) >= 0.14.1 with crate(hashbrown) < 0.15.0~)
Requires:       (crate(hashbrown/raw) >= 0.14.1 with crate(hashbrown/raw) < 0.15.0~)
Requires:       cargo
Requires:       rust >= 1.63

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/RELEASES.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/default) = 2.3.0
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0
Requires:       crate(indexmap/std) = 2.3.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/arbitrary) = 2.3.0
Requires:       (crate(arbitrary) >= 1.0.0 with crate(arbitrary) < 2.0.0~)
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+borsh-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/borsh) = 2.3.0
Requires:       (crate(borsh) >= 1.2.0 with crate(borsh) < 2.0.0~)
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+borsh-devel %{_description}

This package contains library source intended for building other packages which
use the "borsh" feature of the "%{crate}" crate.

%files       -n %{name}+borsh-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+quickcheck-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/quickcheck) = 2.3.0
Requires:       (crate(quickcheck) >= 1.0.0 with crate(quickcheck) < 2.0.0~)
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+quickcheck-devel %{_description}

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%files       -n %{name}+quickcheck-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/rayon) = 2.3.0
Requires:       (crate(rayon/default) >= 1.5.3 with crate(rayon/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustc-rayon-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/rustc-rayon) = 2.3.0
Requires:       (crate(rustc-rayon/default) >= 0.5.0 with crate(rustc-rayon/default) < 0.6.0~)
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+rustc-rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rustc-rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rustc-rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/serde) = 2.3.0
Requires:       (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0~)
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/std) = 2.3.0
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+test_debug-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(indexmap/test_debug) = 2.3.0
Requires:       cargo
Requires:       crate(indexmap) = 2.3.0

%description -n %{name}+test_debug-devel %{_description}

This package contains library source intended for building other packages which
use the "test_debug" feature of the "%{crate}" crate.

%files       -n %{name}+test_debug-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
