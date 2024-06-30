# taskmaster_ai/src/memory/memory_manager.py

import logging
from typing import Dict, Any, Optional
from functools import lru_cache
import sqlite3
import json

class MemoryManager:
    def __init__(self, db_path: str = ':memory:'):
        self.logger = logging.getLogger('MemoryManager')
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memory (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.conn.commit()
        except Exception as e:
            self.logger.error(f"Error creating table: {str(e)}")

    def store_data(self, key: str, data: Dict[str, Any]) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT OR REPLACE INTO memory (key, value) VALUES (?, ?)",
                (key, json.dumps(data))
            )
            self.conn.commit()
            return True
        except Exception as e:
            self.logger.error(f"Error storing data for key {key}: {str(e)}")
            return False

    @lru_cache(maxsize=100)
    def get_data(self, key: str) -> Optional[Dict[str, Any]]:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT value FROM memory WHERE key = ?", (key,))
            result = cursor.fetchone()
            if result:
                return json.loads(result[0])
            return None
        except Exception as e:
            self.logger.error(f"Error retrieving data for key {key}: {str(e)}")
            return None

    def clear_data(self, key: str) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM memory WHERE key = ?", (key,))
            self.conn.commit()
            self.get_data.cache_clear()
            return True
        except Exception as e:
            self.logger.error(f"Error clearing data for key {key}: {str(e)}")
            return False

    def clear_all_data(self) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM memory")
            self.conn.commit()
            self.get_data.cache_clear()
            return True
        except Exception as e:
            self.logger.error(f"Error clearing all data: {str(e)}")
            return False
