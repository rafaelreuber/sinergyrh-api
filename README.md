Encapsula a API SOA da SinergyRH em uma API Rest.

Para usar a API é necessário configurar as seguintes variáveis de ambientes.

| Variável          | Descrição                                 |
| ----------------- | ----------------------------------------- |
| SINERGYRH_USUARIO | Nome do usuário de acesso à API SinergyRH |
| SINERGYRH_SENHA   | Senha de acesso à API SinergyRH           |
| SINERGYRH_CHAVE   | Chave de Criptografia                     |

## Docker

Faça o build da imagem

```bash
docker image build . -t sinergyrh-api
```

Execute o container passando as variáveis de configuração

```bash
docker container run  \
-e SINERGYRH_USUARIO={usuario}\
-e SINERGYRH_SENHA={senha} \
-e SINERGYRH_CHAVE={chave} \
-p 5000:5000 sinergyrh-api
```


