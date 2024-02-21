# Aprenda Git e Github em 3 dias (2024)


## Aula 08:

O comando git init é utilizado para iniciar um novo repositório Git local. Ele cria um novo subdiretório chamado .git no diretório atual, que contém todos os metadados necessários para o gerenciamento das versões do projeto. Após executar git init, você pode começar a adicionar arquivos ao repositório e usar outros comandos Git para rastrear suas alterações.

O comando git status mostra o estado atual do repositório Git em que você está trabalhando. Ele informa sobre arquivos que foram modificados, adicionados, mas ainda não commitados, e arquivos que o Git está rastreando mas que não foram modificados. Esse comando ajuda a entender quais mudanças estão pendentes e a planejar os próximos passos, como commits.


## Aula 09:

O comando ```git add <file>``` adiciona um arquivo específico ao staging area, preparando-o para o próximo commit. Já git add . adiciona todos os arquivos modificados no diretório atual e subdiretórios ao staging area, incluindo novos arquivos e modificações, preparando-os também para o commit.

O comando ```git rm –cached <file>``` remove um arquivo do diretório de trabalho e do índice (staging area), marcando-o para exclusão no próximo commit.


## Aula 10:

O comando git commit -m "message" cria um novo commit com as alterações adicionadas ao staging area, incluindo a mensagem de commit especificada entre as aspas para descrever as mudanças realizadas.


## Aula 11:

O comando git diff exibe as diferenças entre arquivos no diretório de trabalho e no índice (staging area) ou entre commits no histórico do Git, mostrando as alterações linha por linha que ainda não foram adicionadas ao staging area.

O comando git log exibe o histórico de commits do repositório, mostrando informações como o autor do commit, a data e a mensagem de commit. Ele permite rastrear as alterações feitas ao longo do tempo no projeto.

No Git, os arquivos no repositório passam por três estágios principais:
    1. Working Directory (Diretório de Trabalho): É onde você faz todas as suas modificações. Aqui, os arquivos estão no estado "modificado" mas ainda não foram preparados para commit. (git status / git diff)
    2. Staging Area (Área de Preparação ou Índice): Após modificar arquivos, você pode adicioná-los ao staging area com o comando git add. Isso significa que você marcou essas modificações para serem incluídas no próximo commit, mas ainda não realizou o commit de fato. Aqui, os arquivos estão no estado "preparado".
    3. Commit: Quando você executa o comando git commit, o Git tira uma "foto" dos arquivos no staging area, criando um novo commit com essas modificações no histórico do repositório. Essa foto passa a representar o estado atual desses arquivos no repositório. Após o commit, o estado volta a ser "não modificado" até que novas alterações sejam feitas.
Estes estágios permitem um controle detalhado sobre as modificações que você quer incluir em cada commit, facilitando a organização do histórico do projeto e a colaboração em equipe.

## Aula 12:

O comando git commit -a -m "message" realiza dois passos: primeiro, adiciona automaticamente ao commit as alterações em arquivos já rastreados pelo Git, excluindo novos arquivos e removidos; segundo, cria um commit com essas alterações, usando a mensagem especificada.


## Aula 13:

O comando git rm é usado para remover arquivos do diretório de trabalho e do índice do Git. Isso sinaliza que o arquivo deve ser excluído no próximo commit, removendo-o do controle de versão. Além de deletar o arquivo fisicamente do diretório de trabalho, git rm atualiza o índice do Git para refletir a remoção do arquivo, preparando a mudança para ser commitada.

git restore --staged <file> remove um arquivo do staging area sem alterar sua versão no diretório de trabalho.

O comando git restore <file> reverte as alterações feitas em um arquivo no diretório de trabalho para o seu último estado commitado, descartando as modificações não commitadas.


## Aula 14:

O comando git mv <oldfilename> <newfilename> é usado para renomear ou mover um arquivo ou diretório dentro de um repositório Git. Ele automaticamente move ou renomeia o arquivo e prepara a mudança para o próximo commit, atualizando o índice do Git para refletir a nova localização ou nome do arquivo.


