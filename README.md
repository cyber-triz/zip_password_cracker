

# 🔐 ZIP Password Cracker em Python

## 📚 Sobre

Este é um script simples em Python para **tentar descobrir a senha de arquivos ZIP protegidos** usando uma técnica de força bruta com uma **wordlist personalizada**.

O objetivo é ajudar quem está estudando segurança da informação a entender conceitos básicos de brute force e manipulação de arquivos.

> ⚠️ **Atenção:** Use este script apenas em arquivos ZIP seus ou com permissão. Quebrar senhas sem autorização é ilegal e antiético.

---

## ⚙️ Como funciona?

- O script recebe o caminho do arquivo ZIP protegido.
- Recebe o caminho de uma wordlist (`.txt`) com possíveis senhas, uma por linha.
- Tenta abrir o ZIP com cada senha da lista até encontrar a correta.
- Exibe a senha quando encontrada ou avisa se não achar.

---

## 🛠️ Como usar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
