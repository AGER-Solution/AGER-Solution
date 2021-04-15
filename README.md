# AGER Solution datasets

Esses datasets visam identificar folhas de soja para, em seguida, sejam categorizadas entre folhas saudáveis ou doentes. A ideia é realizar um sistema de análise preditiva completo, onde o produtor/agricultor receberá informações precisas e pontuais sobre sua lavoura, a fim de tomar as decisões de maneira mais eficiente e imediata.  

## Indentificação da folha

O [dataset inicial](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/weed-detection-soybean-crops/) é formado exclusivamente por imagens que nos permitirão diferenciar [folhas](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/weed-detection-soybean-crops/broadleaf/) e [grãos de soja](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/weed-detection-soybean-crops/soybean) de outros elementos como [solo](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/weed-detection-soybean-crops/soil/) e [grama](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/weed-detection-soybean-crops/grass/). Assim será possível filtrar os dados coletados para que possamos avaliar essas imagens com clareza.

 
## Categorização da folha

O segundo conjunto de dados está relacionado às variadas doenças que podem surgir durante o processo de crescimento da soja. 

Dentre elas: 
* [Crestamento Bacteriano](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Crestamento-Bacteriano-Bacterial-blight/)
* [Ferrugem](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Ferrugem-Rust/)
* [Folha Carijó (fitotoxidade)](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Folha-Carijo-Soybean-Mosaic-Virus/)
* [Mancha Alvo](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Mancha-Alvo-Southern-blight/)
* [Mela-de-Rhizoctonia](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Mela-Rhizoctonia-aerial-blight/)
* [Míldio](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Mildio-Downy-mildew/)
* [Oídio ](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Oidio-Powdery-mildew/)
* [Plantas saudáveis](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Saudavel-Healthy)
* [Doenças desconhecidas](https://github.com/AGER-Solution/AGER-Solution/tree/main/datasets/Desconhecido-Unknown/)

## Como faremos

A ideia é fornecer o contraste necessário para o desenvolvimento do modelo de redes convolucionais e do machine learning (ML), o qual possui o intuito de detectar pragas e doenças presentes nas culturas de forma rápida e eficaz.
