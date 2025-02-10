const express = require("express");
const path = require("path");
const axios = require("axios");
const cors = require("cors");
const session = require("express-session");
require("dotenv").config();

const app = express();
const port = process.env.PORT || 3000;

// Session configuration
app.use(
  session({
    secret: process.env.SESSION_SECRET || "your-secret-key",
    resave: false,
    saveUninitialized: true,
    cookie: { secure: process.env.NODE_ENV === "production" },
  })
);

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

// Set EJS as templating engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Store default settings
const defaultSettings = {
  provider: "google",
  model: "gemini-pro",
  temperature: 0.7,
};

// Routes
app.get("/", (req, res) => {
  const currentSettings = req.session.settings || defaultSettings;
  res.render("index", { settings: currentSettings });
});

app.post("/chat", async (req, res) => {
  try {
    const { message } = req.body;
    const currentSettings = req.session.settings || defaultSettings;

    const response = await axios.post("http://localhost:5000/chat", {
      message,
      settings: currentSettings,
    });

    res.json(response.data);
  } catch (error) {
    console.error("Chat Error:", error);
    res.status(500).json({
      error: "An error occurred while processing your request",
      details:
        process.env.NODE_ENV === "development" ? error.message : undefined,
    });
  }
});

app.post("/update-settings", async (req, res) => {
  try {
    const { provider, model, temperature } = req.body;

    if (!provider || !model) {
      return res.status(400).json({
        success: false,
        error: "Missing required settings",
      });
    }

    req.session.settings = {
      provider,
      model,
      temperature: parseFloat(temperature),
    };

    const response = await axios.post("http://localhost:5000/update-settings", {
      provider,
      model,
      temperature: parseFloat(temperature),
    });

    if (response.data.success) {
      res.json({
        success: true,
        message: "Settings updated successfully",
      });
    } else {
      throw new Error(response.data.error || "Failed to update settings");
    }
  } catch (error) {
    console.error("Settings Update Error:", error);
    res.status(500).json({
      success: false,
      error: "Failed to update settings",
      details:
        process.env.NODE_ENV === "development" ? error.message : undefined,
    });
  }
});

app.get("/settings", (req, res) => {
  const currentSettings = req.session.settings || defaultSettings;
  res.json({
    success: true,
    settings: currentSettings,
  });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: "Something went wrong!",
    details: process.env.NODE_ENV === "development" ? err.message : undefined,
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}, http://localhost:3000`);
});
