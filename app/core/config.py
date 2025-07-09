import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret')
DEBUG = os.getenv('DEBUG', 'True') == 'True'

MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'legal_consulting')
MYSQL_USER = os.getenv('MYSQL_USER', 'admin')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'texby4-vEnmar-qytbyx')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'legalex-db.cdmoeoeygmj0.ap-south-1.rds.amazonaws.com')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'AKIATX3PHS3HP273TAGK')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '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')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'dashboard-profile-picture')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'eu-north-1')
AWS_S3_CUSTOM_DOMAIN = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',') 