const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose.connect('mongodb://localhost:27017/tute_dude_db')
.then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

// Schema
const UserSchema = new mongoose.Schema({
  name: String,
  email: String
});

const User = mongoose.model('User', UserSchema);


app.post('/api/submit', async (req, res) => {
  console.log("Received data:", req.body);

  try {
    const newUser = new User(req.body);
    await newUser.save();

    res.status(200).json({
      success: true,
      message: "Data submitted successfully"
    });

  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});


app.get('/', (req, res) => {
  res.send("Backend running - Express + MongoDB");
});

app.listen(5000, () => console.log("Server running on port 5000"));