# Deployment with the `jboss/wildfly` Docker image

## Instructions

1. (Optional) In the same directory as _Dockerfile_ place your `helloworld.war`, which will be generated by building source.  See _Application source code_ below. 
2. Run the build with `docker build --tag=wildfly-app .`
3. Run the container with `docker run -it -p 8080:8080 wildfly-app`. Application will be deployed on the container boot.
4. Use `curl` to see the app working:

        $ curl http://localhost:8080/node-info/
```
<html><head><title>helloworld</title></head><body>
<h1>Hello World!</h1>
</body></html>
```

## Example log

```
$ docker run -it wildfly-app
=========================================================================

  JBoss Bootstrap Environment

  JBOSS_HOME: /opt/jboss/wildfly

  JAVA: java

  JAVA_OPTS:  -server -Xms64m -Xmx512m -XX:MaxPermSize=256m -Djava.net.preferIPv4Stack=true -Djboss.modules.system.pkgs=org.jboss.byteman -Djava.awt.headless=true

=========================================================================

09:03:24,625 INFO  [org.jboss.modules] (main) JBoss Modules version 1.3.3.Final
09:03:24,889 INFO  [org.jboss.msc] (main) JBoss MSC version 1.2.2.Final
09:03:24,960 INFO  [org.jboss.as] (MSC service thread 1-8) JBAS015899: WildFly 8.1.0.Final "Kenny" starting
09:03:26,013 INFO  [org.jboss.as.server] (Controller Boot Thread) JBAS015888: Creating http management service using socket-binding (management-http)

[SNIP]

09:03:26,938 INFO  [org.jboss.as.server.deployment] (MSC service thread 1-1) JBAS015876: Starting deployment of "node-info.war" (runtime-name: "node-info.war")
09:03:26,948 INFO  [org.jboss.as.server.deployment.scanner] (MSC service thread 1-4) JBAS015012: Started FileSystemDeploymentService for directory /opt/jboss/wildfly/standalone/deployments
09:03:26,996 INFO  [org.jboss.as.connector.subsystems.datasources] (MSC service thread 1-5) JBAS010400: Bound data source [java:jboss/datasources/ExampleDS]
09:03:27,064 WARN  [org.jboss.metadata.parser.jbossweb.JBossWebMetaDataParser] (MSC service thread 1-4) <replication-mode/> is no longer supported and will be ignored
09:03:27,237 INFO  [org.jboss.ws.common.management] (MSC service thread 1-8) JBWS022052: Starting JBoss Web Services - Stack CXF Server 4.2.4.Final
09:03:27,327 INFO  [org.jboss.weld.deployer] (MSC service thread 1-1) JBAS016002: Processing weld deployment node-info.war
09:03:27,375 INFO  [org.hibernate.validator.internal.util.Version] (MSC service thread 1-1) HV000001: Hibernate Validator 5.1.0.Final
09:03:27,485 INFO  [org.jboss.weld.deployer] (MSC service thread 1-2) JBAS016005: Starting Services for CDI deployment: node-info.war
09:03:27,511 INFO  [org.jboss.weld.Version] (MSC service thread 1-2) WELD-000900: 2.1.2 (Final)

[SNIP]

09:03:28,428 INFO  [org.wildfly.extension.undertow] (MSC service thread 1-8) JBAS017534: Registered web context: /node-info
09:03:28,481 INFO  [org.jboss.as.server] (ServerService Thread Pool -- 28) JBAS018559: Deployed "node-info.war" (runtime-name : "node-info.war")
09:03:28,637 INFO  [org.jboss.as] (Controller Boot Thread) JBAS015961: Http management interface listening on http://0.0.0.0:9990/management
09:03:28,638 INFO  [org.jboss.as] (Controller Boot Thread) JBAS015951: Admin console listening on http://0.0.0.0:9990
09:03:28,638 INFO  [org.jboss.as] (Controller Boot Thread) JBAS015874: WildFly 8.1.0.Final "Kenny" started in 4679ms - Started 296 of 341 services (96 services are lazy, passive or on-demand)
```

## Application source code

To create _helloworld.war_ clone [Quickstart repo](https://github.com/wildfly/quickstart.git), then in _quickstart/helloworld/_ run `mvn package`.

