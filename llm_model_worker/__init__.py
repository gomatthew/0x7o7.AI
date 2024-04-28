# -*- coding: utf-8 -*-
import os
from typing import Dict, List

# Model Settings
TEMPERATURE: float = 0.17
MODEL_ROOT_PATH: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'llm_model')
LLM_MODELS: List[str] = ["Qwen-1_8B-Chat"]
LLM_DEVICE: str = "auto"
DEFAULT_DEVICE: str = 'cpu'
MAX_LENGTH: int = 64
MODEL_CONFIG: Dict[str, Dict] = {
    'Qwen-1_8B-Chat': {'path': 'Qwen/Qwen-1_8B-Chat', 'device': 'auto'}
}

MODEL_MAPPING: Dict[str, List] = {
    'Qwen': ['Qwen-1_8B-Chat']
}
