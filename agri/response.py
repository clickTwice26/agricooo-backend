from pydantic import BaseModel
from typing import Literal

import agri.constants as Constants

class WelcomeMessage(BaseModel):
    message : str = "welcome to agricooo"
    versionNo : float = Constants.versionNo
    version : str = Constants.version

class ErrorMessage(BaseModel):
    errorType : str | None = "warning"
    errorMessage : str | None = "something went wrong"
    errorCode : int | None = 0
class FlashMessage(BaseModel):
    message : str = "Something went wrong"
    category : Literal["info", "error", "success", "warning"] | None  = "info"
