Name:           snapraid-aio-script
Summary:        The definitive all-in-one SnapRAID script.
Version:        3.2
Release:        1%{?dist}
License:        GPLv3+
Group:          Applications/System
URL:            https://github.com/auanasgheps/snapraid-aio-script
Source:         https://github.com/auanasgheps/snapraid-aio-script/archive/refs/tags/v%{version}.tar.gz

%description
The definitive all-in-one SnapRAID script. I hope you'll agree :).
There are many SnapRAID scripts out there, but none has the features I want. So I made my own, inspired by existing solutions.
It is meant to be run periodically (daily), do the heavy lifting and send an email you will actually read.

Supports single and dual parity configurations. It is highly customizable and has been tested with Debian 10/11 and OpenMediaVault 5/6.

%prep
%setup -q

%build

%install
install -d -m 0755 $RPM_BUILD_ROOT/opt/snapraid-aio
install -m 0755 script-config.sh $RPM_BUILD_ROOT/opt/snapraid-aio/script-config.sh
install -m 0755 snapraid-aio-script.sh $RPM_BUILD_ROOT/opt/snapraid-aio/snapraid-aio-script.sh

%files
%doc README.md LICENSE
/opt/snapraid-aio/script-config.sh
/opt/snapraid-aio/snapraid-aio-script.sh

%changelog
* Sat Jul 15 2023 Gordon Schulz <gordon@gordonschulz.de>
Initial commit
