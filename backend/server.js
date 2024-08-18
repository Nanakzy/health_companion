const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
const authRoutes = require('./routes/auth');
const healthPlanRoutes = require('./routes/healthPlans');
const medicationRoutes = require('./routes/medications');
const appointmentRoutes = require('./routes/appointments');
const motivationalSupportRoutes = require('./routes/motivationalSupport');
const authenticateToken = require('./middlewares/authenticateToken');

dotenv.config();
const app = express();
app.use(bodyParser.json());

app.use('/api/auth', authRoutes);
app.use('/api/healthPlans', authenticateToken, healthPlanRoutes);
app.use('/api/medications', authenticateToken, medicationRoutes);
app.use('/api/appointments', authenticateToken, appointmentRoutes);
app.use('/api/motivationalSupport', authenticateToken, motivationalSupportRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
