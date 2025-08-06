#!/bin/bash
set -e

echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing essential tools..."
sudo apt install -y build-essential curl wget git software-properties-common apt-transport-https ca-certificates gnupg lsb-release

echo "Installing Python 3, pip and dev packages..."
sudo apt install -y python3 python3-pip python3-dev python3-venv

echo "Upgrading pip..."
python3 -m pip install --upgrade pip setuptools wheel

echo "Installing Python data science libraries..."
python3 -m pip install numpy pandas matplotlib seaborn scikit-learn scipy statsmodels jupyterlab notebook plotly tensorflow torch torchvision torchaudio

echo "Installing Jupyter Notebook extensions..."
python3 -m pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

echo "Installing R..."
sudo apt install -y r-base r-base-dev

echo "Installing RStudio..."
RSTUDIO_DEB="rstudio-latest-amd64.deb"
wget -O $RSTUDIO_DEB https://download1.rstudio.org/desktop/bionic/amd64/rstudio-2023.06.1-524-amd64.deb
sudo dpkg -i $RSTUDIO_DEB || sudo apt install -f -y
rm $RSTUDIO_DEB

echo "Installing VS Code..."
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install -y code
rm packages.microsoft.gpg

echo "Installing Docker..."
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

echo "Cleaning up..."
sudo apt autoremove -y
sudo apt clean

echo "Setup complete! Please restart your terminal or logout/login to apply group changes for Docker."
