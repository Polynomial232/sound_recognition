"""
    docstring
"""
# pylint: disable=line-too-long

import time
from decouple import config
from sound_recognition import recognition
from db_cofig import db

TABLE_NAME = config("table_name")
SLEEP_TIME = int(config("sleep"))

dbcursor = db.cursor(dictionary=True, buffered=True)

def update_row(develop=True):
    """
        mendapatkan row yang memiliki status = 0 sesuai dengan id terbaru
        lalu akan dilakukan recognition apakah termasuk ringging atau bukan
        kemudian akan row tersebut akan diupdate status menjadi 1 atau 2
        dan deskripsi menjadi `valid` atau `invalid`
    """

    dbcursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE status=0 ORDER BY id")
    tb_result = dbcursor.fetchone()
    
    if tb_result is None:
        db.commit()
        return

    # print(f"before: {tb_result}")
    id_row = tb_result.get('id')

    #  run recognition
    description, status = recognition(tb_result.get('path'))
    status = 0 if develop else status

    update_sql = f"UPDATE {TABLE_NAME} SET status={status}, deskripsi='{description}' WHERE id={id_row}"
    dbcursor.execute(update_sql)

    db.commit()

    dbcursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id={id_row}")
    current_result = dbcursor.fetchone()

    print(current_result)
    print("="*100)

while True:
    update_row(False)
    time.sleep(SLEEP_TIME)
