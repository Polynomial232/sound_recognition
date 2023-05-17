sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install ffmpeg -y
sudo apt install python3.8 -y
sudo apt install python3-pip -y
python3.8 -m pip install pip
echo 'if [ -d "$HOME/.local/bin" ] ; then' >> ~/.bashrc
echo '    PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'fi' >> ~/.bashrc
source ~/.bashrc
sudo apt install python3.8-venv
cp -R install/nltk_data /home/app/
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
