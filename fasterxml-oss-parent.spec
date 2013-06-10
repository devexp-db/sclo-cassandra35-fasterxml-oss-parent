%global oname oss-parent
Name:          fasterxml-oss-parent
Version:       10
Release:       1%{?dist}
Summary:       FasterXML parent pom
Group:         Development/Libraries
# pom file licenses ASL 2.0 and LGPL 2.1
License:       ASL 2.0 and LGPLv2+
URL:           http://fasterxml.com/
# git clone git://github.com/FasterXML/oss-parent.git fasterxml-oss-parent-4
# (cd fasterxml-oss-parent-4/ && git archive --format=tar --prefix=fasterxml-oss-parent-4/ oss-parent-4 | xz > ../fasterxml-oss-parent-4-src-git.tar.xz)
Source0:       https://github.com/FasterXML/oss-parent/archive/oss-parent-%{version}.tar.gz

BuildRequires: java-devel

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin
BuildRequires: replacer

Requires:      replacer

Requires:      java
BuildArch:     noarch

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

%prep
%setup -q -n %{oname}-%{oname}-%{version}

%pom_remove_plugin org.sonatype.plugins:nexus-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin org.codehaus.mojo:taglist-maven-plugin
# remove unavailable com.google.doclava doclava 1.0.3
%pom_xpath_remove "pom:build/pom:extensions/pom:extension[pom:artifactId='wagon-gitsite']"
%pom_xpath_remove "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']" '
<configuration>
  <encoding>UTF-8</encoding>
  <quiet>true</quiet>
  <source>${javac.src.version}</source>
</configuration>'

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
* Tue May 07 2013 gil cattaneo <puntogil@libero.it> 10-1
- update to 10

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 4-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 24 2012 gil cattaneo <puntogil@libero.it> 4-1
- update to 4

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 3-1
- initial rpm