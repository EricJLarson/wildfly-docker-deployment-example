FROM jboss/wildfly
RUN rm /opt/jboss/wildfly/domain/configuration/*.xml
RUN rm /opt/jboss/wildfly/standalone/configuration/standalone*.xml
ADD standalone.xml /opt/jboss/wildfly/standalone/configuration/
ADD helloworld.war /opt/jboss/wildfly/standalone/deployments/

USER root
RUN echo "root:abc123" | chpasswd

ADD yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/
ADD yum.repos.d/CentOS-CR.repo /etc/yum.repos.d/
ADD yum.repos.d/CentOS-Sources.repo /etc/yum.repos.d/
ADD yum.repos.d/CentOS-x86_64-kernel.repo /etc/yum.repos.d/
RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python3 python3-pip

USER jboss 

