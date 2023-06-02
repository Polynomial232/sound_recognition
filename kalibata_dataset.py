from functions.recognition import main
import os

for folder in os.listdir('audio/dataset'):
    for file in os.listdir(f'audio/dataset/{folder}'):
        text = main(os.path.join('audio', 'dataset', folder, file), file[:-4])
        
        with open(f'{folder}.txt', 'a', encoding='utf-8') as classname:
            classname.write(text+"\n")
        
    print(f'{folder} Done')