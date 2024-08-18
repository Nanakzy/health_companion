exports.getAppointments = (req, res) => {
    const appointments = [
        { date: "2024-09-10", time: "10:00 AM", doctor: "Dr. Smith" },
        { date: "2024-09-15", time: "2:00 PM", doctor: "Dr. Lee" }
    ];
    res.json(appointments);
};
