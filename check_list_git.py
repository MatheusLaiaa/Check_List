import logging
import os
from pathlib import Path
import time
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# nomes dos robos 
robos = [
     "2W001 - EKR1_1",
  "2W002 - EKR1_2",
  "2W003 - EKR1_3",
  "2W004 - EKR1_4",
  "2W005 - AKR1_1",
  "2W006 - AKR1_2",
  "2W007 - UDA 1_1",
  "2W008 - UDA1_2",
  "2W009 - UDA 1_3",
  "2W010 - UFB1-1R",
  "2W011 - UFB1-2R",
  "2W012 - UFB2-1R",
  "2W013 - UFB2-2R",
  "2W014 - FKR1-1R",
  "2W015 - FKR1-2R",
  "2W016 - FKR1-3R",
  "2W017 - FKR1-4R",
  "2W018 - FKR1-5R",
  "2W019 - FMR2-1",
  "2W020 - FKR1-5R",
  "2W021 - URT_1-1",
  "2W022 - URT_2-1",
  "2W023 - URT_2-2",
  "2W024 - URT_3-1",
  "2W025 - URT_3-2",
  "2W026 - URT_4-1",
  "2W027 - URT_5-1",
  "2W028 - URT_5-2",
  "2W029 - URT_6-1",
  "2W030 - URT_6-2",
  "2W031 - URT_6-3",
  "2W032 - URT_6-4",
  "2W033 - URT_7-1",
  "2W034 - URT_7-2",
  "2W035 - URT_7-3",
  "2W036 - UKR1-3",
  "2W037 - UKR1-4",
  "2W038 - UKR1-5",
  "2W039 - UKR1-6",
  "2W040 - UKR1-7",
  "2W041 - UKR1-8",
  "2W042 - UKR1-9",
  "2W043 - UMR2-1",
  "2W044 - UMR2-2",
  "2W045 - UMR2-3",
  "2W046 - UMR2-4",
  "2W047 - UMR2-5",
  "2W048 - UMR2-6",
  "2W049 - UMR2-7",
  "2W050 - UMR2-8",
  "2W051 - UMR3-1",
  "2W052 - UMR3-2",
  "2W053 - UMR3-3",
  "2W054 - UMR3-4",
  "2W055 - UMR3-7",
  "2W056 - UMR3-8",
  "2W057 - UMR4-3",
  "2W058 - UMR4-4",
  "2W059 - UMR4-5",
  "2W060 - UMR4-6",
  "2W061 - UMR4-7",
  "2W062 - UMR4-8",
  "2W063 - UMR5-5",
  "2W064 - UMR5-6",
  "2W065 - UMR5-7",
  "2W066 - UMR5-8",
  "2W067 - WHR_1-1",
  "2W068 - WHR_2-1",
  "2W069 - WHR_2-2",
  "2W070 - WHR_2-3",
  "2W071 - WHR_3-1",
  "2W072 - WHR_3-2",
  "2W073 - WHR_3-3",
  "2W074 - WHL_1-1",
  "2W075 - WHL_2-1",
  "2W076 - WHL_2-2",
  "2W077 - WHL_2-3",
  "2W078 - WHL_3-1",
  "2W079 - WHL_3-2",
  "2W080 - WHL_3-3",
  "2W081 - RFR_1_1",
  "2W082 - RFL_1_1",
  "2W083 - RFR_1_3",
  "2W084 - RFL_1_3",
  "2W085 - RFR_1_2",
  "2W086 - RFL_1_2",
  "2W087 - SOR1-1",
  "2W088 - SOR1-3",
  "2W089- SOR1-2",
  "2W090 - SRR0-1",
  "2W091 - SRR0-2",
  "2W092 - SRR0-3",
  "2W093 - SRR0-5",
  "2W094 - SRR1-2",
  "2W095 - SRR1-6",
  "2W096 - SRR2-1",
  "2W097 - SRR2-2",
  "2W098 - SRR2-3",
  "2W099 - SRR2-4",
  "2W100 - SRR2-5",
  "2W101 - SRR2-6",
  "2W102 - SRR2-8",
  "2W103 - SRR3-3",
  "2W104 - SRR4-1",
  "2W105 - SRR4-2",
  "2W106 - SRR4-3",
  "2W107 - SRR4-4",
  "2W108 - SRR4-5",
  "2W109- SRR4-6",
  "2W110 - SRR5-1",
  "2W111 - SRR5-2",
  "2W112 - SOL1-1",
  "2W113 - SOL1-3",
  "2W114 - SOL1-2",
  "2W115 - SLR0-1",
  "2W116 - SLR0-2",
  "2W117 - SLR0-3",
  "2W118 - SLR0-5",
  "2W119 - SLR1-2",
  "2W120 - SLR1-6",
  "2W121 - SLR2-1",
  "2W123 - SLR2-2",
  "2W123 - SLR2-3",
  "2W124 - SLR2-4",
  "2W125 - SLR2-5",
  "2W126 - SLR2-6",
  "2W127 - SLR2-8",
  "2W128 - SLR3-3",
  "2W129 - SLR4-1",
  "2W130 - SLR4-2",
  "2W131 - SLR4-3",
  "2W132 - SLR4-4",
  "2W133 - SLR4-5",
  "2W134 - SLR4-6",
  "2W135 - SLR5-1",
  "2W136 - SLR5-2",
  "2W137 - FBT1-1",
  "2W138 - FBT2-1",
  "2W139 - FBT2-2",
  "2W140- FBT2-8",
  "2W141 - FBT2-9",
  "2W142 - FBT2-10",
  "2W143 - FBT2-11",
  "2W144 - FBT2-12",
  "2W145 - FBT2-13",
  "2W146 - FBT2-14",
  "2W147 - FBT2-15",
  "2W148 - FBT2-16",
  "2W149 - FBT3-1",
  "2W150 - FBT3-2",
  "2W151 - FBT3-3",
  "2W152 - FBT3-7",
  "2W153 - FBT3-12",
  "2W154 - FBT3-16",
  "2W155 - FBT3-13",
  "2W156 - FBT3-14",
  "2W157 - FBT4-1",
  "2W158 - FBT4-2",
  "2W159 - FBT4-4",
  "2W160 - FBT4-5",
  "2W161 - FBT4-6",
  "2W162 - FBT4-11",
  "2W163 - FBT4-12",
  "2W164 - FBT5-5",
  "2W165 - FBT5-6",
  "2W166 - FBT5-9",
  "2W167 - FBT5-10",
  "2W168 - FBT5-11",
  "2W169 - FBT5-12",
  "2W170 - FBT5-13",
  "2W171 - FBT5-14",
  "2W172 - FBT6-5",
  "2W173 - FBT6-6",
  "2W174 - FBT6-10",
  "2W175 - FBT6-11",
  "2W176 - FBT6-3",
  "2W177 - FBT6-13",
  "2W178 - FBT6-16",
  "2W179 - FBT7-3",
  "2W180 - FBT7-4",
  "2W181 - FBT7-5",
  "2W182 - FBT7-6",
  "2W183 - FBT7-9",
  "2W184 - FBT7-10",
  "2W185 - FBT7-13",
  "2W186 - FBT7-14",
  "2W187 - FBT7-15",
  "2W188 - FBT7-16",
  "2W189 - FBT8-7",
  "2W190 - FBT8-8",
  "2W191 - FBT8-9",
  "2W192 - FBT8-10",
  "2W193 - FBT8-13",
  "2W194 - FBT8-14",
  "2W195 - FBT9-1",
  "2W196 - FBT9-2",
  "2W197 - FBT9-7",
  "2W198 - FBT9-8",
  "2W199 - FBT9-9",
  "2W200 - FBT9-10",
  "2W201 - FBT9-11",
  "2W202 - FBT9-12",
  "2W203 - FBT9-13",
  "2W204 - FBT9-14",
  "2W205 - FBT10-3",
  "2W206 - FBT10-4",
  "2W207 - FBT10-5",
  "2W208 - FBT10-6",
  "2W209 - FBT11-1",
  "2W210 - REAR MEMBER RH RB1",
  "2W211 - REAR MEMBER RH RB2",
  "2W212 - REAR MEMBER RH B3+RESPOT",
  "2W213 - REAR MEMBER RH RB4",
  "2W214 - REAR MEMBER RH RB5",
  "2W215 - REAR MEMBER RH RB6",
  "2W216 - REAR MEMBER RH RB7",
  "2W217 - REAR MEMBER LH RB1",
  "2W218 - REAR MEMBER LH RB2",
  "2W219 - REAR MEMBER LH B3+RESPOT",
  "2W220 - REAR MEMBER LH RB4",
  "2W221 - REAR MEMBER LH RB5",
  "2W222 - REAR MEMBER LH RB6",
  "2W223 - REAR MEMBER LH RB7",
  "2W224 - FSM_1-1_RH",
  "2W225 - FSMFR_1_RH",
  "2W226 - FSMFR_2_RH",
  "2W227 - FSM_ASSY_REAR_1_RH",
  "2W228 - FSM_ASSY_REAR_2_RH",
  "2W229 - FSM_1-1_LH",
  "2W230 - FSMFR_1_LH",
  "2W231 - FSMFR_2_LH",
  "2W232 - FSM_ASSY_REAR_1_LH",
  "2W233 - FSM_ASSY_REAR_2_LH",
  "2W234 - FSM_4-1",
  "2W235 - APRON_RH_RB4_1",
  "2W236 - APRON_RH_RB1_1",
  "2W237 - APRON_RH_RB2_2",
  "2W238 - APRON_RH_RB3_2",
  "2W239 - APRON_LH_RB4_1",
  "2W240 - APRON_LH_RB1_1",
  "2W241 - APRON_LH_RB2_2",
  "2W242 - APRON_LH_RB3_2",
  "2W243 - ROCKER_INNER_RH_1_1",
  "2W244 - ROCKER_INNER_RH_2_1",
  "2W245 - ROCKER_INNER_LH_2_2",
  "2W246 - ROCKER_INNER_LH_1_2",
  "2W247 - RDR1-2",
  "2W248 - RDR2-2",
  "2W249 - TGT1-1",
  "2W250 - TGT1-2",
  "2W251 - HD1-1",
  "2W252 - LG1-1",
  "2W253 - LG1-2",
  "2W254 - FDR1-3",
  "2W255 - FDR2-3",
  "2W256 - FDR3-3",
  "2W257 - LG2-1",
  "2W258 - LG3-1",
  "2W259 - LG3-2",
  "2W260 - LG3-3",
  "2W261 - LG3-4",
  "2W262 - RB4-1",
  "2W263 - RB4-2",
  "2W264 - HD1-1",
  "2W265 - HD2-1",
  "2W266 - HD3-1",
  "2W267 - HD3-2",
  "2W268 - HD3-3",
  "2W269 - HD3-4",
  "2W270 - HD4-1",
  "2W271 - DRR3-1",
  "2W272 - DRR4-1",
  "2W273 - DRR 5-1",
  "2W274 - DRR 5-2",
  "2W275 - DRR 5-3",
  "2W276 - DRR 5-4",
  "2W277 - DRR6-1",
  "2W278 - DRL3-1",
  "2W279 - DRL4-1",
  "2W280 - DRL 5-1",
  "2W281 - DRL 5-2",
  "2W282 - DRL 5-3",
  "2W283 - DRL 5-4",
  "2W284 - DRL 6-1",
  "2W285 - MC1000DL-01",
]

