## Primeiro CheckPoint

O objetivo desse primeiro checkpoint é organizar o que fora pesquisado para que fosse possivel a coleta de informações de energia e desempenho de diferentes arquiteturas de deep learning, usando cpu e gpu.

### Configuração inicial

Para que seja possivel fazer as medições é necessário primeiramente instalar o comando perf disponivel através do seguinte comando (para distribução Ubunto no caso):

        sudo apt-get install linux-tools

ou:

        sudo apt-get install linux-tools-common linux-tools-generic

Esses comandos devem ser o suficientes para a instalação do perf, mas dependendo do kernel ele pode pedir outra versão, como no meu caso fora necessario a instalação usando os seguintes comandos:

        sudo apt-get install linux-tools-4.15.0-36-generic
        sudo apt-get install linux-cloud-tools-4.15.0-36-generic

Já para o comando usado para a medição da gpu é apenas necessario a instalação do driver mais recente disponivel para sua placa NVIDIA. Para isso existem diferentes métodos de instalação, o utilizado para esse experimento fora usando o comando apt-get do ubunto e utilizando o numero da ultima versão do diver (pode ser visto no site da propria nvidia). No caso os passos usados foram:

        sudo add-apt-repository ppa:graphics-drivers/ppa
        sudo apt update
        sudo apt install nvidia-384

Com isso basta checar se a instalação ocorreu bem utilisando o seguinte comando:

        lsmod | grep nvidia

As vezes é necessario remover qualquer coisa da nvidia caso não seja bem sucedida a instalação, para isso basta usar:

        sudo apt-get purge nvidia*

###Comandos

Para a cpu será utilizado o seguinte comando:

		perf stat -a -e "power/energy-cores/" -I 1000

O comando acima sera utilizado para pegar informações de energia assim como informações de desempenho (no exemplo temos energia apenas) da cpu. Com ele é possivel fazer um script que ouça esse comando e de dump das informações que precisamos para o projeto.

Esse comando tambem pode ser utilizado para a coleta de dados de energia da gpu mudando o parametro que especifica qual métrica deve ser avaliada, no caso mudando de energy-cores para energy-gpu.

Um ultimo detalhe sobre o perf é para fazer a medição de energia (que é system wide) é necessario alterar uma variavel de sistema chamada perf_event_paranoid, que provavelmente estara com o valor 3 e deverá ser colocada com o valor -1, caso contrario o perf não tem acesso as informações de energia. 

O comando para alterar o valor usado fora esse:

        sudo nano /proc/sys/kernel/perf_event_paranoid

No caso da GPU temos tanto o perf acima como o seguinte comando:

		nvidia-smi --query-gpu=index,timestamp,power.draw,clocks.sm,clocks.mem,clocks.gr --format=csv -l 1

Nesse comando provido pela própria nvida consegue se fazer queries para determinados dados da gpu, no exemplo estamos pegando informações do clock, memoria e power da gpu enquanto ela esta em funcionamento, alem de colocarmos um timestamp em cada linha. Esse comando facilita a captura de dados pois passando o argumento -csv ele mesmo da dump nas informações desejada em um arquivo no formato csv, não havendo necessidade de criar um script para ouvir a query.

Uma observação quanto ao comando acima, esse comando é disponibilizado para placas nvidia, mas nem todas as fetures são suportadas por todas as placas, um exemmplo disso é GTX 860M que não consegue retornar informações de consumo de energia, ou a GTX 1050 que teve essa feature desligada devido a um bug na placa. Placas que aprsentaram suporte a esse tipo de query foram a GTX 970 (testada) e a GTX 1030 (alguns forauns indicam que com ela é possivel)