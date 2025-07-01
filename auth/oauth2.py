# from fastapi.security import OAuth2PasswordBearer
 
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")  # dummy login endpoint for Swagger

# from fastapi.security import OAuth2PasswordBearer
# from fastapi import Depends, HTTPException, status
# from jose import JWTError, jwt
 
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")  # needed for Swagger
 
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, "saurabhsecretkey12345678901234567890", algorithms=["HS256"])
#         return payload
#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

# from fastapi import Security, HTTPException, status

# from fastapi.security import APIKeyHeader

# from jose import jwt, JWTError
 
# SECRET_KEY = "your-secret-key"

# ALGORITHM = "HS256"
 
# # This tells FastAPI to look for the Authorization header

# api_key_header = APIKeyHeader(name="Authorization")
 
# def get_current_user(token: str = Security(api_key_header)):

#     if not token.startswith("Bearer "):

#         raise HTTPException(status_code=403, detail="Authorization must start with Bearer")
 
#     jwt_token = token[len("Bearer "):]

#     try:

#         payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])

#         return payload  # Ex: { "sub": "user@example.com", "role": "admin" }

#     except JWTError:

#         raise HTTPException(status_code=401, detail="Invalid JWT token")


# from fastapi import Security, HTTPException, status

# from fastapi.security import APIKeyHeader

# from jose import jwt, JWTError
 
# SECRET_KEY = "saurabhsecretkey12345678901234567890"  # Use same as jwt.io

# ALGORITHM = "HS256"
 
# api_key_header = APIKeyHeader(name="Authorization")
 
# def get_current_user(token: str = Security(api_key_header)):

#     if not token.startswith("Bearer "):

#         raise HTTPException(status_code=403, detail="Authorization must start with Bearer")
 
#     jwt_token = token[len("Bearer "):]

#     try:

#         payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])

#         return payload

#     except JWTError:

#         raise HTTPException(status_code=401, detail="Invalid JWT token")

 
from fastapi import Depends, HTTPException, status

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from fastapi.openapi.models import HTTPBearer as HTTPBearerModel

from fastapi.openapi.models import SecuritySchemeType

from fastapi.security.base import SecurityBase
 
class SwaggerBearer(HTTPBearer, SecurityBase):
    def __init__(self):
        super().__init__()
        self.model = HTTPBearerModel(
            type="http",  
            scheme="bearer",
            bearerFormat="JWT",
        )
        self.scheme_name = "JWT"

security = SwaggerBearer()
 
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials
 
    expected_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6ImFkbWluIn0.xob4dHm4rikTbAyqBaYtVSRzeO7Sz3chteZBjBoVmM0"  # your token
 
    if token != expected_token:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid or expired token"

        )

    return {"user": "admin"}

 
