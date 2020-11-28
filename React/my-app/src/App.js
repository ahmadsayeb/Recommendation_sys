import React, { useState } from 'react'
import axios from 'axios'

import Search from './components/Search'
import Results from './components/Results'


function App() {
  const [state, setState] = useState({
    s: "",
    results: []
  });
  const apiurl = "http://dae8f5bf307f.ngrok.io/tmdb";

  const search = (e) => {
    if (e.key === "Enter") {
      axios.get(apiurl + "?title=" + state.s).then(({ data }) => {
        // console.log(data)
        let results = data;
        console.log(results)
        setState(prevState => {
          return { ...prevState, results: results }
        })
      });
    }
  }
  
  const handleInput = (e) => {
    let s = e.target.value;

    setState(prevState => {
      return { ...prevState, s: s }
    });
  }


  return (
    <div className="App">
      <header>
        <h1>Movie Database</h1>
      </header>
      <main>
        <Search handleInput={handleInput} search={search} />

        <Results results={state.results}/>

      </main>
    </div>
  );
}

export default App
