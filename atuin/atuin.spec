%global debug_package %{nil}

Name: atuin
Version: 18.0.2
Release: %autorelease
Summary: Magical shell history

License: MIT
URL: https://github.com/atuinsh/atuin
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: gcc

%description
Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.

%prep
%autosetup -p1

%build
cargo build --release

for completion in "bash" "fish" "zsh"; do
    target/release/atuin gen-completions --shell $completion -o .
done

%install
install -Dpm 755 target/release/atuin %{buildroot}%{_bindir}/atuin

install -Dpm 644 atuin.bash %{buildroot}%{_datadir}/bash-completion/completions/atuin
install -Dpm 644 atuin.bash %{buildroot}%{_datadir}/fish/completions/atuin
install -Dpm 644 atuin.bash %{buildroot}%{_datadir}/zsh/site-functions/atuin

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json

strip --strip-all %{buildroot}%{_bindir}/*


%files
%license LICENSE
%doc README.md
%doc docs/docs
%{_bindir}/atuin
%{_datadir}/bash-completion/completions/atuin
%{_datadir}/fish/completions/atuin
%{_datadir}/zsh/site-functions/atuin

%changelog
%autochangelog

