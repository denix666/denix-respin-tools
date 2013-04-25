denix-respin-tools
==================

This package contains the kickstart files and scripts to make own desktop/server respin, live boot CDROM image.

denix-respin-creator - is a script to make respin of the original Fedora installation DVD.
denix-livecd-creator - is a script to make DeniX-OS Live boot CDROM image.

Installation
============

**From yum repository:**

Fedora `19` - install the denix repo:

```vim
#rpm -ivh http://fedora.os.vc/yum/base/19/i386/denix-x-repo-1.0-4.fc19.noarch.rpm
```
and then install the package as regular:

```vim
#yum install denix-respin-tools
```


**Manual RPM installation:**

If you want to install this package manualy, download the latest version from one of my mirrors:

http://mirror.os.vc/denix-repo/yum/base/19

and install it by using this command as root:

```vim
#rpm -ivh denix-respin-tools.xx.x-xx.x1.noarch.rpm
```


**Howto build RPM from source:**

Clone my git repository and run the build script:

```vim
$mkdir git-repos
$cd git-repos
$git clone https://github.com/denix666/denix-respin-tools.git
$cd denix-respin-tools
$./build_denix-respin-tools.sh
```


Usage
=====

At the moment supported Fedora versions for respin: `14,15,16,17,18` and to build live CD: `18` + Support for `Alpha-19`

Review and edit the kickstart files in `/usr/share/denix-respin-tools/kickstart.d`

To build the same of running version respin execute:
```vim
#denix-respin-creator
```

To build the next version of respin from running box execute:
```vim
#denix-respin-creator --dest_ver=<next_ver>
```
