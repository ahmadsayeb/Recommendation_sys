import React from 'react'
import Result from './Result'

function Results ({results}) {
	// console.log(results)
	return (
		<section className="results">
			{results.map(result => (
				<Result key={result.imdb_id} result={result}/>
			))}
		</section>
	)
}

export default Results
