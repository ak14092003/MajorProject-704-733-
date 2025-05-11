import React, { useState } from 'react';
import axios from 'axios';
import './form.css';

const FuturisticForm = () => {
  const [inputs, setInputs] = useState({
    co: '', no: '', no2: '', o3: '', so2: '', pm10: '', nh3: '',
    UP_AQI: '', Haryana_AQI: '', Wind_Speed_kmph: '', Wind_Direction_deg: '',
    Wind_Speed_kmph_UP: '', Wind_Direction_deg_UP: ''
  });

  const [results, setResults] = useState(null);

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    const res = await axios.post('http://127.0.0.1:8000/predict/', inputs);
    setResults(res.data);
  };

  return (
    <div className="form-container">
      <h2>Delhi AQI Predictor 🚀</h2>
      <div className="grid">
        {Object.keys(inputs).map(key => (
          <input key={key} name={key} type="number" value={inputs[key]} onChange={handleChange} placeholder={key} />
        ))}
      </div>
      <button onClick={handleSubmit}>Predict</button>

      {results && (
        <div className="results">
          <h3>Predicted AQI Scores</h3>
          <p>🌳 Decision Tree: {results.DecisionTree}</p>
          <p>🌲 Random Forest: {results.RandomForest}</p>
          <p>📈 Linear Regression: {results.LinearRegression}</p>
        </div>
      )}
    </div>
  );
};

export default FuturisticForm;
