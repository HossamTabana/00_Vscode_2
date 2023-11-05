# Use an ARM-based Python runtime as a parent image
FROM arm64v8/python:3.8-buster as base

# Set the working directory in the container
WORKDIR /workspace

# Environment Variables
ENV HADOOP_VERSION=3.3.6
ENV PATH /miniconda/bin:$PATH

# 1. Install Java, wget and other dependencies
RUN apt-get update && \
    apt-get install -y default-jdk wget && \
    rm -rf /var/lib/apt/lists/* 

# 2. Install Hadoop
RUN wget https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz && \
    tar -xzvf hadoop-$HADOOP_VERSION.tar.gz && \
    mv hadoop-$HADOOP_VERSION /usr/local/hadoop && \
    rm hadoop-$HADOOP_VERSION.tar.gz

# 3. Install Python packages
RUN pip install pyspark pandas numpy scipy scikit-learn

# 4. Install Miniconda (you'll need to find an ARM64-compatible Miniconda installer)
# Instructions here are for x86_64 so you'll need to adapt this part
# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
#     bash miniconda.sh -b -p /miniconda && \
#     rm miniconda.sh

# 5. Create a Conda environment
# RUN conda create --name pyspark_ibra

# The code to run the app when the container is started
CMD ["bash"]
