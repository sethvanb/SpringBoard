import React from "react"

export default function Form() {
  const [formData, setFormData] = React.useState({ homeTeam: "", awayTeam: "" });
  const [selected, setSelected] = React.useState("none");

  // teamTags=['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']
  
  function handleChange(event) {
    setSelected(event.target.value);
    setFormData({homeTeam: event.target.value.substr(0, 3), awayTeam: event.target.value.substr(4, 3)});
    console.log(formData);
  }
  
  return (
    <form>          
      <label htmlFor="game">Select A Game</label>
      <br />
      <select id="game" value={selected} onChange={handleChange}>
        <option disabled value="none"> -- select an option -- </option>
        <option value="SFG-LAD">Giants vs Dodgers</option>
        <option value="OAK-LAA">A's vs Angels</option>
      </select>
    </form>
  )
}