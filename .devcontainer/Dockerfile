FROM docker.io/jupyter/scipy-notebook:latest

USER root

# Create jovyan group and add user to it
RUN groupadd -f jovyan \
    && usermod -g jovyan -aG users jovyan

# Configure sudo to allow jovyan to execute sudo commands without a password
RUN echo 'jovyan ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/jovyan-nopasswd

# Ensure the file permissions are set correctly
RUN chmod 0440 /etc/sudoers.d/jovyan-nopasswd

# Switch to jovyan user for further setup
USER jovyan