import pymysql
import sys

# 1. เชื่อมต่อ pymysql
pymysql.install_as_MySQLdb()

# 2. หลอกเวอร์ชันให้สูงกว่าที่มันต้องการ (ใช้ 2.2.8 ไปเลย)
pymysql.version_info = (2, 2, 8, "final", 0)

# 3. ฉีดค่าเข้าไปในระบบของ MySQLdb ด้วย
sys.modules['MySQLdb'].__version__ = '2.2.8'