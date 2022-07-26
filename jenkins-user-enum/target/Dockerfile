FROM jenkins/jenkins:lts-jdk11

RUN jenkins-plugin-cli --plugins matrix-auth:3.1.5

ENV JENKINS_USER admin
ENV JENKINS_PASS admin

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

COPY setup.groovy /usr/share/jenkins/ref/init.groovy.d/
