$(document).ready(function(){
	$.ajax({
		type: 'GET',
		url: "https://swapi-api.hbtn.io/api/films/?format=json",
		success: function(films) {
			console.log(films)
			$.each(films.results, function(counter, film){
				$("UL#list_movies").append('<li>' + film.title + '</li>');

			});
		}
	});
});