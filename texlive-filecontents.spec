%global tl_name filecontents
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5a
Release:	%{tl_revision}.1
Summary:	Create an external file from within a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filecontents
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filecontents.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX2e's filecontents and filecontents* environments enable a LaTeX
source file to generate external files as it runs through LaTeX.
However, there are two limitations of these environments: they refuse to
overwrite existing files, and they can only be used in the preamble of a
document. The filecontents package removes these limitations, letting
you overwrite existing files and letting you use
filecontents/filecontents* anywhere. As of September 2019 the author
tells us: "This package is no longer necessary due to its functionality
having moved into recent LaTeX kernels. It's probably better not to move
the package to obsolete because users may need it to rebuild old
documents. Version 1.5 provides full functionality when run with an
older kernel but issues a warning message and disables itself when run
with a newer kernel." Supply the overwrite option to LaTeX's built-in
filecontents environment to mimic this package's behavior:
\begin{filecontents}[overwrite]{my-file}...\end{filecontents}

