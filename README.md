denix-respin-tools
==================

denix-respin-tools - is a set of the scripts to make respin of the original Fedora installation DVD. This package contains the kickstart files and script to make own desktop/server respin.


Installation
============

**From yum repository:**

Fedora `16,17` - install the denix-x repo:

```vim
#rpm -ivh http://fedora.os.vc/yum/base/x1/i386/denix-repo-1.1-2.x1.noarch.rpm
```
and then install the package as regular:

```vim
#yum install denix-respin-tools
```


**Manual RPM installation:**

If you want to install this package manualy, download the latest version from one of my mirrors:

http://mirror.os.vc/denix-repo/yum/base/x1

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

At the moment supported Fedora versions: `14,15,16,17`

Review and edit the kickstart files in `/usr/share/denix-respin-tools/kickstart.d`

To build the same of running version respin execute:
```vim
#denix-respin-creator
```

To build the next version of respin from running box execute:
```vim
#denix-respin-creator --dest_ver=<next_ver>
```
