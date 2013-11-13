%bcond_without bootstrap
%global packname  statmod
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.4.18
Release:          2
Summary:          Statistical Modeling
Group:            Sciences/Mathematics
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/statmod_1.4.18.tar.gz
Requires:         R-core R-MASS
%if %{without bootstrap}
Requires:         R-tweedie
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS
%if %{without bootstrap}
BuildRequires:    R-tweedie
%endif

%description
Various statistical modeling functions including growth curve comparisons,
limiting dilution analysis, mixed linear models, heteroscedastic
regression, Tweedie family generalized linear models, the inverse-Gaussian
distribution and Gauss quadrature.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4.14-2
+ Revision: 778935
- Rebuild with proper dependencies

* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4.14-1
+ Revision: 776574
- Import R-statmod
- Import R-statmod


