from typing import List, Optional

from dtos.base_response_dto import BaseResponse
from resources.config import settings


class FaceToVec(BaseResponse):
    data: Optional[List[float]] = None

    def set_succeed_response(self, code:int, data: List[float] ):
        self.code = code
        self.message = settings.response_code[str(code)]
        self.success = True
        self.data = data
