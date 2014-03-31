Name:           iwidgets
BuildRequires:  tcl-devel
Version:        4.1
Release:        %mkrel 3
Source0:        %{name}41.tgz
BuildArch:      noarch
Summary:        Widget Extension for Tcl/Tk
License:        MIT
Group:          System/Libraries
Requires:       itk
URL: http://chiselapp.com/user/rene/repository/iwidgets/index

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
%setup -q -n %name%version
sed -i -e "s/itk 4/Itk/" library/pkgIndex.tcl

%build

%install
mkdir -p %buildroot%tcl_sitelib
cp -a library %buildroot%tcl_sitelib/%name%version

%files
%doc license.terms README
%tcl_sitelib/%name%version


%changelog
* Mon Oct 21 2013 umeabot <umeabot> 4.1-3.mga4
+ Revision: 538724
- Mageia 4 Mass Rebuild

* Wed Oct 02 2013 joequant <joequant> 4.1-2.mga4
+ Revision: 490244
- make this work with older Itk

* Tue Oct 01 2013 joequant <joequant> 4.1-1.mga4
+ Revision: 490105
- change group
- imported package iwidgets

