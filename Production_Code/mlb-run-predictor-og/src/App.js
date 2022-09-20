import React from 'react';
import './App.css';

function App() {
  const [data, setData] = React.useState(null);
  const [formData, setFormData] = React.useState({ homeTeam: "", awayTeam: "" });
  const [selected, setSelected] = React.useState("none");
  const [options, setOptions] = React.useState([]);
  
  function handleChange(event) {
    setData(null);
    setSelected(event.target.value);
    setFormData({homeTeam: event.target.value.substr(0, 3), awayTeam: event.target.value.substr(4, 3)});
  }
  React.useEffect(() => {
    if(options.length == 0){
      fetch("http://localhost:3001/api/games")
      .then((res) => res.json())
      .then((data) => setOptions(JSON.parse(data[0].replace(/\'/g, "\"")).results));
    }
  }, []);

  React.useEffect(() => {
    if(formData.homeTeam != "" && formData.awayTeam != ""){
      fetch("http://localhost:3001/api/predict?homeTeam=" + formData.homeTeam + "&awayTeam=" + formData.awayTeam)
      .then((res) => res.json())
      .then((data) => setData(data.results));
    }
  }, [formData]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>MLB Run Predictor</h1>
        { options.length ? (
        <form>          
          <label htmlFor="game">Select A Game</label>
          <br />
          <select id="game" value={selected} onChange={handleChange}>
            <option disabled value="none"> -- select an option -- </option>
            {options.map((option, index) => (
              <option key={index} value={option.value}>
                {option.text}
              </option>
            ))}
          </select>
        </form>):(<h3>Loading Todays Games...</h3>)}
        <br></br>
        { selected != "none" ? 
        (<div>
          <p>{!data ?  "Loading..." : formData.homeTeam + " " + data[0]}</p>
          <p>{!data ? "Loading..." :  formData.awayTeam + " " + data[1]}</p>
        </div>)
        : (<div></div>)
        }
      </header>
    </div>
  );
}

export default App;
