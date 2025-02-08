# models/engine/file_storage.py

class FileStorage:
    # existing code...

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()

