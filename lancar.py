import streamlit.web.cli as stcli
import sys
import os

if __name__ == "__main__":
    try:
        # Aponta para o arquivo principal do seu app
        sys.argv = [
            "streamlit",
            "run",
            os.path.abspath("app.py"),  # Verifique se o nome do seu arquivo principal é app.py
            "--global.developmentMode=false",
        ]
        sys.exit(stcli.main())
    except Exception as e:
        print("\n========================================")
        print("❌ OCORREU UM ERRO AO INICIAR O APLICATIVO:")
        print(e)
        print("========================================")
        input("\nPressione ENTER para fechar esta janela...")