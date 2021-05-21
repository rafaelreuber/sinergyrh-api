import os
import clr
import xmltodict
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from zeep import Client

SINERGYRH_WSDL = "https://www.folhasinergyrh.com.br/Sinergy.WebServices.Dados/DadosFuncionarios.asmx?WSDL"
SINERGYRH_USUARIO = os.getenv("SINERGYRH_USUARIO")
SINERGYRH_SENHA = os.getenv("SINERGYRH_SENHA")
SINERGYRH_CHAVE = os.getenv("SINERGYRH_CHAVE")

clr.AddReference('CryptSinergyClient')
import CryptSinergyClient

client = Client(SINERGYRH_WSDL)

headers = {
    "AuthSoapHd": {"Usuario": SINERGYRH_USUARIO, "Senha": SINERGYRH_SENHA}
}

app = Flask(__name__)
CORS(app)


@app.get("/funcionario/<cpf>")
def funcionario(cpf):
    """
    Retorna dos dados do funcionário na plataforma Sinergyrh
    :param cpf: CPF do funcionário
    """
    resultado = client.service.getDadosFuncionariosPorCpf(cpf, _soapheaders=headers)
    xml = CryptSinergyClient.Crypt.Descriptografar(resultado, SINERGYRH_CHAVE)
    dados = xmltodict.parse(xml)
    funcionario = dados['Funcionarios']
    del funcionario['@xmlns:xsi']
    del funcionario['@xmlns:xsd']
    return jsonify(funcionario)


if __name__ == '__main__':
    app.run()
