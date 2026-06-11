class Booking:
    _id_counter = 1
    all_bookings = []

    def __init__(self, screening_id, customer_name, seats_booked, booking_id=None):
        self.screening_id = int(screening_id)
        self.customer_name = customer_name
        self.seats_booked = seats_booked

        if booking_id:
            self.id = booking_id
            if booking_id >= Booking._id_counter:
                Booking._id_counter = booking_id + 1
        else:
            self.id = Booking._id_counter
            Booking._id_counter += 1

        Booking.all_bookings.append(self)

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Customer name cannot be empty.")
        self._customer_name = value.strip()

    @property
    def seats_booked(self):
        return self._seats_booked

    @seats_booked.setter
    def seats_booked(self, value):
        try:
            val = int(value)
        except (ValueError, TypeError):
            raise ValueError("Seats must be a valid integer.")
        if val <= 0:
            raise ValueError("Must book at least 1 seat.")
        self._seats_booked = val

    def to_dict(self):
        return {"id": self.id, "screening_id": self.screening_id, "customer_name": self.customer_name, "seats_booked": self.seats_booked}

    def __repr__(self):
        return f"<Booking {self.id}: {self.customer_name} ({self.seats_booked} seats)>"