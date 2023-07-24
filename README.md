# CasePetLove
Nesse README eu irei explicar oque realizei nos códigos presente nesse repositório

#Raw
A pasta [Raw](https://github.com/Lopesandr/CasePetLove/tree/main/Raw) é onde está os dados sem nenhuma modificação, é onde esta o arquivo CSV diponibilizado por vocês(PetLove). Precisei colocar os dados em um 
arquivo .gitigore por conta do tamanho do arquivo.

#Truested 
A pasta [Truested](https://github.com/Lopesandr/CasePetLove/tree/main/Truested) contém um arquivo chamado "Limpeza.py" neste arquivo eu faço algumas
verificações para saber com quais dados estou manipulando. Faço tudo isso usando a bibliote pandas do python Faço verificação para ver se tem dados nulos, faço um ```print(df.info())```para ver as informações sobre o DateFrame
e também uso um ```print(df.describe())``` para saber algumas estatisticas gerais sobre os dados. Isso tudo foi para mim conhecer melhor os dados e oque eu iria trazer na análise final.
Depois disso eu precisei fazer a tipagem de algumas colunas que tinham datas porque no power bi iria ser mais facíl manipular as colunas de data se o tipo dela fossem
datetime(que é um tipo de dado que tem data e hora), eu fiz isso usando o pandas. Depois de tudo pronto exportei um novo arquivo csv com essa alteração, e este arquivo csv alterado
esta no .gitignore também.

#Refiend
A pasta [Refiend](https://github.com/Lopesandr/CasePetLove/tree/main/Refiend) contém um arquivo python chamado "Selecionando colunas", neste arquivo eu seleciono
apenas as colunas que eu irei usar para a analise no power bi e depois de fazer essa seleção eu exporto um arquivo excel com apenas essas colunas e os dados contidas
nelas para poder levar esse aqruivo para o power bi. O aqruivo excel também esta no .gitignore.
