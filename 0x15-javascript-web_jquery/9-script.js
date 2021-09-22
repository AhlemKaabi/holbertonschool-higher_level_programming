// import from the head tag
$.ajax({
		type: 'GET',
		url: "https://fourtonfish.com/hellosalut/?lang=fr",
		success: function(data) {
			$('DIV#hello').html(data.hello)
		}
});