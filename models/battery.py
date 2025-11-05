from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class BatteryLog(db.Model):
    __tablename__ = 'battery_logs'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    battery_percent = db.Column(db.Float, nullable=False)
    battery_voltage = db.Column(db.Float, nullable=False)
    battery_temperature = db.Column(db.Float, nullable=False)  # Celsius
    status = db.Column(db.String(20))  # charging, discharging, idle
    health_status = db.Column(db.String(20))  # good, degraded, critical
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def to_dict(self):
        return {
            'id': self.id,
            'vehicle_id': self.vehicle_id,
            'battery_percent': self.battery_percent,
            'battery_voltage': self.battery_voltage,
            'battery_temperature': self.battery_temperature,
            'status': self.status,
            'health_status': self.health_status,
            'timestamp': self.timestamp.isoformat()
        }


class ChargingSession(db.Model):
    __tablename__ = 'charging_sessions'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('charging_stations.id'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=True)
    battery_percent_start = db.Column(db.Float, nullable=False)
    battery_percent_end = db.Column(db.Float, nullable=True)
    energy_kwh = db.Column(db.Float, nullable=True)
    cost = db.Column(db.Float, nullable=True)
    duration_minutes = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(20), default='active')  # active, completed, failed

    vehicle = db.relationship('Vehicle', backref='charging_sessions')
    station = db.relationship('ChargingStation', backref='sessions')

    def to_dict(self):
        return {
            'id': self.id,
            'vehicle_id': self.vehicle_id,
            'station_id': self.station_id,
            'battery_percent_start': self.battery_percent_start,
            'battery_percent_end': self.battery_percent_end,
            'energy_kwh': self.energy_kwh,
            'cost': self.cost,
            'duration_minutes': self.duration_minutes,
            'status': self.status,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None
        }