
# Choose your desired base image
FROM ibrahho/pyspark-notebook:latest

# name your environment and choose the python version
ARG conda_env=pyspark_ibrahho_test
ARG py_ver=3.11

# you can add additional libraries you want mamba to install by listing them below the first line and ending with "&& \"
RUN mamba create --yes -p "${CONDA_DIR}/envs/${conda_env}" python=${py_ver} ipython ipykernel && \
    mamba clean --all -f -y

# alternatively, you can comment out the lines above and uncomment those below
# if you'd prefer to use a YAML file present in the docker build context

# COPY --chown=${NB_UID}:${NB_GID} environment.yml "/home/${NB_USER}/tmp/"
# RUN cd "/home/${NB_USER}/tmp/" && \
#     mamba env create -p "${CONDA_DIR}/envs/${conda_env}" -f environment.yml && \
#     mamba clean --all -f -y

# create Python kernel and link it to jupyter
RUN set -e; \
    permission_fix() { \
        for d in "$@"; do \
            find "${d}" \
                ! \( \
                    -group "${NB_GID}" \
                    -a -perm -g+rwX \
                \) \
                -exec chgrp "${NB_GID}" -- {} \+ \
                -exec chmod g+rwX -- {} \+ ; \
            find "${d}" \
                \( \
                    -type d \
                    -a ! -perm -6000 \
                \) \
                -exec chmod +6000 -- {} \+ ; \
        done \
    }; \ 
        "${CONDA_DIR}/envs/${conda_env}/bin/python" -m ipykernel install --user --name="${conda_env}" && \
        permission_fix "${CONDA_DIR}" "/home/${NB_USER}"

# any additional pip installs can be added by uncommenting the following line
RUN "${CONDA_DIR}/envs/${conda_env}/bin/pip" install pyspark pandas --no-cache-dir

# if you want this environment to be the default one, uncomment the following line:
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"
