const express = require('express');
const { getMotivationalSupport } = require('../controllers/motivationalSupportController');
const router = express.Router();

router.get('/', getMotivationalSupport);

module.exports = router;
