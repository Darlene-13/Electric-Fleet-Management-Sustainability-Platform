class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
    start_location = db.Column(db.String(200), nullable=False)
    end_location = db.Column(db.String(200), nullable=True)
    start_latitude = db.Column(db.Float, nullable=False)
    start_longitude = db.Column(db.Float, nullable=False)
    end_latitude = db.Column(db.Float, nullable=True)
    end_longitude = db.Column(db.Float, nullable=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    end_time = db.Column(db.DateTime, nullable=True)
    distance_km = db.Column(db.Float, nullable=True)
    duration_minutes = db.Column(db.Integer, nullable=True)
    battery_used_percent = db.Column(db.Float, nullable=True)
    fare_amount = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(20), default='active')  # active, completed, cancelled
    rating = db.Column(db.Float, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    gps_logs = db.relationship('GPSLog', backref='trip', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'vehicle_id': self.vehicle_id,
            'driver_id': self.driver_id,
            'start_location': self.start_location,
            'end_location': self.end_location,
            'distance_km': self.distance_km,
            'duration_minutes': self.duration_minutes,
            'battery_used_percent': self.battery_used_percent,
            'fare_amount': self.fare_amount,
            'status': self.status,
            'rating': self.rating,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'created_at': self.created_at.isoformat()
        }

