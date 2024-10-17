Name:		texlive-jmlr
Version:	61957
Release:	2
Summary:	Class files for the Journal of Machine Learning Research
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jmlr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmlr.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/jmlr
%doc %{_texmfdistdir}/doc/latex/jmlr
#- source
%doc %{_texmfdistdir}/source/latex/jmlr

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
