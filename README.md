<!--
  GitHub Profile · Guilherme Alves
  Dark Technical Minimalism
  Fileira de construção: fundamento → experimento → código → documento.
-->

<p align="center">
  <pre>
  ██████╗ ██╗   ██╗██╗██╗  ██╗███████╗██████╗ ███╗   ███╗███████╗
 ██╔════╝ ██║   ██║██║██║  ██║██╔════╝██╔══██╗████╗ ████║██╔════╝
 ██║  ███╗██║   ██║██║███████║█████╗  ██████╔╝██╔████╔██║█████╗
 ██║   ██║██║   ██║██║██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══╝
 ╚██████╔╝╚██████╔╝██║██║  ██║███████╗██║  ██║██║ ╚═╝ ██║███████╗
  ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
  </pre>
  <sub>Cybersecurity Student · Developer<br/>Building. Learning. Documenting.</sub>
</p>

<p align="center">
  <em>Caderno público de estudos em cibersegurança.</em><br/>
  Este GitHub registra o que estou aprendendo, os experimentos que desenvolvo
  e como transformo teoria em código.
</p>

---

## `// foco atual`

| Foco                       | Andamento          |
| -------------------------- | ------------------ |
| Cybersecurity              | ██████████████░░░░ |
| Python · Automação         | ████████████████░░ |
| Low Level (C · Assembly)   | ██████████░░░░░░░░ |
| Redes                      | ███████████░░░░░░░ |

Roteiro organizado em **M0 → M25** — dos fundamentos da computação ao *security research*:

```text
Fundamentos → Bits/Binário/Hex → C & Memória → Assembly & Debugging
→ Exploit Dev → RE & Malware → Redes → Web Security
→ Blue Team / SOC → DFIR & Forense → CTF & Research
```

---

## `// linguagens`

| Linguagem    | Nível          | Evidência                                            |
| ------------ | -------------- | ---------------------------------------------------- |
| Python       | Intermediário  | AEGIS, sentinel-firewall, AuthGym, ferramentas       |
| HTML / CSS   | Intermediário  | Barber-site, portfolios                              |
| JavaScript   | Intermediário  | Front-end: Firewall.js, Lab-Cyber                    |
| Node.js      | Em construção  | Express/Fastify: Secure E-commerce Lab               |
| Bash / Shell | Básico/Inter  | Automação Linux, Hyprland config                     |
| SQL (SQLite) | Básico         | Helpers + seed runner                                |
| Lua          | Básico         | LÖVE (StreetKick), configs Hyprland                 |
| C            | Em estudo      | Fundamentos: memória, inteiros, endianness           |

> Níveis medidos pelo **código real enviado neste perfil**, não por autoavaliação.

![Python](https://img.shields.io/badge/Python-Intermedi%C3%A1rio-38BDF8?style=flat&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML%2FCSS-Intermedi%C3%A1rio-38BDF8?style=flat&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Intermedi%C3%A1rio-38BDF8?style=flat&logo=javascript&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-Em%20constru%C3%A7%C3%A3o-F59E0B?style=flat&logo=nodedotjs&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-B%C3%A1sico%2FInter.-2DD4BF?style=flat&logo=gnubash&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-B%C3%A1sico-8B949E?style=flat&logo=sqlite&logoColor=white)
![C](https://img.shields.io/badge/C-Em%20estudo-F59E0B?style=flat&logo=c&logoColor=white)
![Lua](https://img.shields.io/badge/Lua-B%C3%A1sico-8B949E?style=flat&logo=lua&logoColor=white)

---

## `// ferramentas & ambiente`

**Sistemas** `Linux (Fedora)` `Git` `Docker`
**Low Level** `GCC` `xxd` `od` `file`
**Cyber** `Wireshark` `MITRE ATT&CK` `TryHackMe` `Hack The Box` `PortSwigger`
**Em estudo** `Assembly x86` `GDB` `radare2`

---

## `// projetos`

Projetos com código real. **Status honesto**: o que está público, o que é
local e o que está em construção.

### 🛡 AEGIS — Security Automation Toolkit
Plataforma modular de **SOC / Blue Team** em Python: comandos de rede, sistema,
logs, web, integridade e threat intel. CLI com Typer, UI com Rich, coleta via psutil.
`Python` `Typer` `Rich` `psutil` — `● ativo (local, em breve público)`

### 🔥 sentinel-firewall
Mini **Firewall & Intrusion Detection System**: análise de conexões,
blacklist de IPs e logging de alertas em JSON. 100% autoral.
`Python` `OOP` `JSON` — `● público`

### 💪 AuthGym
Sistema de **controle de acesso para academias** com reconhecimento facial
(OpenCV + MediaPipe).
`Python` `OpenCV` `MediaPipe` — `● público`

### 🔍 Lab-Cyber
Plataforma educacional de cibersegurança com **100 desafios práticos**.
`JavaScript` — `● público`

### 🐳 Laboratório de Pentest (Docker)
Ambiente **isolado** (rede interna) com Kali + DVWA + Juice Shop + Metasploitable
para estudo de pentest e Burp Suite.
`Shell` `Docker` `nmap` `sqlmap` — `○ local (não publicado)`

### 🛒 Secure E-commerce Lab
Laboratório de **segurança web / backend** em Express: sessões, CSRF,
validação, rate limiting e modo de treino com vulnerabilidades (IDOR, XSS).
`Node.js` `Express` `SQLite` — `● concluído`

### 🧪 Outros
`StreetKick` (Lua/LÖVE) · `Studying-C` (fundamentos de C) · `Hyprland-cyber` (dotfiles Linux) ·
`Barber-site` (HTML/CSS/JS) · `Avaliacao` (JS) · `Cyber Portfolio` (site)

---

## `// trilha de estudos`

Dias 1–4 concluídos · estudando representação de dados:

* [x] Binário e hexadecimal
* [x] Inteiros e integer overflow
* [x] Endianness · ASCII · UTF-8
* [x] IEEE 754 e ponto flutuante (NaN, infinity)
* [ ] Assembly x86 · debugging

---

## `// filosofia`

```text
Learn → Build → Break → Understand → Document
```

Não quero só usar ferramentas — quero entender **o que acontece por baixo delas**.

---

## `// contato`

- GitHub: [Guilherme137alves77](https://github.com/Guilherme137alves77)
- LinkedIn: [Guilherme Alves](https://www.linkedin.com/in/guilherme-alves-3715a3362)
- Portfolio: [Cyber Portfolio](https://guilherme137alves77.github.io/cyber-portfolio/)

---

```text
$ whoami

guilherme@security-lab
Cybersecurity student
Developer
Linux user
Always learning.
```
