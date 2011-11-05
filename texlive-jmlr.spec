# revision 21830
# category Package
# catalog-ctan /macros/latex/contrib/jmlr
# catalog-date 2011-03-24 23:50:46 +0100
# catalog-license lppl
# catalog-version 1.11
Name:		texlive-jmlr
Version:	1.11
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The jmlr bundle provides a class for authors (jmlr) and a class
for production editors (jmlrbook), as well as a script
makejmlrbook The jmlrbook class may can be used to combine
articles written using the jmlr class into a book. The jmlrbook
class uses the combine class and the hyperref package to
produce either a colour hyperlinked book for on-line viewing or
a greyscale nonhyperlinked book for printing. The makejmlrbook
Perl script can be used to create the colour hyperlinked and
greyscale nonhyperlinked PDFs of a document using the jmlrbook
class. It can also create a set of HTML files that list the
included papers with links to their abstracts and the
individual articles as PDFs.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/jmlr/makejmlrbook
%{_texmfdistdir}/scripts/jmlr/makejmlrbook.bat
%{_texmfdistdir}/tex/latex/jmlr/jmlr.cls
%{_texmfdistdir}/tex/latex/jmlr/jmlrbook.cls
%doc %{_texmfdistdir}/doc/latex/jmlr/CHANGES
%doc %{_texmfdistdir}/doc/latex/jmlr/INSTALL
%doc %{_texmfdistdir}/doc/latex/jmlr/README
%doc %{_texmfdistdir}/doc/latex/jmlr/jmlr-manual.html
%doc %{_texmfdistdir}/doc/latex/jmlr/jmlr-manual.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/jmlr-manual0x.png
%doc %{_texmfdistdir}/doc/latex/jmlr/jmlr-manual1x.png
%doc %{_texmfdistdir}/doc/latex/jmlr/jmlr-manual2x.png
%doc %{_texmfdistdir}/doc/latex/jmlr/jmlr-manual3x.png
%doc %{_texmfdistdir}/doc/latex/jmlr/jmlr.pdf
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/bookLogo-gray.png
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/bookLogo.png
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/jmlrbook-sample.pdf
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/jmlrbook-sample.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper1/paper1.bib
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper1/paper1.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper2/paper2.bib
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper2/paper2.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper3/paper3.bib
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper3/paper3.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper4/paper4.bib
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/paper4/paper4.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/proceedings-sample.pdf
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-books/proceedings-sample.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/images/circle-gray.png
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/images/circle.jpg
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/images/nodes-gray.png
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/images/nodes.png
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/images/square-gray.png
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/images/square.png
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/images/teximage.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/jmlr-sample.bib
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/jmlr-sample.pdf
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/jmlr-sample.tex
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/jmlrwcp-sample.pdf
%doc %{_texmfdistdir}/doc/latex/jmlr/sample-papers/jmlrwcp-sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/jmlr/jmlr.dtx
%doc %{_texmfdistdir}/source/latex/jmlr/jmlr.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
