$(document).ready(function(){ 
	$('#sub').click(function(){
		var comp=$('#company').val();
		console.log(comp)
		if (comp=='gb') 
		{
			window.location.href='/nitro_wheels/gb/'	
		}
		if (comp=='en') 
		{
			window.location.href='/nitro_wheels/en/'	
		}		
		if (comp=='sp') 
		{
			window.location.href='/nitro_wheels/sp/'	
		}		
	});
});