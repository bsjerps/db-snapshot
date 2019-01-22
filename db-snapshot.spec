Name:           db-snapshot
Summary:        Snapshot (clone) of Oracle database using storage snaps
Version:	0.1
Release:	1%{?dtap}
BuildArch:      noarch
Group:		Outrun/Extras
License:	GPLv3+
Source0:	%{name}-%{version}.tbz2

%description
Clones an Oracle database from an ASM based storage snapshot.
Requires a separate storage snapshot refresh script.

%prep
%setup -n %{name}

%install
rm -rf %{buildroot}

%make_install

install -m 0755 -d %{buildroot}/usr/bin

install -m 0755 -pt %{buildroot}/usr/bin bin/*

%files
/usr/bin/*
/usr/share/man/man1/*
/usr/share/%{name}

