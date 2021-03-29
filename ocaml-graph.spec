#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), remove when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		_enable_debug_packages	0

Summary:	OCaml library for arc and node graphs
Name:		ocaml-graph
Version:	1.8.8
Release:	1
License:	LGPLv2 with exceptions
Group:		Libraries
Source0:	http://ocamlgraph.lri.fr/download/ocamlgraph-%{version}.tar.gz
# Source0-md5:	9d71ca69271055bd22d0dfe4e939831a
URL:		http://ocamlgraph.lri.fr/
BuildRequires:	libart_lgpl-devel
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-lablgtk2-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ocamlgraph provides several different implementations of graph data
structures. It also provides implementations for a number of classical
graph algorithms like Kruskal's algorithm for MSTs, topological
ordering of DAGs, Dijkstra's shortest paths algorithm, and
Ford-Fulkerson's maximal-flow algorithm to name a few. The algorithms
and data structures are written functorially for maximal reusability.
Also has input and output capability for Graph Modeling Language file
format and Dot and Neato graphviz (graph visualization) tools.

%package devel
Summary:	OCaml library for arc and node graphs - development files
Group:		Development/Libraries
%requires_eq ocaml

%description devel
Ocamlgraph provides several different implementations of graph data
structures. It also provides implementations for a number of classical
graph algorithms like Kruskal's algorithm for MSTs, topological
ordering of DAGs, Dijkstra's shortest paths algorithm, and
Ford-Fulkerson's maximal-flow algorithm to name a few. The algorithms
and data structures are written functorially for maximal reusability.
Also has input and output capability for Graph Modeling Language file
format and Dot and Neato graphviz (graph visualization) tools.

This package contains files needed to develop OCaml programs using
Ocamlgraph library.

%prep
%setup -q -n ocamlgraph-%{version}

%build
%configure

%{__make} -j1 all %{?with_ocaml_opt:opt} \
	CC="%{__cc} %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/ocaml/ocamlgraph,%{_examplesdir}/%{name}-%{version}}

cp -p *.cm[ixao]* %{?with_ocaml_opt:*.a} $RPM_BUILD_ROOT%{_libdir}/ocaml/ocamlgraph
cp -p META $RPM_BUILD_ROOT%{_libdir}/ocaml/ocamlgraph

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS FAQ
%dir %{_libdir}/ocaml/ocamlgraph
%{_libdir}/ocaml/ocamlgraph/META
%{_libdir}/ocaml/ocamlgraph/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ocamlgraph/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%doc LICENSE lib/*.mli src/*.mli
%{_libdir}/ocaml/ocamlgraph/*.cmo
%{_libdir}/ocaml/ocamlgraph/*.cm[ix]
%if %{with ocaml_opt}
%{_libdir}/ocaml/ocamlgraph/*.[ao]
%{_libdir}/ocaml/ocamlgraph/*.cmxa
%endif
%{_examplesdir}/%{name}-%{version}
