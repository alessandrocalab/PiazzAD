from datetime import datetime, timedelta, timezone

from app.core.security import generate_session_token, hash_session_token
from app.core.constants import SESSION_TOKEN_DURATION
from app.db_interfaces.session import SessionDBInterface

class Session:


    def __init__(self, session_db: SessionDBInterface):
        self.session_db=session_db


    def create_session(self, user_id)->str:

        token=generate_session_token()

        token_hash=hash_session_token(token)

        expires_at=datetime.now(timezone.utc)+timedelta(days=SESSION_TOKEN_DURATION)

        #save session
        self.session_db.create(
            user_id,
            token_hash,
            expires_at
        )

        return token

    
    def validate_session(self, token: str|None)->int|None:
        
        if not token:
            return None
        
        token_hash=hash_session_token(token)
        session=self.session_db.get_by_hash(token_hash)

        if session is None:
            return None

        if session.revoked_at is not None:
            return None
        
        if session.expires_at <= datetime.now(timezone.utc):
            return None

        return session.user_id

    def revoke_session(self, token: str | None)->None:
        
        if not token:
            return

        token_hash = hash_session_token(token)

        self.session_db.revoke_by_hash(
            token_hash,
            revoked_at=datetime.now(timezone.utc)
        )