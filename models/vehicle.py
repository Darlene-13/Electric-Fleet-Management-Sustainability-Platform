from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()


class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(20), unique=True, nullable=False, index=True)
    model = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    year_manufactured = db.Column(db.Integer, nullable=False)
    vin = db.Column(db.String(50), unique=True, nullable=False)
    battery_capacity_kwh = db.Column(db.Float, nullable=False)  # e.g., 75 kWh
    motor_power_kw = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='available')  # available, in_use, charging, maintenance
    current_odometer_km = db.Column(db.Float, default=0.0)
    current_battery_percent = db.Column(db.Float, default=100.0)
    last_gps_latitude = db.Column(db.Float, nullable=True)
    last_gps_longitude = db.Column(db.Float, nullable=True)
    last_gps_update = db.Column(db.DateTime, nullable=True)
    assigned_driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    driver = db.relationship('Driver', backref='assigned_vehicles', foreign_keys=[assigned_driver_id])
    battery_logs = db.relationship('BatteryLog', backref='vehicle', lazy=True, cascade='all, delete-orphan')
    trips = db.relationship('Trip', backref='vehicle', lazy=True, cascade='all, delete-orphan')
    maintenance_records = db.relationship('MaintenanceRecord', backref='vehicle', lazy=True,
                                          cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'plate_number': self.plate_number,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'battery_capacity_kwh': self.battery_capacity_kwh,
            'motor_power_kw': self.motor_power_kw,
            'status': self.status,
            'odometer_km': self.current_odometer_km,
            'battery_percent': self.current_battery_percent,
            'location': {
                'latitude': self.last_gps_latitude,
                'longitude': self.last_gps_longitude,
                'last_update': self.last_gps_update.isoformat() if self.last_gps_update else None
            },
            'assigned_driver_id': self.assigned_driver_id,
            'created_at': self.created_at.isoformat()
        }
