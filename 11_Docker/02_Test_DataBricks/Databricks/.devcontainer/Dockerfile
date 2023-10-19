# Choose your desired base image
FROM jupyter/pyspark-notebook:latest

# name your environment and choose the python version
ARG conda_env=vscode_pyspark_ibrahho
ARG py_ver=3.11

# create environment with necessary libraries
RUN mamba create --yes -p "${CONDA_DIR}/envs/${conda_env}" python=${py_ver} ipython ipykernel pyodbc openjdk-8-jre-headless && \
    mamba clean --all -f -y

# create Python kernel and link it to jupyter
RUN "${CONDA_DIR}/envs/${conda_env}/bin/python" -m ipykernel install --user --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# additional pip installs
RUN "${CONDA_DIR}/envs/${conda_env}/bin/pip" install pyspark pandas numpy matplotlib --no-cache-dir

# Copy the Databricks JDBC driver from the build context to the container
COPY DatabricksJDBC42.jar /opt/DatabricksJDBC42.jar

# default environment activation
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"
