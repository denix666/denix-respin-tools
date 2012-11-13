Name:		denix-respin-tools
Version:	17.3
Release:	0%{?dist}
Summary:	Respin scripts by -=DeN=-
Group:		Scripts
License:	GPL
URL:		http://os.vc
Requires:	pungi wget usermode denix-colors
Source0:        %{name}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%description
Set of scripts to make Fedora based respins.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
cp -r %{_builddir}/%{name} %{buildroot}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}

%files
%defattr(-,root,root,-)
%attr(-,root,root) /usr/share/denix-respin-tools/kickstart.d
%attr(-,root,root) /usr/share/denix-respin-tools/isolinux
%attr(0755,root,root) /usr/share/denix-respin-tools/denix-respin-creator
%attr(0755,root,root) /usr/bin/denix-respin-creator
%attr(0644,root,root) /etc/pam.d/denix-respin-creator
%attr(0644,root,root) /etc/security/console.apps/denix-respin-creator
