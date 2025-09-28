# Base image: lightweight Ubuntu
FROM ubuntu:20.04

# Disable interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Java (required for Hadoop), Python3, SSH, wget
RUN apt-get update && apt-get install -y openjdk-8-jdk python3 python3-pip ssh rsync wget curl nano vim && apt-get clean

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install Hadoop 3.2.1
# RUN wget https://downloads.apache.org/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz && tar -xvzf hadoop-3.2.1.tar.gz && mv hadoop-3.2.1 /usr/local/hadoop && rm hadoop-3.2.1.tar.gz
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz && tar -xvzf hadoop-3.3.6.tar.gz && mv hadoop-3.3.6 /usr/local/hadoop && rm hadoop-3.3.6.tar.gz


# Set Hadoop environment variables
ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Copy Python MapReduce scripts into container
WORKDIR /root
COPY mapper.py reducer.py mapper1.py reducer1.py ./

# Expose Hadoop web UI ports (optional)
EXPOSE 9870 8088

# Default command: start bash (user can run Hadoop manually)
CMD ["/bin/bash"]
