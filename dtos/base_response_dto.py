from pydantic import BaseModel

from resources.config import settings


class BaseResponse(BaseModel):
    code: int = 200
    success: bool = True
    message: str = "status message"

    def set_error_response(self, code:int):
        self.code = code
        self.message = settings.response_code[str(code)]
        self.success = False