FROM jboss/wildfly
RUN rm /opt/jboss/wildfly/domain/configuration/*.xml
RUN rm /opt/jboss/wildfly/standalone/configuration/standalone*.xml
ADD standalone.xml /opt/jboss/wildfly/standalone/configuration/
ADD helloworld.war /opt/jboss/wildfly/standalone/deployments/

