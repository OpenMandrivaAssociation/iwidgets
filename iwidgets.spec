Summary:	Widget Extension for Tcl/Tk
Name:		iwidgets
Version:	4.1
Release:	4
License:	MIT
Group:		System/Libraries
Url:		http://chiselapp.com/user/rene/repository/iwidgets/index
Source0:	%{name}41.tgz
BuildArch:	noarch
BuildRequires:	pkgconfig(tcl)
Requires:	itk

%description
[incr Widgets] is an object-oriented mega-widget set that extends
Tcl/Tk and is based on [incr Tcl] and [incr Tk].  This set of
mega-widgets delivers many new, general purpose widgets like option
menus, comboboxes, selection boxes, and various dialogs whose
counterparts are found in Motif and Windows. Since [incr Widgets] is
based on the [incr Tk] extension, the Tk framework of configuration
options, widget commands, and default bindings is maintained.  In other
words, each [incr Widgets] mega-widget seamlessly blends with the
standard Tk widgets. They look, act, and feel like Tk widgets. In
addition, all [incr Widgets] mega-widgets are object oriented and may
themselves be extended, using either inheritance or composition.

%prep
%setup -qn %{name}%{version}
sed -i -e "s/itk 4/Itk/" library/pkgIndex.tcl

%build

%install
mkdir -p %{buildroot}%{tcl_sitelib}
cp -a library %{buildroot}%{tcl_sitelib}/%{name}%{version}

%files
%doc license.terms README
%{tcl_sitelib}/%{name}%{version}

