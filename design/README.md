# Design — GitHub Profile: QA Automation Lab

Identidade: **Dark Technical Minimalism**.
A ideia é parecer um laboratório pessoal de **QA Automation**, que pesquisa
\"por que quebrou?\" com método — não um template nem um perfil "hacker" genérico.
Narrativa: QA como porta de entrada, segurança (pentest) como destino.

---

## 1. Paleta

| Token            | Hex       | Uso                                        |
| ---------------- | --------- | ------------------------------------------ |
| Background       | `#080C12` | fundo geral                                |
| Secondary        | `#0D1117` | painéis, janela do terminal                |
| Cards            | `#161B22` | cards, camadas, chips                      |
| Border           | `#30363D` | bordas, linhas, grid de pontos             |
| Primary          | `#58A6FF` | destaques, links, prompts `$`, `// labels` |
| Status           | `#3FB950` | outputs, "em andamento", status            |
| Text             | `#E6EDF3` | texto principal                            |
| Muted            | `#8B949E` | texto secundário, hex/tags                 |
| Light blue (dev) | `#79C0FF` | categoria Development                       |
| Amber            | `#D29922` | apenas pontual (Git/chips)                 |

Regra: azul/cinza dominam; verde só em status. Sem neon, sem "cara de hacker".

## 2. Tipografia

- Mono (todo o "código"/terminal):
  `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`
- Sans (títulos/headings):
  `Segoe UI, Roboto, 'Helvetica Neue', Arial, sans-serif`

## 3. Arquivos

```
github-profile/
├── README.md                  → o perfil (usa tokens {{TOKEN}})
├── assets/
│   ├── header.svg             → banner: GUILHERME ALVES + rede/hex/terminal
│   ├── terminal.svg           → identidade: whoami/focus/system/learning/status
│   ├── architecture.svg       → stack hardware → automação
│   ├── learning.svg           → painel "currently learning" (3 colunas)
│   ├── timeline.svg           → roadmap "qa → security" (fundamentos de teste como porta para pentest)
│   └── lab.svg                → "security lab" (tools + plataformas)
├── scripts/
│   ├── config.json            → seus dados (usuário, linkedin, portfolio)
│   └── generate-profile.py    → preenche os tokens do README
└── design/
    └── README.md              → este documento
```

## 4. Por que SVG dentro de `<img>`?

O README do GitHub tem limites importantes:

- sem JavaScript
- HTML sanitizado (`class`/`id` são removidos; estilos inline são limitados a
  um conjunto de propriedades CSS)
- só Markdown/HTML/SVG comuns

Por isso, **todos os elementos visuais** (banner, terminal, roadmap, painéis)
são SVGs renderizados como `<img src="assets/....svg">`. Eles:

- funcionam igual em tema claro ou escuro do GitHub;
- garantem as cores/arestas/glows exatas;
- são vetoriais (não ficam pixelados).

Os textos e tabelas ficam em Markdown/HTML para continuarem selecionáveis e
com links reais.

## 5. Personalização

```bash
# 1. edite seus dados
$EDITOR scripts/config.json

# 2. gere o README
python3 scripts/generate-profile.py
```

O script troca `{{GITHUB_USERNAME}}`, `{{LINKEDIN_URL}}`, `{{PORTFOLIO_URL}}`
e `{{YEAR}}`. Se algum campo estiver vazio, o token é mantido e um aviso é
impresso.

Ajustes manuais:

- **Projetos**: o `SENTINEL` é o projeto ativo de exemplo (não invente
  funcionalidades — edite a descrição e o link real do repo). As linhas
  `YOUR_PROJECT_02/03` são exemplos de slots: remova ou preencha com seus
  projetos reais.
- **Stats**: usa `github-readme-stats` (serviço externo). Necessita do username
  real no `config.json`. Cores já alinhadas à paleta.
- **SVGs**: abra os arquivos em `assets/` e edite as cores/textos se quiser.
  Mantenha `viewBox` e `xmlns` para continuarem válidos.

## 6. Publicação

1. Crie o repositório `<seu-usuario>/<seu-usuario>` (público).
2. Copie `README.md` e a pasta `assets/` para a **raiz** do repositório
   (os caminhos das imagens são relativos: `assets/header.svg`).
3. Opcional: suba também `scripts/` e `design/` para versionar o template.
4. Pronto — o perfil renderiza automaticamente.

## 7. Regras de conteúdo (honestidade)

- Mantenha "Student" no subtítulo — a trajetória transmite construção, não
  títulos falsos.
- Descrições de projetos devem refletir o que existe de verdade.
- Status possíveis: `● ACTIVE` (teal), `○ draft` (muted), `○ planning`.

## 8. Estrutura narrativa

Header → Foco (bloco no README) → Stack (`stack.svg`) → Trilha de Estudos →
Selected Projects (destaque para `java-qa` → projetos de segurança) →
Journey `qa → security` (`timeline.svg`) → Security Lab (`lab.svg`) →
GitHub Stats → Identity (`terminal.svg`) → Footer.

A ordem conta a história: quem sou → o que estudo → o que construo → onde
estou → com que ferramentas → números → identidade → despedida.
