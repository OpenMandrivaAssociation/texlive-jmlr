%global tl_name jmlr
%global tl_revision 61957

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.30
Release:	%{tl_revision}.1
Summary:	Class files for the Journal of Machine Learning Research
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jmlr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The jmlr bundle provides a class for authors (jmlr) and a class for
production editors (jmlrbook). The jmlrbook class can be used to combine
articles written using the jmlr class into a book. The class uses the
combine class and the hyperref package to produce either a colour
hyperlinked book for on-line viewing or a greyscale nonhyperlinked book
for printing. Production editors can use makejmlrbookgui to help build
the proceedings from the articles.

