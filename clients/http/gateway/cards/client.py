from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient

class IssueCardRequest(TypedDict):
    """
    Структура данных для выпуска карты.
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    def issue_virtual_card_api(self, request: IssueCardRequest) -> Response:
        """
        Выпустить виртуальную карту.

        :param request: Сигнатура запроса на выпуск карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequest) -> Response:
        """
        Выпустить физическую карту.

        :param request: Сигнатура запроса на выпуск карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post("/api/v1/cards/issue-physical-card", json=request)