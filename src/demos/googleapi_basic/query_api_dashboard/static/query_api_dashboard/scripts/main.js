// AJAX for posting
function create_post() {
	console.log("create post is working!")
    //console.log($('#post-text').val())

    $.ajax({
    	url  : "create_post", // endpoint
    	type : "POST", // HTTP Post request
    	data : { the_post : $('#post-text').val() }, // Data sent with request

    	// Handle successful message
    	success : function (json) {
    		$('$post-text').val(''); // Removes the value from the input field upon completion
    		console.log(json); // Log the returned json object to the console
    		console.log("success"); // Sanity check
    	},

    	// Handle failed message
    	error : function(xhr, errmsg, err) {
    		$('#results').html("<div class='alert-box alert radius' data-alert><font color='red'>Oops! We have encountered an error: "+errmsg+" <a href='#' class='close'>&times;</a></font></div>"); // Insert into the DOM
    		//console.log(xhr.status + ": " + xhr.responseText);
    	}
    })
}

// Submit HTTP Post Transaction
$('#post-form').on('submit', function(event){
	event.preventDefault()
	create_post()
});
