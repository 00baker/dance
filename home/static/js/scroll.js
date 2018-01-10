$(document).ready(function(){

	/* ====================================================================
	
	Navigation scroll

	=======================================================================  */

	// Scroll to point on page

	// Options

	var scroll_speed = 500; // Scroll speed. Set to 0 for instant snap
	var nav_links = $('ul li a'); // Nav link elements

	function scroll_to(element){
		$('html, body').animate({
	    	scrollTop: $(element).offset().top -75 // Scroll to element
	  	}, scroll_speed);
	}

	nav_links.click(function() {
		var id = $(this).html().toLowerCase().replace(" ", ""); // Get clicked link
		var target = $('[scroll_target = ' + id + ']'); // Set the target element
		scroll_to(target); // Scroll to target
	});

	/* ====================================================================
	
	Responsive menu

	=======================================================================  */

	// Options

	
})