# função de login
def login(page, username, password):
    page.goto("https://spa.checklistfacil.com.br/login?lang=pt-br", wait_until="load")
    page.fill("[name='user-name']", username)
    page.click("text= Continuar ")
    page.fill("[name='user-password']", password)
    page.click("text= Entrar ")
    page.wait_for_url("https://app.checklistfacil.com.br/", timeout=70000)
    logger.info("Login realizado com sucesso.")

# função para criar checklist
def criar_checklist(nome_checklist, page):
    page.goto("https://app.checklistfacil.com.br/settings/checklists", wait_until="load")
    logger.info(f'Criando checklist "{nome_checklist}"...')
    page.click('[id="button-create-new"]', timeout=7000)
    page.click("span.segment__name:has-text('Novo Checklist')", timeout=7000)
    page.get_by_role("combobox", name="Assunto").click()
    page.get_by_role("option", name="Gestão de Manutenção", exact=True).click(timeout=7000)
    page.get_by_label("Nome", exact=True).fill(nome_checklist, timeout=5000)
    page.get_by_role("button", name="Salvar", exact=True).click(timeout=10000)
    page.get_by_role("button", name="Importar itens via planilha").wait_for(state="visible", timeout=50000)
    logger.info(f'Checklist "{nome_checklist}" criado com sucesso!')

