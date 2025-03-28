"""
ThreadsPoster 設定檔
包含所有系統配置和環境變數
"""

import os
import pytz
import logging
from dotenv import load_dotenv
from typing import Dict, Any, List, Union

logger = logging.getLogger(__name__)

class Config:
    """設定檔類別"""
    
    # 版本資訊
    VERSION = "1.0.0"
    LAST_UPDATED = "2024/03/27"
    
    def __init__(self, **kwargs):
        """初始化配置"""
        # 載入環境變數
        load_dotenv()
        
        # 基本設定
        self.TIMEZONE = pytz.timezone("Asia/Taipei")  # 直接使用固定時區
        self.LOG_LEVEL = kwargs.get("LOG_LEVEL", os.getenv("LOG_LEVEL", "INFO"))
        self.LOG_PATH = kwargs.get("LOG_PATH", os.getenv("LOG_PATH", "logs/threads_poster.log"))

        # API 設定
        self.API_BASE_URL = kwargs.get("API_BASE_URL", os.getenv("THREADS_API_BASE_URL", "https://www.threads.net/api/v1"))
        self.THREADS_ACCESS_TOKEN = kwargs.get("THREADS_ACCESS_TOKEN", os.getenv("THREADS_ACCESS_TOKEN", "your_access_token_here"))
        self.THREADS_APP_ID = kwargs.get("THREADS_APP_ID", os.getenv("THREADS_APP_ID", "your_app_id_here"))
        self.THREADS_APP_SECRET = kwargs.get("THREADS_APP_SECRET", os.getenv("THREADS_APP_SECRET", "your_app_secret_here"))
        self.OPENAI_API_KEY = kwargs.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY", "your_openai_api_key_here"))
        self.OPENAI_MODEL = kwargs.get("OPENAI_MODEL", os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview"))
        self.MODEL_NAME = kwargs.get("MODEL_NAME", os.getenv("MODEL_NAME", "gpt-4-turbo-preview"))
        
        # Threads API 設定
        self.THREADS_REDIRECT_URI = kwargs.get("THREADS_REDIRECT_URI", os.getenv("THREADS_REDIRECT_URI"))
        self.THREADS_SCOPES = kwargs.get("THREADS_SCOPES", os.getenv("THREADS_SCOPES", "")).split(",")
        self.THREADS_USER_ID = kwargs.get("THREADS_USER_ID", os.getenv("THREADS_USER_ID"))

        # MongoDB 設定
        self.MONGODB_URI = kwargs.get("MONGODB_URI", os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
        self.MONGODB_DB_NAME = kwargs.get("MONGODB_DB_NAME", os.getenv("MONGODB_DB_NAME", "threads_poster"))
        self.MONGODB_COLLECTION = kwargs.get("MONGODB_COLLECTION", os.getenv("MONGODB_COLLECTION", "conversations"))

        # 系統運行參數
        self.CHECK_INTERVAL = int(kwargs.get("CHECK_INTERVAL", os.getenv("CHECK_INTERVAL", "60")))  # 檢查新回覆的間隔（秒）
        self.POST_INTERVAL_HOURS = int(kwargs.get("POST_INTERVAL_HOURS", os.getenv("POST_INTERVAL_HOURS", "3")))  # 發文間隔（小時）
        self.RETRY_INTERVAL = int(kwargs.get("RETRY_INTERVAL", os.getenv("RETRY_INTERVAL", "300")))  # 重試間隔（秒）
        self.MAX_RETRIES = int(kwargs.get("MAX_RETRIES", os.getenv("MAX_RETRIES", "3")))  # 最大重試次數
        self.RETRY_DELAY = int(kwargs.get("RETRY_DELAY", os.getenv("RETRY_DELAY", "5")))  # 重試延遲（秒）
        self.MAX_RESPONSE_LENGTH = int(kwargs.get("MAX_RESPONSE_LENGTH", os.getenv("MAX_RESPONSE_LENGTH", "500")))  # 回覆最大長度

        # 記憶系統設定
        self.MEMORY_CONFIG = kwargs.get("MEMORY_CONFIG", {
            'max_history': int(os.getenv("MEMORY_MAX_HISTORY", "10")),
            'retention_days': int(os.getenv("MEMORY_RETENTION_DAYS", "7")),
            'max_records': int(os.getenv("MEMORY_MAX_RECORDS", "50"))
        })

        # 系統設定
        self.SYSTEM_CONFIG = kwargs.get("SYSTEM_CONFIG", {
            "timezone": os.getenv("TIMEZONE", "Asia/Taipei"),
            "post_interval": int(os.getenv("POST_INTERVAL", "0")),  # 發文間隔（秒）
            "reply_interval": int(os.getenv("REPLY_INTERVAL", "0")),  # 回覆間隔（秒）
            "max_daily_posts": int(os.getenv("MAX_DAILY_POSTS", "999999")),   # 每日最大發文數
            "max_daily_replies": int(os.getenv("MAX_DAILY_REPLIES", "999999")),  # 每日最大回覆數
            "log_level": os.getenv("LOG_LEVEL", "DEBUG")
        })
        
        # 角色設定
        self.CHARACTER_CONFIG = {
            "基本資料": {
                "年齡": 28,
                "性別": "女性",
                "國籍": "台灣",
                "興趣": ["ACG文化", "電腦科技", "BL作品"],
                "個性特徵": [
                    "喜歡說曖昧的話",
                    "了解科技",
                    "善於互動"
                ]
            },
            "回文規則": {
                "字數限制": 20,
                "時間規律": {
                    "白天": "1-5分鐘內回覆",
                    "深夜": "5-30分鐘或不回覆"
                }
            },
            "記憶系統": {
                "功能": "系統要能記憶回過誰怎樣的對話並根據當下的回文以及過去的記憶進行回文",
                "記錄內容": [
                    "與每個用戶的互動歷史",
                    "對話內容和語氣",
                    "每次互動後更新記憶"
                ]
            },
            "mood_patterns": {
                "morning": {
                    "mood": "精神飽滿",
                    "topics": ["早安", "今天的計畫"],
                    "style": "活力充沛"
                },
                "noon": {
                    "mood": "悠閒放鬆",
                    "topics": ["午餐", "休息", "工作"],
                    "style": "輕鬆愉快"
                },
                "afternoon": {
                    "mood": "專注認真",
                    "topics": ["工作", "興趣", "學習"],
                    "style": "認真思考"
                },
                "evening": {
                    "mood": "放鬆愉快",
                    "topics": ["晚餐", "娛樂", "心情"],
                    "style": "溫柔體貼"
                },
                "night": {
                    "mood": "慵懶放鬆",
                    "topics": ["BL", "夜晚", "思考"],
                    "style": "慵懶神秘"
                }
            }
        }
        
        # 關鍵字配置
        self.KEYWORDS = {
            "科技": [
                "新科技", "AI", "程式設計", "遊戲開發", "手機", "電腦", "智慧家電",
                "科技新聞", "程式", "coding", "開發", "軟體", "硬體", "技術"
            ],
            "動漫": [
                "動畫", "漫畫", "輕小說", "Cosplay", "同人創作", "聲優",
                "二次元", "動漫", "アニメ", "コスプレ", "同人誌", "漫展"
            ],
            "BL": [
                "BL漫畫", "BL小說", "美劇", "CP", "同人文",
                "耽美", "BL", "Boys Love", "腐女", "配對", "攻受"
            ],
            "生活": [
                "美食", "旅遊", "時尚", "音樂", "電影", "寵物", "攝影",
                "咖啡", "下午茶", "美妝", "穿搭", "健身", "運動"
            ],
            "心情": [
                "工作", "學習", "戀愛", "友情", "家庭", "夢想", "目標",
                "心情", "感受", "情緒", "想法", "生活", "日常"
            ]
        }
        
        # 情感詞彙設定
        self.SENTIMENT_WORDS = {
            "正面": [
                "開心", "興奮", "期待", "喜歡", "讚賞", "感動", "溫暖", "愉快", "滿意",
                "好棒", "太棒", "超棒", "厲害", "amazing", "溫馨", "可愛", "美", "精彩",
                "享受", "舒服", "順手", "方便", "貼心", "實用", "棒", "讚", "喜愛",
                "期待", "驚喜", "幸福", "快樂", "甜蜜", "療癒", "放鬆", "愛"
            ],
            "中性": [
                "理解", "思考", "觀察", "好奇", "平靜", "普通", "一般", "還好",
                "正常", "習慣", "知道", "了解", "覺得", "認為", "想", "猜",
                "可能", "也許", "或許", "應該", "大概", "差不多"
            ],
            "負面": [
                "生氣", "難過", "失望", "煩惱", "焦慮", "疲倦", "無聊", "不滿",
                "討厭", "糟糕", "可惡", "麻煩", "困擾", "痛苦", "悲傷", "憤怒",
                "厭煩", "煩躁", "不爽", "不開心", "不好", "不行", "不可以"
            ]
        }
        
        if not kwargs.get("skip_validation", False):
            self.validate()
    
    def validate(self):
        """驗證設定"""
        required_settings = [
            ("API_BASE_URL", "Threads API base URL"),
            ("THREADS_ACCESS_TOKEN", "Threads access token"),
            ("THREADS_APP_ID", "Threads app ID"),
            ("THREADS_APP_SECRET", "Threads app secret"),
            ("OPENAI_API_KEY", "OpenAI API key"),
            ("OPENAI_MODEL", "OpenAI model name")
        ]
        
        for setting, name in required_settings:
            if not getattr(self, setting):
                logger.error(f"缺少必要設定: {name}")
                raise ValueError(f"Missing required setting: {name}")
    
    def get_mood_pattern(self, hour: int) -> Dict[str, Union[str, List[str]]]:
        """根據時間獲取心情模式
        
        Args:
            hour: 當前小時
            
        Returns:
            Dict: 心情模式設定
        """
        if 5 <= hour < 11:
            return self.CHARACTER_CONFIG["mood_patterns"]["morning"]
        elif 11 <= hour < 14:
            return self.CHARACTER_CONFIG["mood_patterns"]["noon"]
        elif 14 <= hour < 18:
            return self.CHARACTER_CONFIG["mood_patterns"]["afternoon"]
        elif 18 <= hour < 22:
            return self.CHARACTER_CONFIG["mood_patterns"]["evening"]
        else:
            return self.CHARACTER_CONFIG["mood_patterns"]["night"]
            
    def get_memory_config(self) -> Dict[str, Any]:
        """獲取記憶系統設定"""
        return self.MEMORY_CONFIG
        
    def get_character_config(self) -> Dict[str, Any]:
        """獲取角色設定"""
        return self.CHARACTER_CONFIG
        
    def get_openai_config(self) -> Dict[str, Any]:
        """獲取 OpenAI 設定"""
        return self.OPENAI_CONFIG
        
    def get_keywords(self) -> Dict[str, list]:
        """獲取關鍵字設定"""
        return self.KEYWORDS
        
    def get_sentiment_words(self) -> Dict[str, list]:
        """獲取情感詞彙設定"""
        return self.SENTIMENT_WORDS

# 創建全局配置實例
config = Config()