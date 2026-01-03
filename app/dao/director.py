from typing import Dict, List, Optional, Tuple, Union

from app.setup_db import db
from app.dao.models.directors_model import Director

# DAO for directors
class DirectorDAO:
    def __init__(self, session: db.session) -> None:
        self.session = session

    # method for getting all directors
    def get_all(self) -> List[Optional[Dict[str, str]]]:
        return self.session.query(Director).all()

    # method for getting director by id
    def get_one(self, did: int) -> Union[str, Dict[str, str]]:
        try:
            director = self.session.query(Director).filter(Director.id == did).one()

            return director
        except Exception as e:
            return str(e)