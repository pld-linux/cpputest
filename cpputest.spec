Summary:	CppUTest unit testing and mocking framework for C/C++
Summary(pl.UTF-8):	CppUTest - szkielet testów jednostkowych i atrap dla C/C++
Name:		cpputest
Version:	3.8
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	https://github.com/cpputest/cpputest/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e8fdbbb5dd37d32d65919f240f984905
URL:		https://cpputest.github.io/
BuildRequires:	libstdc++-devel >= 6:4.7
Requires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
CppUTest unit testing and mocking framework for C/C++.

%description -l pl.UTF-8
CppUTest - szkielet testów jednostkowych i atrap dla C/C++.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README.md README_CppUTest_for_C.txt README_UsersOfPriorVersions.txt
%{_libdir}/libCppUTest.a
%{_libdir}/libCppUTestExt.a
%{_includedir}/CppUTest
%{_includedir}/CppUTestExt
%{_pkgconfigdir}/cpputest.pc
