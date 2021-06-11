import os
import shutil
import random
import subprocess

# selecionando diretorio raiz
APP_FOLDER = os.getcwd()

# array de registros
rec = []

for i in range(250):
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SOYBEAN IMAGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  cwd = APP_FOLDER + "/soybean/"
  # escolhendo arquivo aleatoriamente
  choice = random.choice(os.listdir(cwd))

  # atribuindo um hash para o arquivo escolhido
  md5 = str(subprocess.check_output(['md5sum', cwd + choice]))[2:32]

  # armazenando arquivos ja transferidos
  if md5 not in rec:
    rec.append(md5) 

    # movendo arquivo
    original = APP_FOLDER + "/soybean/" + choice
    target = APP_FOLDER + "/randomized_dataset/" + md5 + '.jpeg'

    shutil.copyfile(original,target)
 
  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GRASS IMAGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  cwd = APP_FOLDER + "/grass/"
  # escolhendo arquivo aleatoriamente
  choice = random.choice(os.listdir(cwd))

  # atribuindo um hash para o arquivo escolhido
  md5 = str(subprocess.check_output(['md5sum', cwd + choice]))[2:32]

  # armazenando arquivos ja transferidos
  if md5 not in rec:
    rec.append(md5) 

    # movendo arquivo
    original = APP_FOLDER + "/grass/" + choice
    target = APP_FOLDER + "/randomized_dataset/" + md5 + '.jpeg'

    shutil.copyfile(original,target)

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SOIL IMAGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  cwd = APP_FOLDER + "/soil/"
  # escolhendo arquivo aleatoriamente
  choice = random.choice(os.listdir(cwd))

  # atribuindo um hash para o arquivo escolhido
  md5 = str(subprocess.check_output(['md5sum', cwd + choice]))[2:32]

  # armazenando arquivos ja transferidos
  if md5 not in rec:
    rec.append(md5) 

    # movendo arquivo
    original = APP_FOLDER + "/soil/" + choice
    target = APP_FOLDER + "/randomized_dataset/" + md5 + '.jpeg'

    shutil.copyfile(original,target)

  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BROADLEAF IMAGE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  cwd = APP_FOLDER + "/broadleaf/"
  # escolhendo arquivo aleatoriamente
  choice = random.choice(os.listdir(cwd))

  # atribuindo um hash para o arquivo escolhido
  md5 = str(subprocess.check_output(['md5sum', cwd + choice]))[2:32]

  # armazenando arquivos ja transferidos
  if md5 not in rec:
    rec.append(md5) 

    # movendo arquivo
    original = APP_FOLDER + "/broadleaf/" + choice
    target = APP_FOLDER + "/randomized_dataset/" + md5 + '.jpeg'

    shutil.copyfile(original,target)

