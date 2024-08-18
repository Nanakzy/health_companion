const express = require('express');
const { getHealthPlan } = require('../controllers/healthPlanController');
const router = express.Router();

router.get('/', getHealthPlan);

module.exports = router;
