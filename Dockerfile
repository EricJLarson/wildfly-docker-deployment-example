FROM jboss/wildfly
ADD standalone.xml /opt/jboss/wildfly/standalone/configuration/
ADD helloworld.war /opt/jboss/wildfly/standalone/deployments/
