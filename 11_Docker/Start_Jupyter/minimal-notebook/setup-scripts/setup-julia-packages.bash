#!/bin/bash
set -exuo pipefail
# Requirements:
# - Run as non-root user
# - The JULIA_PKGDIR environment variable is set
# - Julia is already set up, with the setup-julia.bash command

# Install base Julia packages
julia -e '
import Pkg;
Pkg.update();
Pkg.add([
    "HDF5",
    "IJulia",
    "Pluto"
]);
Pkg.precompile();
'

# Move the kernelspec out of ${HOME} to the system share location.
# Avoids problems with runtime UID change not taking effect properly
# on the .local folder in the jovyan home dir.
mv "${HOME}/.local/share/jupyter/kernels/julia"* "${CONDA_DIR}/share/jupyter/kernels/"
chmod -R go+rx "${CONDA_DIR}/share/jupyter"
rm -rf "${HOME}/.local"

# Replace fix-permissions for "${JULIA_PKGDIR}" and "${CONDA_DIR}/share/jupyter"
for d in "${JULIA_PKGDIR}" "${CONDA_DIR}/share/jupyter"; do
    find "${d}" \
        ! \( \
            -group "${NB_GID}" \
            -a -perm -g+rwX \
        \) \
        -exec chgrp "${NB_GID}" -- {} \+ \
        -exec chmod g+rwX -- {} \+ ;
    find "${d}" \
        \( \
            -type d \
            -a ! -perm -6000 \
        \) \
        -exec chmod +6000 -- {} \+ ;
done

# Install jupyter-pluto-proxy to get Pluto to work on JupyterHub
mamba install --yes \
    'jupyter-pluto-proxy' && \
    mamba clean --all -f -y

# Replace fix-permissions for "${CONDA_DIR}" and "/home/${NB_USER}"
for d in "${CONDA_DIR}" "/home/${NB_USER}"; do
    find "${d}" \
        ! \( \
            -group "${NB_GID}" \
            -a -perm -g+rwX \
        \) \
        -exec chgrp "${NB_GID}" -- {} \+ \
        -exec chmod g+rwX -- {} \+ ;
    find "${d}" \
        \( \
            -type d \
            -a ! -perm -6000 \
        \) \
        -exec chmod +6000 -- {} \+ ;
done

