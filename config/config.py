import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://user:password@localhost:5432/greenwheels_fleet'
    )

    # Kafka
    KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')
    KAFKA_TOPIC_GPS = 'vehicle-gps-tracking'
    KAFKA_TOPIC_BATTERY = 'battery-status'
    KAFKA_TOPIC_TRIPS = 'trip-events'
    KAFKA_TOPIC_MAINTENANCE = 'maintenance-alerts'
    KAFKA_TOPIC_CHARGING = 'charging-station-status'
    KAFKA_CONSUMER_GROUP = 'greenwheels-consumers'

    # Redis
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

    # Battery thresholds
    BATTERY_WARNING_LEVEL = 20  # %
    BATTERY_CRITICAL_LEVEL = 10  # %
    BATTERY_OPTIMAL_CHARGE = 80  # %

    # GPS tracking
    GPS_UPDATE_INTERVAL = 30  # seconds
    GEOFENCE_RADIUS = 5  # km from charging stations

    # Maintenance thresholds
    SERVICE_INTERVAL_KM = 10000  # km
    TIRE_REPLACEMENT_KM = 50000  # km
    BRAKE_SERVICE_KM = 15000  # km
