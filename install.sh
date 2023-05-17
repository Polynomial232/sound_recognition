chmod 777 resetpm2.sh
./resetpm2.sh
sudo apt update && sudo apt upgrade -y
sudo apt-get install p7zip p7zip-full
7za x /home/app/sound_recognition.7z -o/home/app/sound_recognition_model
git clone https://github.com/Polynomial232/sound_recognition.git
cp /home/app/sound_recognition_model/ringing_detection/model/ringing_1680688942.8656914.h5 /home/app/sound_recognition/ringing_detection/model/ringing_1680688942.8656914.h5
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
cp -R /home/app/sound_recognition_model/install/nltk_data /home/app/
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
rm -rf /home/app/sound_recognition_model
