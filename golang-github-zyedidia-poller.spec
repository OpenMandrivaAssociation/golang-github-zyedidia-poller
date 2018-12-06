# Run tests in check section
# Tests fail on ppc/aarch64
%ifarch ppc ppc64 ppc64le aarch64
%bcond_with check
%else
%bcond_without check
%endif

%global goipath         github.com/zyedidia/poller
%global commit          ab09682913b79f402713d1df1977dedc19eb25ac

%global common_description %{expand:
An epoll(7)-based file-descriptor multiplexer.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: An epoll(7)-based file-descriptor multiplexer
License: BSD
URL:     %{gourl}
Source:  %{gosource}

Patch0:  poller-ab09682-fix_import.patch

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q
%patch0 -p1


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitab09682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180314gitab09682
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170616gitab09682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20170616gitab09682
- First package for Fedora

