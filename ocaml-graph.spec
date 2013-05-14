Summary:	OCaml library for arc and node graphs
Name:		ocaml-graph
Version:	1.8.2
Release:	2
License:	LGPLv2 with exceptions
Group:		Libraries
Source0:	http://ocamlgraph.lri.fr/download/ocamlgraph-%{version}.tar.gz
# Source0-md5:	efa4394bc4651c90de443ff61c7477e6
URL:		http://ocamlgraph.lri.fr/
BuildRequires:	libart_lgpl-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ocaml-lablgtk2-gnome-devel
BuildRequires:	ocaml >= 3.04-7
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ocamlgraph provides several different implementations of graph data
structures. It also provides implementations for a number of classical
graph algorithms like Kruskal's algorithm for MSTs, topological
ordering of DAGs, Dijkstra's shortest paths algorithm, and
Ford-Fulkerson's maximal-flow algorithm to name a few. The algorithms
and data structures are written functorially for maximal
reusability. Also has input and output capability for Graph Modeling
Language file format and Dot and Neato graphviz (graph visualization)
tools.

%package devel
Summary:	OCaml library for arc and node graphs - development files
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
Ocamlgraph provides several different implementations of graph data
structures. It also provides implementations for a number of classical
graph algorithms like Kruskal's algorithm for MSTs, topological
ordering of DAGs, Dijkstra's shortest paths algorithm, and
Ford-Fulkerson's maximal-flow algorithm to name a few. The algorithms
and data structures are written functorially for maximal
reusability. Also has input and output capability for Graph Modeling
Language file format and Dot and Neato graphviz (graph visualization)
tools.

This package contains files needed to develop OCaml programs using
Ocamlgraph library.

%prep
%setup -q -n ocamlgraph-%{version}

%build
%configure

%{__make} CC="%{__cc} %{rpmcflags} -fPIC" opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{ocamlgraph,stublibs}
install *.cm[ixa]* *.a $RPM_BUILD_ROOT%{_libdir}/ocaml/ocamlgraph

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ocamlgraph
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ocamlgraph/META <<EOF
requires = ""
version = "%{version}"
description = "Generic Graph Library"
directory = "+ocamlgraph"
archive(byte) = "graph.cma"
archive(native) = "graph.cmxa"
linkopts = ""
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc CHANGES CREDITS FAQ
%doc LICENSE lib/*.mli src/*.mli
%dir %{_libdir}/ocaml/ocamlgraph
%{_libdir}/ocaml/ocamlgraph/*.cm[ixa]*
%{_libdir}/ocaml/ocamlgraph/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/ocamlgraph
