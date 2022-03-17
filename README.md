# demo_nifi
Demonstração da criação de um DataFlow completo utilizando o Apache NiFi juntamente a tecnologias como Docker e MySQL.

Breve explicação sobre os arquivos:
  - docker-compose.yml: Arquivo Docker Compose utilizado para criação dos containers/serviços do Apache NiFi e do MySQL;
  - gerador_pessoa.py: Script em Python responsável por criar cadastros fictícios e fazer o post para o NiFi;
  - Projeto_NiFi.xml: Template do DataFlow criado com o Apache NiFi. Para utilizá-lo, basta fazer seu upload dentro da interface do NiFi;
  - script.sql: Script SQL utilizado para criação da tabela para armazenamento dos cadastros dentro do MySQL;

Link para o vídeo completo com a criação do DataFlow:
  https://youtu.be/4fUoMk1qz7Y
