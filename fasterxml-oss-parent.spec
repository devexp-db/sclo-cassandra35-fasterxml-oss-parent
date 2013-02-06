Name:          fasterxml-oss-parent
Version:       4
Release:       2%{?dist}
Summary:       FasterXML parent pom
Group:         Development/Libraries
License:       ASL 2.0
URL:           http://fasterxml.com/
# git clone git://github.com/FasterXML/oss-parent.git fasterxml-oss-parent-4
# (cd fasterxml-oss-parent-4/ && git archive --format=tar --prefix=fasterxml-oss-parent-4/ oss-parent-4 | xz > ../fasterxml-oss-parent-4-src-git.tar.xz)
Source0:       %{name}-%{version}-src-git.tar.xz

# remove unavailable extension org.kathrynhuxtable.maven.wagon wagon-gitsite 0.3.1
# fix javadoc configration, remove unavailable com.google.doclava doclava 1.0.3
Patch0:        fasterxml-oss-parent-3-pom.patch

BuildRequires: java-devel
BuildRequires: jpackage-utils

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin

Requires:      java
Requires:      jpackage-utils
BuildArch:     noarch

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin

%build
# nothing to do
%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%check
mvn-rpmbuild verify

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE README.creole

%changelog
* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 24 2012 gil cattaneo <puntogil@libero.it> 4-1
- update to 4

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 3-1
- initial rpm