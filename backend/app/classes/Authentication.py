from app.core.security import verify_password, hash_password
from app.core.exceptions import UnauthorizedError, ForbbidendError, ConflictError
from app.classes.Session import Session

class Authentication:

    def __init__(self, user_DB_interface, session: Session): 
        self.user_DB_interface=user_DB_interface
        self.session=session


    def register(self, email: str, password: str)->int:

        already_exixsting_user = self.user_DB_interface.get_by_email(email)

        if already_exixsting_user is not None:
            ConflictError("Email already associated with an account")

        password_hash=hash_password(password)

        user = self.user_DB_interface.create( #TODO align with real DB
            email,
            password_hash
        )

        return user.id

    def login(self, email: str, password: str)->str:

        user=self.user_DB_interface.get_by_email(email)

        if not user:
            UnauthorizedError("Invalid email or password")

        if not verify_password(password, user.password_hash):
            UnauthorizedError("Invalid email or password")

        if not user.is_active: #TODO we shall use a user_status table, we need to wait Adriquad to implement DB conn
            ForbbidendError("Your account is not active")

        token = self.session.create_session(user.id)

        return token



    def change_password(
            self,
            user_id: int,
            current_password: str,
            new_password: str
    )->None:

        user = self.user_DB_interface.get_by_id(user_id)

        if not user:
            UnauthorizedError("Invalid credentials")
        if not user.is_active: #TODO we shall use a user_status table, we need to wait Adriquad to implement DB conn
            ForbbidendError("Your account is not active")

        if not verify_password(current_password, user.password_hash):
            UnauthorizedError("Incorrect password")

        if verify_password(new_password, user.password_hash): #TODO vanno verificate tutte le password precedenti
            ConflictError("You should use a new password")

        password_hash=hash_password(new_password)

        self.user_DB_interface.updatePassword(
            user_id,
            password_hash
        )

        #TODO revoke all user sessions





    def logout(self, token: str | None)->None:
        self.session.revoke_session(token)
        