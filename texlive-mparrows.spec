Name:		texlive-mparrows
Version:	39729
Release:	2
Summary:	MetaPost module with different types of arrow heads
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mparrows
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparrows.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mparrows.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to provide different types of arrow heads to be used
with MetaPost commands drawarrow and drawdblarrow commands.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/metapost/mparrows
%doc %{_texmfdistdir}/doc/metapost/mparrows

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