# função para importar planilha
def importar_itens_via_planilha(page, caminho_arquivo):
    try:
        logger.info(f"Importando arquivo: {caminho_arquivo.name}")
        page.get_by_role("button", name="Importar itens via planilha").click()
        page.get_by_role("button", name="Carregar").click()
        page.locator('input[type="file"]').set_input_files(str(caminho_arquivo))
        logger.info("Arquivo enviado, iniciando importação...")
        page.get_by_role("button", name="Iniciar importação").click()
        page.get_by_role("button", name="Ir para estrutura").wait_for(state="visible", timeout=50000)
        page.get_by_role("button", name="Ir para estrutura").click()
        logger.info(f"Importação do arquivo {caminho_arquivo.name} concluída.")
        return True
    except Exception as e:
        logger.error(f"Erro ao importar {caminho_arquivo.name}: {e}")
        return False
    

# função para configurar usuários do checklist
def configurar_usuarios_checklist(page, usuarios: list[str]):
    try:
        logger.info("Configurando permissões de visualização do checklist...")
        page.get_by_role("tab", name="Usuários").wait_for(state="visible", timeout=15000)
        page.get_by_role("tab", name="Usuários").click()

        for usuario in usuarios:
            logger.info(f"Procurando linha do usuário: {usuario}")
            linha_usuario = page.locator(f'tr:has-text("{usuario}")')
            linha_usuario.wait_for(timeout=15000)

            aplica_toggle = linha_usuario.locator('[data-toggle-group-by="toggleApply"]')
            input_toggle = aplica_toggle.locator('input.toggle__input')

            valor_atual = input_toggle.get_attribute("value")
            if valor_atual == "0":
                logger.info(f"Marcando 'Aplica' para {usuario}")
                aplica_toggle.click()
            else:
                logger.info(f"'Aplica' já está marcado para {usuario}")

        # clica em salvar
        salvar_btn = page.locator('#button-form-save')
        salvar_btn.wait_for(state="visible", timeout=20000)
        salvar_btn.click()
        logger.info("Cliquei em salvar, aguardando o modal...")

        # espera pelo modal visível com texto único
        modais = page.locator(".mdc-dialog__surface").filter(has_text="Tem certeza que deseja alterar este vínculo?")
        modal_encontrado = None
        for i in range(modais.count()):
            modal = modais.nth(i)
            if modal.is_visible():
                modal_encontrado = modal
                break

        if not modal_encontrado:
            raise Exception("Modal de confirmação visível não encontrado.")

        # dentro do modal correto, localiza botão Confirmar habilitado
        confirmar_btn = modal_encontrado.locator("button:has-text('Confirmar')")

        for _ in range(20):  # tenta por até 10 segundos
            if confirmar_btn.is_visible() and confirmar_btn.is_enabled():
                confirmar_btn.click()
                logger.info("Botão 'Confirmar' clicado com sucesso.")
                break
            time.sleep(0.5)
        else:
            raise TimeoutError("Botão 'Confirmar' não habilitou a tempo.")

        logger.info("Permissões configuradas e confirmadas com sucesso.")

    except Exception as e:
        logger.error(f"Erro ao configurar usuários: {e}")

