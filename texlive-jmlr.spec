Name:		texlive-jmlr
Version:	1.24
Release:	1
Summary:	Class files for the Journal of Machine Learning Research
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jmlr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The jmlr bundle provides a class for authors (jmlr) and a class
for production editors (jmlrbook), as well as a script
makejmlrbook The jmlrbook class may can be used to combine
articles written using the jmlr class into a book. The class
uses the combine class and the hyperref package to produce
either a colour hyperlinked book for on-line viewing or a
greyscale nonhyperlinked book for printing. The makejmlrbook
Perl script can be used to create the colour hyperlinked and
greyscale nonhyperlinked PDFs of a document using the jmlrbook
class. It can also create a set of HTML files that list the
included papers with links to their abstracts and the
individual articles as PDFs.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/jmlr
%{_texmfdistdir}/tex/latex/jmlr
%doc %{_texmfdistdir}/doc/latex/jmlr
#- source
%doc %{_texmfdistdir}/source/latex/jmlr

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
