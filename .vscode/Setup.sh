#!/bin/bash

# =============================================
# DATA SCIENCE ENVIRONMENT SETUP SCRIPT (Ubuntu)
# =============================================

# Update & Upgrade System
echo "[1] Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

# Install essential dependencies
echo "[2] Installing dependencies (curl, wget, build tools, etc.)..."
sudo apt install -y \
    curl wget git unzip \
    build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev \
    software-properties-common ca-certificates


# Test GitHub SSH Connection
echo "[6] Testing GitHub SSH connection..."
ssh -T git@github.com

# ==================
# 2. Install PyEnv (Python Version Manager)
# ==================
echo "[7] Installing PyEnv..."
curl https://pyenv.run | bash

# Add PyEnv to PATH
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

# Install Latest Python
echo "[8] Installing Python via PyEnv..."
pyenv install 3.11.4  # Latest stable Python (adjust as needed)
pyenv global 3.11.4

# ==================
# 3. Install Miniconda (for Virtual Environments)
# ==================
echo "[9] Installing Miniconda..."
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/miniconda
rm ~/miniconda.sh
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# ==================
# 4. Install Jupyter Lab & Data Science Libraries
# ==================
echo "[10] Installing Jupyter Lab & Data Science Libraries..."
pip install --upgrade pip
pip install \
    jupyterlab numpy pandas matplotlib seaborn \
    scikit-learn tensorflow torch keras \
    plotly statsmodels xgboost lightgbm \
    flask fastapi sqlalchemy

# ==================
# 5. Install VS Code (Optional)
# ==================
echo "[11] Installing VS Code..."
sudo apt install -y wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update -y
sudo apt install -y code

# Install VS Code Extensions for Data Science
echo "[12] Installing VS Code Extensions..."
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension ritwickdey.LiveServer

# ==================
# 6. Install Docker (Optional)
# ==================
echo "[13] Installing Docker..."
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# ==================
# FINAL STEPS
# ==================
echo "[14] Cleaning up..."
sudo apt autoremove -y

echo "===================================="
echo "✅ Data Science Environment Ready!"
echo "===================================="
echo "Python: $(python --version)"
echo "Pip: $(pip --version)"
echo "Git: $(git --version)"
echo "Jupyter Lab: $(jupyter --version)"
echo "===================================="
echo "Run 'jupyter lab' to start Jupyter."
echo "Run 'code' to open VS Code."
echo "===================================="