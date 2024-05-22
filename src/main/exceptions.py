from fastapi import HTTPException
from starlette import status


class ApplicationException(HTTPException):
    def __init__(
        self,
        key: str,
        message: str = None,
        details: any = None,
        status_code: int = None,
    ):
        """
        Construtor.
        - key: identificador unico do erro dentro da aplicação.
        - message: Mensagem do erro.
        - details: Detalhes do erro.
        - http_status_code: Código do erro HTTP (valor padrão 500).
        """
        self.key = key if key is not None else "application_with_error"
        self.message = message
        self.details = details
        self.status_code = status_code if status_code is not None else 500
