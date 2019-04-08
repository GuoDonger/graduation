
jQuery().ready(function(){

	    $('#slideshow').jCarouselLite({ 
    	btnPrev:   '#placenav #butprev', 
	    btnNext:   '#placenav #butnext', 
		easing:'easeInOutExpo', //Animation for Images Slideshow
		speed:900,
		vertical:true,
		visible:1
		});
		
	    $('#introright').jCarouselLite({ 
    	btnPrev:   '#placenav #butprev', 
	    btnNext:   '#placenav #butnext', 
		easing:'easeInOutExpo', //Animation for Text
		speed:900,
		visible:1
		});
		
		$('#captionslideshow').jCarouselLite({ 
    	btnPrev:   '#placenav #butprev', 
	    btnNext:   '#placenav #butnext', 
		easing:'easeInOutExpo', //Animation for Photo Caption
		speed:900,
		visible:1
		});
});