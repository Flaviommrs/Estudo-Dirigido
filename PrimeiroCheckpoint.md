### Primeiro CheckPoint

O objetivo desse primeiro checkpoint é organizar o que fora pesquisado para que fosse possivel a coleta de informações de energia e desempenho de diferentes aquiteturas de deep learning, usando cpu e gpu.


Para a cpu será utilizado o seguinte comando:

		perf stat -a -e "power/energy-cores" -I 1000 sleep 30


O comando acima sera utilizado para pegar informações de energia assim como informações de desempenho (no exemplo temos energia apenas) da cpu. Com ele é possivel fazer um script que ouça esse comando e de dump das informações que precisamos para o projeto.


Esse comando tambem pode ser utilizado para a coleta de dados de energia da gpu mudando o parametro que especifica qual métrica deve ser avaliada.


No caso da GPU temos tanto o perf acima como o seguinte comando:

		nvidia-smi --query-gpu=index,timestamp,power.draw,clocks.sm,clocks.mem,clocks.gr --format=csv -l 1

Nesse comando provido pela própria nvida consegue se fazer queries para determinados dados da gpu, no exemplo estamos pegando informações do clock, memoria e power da gpu enquanto ela esta em funcionamento, alem de colocarmos um timestamp em cada linha. Esse comando facilita a captura de dados pois passando o argumento -csv ele mesmo da dump nas informações desejada em um arquivo no formato csv, não havendo necessidade de criar um script para ouvir a query.

Uma observação quanto ao comando acima, esse comando é disponibilizado para placas nvidia, mas nem todas as fetures são suportadas por todas as placas, um exemmplo disso é GTX 860M que não consegue retornar informações de consumo de energia, ou a GTX 1050 que teve essa feature desligada devido a um bug na placa. Placas que aprsentaram suporte a esse tipo de query foram a GTX 970 (testada) e a GTX 1030 (alguns forauns indicam que com ela é possivel)