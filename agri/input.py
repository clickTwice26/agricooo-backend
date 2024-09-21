from pydantic import BaseModel, field_validator

class accountCreationInfo(BaseModel):
    fullName: str
    phoneNumber: str
    email : str | None = None
    clientDeviceInfo : str | None = None
    accountCreationIp : str | None = None

    @field_validator("phoneNumber")
    def validate_phoneNumber(cls, value: str):
        if not value.isdigit() or len(value) != 11 or not value.startswith("01"):
            raise ValueError("provide a valid phone number")
        return value
    @field_validator("email")
    def validate_email(cls, value: str):
        if value is None:
            return None
        if not value.count("@") == 1 or not len(value.split("@")) > 1:
            raise ValueError("provide a valid email address")
        else:
            return value

class aiReplyInput(BaseModel):
    prompt : str
    chatId : str | None = None
    accessToken : str

class seekUserInfo(BaseModel):
    accessToken: str

