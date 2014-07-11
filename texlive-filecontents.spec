# revision 24250
# category Package
# catalog-ctan /macros/latex/contrib/filecontents
# catalog-date 2011-10-09 16:42:04 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-filecontents
Version:	1.3
Release:	8
Summary:	Extended filecontents and filecontents* environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/filecontents
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX2e's filecontents and filecontents* environments enable a
LaTeX source file to generate external files as it runs through
LaTeX. However, there are two limitations of these
environments: they refuse to overwrite existing files, and they
can only be used in the preamble of a document. The
filecontents package removes these limitations, letting you
overwrite existing files and letting you use
filecontents/filecontents* anywhere.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/filecontents/filecontents.sty
%doc %{_texmfdistdir}/doc/latex/filecontents/README
%doc %{_texmfdistdir}/doc/latex/filecontents/filecontents.pdf
#- source
%doc %{_texmfdistdir}/source/latex/filecontents/filecontents.dtx
%doc %{_texmfdistdir}/source/latex/filecontents/filecontents.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 751840
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718437
- texlive-filecontents
- texlive-filecontents
- texlive-filecontents
- texlive-filecontents

