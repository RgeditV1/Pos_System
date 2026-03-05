import logging
import sys
from datetime import datetime
from pathlib import Path

def setup_logging(level: int = logging.INFO) -> None: 
    '''Aqui definiremos como funcionara el sistema de logs'''
    logs_dir = Path.cwd() / 'logs'
    if getattr(sys, 'frozen', False): # en dado caso que estemos usando el archivo compilado
        logs_dir = Path.home() /'.pos_system' / 'logs'

    logs_dir.mkdir(parents=True, exist_ok=True)

    log_file = logs_dir / f"pos_{datetime.now().strftime('%Y-%m-%d')}.txt"

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    if root_logger.handlers:
        root_logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)
