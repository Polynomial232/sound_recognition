# Sound-Recognition

## Ekstrak 7z

Install 7z
```bash
sudo apt-get install p7zip p7zip-full
```
Ekstraks 7z File
```bash
7za x sound_recognition.7z -o./sound_recognition
```


## Installasi

Update Linux
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install software-properties-common -y
```
```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
```

Install ffmpeg
```bash
sudo apt install ffmpeg -y
```

Install Python3.8
```bash
sudo apt install python3.8 -y
```

Install pip Python
```bash
sudo apt install python3-pip -y
```

Install pip Python3.8
```bash
python3.8 -m pip install pip
```

Buka bashrc
```bash
nano ~/.bashrc
```

Copy, lalu paste ke paling bawah bashrc
```bash
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

Muat ulang pengaturan bashrc
```bash
source ~/.bashrc
```

Cek Versi pip
```bash
pip --version
```

Install Python Virtual Enviroment
```bash
sudo apt install python3.8-venv
```

Buat Virtual Enviroment Python3.8
```bash
python3.8 -m venv venv
```

Aktifkan Virutal Enviroment
```bash
source venv/bin/activate
```

Install Package Python
```bash
pip install -r requirements.txt
```

Copy direktori nltk_data
```bash
cp -R install/nltk_data /home/app/
```
## Menjalakan Program

### Jalankan program menggunakan Python3.8
```bash
source venv/bin/activate
python3.8 app.py
```

### Jalankan program menggunakan pm2
copy file app.py menjadi app
```bash
cp app.py app
```
jalankan menggunakan pm2
*pastikan virutal enviroment (venv) python aktif
```bash
pm2 start app --interpreter venv/bin/python3.8 --name sound-recognition
```

## Authors



[Polynomial232](https://github.com/Polynomial232)

