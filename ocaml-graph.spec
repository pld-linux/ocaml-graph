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
Version:	2.0.0
Release:	2
License:	LGPL v2.1 with exceptions
Group:		Libraries
#Source0Download: https://github.com/backtracking/ocamlgraph/releases
Source0:	https://github.com/backtracking/ocamlgraph/releases/download/%{version}/ocamlgraph-%{version}.tbz
# Source0-md5:	2d07fcf3501e1d4997c03fa94cea22f0
Patch0:		%{name}-no-stdlib-shims.patch
URL:		http://ocamlgraph.lri.fr/
BuildRequires:	libart_lgpl-devel
BuildRequires:	ocaml >= 3.10.0
BuildRequires:	ocaml-dune >= 2.0
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

%package gtk
Summary:	Displaying graphs using OCamlGraph and GTK
Summary(pl.UTF-8):	Wyświetlanie grafów przy użyciu bibliotek OCamlGraph i GTK
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
Displaying graphs using OCamlGraph and GTK.

%description gtk -l pl.UTF-8
Wyświetlanie grafów przy użyciu bibliotek OCamlGraph i GTK.

%package gtk-devel
Summary:	Displaying graphs using OCamlGraph and GTK - development files
Summary(pl.UTF-8):	Wyświetlanie grafów przy użyciu bibliotek OCamlGraph i GTK - pliki programistyczne
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk-devel
Displaying graphs using OCamlGraph and GTK.

This package contains files needed to develop OCaml programs using
Ocamlgraph GTK library.

%description gtk-devel -l pl.UTF-8
Wyświetlanie grafów przy użyciu bibliotek OCamlGraph i GTK.

Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki Ocamlgraph GTK.

%prep
%setup -q -n ocamlgraph-%{version}
%patch0 -p1

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/{ocamlgraph,ocamlgraph_gtk}/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/{ocamlgraph,ocamlgraph_gtk}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md COPYING CREDITS FAQ LICENSE README.md TODO.md
%dir %{_libdir}/ocaml/ocamlgraph
%{_libdir}/ocaml/ocamlgraph/META
%{_libdir}/ocaml/ocamlgraph/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ocamlgraph/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ocamlgraph/*.cmi
%{_libdir}/ocaml/ocamlgraph/*.cmt
%{_libdir}/ocaml/ocamlgraph/*.cmti
%{_libdir}/ocaml/ocamlgraph/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ocamlgraph/*.a
%{_libdir}/ocaml/ocamlgraph/*.cmx
%{_libdir}/ocaml/ocamlgraph/*.cmxa
%endif
%{_libdir}/ocaml/ocamlgraph/dune-package
%{_libdir}/ocaml/ocamlgraph/opam
%{_examplesdir}/%{name}-%{version}

%files gtk
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/ocamlgraph_gtk
%{_libdir}/ocaml/ocamlgraph_gtk/META
%{_libdir}/ocaml/ocamlgraph_gtk/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ocamlgraph_gtk/*.cmxs
%endif

%files gtk-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ocamlgraph_gtk/*.cmi
%{_libdir}/ocaml/ocamlgraph_gtk/*.cmt
%{_libdir}/ocaml/ocamlgraph_gtk/*.cmti
%{_libdir}/ocaml/ocamlgraph_gtk/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ocamlgraph_gtk/*.a
%{_libdir}/ocaml/ocamlgraph_gtk/*.cmx
%{_libdir}/ocaml/ocamlgraph_gtk/*.cmxa
%endif
%{_libdir}/ocaml/ocamlgraph_gtk/dune-package
%{_libdir}/ocaml/ocamlgraph_gtk/opam
