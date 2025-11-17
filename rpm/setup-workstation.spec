Name:           setup-workstation
Version:        2025.11.6
Release:        1%{?dist}
Summary:        Ansible-based Workstation Setup

License:        MIT
URL:            https://github.com/c4t3l/setup-workstation
Source0:        %{url}/archive/%{version}/setup-workstation-%{version}.tar.gz

BuildRequires:  ansible
BuildRequires:  systemd-rpm-macros
%{?sysusers_requires_compat}


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
install -Dpm 0644 %{S:10} %{buildroot}%{_sysusersdir}/%{name}.conf


%check
ansible-playbook -vvvv --syntax-check --inventory hosts default.yml 


%files
%license LICENSE
%doc README.md
/opt/setup-workstation/
%{_sysusersdir}/%{name}.conf


%changelog
* Mon Nov 17 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.6-1
- Updated to 2025.11.6

* Mon Nov 17 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.5-1
- Update to 2025.11.5

* Mon Nov 17 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.4-1
- Update to 2025.11.4

* Mon Nov 17 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.3-1
- Update to 2025.11.3

* Mon Nov 17 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.2-2
- Fix post install links

* Sun Nov 16 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.2-1
- Update to 2025.11.2

* Sun Nov 16 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.1-2
- Update kroot uid

* Sat Nov 15 2025 Robby Callicotte <rcallicotte@fedoraproject.org> - 2025.11.1
- Initial build
