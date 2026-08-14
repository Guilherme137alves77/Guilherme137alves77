# Design — GitHub Profile: Cybersecurity Engineering Lab

Identidade: **Dark Technical Minimalism**.
A ideia é parecer um laboratório pessoal de segurança, não um template nem um
perfil "hacker" genérico. Sem caveiras, sem chuva de código, sem neon exagerado.

---

## 1. Paleta

| Token             | Hex       | Uso                                        |
| ----------------- | --------- | ------------------------------------------ |
| Background        | `#080B10` | fundo geral                                |
| Secondary         | `#0D1117` | painéis, janela do terminal                |
| Cards             | `#111820` | cards, camadas, chips                      |
| Border            | `#1C2733` | bordas, linhas, grid de pontos             |
| Primary           | `#38BDF8` | destaques, links, prompts `$`, `// labels` |
| Secondary accent  | `#2DD4BF` | teal — outputs, "in progress", status      |
| Text              | `#E6EDF3` | texto principal                            |
| Muted             | `#8B949E` | texto secundário, hex/tags                 |
| Light blue (dev)  | `#7DD3FC` | categoria Development                       |
| Green             | `#4ADE80` | apenas pontual: `building...`              |
| Amber             | `#F59E0B` | apenas pontual: Git e MITRE ATT&CK no lab  |

Regra: azul/ciano dominam. Verde e âmbar aparecem só em pontos específicos.

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
│   ├── timeline.svg           → roadmap "cybersecurity journey"
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

Header → About (`architecture.svg`) → Currently Learning (`learning.svg`) →
Selected Projects → Cybersecurity Journey (`timeline.svg`) → Security Lab
(`lab.svg`) → GitHub Stats → Identity (`terminal.svg`) → Footer.

A ordem conta a história: quem sou → o que estudo → o que construo → onde
estou → com que ferramentas → números → identidade → despedida.
