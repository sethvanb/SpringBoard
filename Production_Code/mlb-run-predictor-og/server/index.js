const express = require("express");
const cors = require('cors');
const PythonShell = require('python-shell').PythonShell;

const PORT = process.env.PORT || 3001;

const app = express();

app.use(cors());

app.get("/api/predict", async (req, res) => {
  var options = {
    mode: 'text',
    pythonPath: 'python3',
    pythonOptions: ['-u'],
    scriptPath: './server/',
    args: [req.query.homeTeam, req.query.awayTeam]
  };

  PythonShell.run('inference.py', options, function (err, results) {
    if (err) 
      throw err;
    console.log(results);
    res.json({ results: results });
  });
});

app.get("/api/games", async (req, res) => {
  var options = {
    mode: 'text',
    pythonPath: 'python3',
    pythonOptions: ['-u'],
    scriptPath: './server/',
    args: []
  };

  PythonShell.run('dailyGames.py', options, function (err, results) {
    if (err) 
      throw err;
    console.log(results);
    res.json(results);
  });
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});