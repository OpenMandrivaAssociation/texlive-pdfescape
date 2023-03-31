Name:		texlive-pdfescape
Version:	53082
Release:	2
Summary:	Implements pdfTeX's escape features using TeX or e-TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfescape
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfescape.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfescape.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfescape.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements pdfTeX's escape features
(\pdfescapehex, \pdfunescapehex, \pdfescapename,
\pdfescapestring) using TeX or e-TeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pdfescape
%{_texmfdistdir}/tex/generic/pdfescape
%doc %{_texmfdistdir}/doc/latex/pdfescape

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
