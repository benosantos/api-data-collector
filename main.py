import json
from pathlib import Path
import requests


def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        print("Status HTTP:", resposta.status_code)
        print("ID:", dados["id"])
        print("Tarefa:", dados["title"])
        print("Concluída:", dados["completed"])

        caminho = Path("tarefa.json")

        with caminho.open("w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        print(f"Dados salvos em: {caminho.resolve()}")

    except requests.exceptions.Timeout:
        print("Erro: a requisição demorou demais.")

    except requests.exceptions.HTTPError as erro:
        print("Erro HTTP:", erro)

    except requests.exceptions.RequestException as erro:
        print("Erro de conexão:", erro)

    except (KeyError, ValueError) as erro:
        print("Erro ao processar os dados:", erro)

    except OSError as erro:
        print("Erro ao salvar o arquivo:", erro)


if __name__ == "__main__":
    main()