## Aula 15:

Para modificar o último commit é git commit --amend -m "message". Esse comando permite que você altere a mensagem do último commit ou inclua novas alterações nele, sem criar um novo commit.
Aula 17:

    • git reset --soft <commit>: Move o ponteiro HEAD para o commit especificado, mas deixa o staging area e o diretório de trabalho como estão, permitindo que você recrie o commit com alterações diferentes se desejar.
    • git reset --mixed <commit> (padrão): Move o ponteiro HEAD para o commit especificado e atualiza o staging area para corresponder a esse commit, mas deixa o diretório de trabalho inalterado. Alterações que estavam staged agora estão unstaged, mas ainda presentes.
    • git reset --hard <commit>: Move o ponteiro HEAD para o commit especificado, atualiza o staging area e o diretório de trabalho para corresponder a esse commit, descartando todas as alterações no diretório de trabalho e no staging area que não estavam presentes no commit especificado.


## Aula 18:

O git alias permite criar atalhos para comandos Git, facilitando a execução de comandos longos ou frequentemente usados. Você pode configurar aliases de duas formas: globalmente, afetando todos os repositórios Git no sistema do usuário, ou localmente, específico para um repositório individual.
    • Alias Global: Configurado através do comando git config --global alias.<aliasname> '<command>', o alias global é acessível de qualquer repositório no sistema do usuário. Por exemplo, git config --global alias.ci 'commit' permite usar git ci como um atalho para git commit.
    • Alias Não Global (Local): Configurado com git config --local alias.<aliasname> '<command>', o alias local só é aplicável ao repositório atual. Isso é útil para comandos específicos de um projeto.


## Aula 19:

O comando git branch é usado para gerenciar ramificações (branches) dentro de um repositório Git. Ele tem várias funções, dependendo de como é usado:
    • Sem argumentos, git branch lista todas as branches locais no repositório, indicando a branch atual com um asterisco.
    • Com um nome de branch como argumento, git branch <branchname> cria uma nova branch com esse nome.
Para trocar para uma branch existente: git switch <branchname>. Isso muda o diretório de trabalho para refletir o estado da branch especificada.
git merge -m "message" branchName une a branch especificada à branch atual, com uma mensagem de commit personalizada para o merge.


## Aula 20:

O comando `git branch -d BranchName` deleta a branch especificada (`BranchName`), desde que as suas alterações tenham sido mescladas em outra branch, evitando a perda de trabalho.


## Aula 24:

Para acessar o GitHub usando tokens de acesso pessoal (Personal Access Tokens - PATs), você precisa seguir alguns passos. Esses tokens servem como uma alternativa segura às senhas para autenticação em APIs e na linha de comando. Aqui está um pequeno guia:
1. Criar um Token de Acesso Pessoal (PAT)
    1. Acesse o GitHub: Faça login na sua conta no GitHub.
    2. Acesse as Configurações: No canto superior direito, clique na sua foto de perfil e vá para "Settings".
    3. Segurança: No menu lateral, selecione "Developer settings".
    4. Tokens de Acesso Pessoal: Clique em "Personal access tokens", depois em "Generate new token".
    5. Gerar Token: Dê um nome ao seu token em "Note", selecione os escopos ou permissões que o token precisa e clique em "Generate token" no final da página.
    6. Copie seu Token: Copie o token gerado para um lugar seguro, pois você não poderá vê-lo novamente após fechar a página.
2. Usar o Token para Autenticação
    • Na Linha de Comando: Quando você executar operações que requerem autenticação, use o token como sua senha. Por exemplo, ao clonar um repositório privado, digite seu nome de usuário do GitHub e use o token no lugar da senha.
    • Em Aplicações: Use o token para autenticar solicitações em APIs do GitHub, substituindo a senha pelo token no cabeçalho de autenticação.


## Aula 25:

git push envia as alterações de uma branch específica para um repositório remoto. git push --all envia todas as branches do repositório local para o remoto.