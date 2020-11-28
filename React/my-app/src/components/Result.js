import React from 'react'

function Result({result}) {
	return (
		<div className="result">
			<img src={'http://image.tmdb.org/t/p/w185' + result.poster_path} />
			<h3>{result.title}</h3>
			<p>{result.Genres}</p>
		</div>
	)
}

export default Result
