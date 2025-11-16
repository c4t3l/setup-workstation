Name:           setup-workstation
Version:        2025.11.1
Release:        1%{?dist}
Summary:        Ansible-based Workstation Setup

License:        MIT
URL:            https://github.com/c4t3l/setup-workstation
Source0:        %{url}/archive/%{version}/setup-workstation-%{version}.tar.gz

BuildRequires:  ansible
Requires:       ansible
Requires:       ansible-collection-community-general

BuildArch:      noarch

%description
KDE-based workstation setup and initial configuration.

%prep
%autosetup


%build
# Nothing to build


%install
install -Dpm 0644 -t %{buildroot}/opt/%{name} default.yml
install -Dpm 0644 -t %{buildroot}/opt/%{name} hosts
install -Dpm 0644 -t %{buildroot}/opt/%{name}/vars vars/*
cp -prv roles %{buildroot}/opt/%{name}/.

install -Dpm 0755 -t %{buildroot}/opt/%{name}/dist dist/*
%dnl install -Dpm 0755 -t %{buildroot}/opt/%{name} %{name}.desktop


%check
ansible-playbook -vvvv --syntax-check --inventory hosts default.yml 

%files
%license LICENSE
%doc README.md
/opt/setup-workstation/



%changelog
* Sat Nov 15 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.1
- Initial build
