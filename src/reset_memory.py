#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
重置資料庫中的記憶
"""

import asyncio
import logging
from database import Database
from config import Config

async def main():
    """主函數"""
    try:
        # 初始化設定
        config = Config()
        
        # 初始化資料庫
        db = Database(config)
        await db.initialize()
        
        # 刪除所有記憶
        await db.personality_memories.delete_many({})
        print("已刪除所有記憶")
        
        # 重新初始化記憶
        await db._init_personality_memory()
        print("已重新初始化記憶")
        
        # 關閉資料庫連接
        await db.close()
        print("資料庫連接已關閉")
        
    except Exception as e:
        print(f"重置記憶時發生錯誤：{str(e)}")
        
if __name__ == "__main__":
    # 設定日誌
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    asyncio.run(main()) 