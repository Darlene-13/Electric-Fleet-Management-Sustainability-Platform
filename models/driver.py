class Driver(db.Model):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    id_number = db.Column(db.String(50), unique=True, nullable=False)
    license_number = db.Column(db.String(50), unique=True, nullable=False)
    license_expiry = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='active')  # active, inactive, suspended
    total_trips = db.Column(db.Integer, default=0)
    total_distance_km = db.Column(db.Float, default=0.0)
    total_earnings = db.Column(db.Float, default=0.0)
    rating = db.Column(db.Float, default=5.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    trips = db.relationship('Trip', backref='driver', lazy=True)
    earnings = db.relationship('DriverEarnings', backref='driver', lazy=True, cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'driver_id': self.driver_id,
            'name': self.name,
            'phone': self.phone,
            'license_number': self.license_number,
            'status': self.status,
            'total_trips': self.total_trips,
            'total_distance_km': round(self.total_distance_km, 2),
            'total_earnings': round(self.total_earnings, 2),
            'rating': round(self.rating, 1),
            'created_at': self.created_at.isoformat()
        }
