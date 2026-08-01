Name:           hitch
Version:        0.1.0
Release:        1%{?dist}
Summary:        Generate and manage systemd units from Podman Compose files
License:        MIT
URL:            https://github.com/kuyacarlo/hitch
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang >= 1.22
BuildRequires:  git

# Vendored deps — no network needed during build
Provides:       bundled(golang(*))

%description
hitch converts Docker Compose files into systemd units managed by
Podman. It handles generation, installation, enable/disable, and lifecycle
operations for rootless or system-wide containers.

%prep
%autosetup -n %{name}-%{version}

%build
export GOFLAGS="-mod=vendor"
go build -o hitch -ldflags "-X main.version=%{version}" .

# Generate shell completions
./hitch completions bash > hitch.bash
./hitch completions zsh > _hitch
./hitch completions fish > hitch.fish

%install
install -Dpm 0755 hitch %{buildroot}%{_bindir}/hitch

# Shell completions
install -Dpm 0644 hitch.bash %{buildroot}%{_datadir}/bash-completion/completions/hitch
install -Dpm 0644 _hitch %{buildroot}%{_datadir}/zsh/site-functions/_hitch
install -Dpm 0644 hitch.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/hitch.fish

%check
export GOFLAGS="-mod=vendor"
go test ./...

%files
%license LICENSE
%{_bindir}/hitch
%{_datadir}/bash-completion/completions/hitch
%{_datadir}/zsh/site-functions/_hitch
%{_datadir}/fish/vendor_completions.d/hitch.fish

%changelog
* Sat Aug 01 2026 kuyacarlo <kuyacarlo@users.noreply.github.com> - 0.1.0-1
- Initial package
