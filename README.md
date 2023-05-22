# Sound-Recognition

## Installasi

Update Linux
```bash
git clone https://github.com/Polynomial232/sound_recognition.git
```
```bash
cd sound_recognition
```
```bash
chmod 777 install.sh
```
```bash
./install.sh
```

## Menjalakan Program

### Jalankan program menggunakan pm2

buat file .env dengan ketentuan yang ada pada server yang sudah terinstall
```bash
nano .env
```

contoh isi file .env
```bash
PC_CODE=
IP_API=
PORT_API=
IP_UPLOAD=
PORT_UPLOAD=
TIME_DELETE=
COOLDOWN=
```

pastikan virutal enviroment (venv) python aktif
```bash
source venv/bin/activate
```

jalankan menggunakan pm2
```bash
pm2 start app --interpreter venv/bin/python3.8 --name sound-recognition
```

## Cek Log Error

[googleDocs](https://docs.google.com/document/d/1cx1TzyGhWQISAM5Gd_T4sartV0rtOeu3lb-iA1DgmGQ/edit?usp=sharing)

## Authors


[Polynomial232](https://github.com/Polynomial232)

