Summary:	A fast logfile IP address resolver and related utilities.
Name:		fastresolve
Version:	2.11
Release:	1
#Copyright:	GPL
License:	GPL
Group:		Utilities
Source:		fastresolve-%{version}.tar.gz
URL:		https://github.com/dmacnet/fastresolve
Vendor:		David MacKenzie
Packager:	fastresolve-bugs@djmnet.org
BuildRoot:	%{_tmppath}/%{name}-root
# There doesn't appear to be a version-independent db-devel virtual
# package, so we have to pick a particular version. Change the below
# line if you want to build against a different version.
BuildRequires:	adns-devel zlib-devel db5-devel
Requires:	perl-BerkeleyDB

# Use an installation of Berkeley DB with C++ support,
# separate from glibc to avoid conflicts with it.
# DB 2.x through 5.x should work.
#define dbroot /usr/BerkeleyDB/2.7
#define dbroot /usr/BerkeleyDB/3.1
%define dbroot /usr/BerkeleyDB/5.4

%description
Fastresolve is a package of programs which process Web log files to
get DNS information for log analysis. It sends many queries in
parallel, and caches results, for speed.

%prep
%setup

%build
# Undo bogus option set by Linux-Mandrake 7.0:
COPTS="-g ${RPM_OPT_FLAGS} -fexceptions"
CPPFLAGS="-I%{dbroot}/include" LDFLAGS="-L%{dbroot}/lib -Wl,-rpath,%{dbroot}/lib" CXXFLAGS="$COPTS" PERL=/usr/bin/perl ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1 $RPM_BUILD_ROOT/%{_datadir}/fastresolve
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README doc/TODO doc/timings
%config /%{_sysconfdir}/fastresolve/analog.cfg
%{_bindir}/dns-terror
%{_mandir}/man1/dns-terror.1*
%{_bindir}/btree-dump
%{_bindir}/convert-ip-db
%{_bindir}/expire-ip-db
%{_bindir}/rebuild-ip-db
%{_bindir}/reresolve
%{_bindir}/make-report
%{_mandir}/man1/btree-dump.1*
%{_mandir}/man1/convert-ip-db.1*
%{_mandir}/man1/expire-ip-db.1*
%{_mandir}/man1/rebuild-ip-db.1*
%{_mandir}/man1/reresolve.1*
%{_mandir}/man1/make-report.1*

%changelog
* Sat May 17 2003 David J. MacKenzie <djm@djmnet.org> 2.10-1
- New release.

* Wed Jan 31 2001 David J. MacKenzie <djm@web.us.uu.net> 2.8-2
- Use more RPM macros to get the right directories.
