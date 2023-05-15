# Sound-Recognition


## Installasi

Update Linux
```bash
sudo apt update && sudo apt upgrade
```
```bash
sudo apt install software-properties-common
```
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

Install ffmpeg
```bash
sudo apt install ffmpeg
```

Install Python3.8
```bash
sudo apt install python3.8
```

Install pip Python
```bash
sudo apt install python3-pip
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

### Jalankan program dibackground
Beri akses root untuk run_background.sh
```bash
chmod 777 run_background.sh
```

- start: Jalankan program
```bash
./run_background.sh start
```

- status: Lihat status program
```bash
./run_background.sh status
```

- kill: Kill atau Stop program
```bash
./run_background.sh kill
```

- restart: Restart program
```bash
./run_background.sh restart
```

- logs: Logs program
```bash
./run_background.sh logs
```

## Authors



[Polynomial232](https://github.com/Polynomial232)

