from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


logs = [
    {
        "ip_address": "52.70.240.171",
        "timestamp": "[04/May/2024:02:26:33 -0700]",
        "request": "GET /self.logs/access.log.2021-03-21.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 14674,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    },
    {
        "ip_address": "3.224.220.101",
        "timestamp": "[04/May/2024:02:26:33 -0700]",
        "request": "GET /self.logs/access.log.2021-03-20.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 13907,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    },
    {
        "ip_address": "3.224.220.101",
        "timestamp": "[04/May/2024:02:26:33 -0700]",
        "request": "GET /self.logs/access.log.2021-03-19.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 12836,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    },
    {
        "ip_address": "3.224.220.101",
        "timestamp": "[04/May/2024:02:26:35 -0700]",
        "request": "GET /self.logs/access.log.2021-03-18.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 18652,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    },
    {
        "ip_address": "52.70.240.171",
        "timestamp": "[04/May/2024:02:26:39 -0700]",
        "request": "GET /self.logs/access.log.2021-03-17.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 46924,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    },
    {
        "ip_address": "23.22.35.162",
        "timestamp": "[04/May/2024:02:26:43 -0700]",
        "request": "GET /self.logs/access.log.2021-03-16.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 18819,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    },
    {
        "ip_address": "23.22.35.162",
        "timestamp": "[04/May/2024:02:26:47 -0700]",
        "request": "GET /self.logs/access.log.2021-03-15.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 52065,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    },
    {
        "ip_address": "23.22.35.162",
        "timestamp": "[04/May/2024:02:26:52 -0700]",
        "request": "GET /self.logs/access.log.2021-03-13.gz HTTP/1.1",
        "status_code": 200,
        "response_size": 21269,
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)"
    }
]


class Log(BaseModel):
    ip_address: str  # The IP address of the client
    timestamp: str   # The time when the log was created
    request: str     # The HTTP request made
    status_code: int # The HTTP response status code
    response_size: int # The size of the response in bytes
    user_agent: str  # The user agent of the client


@app.get("/logs/")
async def get_logs():
    return logs