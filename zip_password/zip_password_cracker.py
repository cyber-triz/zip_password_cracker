import zipfile

def crack_zip(zip_path, wordlist_path):
    with zipfile.ZipFile(zip_path) as zf, open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
        print(f"Tentando abrir {zip_path} usando a wordlist {wordlist_path}...\n")
        for line in wordlist:
            password = line.strip()
            try:
                zf.extractall(pwd=password.encode('utf-8'))
                print(f"[+] Senha encontrada: {password}")
                return password
            except:
                pass
        print("[-] Senha não encontrada na wordlist.")
        return None

if __name__ == "__main__":
    zip_file = input("Caminho do arquivo ZIP: ")
    wordlist_file = input("Caminho da wordlist (arquivo txt): ")
    crack_zip(zip_file, wordlist_file)
