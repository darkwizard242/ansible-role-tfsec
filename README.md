[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-tfsec.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-tfsec) ![Ansible Role](https://img.shields.io/ansible/role/48533?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/48533?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/48533?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-tfsec&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-tfsec) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-tfsec?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-tfsec?color=orange&style=flat-square)

# Ansible Role: tfsec

Role to install (_by default_) `tfsec` on **Debian/Ubuntu** and **EL** systems. [Scout](https://github.com/liamg/tfsec) is a static analysis (security based) for scanning terraform code. originally developed by [Liam Galvin](https://github.com/liamg).

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
tfsec_app: tfsec
tfsec_version: 0.22.0
tfsec_osarch: linux-amd64
tfsec_dl_url: https://github.com/liamg/{{ tfsec_app }}/releases/download/v{{ tfsec_version }}/{{ tfsec_app }}-{{ tfsec_osarch }}
tfsec_bin_path: "/usr/local/bin/{{ tfsec_app }}"
tfsec_bin_permission_mode: '0755'
```

### Variables table:

Variable                  | Value (default)                                                                                                      | Description
------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------
tfsec_app                 | tfsec                                                                                                                | Defines the app to install i.e. **tfsec**
tfsec_version             | 0.22.0                                                                                                               | Defined to dynamically fetch the desired version to install. Defaults to: **0.22.0**
tfsec_osarch              | linux-amd64                                                                                                          | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **linux-amd64**
tfsec_dl_url              | <https://github.com/liamg/{{> tfsec_app }}/releases/download/v{{ tfsec_version }}/{{ tfsec_app }}-{{ tfsec_osarch }} | Defines URL to download the tfsec binary from.
tfsec_bin_path            | "/usr/local/bin/{{ tfsec_app }}"                                                                                     | Defined to dynamically set the appropriate path to store tfsec binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin/tfsec**
tfsec_bin_permission_mode | '0755'                                                                                                               | Defines the permission mode level for the file.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **tfsec**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.tfsec
```

For customizing behavior of role (i.e. specifying the desired **tfsec** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.tfsec
  vars:
    tfsec_version: 0.18.0
```

For customizing behavior of role (i.e. placing binary of **tfsec** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.tfsec
  vars:
    tfsec_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-tfsec/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
