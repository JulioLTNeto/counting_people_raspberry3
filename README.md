# Contador de pessoas na linguagem Python, feito para o uso do Raspberry PI 3

Bibliotecas usadas - 
  OpenCV: Usada para o processamento de imagem
  numpy: Usado para contagem de matrizes e outros tipos de dadps
  supabase: É o sistema de banco de dados online que usei. É gratuito, mas se não for usado durante uma semana o seu servidor é automaticamente desligado
  base64: Irá transformar as imagens que o OpenCV realiza a contagem para Base64.

O sistema em questão é um sistema de contagem de pessoas, onde o sistema possui uma hora de inicio e termino de funcionamento por dia, e tambem possui uma feixa de tempo de espera para uma nova contagem de pessoas.

O sistema como é feito pensando o Raspberry PI 3 possui um arquivo onde lá tem a função onde através do modulo de camera, o próprio sistema tira a foto do local desejado.

Como o código foi feito visando o Raspberry PI 3, foi nescessário por buscar bibliotecas e um código que não fossem custosos para a máquina. O Yolo por exemplo, embora possua uma versão do arquivo de contagem que tenha a opção de realizar a contagem com ele, ele não foi usado na versão final. Já que mesmo funcionando melhor do que a versão final ao ser executano no computador, ao ser executado no raspberry o sistema não conseguia realizar a contagem.
