%global tl_name mparrows
%global tl_revision 39729

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	MetaPost module with different types of arrow heads
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/mparrows
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mparrows.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mparrows.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to provide different types of arrow heads to be used with
MetaPost commands drawarrow and drawdblarrow commands.

