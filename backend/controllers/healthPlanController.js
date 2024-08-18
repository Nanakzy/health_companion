exports.getHealthPlan = (req, res) => {
    const healthPlan = {
        plan: "Your personalized health plan includes daily exercise, a balanced diet, and regular check-ups."
    };
    res.json(healthPlan);
};
