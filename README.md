# Automação Check List

## Objetivo

Essa automação a ideia de reduzir o tempo do cliente de forma em que gere automaticamente seu check list, de acordo com a necessidade do mesmo. Esse check list tem objetivo de criar um check list, colocando o nome e o assunto de forma automatica, em seguida fazendo o upload de acordo com a pasta indica dentro do programa que está localizada em seu PC e selecionando as pessoas que podem vizualizar esse check list. Deixando mais pratico e economizando tempo ao cliente. Esse projeto surgiu de acordo com a necessidade do cliente de automatizar o seu processo, na ideia de aconomizar tempo. 

Bibliotecas utilizadas e o logger, logo em seguida os nomes de cada robo.

<img width="469" height="228" alt="image" src="https://github.com/user-attachments/assets/8570c625-b2a0-4cea-90b5-5d31612a1017" />

As funções para criar o check list, logar no app e também para importa a planilha.

/Login 
Vai à página de login.
Preenche usuário e senha.
Clica em "Entrar".
Espera por carregamento
Isso garante que o login foi bem-sucedido ao verificar um elemento do painel (“Dashboard”).

/Criação de Checklist
Navega até a página de checklists e clica em "Criar novo".
Preenche os campos de assunto e nome e clica em "Salvar".
Usa wait_for_selector para garantir que o botão “Importar” aparece antes de prosseguir.

/Importação de planilha
Abre o seletor de arquivos com click().
Usa expect_file_chooser() + set_files(...) para garantir que o arquivo seja capturado corretamente 
Usa await page.locator('input[type="file"]').set_input_files(...) para uploads diretos, incluindo múltiplos arquivos 
Crownstack Blog
Aguarda confirmação de upload (botão "Ir para estrutura") antes de prosseguir.

<img width="931" height="764" alt="image" src="https://github.com/user-attachments/assets/4c55c80b-cba0-41b7-a882-7bceaf217cee" />

A função a seguir tem o objetivo de buscar pelo nome do usuario indicado ao programa e habilitar para vizualição do check list.

/Acessa a aba “Usuários” do checklist.
Para cada usuário na lista:
usca a linha do usuário na tabela (tr:has-text("{usuario}")).
Obtém o toggle de permissão (checkbox).
Lê o atributo "value" para saber se já está ativo.
Caso esteja "0", clica para ativar a permissão "Aplica".
Clica em Salvar e aguarda o modal de confirmação.
Clica em Confirmar dentro do modal.
Retorna True (sucesso) ou False (em caso de erro).

<img width="1027" height="812" alt="image" src="https://github.com/user-attachments/assets/5a85b165-349d-4cfb-bfa1-a8ded82d4888" />
<img width="804" height="535" alt="image" src="https://github.com/user-attachments/assets/988adcbe-eaef-454a-80a4-d864e8733ab3" />

Localiza planilhas
Captura todos os arquivos .xlsx da pasta indicada.
Se não houver, registra erro e encerra.
Inicializa Playwright
Usa sync_playwright() dentro de with, garantindo fechamento automático do browser ao final. 
Abre o navegador em modo visível (headless=False) para facilitar a depuração.
Autenticação
Chama a função login(page, username, password) para efetuar login.
Menu interativo
Permite ao usuário escolher qual "robô" executar ou sair.
Processamento dos arquivos
Para cada arquivo escolhido:
Cria checklist (criar_checklist).
Importa itens da planilha (importar_itens_via_planilha).
Configura permissões de usuários (configurar_usuarios_checklist), se a importação foi bem-sucedida.
Tratamento de erros específico para cada passo, o que evita que uma falha interrompa todo o script.
Encerramento
Fecha o browser ao sair do loop.

Registra finalização da execução no log.



<img width="1576" height="816" alt="image" src="https://github.com/user-attachments/assets/be39165f-5070-42b5-8ceb-f8255740d405" />


