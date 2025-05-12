import os
from dotenv import load_dotenv
import requests


load_dotenv()


class CertifactionAPI:

    def __init__(self):
        self.base_url = "http://localhost:8082"

    def _request(self, method, path, **kwargs):
        return requests.request(
            method,
            f"{self.base_url}/{path}",
            headers={
                "Accept-Language": "de",
                "Content-Type": "application/json",
                "Authorization": os.environ.get("CERTIFACTION_API_KEY"),
            },
            **kwargs,
        )

    def prepare_document(self, path):
        with open(path, "rb") as f:
            # Send the POST request with the file as binary data
            resp = self._request(
                "POST",
                f"prepare?scope=sign&upload=true&additional-page=false",
                data=f,
            )
            resp.raise_for_status()
            file_url = resp.headers["Location"]
            return file_url

    def send_signing_request(self, objs, email, send_email=False):
        file_urls = [self.prepare_document(obj["pdf_path"]) for obj in objs]

        signing_mode = "SES"
        webhook_url = ""
        send_email_text = "true" if send_email else "false"
        x_coord = 1050
        y_coord = 100
        resp = self._request(
            "POST",
            f"request/create?send-email={send_email_text}&email={email}&webhook-url={webhook_url}&legal-weight={signing_mode}&additional-page=false&position-x={x_coord}&position-y={y_coord}&height=100&page=1",
            json={
                "files": [
                    {
                        "url": file_url,
                        "name": obj["name"],
                    }
                    for file_url, obj in zip(file_urls, objs)
                ]
            },
        )
        resp.raise_for_status()
        return resp.json()["request_url"]
