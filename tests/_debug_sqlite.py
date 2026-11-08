"""Debug: SQLite + BigInteger autoincrement fix"""
import sys
sys.path.insert(0, ".")

from sqlalchemy import create_engine, event, Integer, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

# Patch Enum để dùng non-native trên SQLite
from sqlalchemy import Enum as SAEnum
_orig_init = SAEnum.__init__
def _patched_init(self, *args, **kwargs):
    kwargs.setdefault("native_enum", False)
    _orig_init(self, *args, **kwargs)
SAEnum.__init__ = _patched_init

# Patch BigInteger → Integer cho SQLite (SQLite AUTOINCREMENT chỉ hoạt động với INTEGER)
from sqlalchemy import TypeDecorator
@event.listens_for(engine, "connect")
def _on_connect(dbapi_conn, connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# Override BigInteger rendering cho SQLite
from sqlalchemy.ext.compiler import compiles
@compiles(BigInteger, "sqlite")
def _bi_to_int(element, compiler, **kw):
    return "INTEGER"

from app.core.database import Base
from app.modules.accounts.models import User, OAuthAccount

Base.metadata.create_all(bind=engine)
print("Tables created OK!")

Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
db = Session()

user = User(display_name="Test", role="user", status="active", token_version=0, failed_login_count=0)
db.add(user)
db.commit()
db.refresh(user)
print(f"User created: id={user.id}, display_name={user.display_name}")

oauth = OAuthAccount(user_id=user.id, provider="facebook", provider_user_id="12345")
db.add(oauth)
db.commit()
print(f"OAuth created: provider={oauth.provider}")

db.close()
print("ALL OK!")
