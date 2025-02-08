# models/engine/db_storage.py

class DBStorage:
    # existing code...

    def close(self):
        """Removes current session"""
        self.__session.remove()

