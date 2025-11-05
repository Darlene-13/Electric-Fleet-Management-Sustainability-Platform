class ChargingStation(db.Model):
    __tablename__ = 'charging_stations'

    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    total_chargers = db.Column(db.Integer, nullable=False)
    available_chargers = db.Column(db.Integer, nullable=False)
    charger_type = db.Column(db.String(50))  # AC, DC, CCS, etc
    max_power_kw = db.Column(db.Float, nullable=False)
    cost_per_kwh = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='operational')  # operational, maintenance, offline
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'station_id': self.station_id,
            'name': self.name,
            'location': self.location,
            'coordinates': {'latitude': self.latitude, 'longitude': self.longitude},
            'total_chargers': self.total_chargers,
            'available_chargers': self.available_chargers,
            'charger_type': self.charger_type,
            'max_power_kw': self.max_power_kw,
            'cost_per_kwh': self.cost_per_kwh,
            'status': self.status
        }