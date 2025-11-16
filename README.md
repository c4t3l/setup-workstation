# Workstation

[![Copr build status](https://copr.fedorainfracloud.org/coprs/rcallicotte/setup-workstation/package/setup-workstation/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/rcallicotte/setup-workstation/package/setup-workstation/)

This is a playbook for setting up a KDE workstation.

## Using kitchen-ci

You must have the following installed to automate this playbook:

- rubygem-test-kitchen
- rubygem-kitchen-ansible
- rubygem-kitchen-qemu

### Test image

You must provide your own image.  This repo supports qcow2 based images for use with the `kitchen-qemu` driver.

Suggestions: 

- kiwi
- mkosi

### Runing kitchen

The usual way: `kitchen test`
Quick way: `kitchen verify`
Setup: `kitchen converge`
With sdl: `DPY=sdl kitchen converge`
With gtk: `DPY=gtk kitchen converge`

You must have sdl and/or gtk installed to display graphical console.

## References

- https://kitchen.ci/docs/getting-started/introduction/
- https://github.com/neillturner/kitchen-ansible
- https://github.com/esmil/kitchen-qemu/
- https://docs.pytest.org/en/stable/
- https://testinfra.readthedocs.io/en/latest/index.html
- https://osinside.github.io/kiwi/
- https://mkosi.systemd.io/
