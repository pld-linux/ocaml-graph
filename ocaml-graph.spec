#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		_enable_debug_packages	0

Summary:	OCaml library for arc and node graphs
Summary(pl.UTF-8):	Biblioteka OCamla do grafów z wierzchołków i krawędzi
Name:		ocaml-graph
Version:	1.8.8
Release:	2
License:	LGPL v2 with exceptions
Group:		Libraries
Source0:	http://ocamlgraph.lri.fr/download/ocamlgraph-%{version}.tar.gz
# Source0-md5:	9d71ca69271055bd22d0dfe4e939831a
URL:		http://ocamlgraph.lri.fr/
BuildRequires:	libart_lgpl-devel
BuildRequires:	ocaml >= 3.10.0
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ocaml-lablgtk2-gnome-devel
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

%description -l pl.UTF-8
Ocamlgraph udostępnia kilka różnych implementacji struktur danych
grafów. Zawiera także implementacje wielu klasycznych algorytmów
grafowych, m.in. algorytm Kruskala wyznaczania drzewa rozpinającego,
sortowania topologicznego skierowanych grafów acyklicznych, algorytm
najkrótszej ścieżki Dijkstry, algorytm maksymalnego przepływu
Forda-Fulkersona. Algorytmy i struktury danych zostały napisane w
oparciu o funktory w celu zwiększenia możliwości zastosowań. Możliwe
jest także wejście i wyjście w postaci formatu plików Graph Modeling
Language oraz narzędzi Dot i Neato z projektu graphviz (służącego do
wizualizacji grafów).

%package devel
Summary:	OCaml library for arc and node graphs - development files
Summary(pl.UTF-8):	Biblioteka OCamla do grafów łuków i węzłów - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
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

%description devel -l pl.UTF-8
Ocamlgraph udostępnia kilka różnych implementacji struktur danych
grafów. Zawiera także implementacje wielu klasycznych algorytmów
grafowych, m.in. algorytm Kruskala wyznaczania drzewa rozpinającego,
sortowania topologicznego skierowanych grafów acyklicznych, algorytm
najkrótszej ścieżki Dijkstry, algorytm maksymalnego przepływu
Forda-Fulkersona. Algorytmy i struktury danych zostały napisane w
oparciu o funktory w celu zwiększenia możliwości zastosowań. Możliwe
jest także wejście i wyjście w postaci formatu plików Graph Modeling
Language oraz narzędzi Dot i Neato z projektu graphviz (służącego do
wizualizacji grafów).

Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki Ocamlgraph.

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
%doc CHANGES COPYING CREDITS FAQ LICENSE README.adoc
%dir %{_libdir}/ocaml/ocamlgraph
%{_libdir}/ocaml/ocamlgraph/META
%{_libdir}/ocaml/ocamlgraph/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ocamlgraph/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%doc lib/*.mli src/*.mli
%{_libdir}/ocaml/ocamlgraph/*.cmi
%{_libdir}/ocaml/ocamlgraph/*.cmo
%if %{with ocaml_opt}
%{_libdir}/ocaml/ocamlgraph/*.a
%{_libdir}/ocaml/ocamlgraph/*.cmx
%{_libdir}/ocaml/ocamlgraph/*.cmxa
%endif
%{_examplesdir}/%{name}-%{version}
