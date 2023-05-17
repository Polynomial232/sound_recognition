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

pastikan virutal enviroment (venv) python aktif
```bash
source venv/bin/activate
```

jalankan menggunakan pm2
```bash
pm2 start app --interpreter venv/bin/python3.8 --name sound-recognition
```

## Authors


[Polynomial232](https://github.com/Polynomial232)

