exports.getMotivationalSupport = (req, res) => {
    const motivationalSupport = [
        { topic: "Emotional Support", link: "https://example.com/emotional-support" },
        { topic: "Exercise", link: "https://example.com/exercise" },
        { topic: "How to Handle Stress", link: "https://example.com/handle-stress" },
        { topic: "Coping with a Chronic Illness", link: "https://example.com/coping-chronic-illness" }
    ];
    res.json(motivationalSupport);
};
