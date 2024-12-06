Documentação do Processo de Desenvolvimento
Objetivo
O objetivo deste projeto foi criar uma Calculadora de Média Escolar usando Python e gerenciar o desenvolvimento com Git, aplicando boas práticas de versionamento e organização.

Etapas do Desenvolvimento
Configuração Inicial

Instalei o Git e configurei meu nome de usuário e e-mail:
bash
Copiar código
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
Criei um repositório no GitHub e clonei localmente:
bash
Copiar código
git clone <URL-do-repositório>
Planejamento do Projeto

Documentei os objetivos, funcionalidades e cronograma no arquivo README.md.
Dividi as funcionalidades principais em diferentes etapas e branchs.
Desenvolvimento

Criei uma branch para cada funcionalidade principal:
entrada_de_dados: entrada de notas do aluno.
calculo_media: cálculo da média das notas.
verificar_aprovacao: exibição do status do aluno.
Usei commits frequentes para registrar mudanças e mensagens descritivas para cada alteração:
bash
Copiar código
git add .
git commit -m "Implementa função de entrada de notas"
Testes e Integração

Testei individualmente cada funcionalidade antes de fazer o merge com a branch principal:
bash
Copiar código
git merge entrada_de_dados
git merge calculo_media
Resolvi conflitos, quando ocorreram, utilizando o Visual Studio Code.
Documentação e Finalização

Capturei prints de tela e documentei o processo de desenvolvimento em detalhes.
Atualizei o arquivo README.md para incluir instruções de uso.
Desafios Enfrentados
Erro ao Criar Branch com Espaços no Nome

Tentei criar uma branch com espaços no nome (entrada de dados.py) e recebi um erro.
Solução: Renomeei a branch para usar underscores (entrada_de_dados).
Erro de Autenticação no GitHub

O repositório remoto negou permissões devido a uma configuração incorreta de autenticação.
Solução: Configurei o Git para usar autenticação com token no GitHub.
Conflitos de Merge

Durante o merge, ocorreram conflitos em alguns arquivos.
Solução: Resolvi os conflitos manualmente no Visual Studio Code, revisando cuidadosamente as mudanças.
Como o Git Ajudou no Projeto
Organização

As branches permitiram trabalhar em diferentes funcionalidades de forma independente, facilitando a integração.
Histórico de Mudanças

Os commits frequentes criaram um histórico detalhado do progresso, permitindo reverter alterações se necessário.
Colaboração e Controle

O uso do GitHub permitiu armazenar e gerenciar o código remotamente, garantindo backup e controle de versão.
Conclusão
Apesar dos desafios enfrentados, o uso do Git e do GitHub foi essencial para organizar e documentar o processo de desenvolvimento. O projeto serviu como uma ótima prática para consolidar conceitos de versionamento e colaboração.
