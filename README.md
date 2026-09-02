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

| Linguagem    | Nível            | Evidência                                            |
| ------------ | ---------------- | ---------------------------------------------------- |
| Python       | Iniciante/Inter  | AEGIS, sentinel-firewall, AuthGym, ferramentas       |
| HTML / CSS   | Intermediário    | Barber-site, portfolios                              |
| JavaScript   | Iniciante/Inter  | Front-end: Firewall.js, Lab-Cyber                    |
| Node.js      | Iniciante        | Express/Fastify: Secure E-commerce Lab               |
| Bash / Shell | Iniciante/Inter  | Automação Linux, Hyprland config                     |
| SQL (SQLite) | Iniciante        | Helpers + seed runner                                |
| Lua          | Iniciante        | LÖVE (StreetKick), configs Hyprland                 |
| C            | Iniciante        | Fundamentos: memória, inteiros, endianness           |

> Níveis medidos pelo **código real enviado neste perfil**, não por autoavaliação.

![Python](https://img.shields.io/badge/Python-Iniciante%2FInter-38BDF8?style=flat&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML%2FCSS-Intermedi%C3%A1rio-38BDF8?style=flat&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Iniciante%2FInter-38BDF8?style=flat&logo=javascript&logoColor=white)
![Node](https://img.shields.io/badge/Node.js-Iniciante-F59E0B?style=flat&logo=nodedotjs&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Iniciante%2FInter-2DD4BF?style=flat&logo=gnubash&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Iniciante-8B949E?style=flat&logo=sqlite&logoColor=white)
![C](https://img.shields.io/badge/C-Iniciante-F59E0B?style=flat&logo=c&logoColor=white)
![Lua](https://img.shields.io/badge/Lua-Iniciante-8B949E?style=flat&logo=lua&logoColor=white)

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

### <img src="assets/icons/aegis.svg" width="20" height="20" alt="AEGIS"/> AEGIS — Security Automation Toolkit
Plataforma modular de **SOC / Blue Team** em Python: comandos de rede, sistema,
logs, web, integridade e threat intel. CLI com Typer, UI com Rich, coleta via psutil.
`Python` `Typer` `Rich` `psutil` — `● ativo (local, em breve público)`

### <img src="assets/icons/sentinel.svg" width="20" height="20" alt="sentinel-firewall"/> sentinel-firewall
Mini **Firewall & Intrusion Detection System**: análise de conexões,
blacklist de IPs e logging de alertas em JSON. 100% autoral.
`Python` `OOP` `JSON` — `● público`

### <img src="assets/icons/authgym.svg" width="20" height="20" alt="AuthGym"/> AuthGym
Sistema de **controle de acesso para academias** com reconhecimento facial
(OpenCV + MediaPipe).
`Python` `OpenCV` `MediaPipe` — `● público`

### <img src="assets/icons/lab-cyber.svg" width="20" height="20" alt="Lab-Cyber"/> Lab-Cyber
Plataforma educacional de cibersegurança com **100 desafios práticos**.
`JavaScript` — `● público`

### <img src="assets/icons/docker-lab.svg" width="20" height="20" alt="Docker Lab"/> Laboratório de Pentest (Docker)
Ambiente **isolado** (rede interna) com Kali + DVWA + Juice Shop + Metasploitable
para estudo de pentest e Burp Suite.
`Shell` `Docker` `nmap` `sqlmap` — `○ local (não publicado)`

### <img src="assets/icons/ecommerce.svg" width="20" height="20" alt="Secure E-commerce"/> Secure E-commerce Lab
Laboratório de **segurança web / backend** em Express: sessões, CSRF,
validação, rate limiting e modo de treino com vulnerabilidades (IDOR, XSS).
`Node.js` `Express` `SQLite` — `● concluído`

### <img src="assets/icons/others.svg" width="20" height="20" alt="Outros"/> Outros
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
