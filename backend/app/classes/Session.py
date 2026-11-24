from datetime import datetime, timedelta, timezone

from app.core.security import generate_session_token, hash_session_token
from app.core.constants import SESSION_TOKEN_DURATION
from app.db_interfaces.session import SessionDBInterface

class Session:


    def __init__(self, session_db: SessionDBInterface):
        self.session_db=session_db


    def create_session(self, user_email)->str:

        token=generate_session_token()

        token_hash=hash_session_token(token)

        expires_at=datetime.now(timezone.utc)+timedelta(days=SESSION_TOKEN_DURATION)

        #save session
        self.session_db.create(
            user_email,
            token_hash,
            expires_at
        )

        return token