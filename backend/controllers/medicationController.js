exports.getMedications = (req, res) => {
    const medications = [
        { name: "Metformin", dosage: "500mg", frequency: "Twice a day" },
        { name: "Atorvastatin", dosage: "20mg", frequency: "Once a day" }
    ];
    res.json(medications);
};