# agora fora dessa função, defina:
def esperar_botao_confirmar_habilitar(page, timeout=30):
    logger.info("Esperando botão 'Confirmar' habilitar...")
    confirmar_btn = page.locator("button.mdc-dialog__button").filter(has_text="Confirmar").first

    confirmar_btn.wait_for(state="visible", timeout=timeout * 1000)

    for _ in range(timeout * 2):  # 2 checagens por segundo
        if confirmar_btn.is_enabled():
            logger.info("Botão 'Confirmar' habilitado!")
            return confirmar_btn
        time.sleep(0.5)

    raise TimeoutError("O botão 'Confirmar' não foi habilitado dentro do tempo esperado.")
# Função principal
def run(username, password):
    usuarios_autorizados = [
        "Antônio Carlos da Silva Moreira",
        "Pedro Henrique Melo da Silva",
        "Thiago Marques Sanchez"
    ]

    base_sub = Path(r"C:\Users\matheus.ferreira\Documents\PROGRAMA\SUB")
    xls_files = list(base_sub.rglob("*.xlsx"))
    if not xls_files:
        logger.error("Nenhum arquivo .xlsx encontrado na pasta SUB")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login(page, username, password)

        while True:
            print("\nSelecione o robô para processar:")
            for i, robo in enumerate(robos, 1):
                print(f"{i}. {robo}")
            print(f"{len(robos) + 1}. Sair")

            try:
                escolha = int(input("\nDigite o número do robô desejado: "))
                if escolha == len(robos) + 1:
                    print("Saindo...")
                    break
                elif 1 <= escolha <= len(robos):
                    robo_selecionado = robos[escolha - 1]
                    print(f"Processando o robô: {robo_selecionado}")

                    for arquivo in xls_files:
                        nome_checklist = f"{robo_selecionado} - {arquivo.stem}"
                        try:
                            criar_checklist(nome_checklist, page)
                            sucesso = importar_itens_via_planilha(page, arquivo)
                            if sucesso:
                                configurar_usuarios_checklist(page, usuarios_autorizados)
                            else:
                                logger.error(f"Falha na importação: {robo_selecionado} / {arquivo.name}")
                        except Exception as geral_e:
                            logger.error(f"Erro geral no checklist {nome_checklist}: {geral_e}")
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        browser.close()
        logger.info("Execução finalizada.")

if __name__ == "__main__":
    run(username="nome do seu usuario para logar no site ", password="senha do seu usuario")
