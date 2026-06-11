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

