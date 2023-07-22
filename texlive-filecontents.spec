Name:		texlive-filecontents
Version:	66740
Release:	1
Summary:	Extended filecontents and filecontents* environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/filecontents
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
