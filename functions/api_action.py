import requests
from datetime import datetime
from decouple import config

IP_API = config("IP_API")
PORT_API = config("PORT_API")
IP_UPLOAD = config("IP_UPLOAD")
PORT_UPLOAD = config("PORT_UPLOAD")
PC_CODE = config("PC_CODE")

def do_put(filename, device_code, result_id, msisdn, status,classes, ttl_process="0s", text="None"):
    print(f"{datetime.now()}\t {filename}, Status: {status}, Deskripsi: {classes}, Time Process: {ttl_process}")

    update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}&deviceCode={device_code}&id={result_id}&msisdn={msisdn}&status={status}&desc={classes}&text={text}"
    result_update = requests.put(update_url)

    print(f"{datetime.now()}\t PUT Status: {result_update.status_code}, {result_update.content}")

    return result_update.status_code

def do_get():
    get_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}"
    result_get = requests.get(get_url, timeout=10)

    return result_get