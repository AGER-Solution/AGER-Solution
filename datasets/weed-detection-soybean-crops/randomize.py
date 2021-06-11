import os
import shutil
import random
import subprocess

# selecionando diretorio raiz
APP_FOLDER = os.getcwd()

# array de registros
rec = []

def select_image_from(dataset):
    cwd = APP_FOLDER + "/" + dataset
    # escolhendo arquivo aleatoriamente
    choice = random.choice(os.listdir(cwd))

    # atribuindo um hash para o arquivo escolhido
    md5 = str(subprocess.check_output(['md5sum', cwd + choice]))[2:32]

    # armazenando arquivos ja transferidos
    if md5 not in rec:
        rec.append(md5)

        # movendo arquivo
        original = APP_FOLDER + "/" + dataset + "/" + choice
        target = APP_FOLDER + "/randomized_dataset/" + md5 + '.jpeg'

        shutil.copyfile(original, target)



for i in range(250):
    select_image_from('soybean')
    select_image_from('grass')
    select_image_from('broadleaf')
    select_image_from('soil')
