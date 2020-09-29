$(document).ready(function(){ 
	$('#sub').click(function(){
		var comp=$('#company').val();
		console.log(comp)
		if (comp=='yamaha') 
		{
			window.location.href='/nitro_wheels/yamaha/'	
		}
		if (comp=='hd') 
		{
			window.location.href='/nitro_wheels/harleyDavidson/'	
		}		
	});
})