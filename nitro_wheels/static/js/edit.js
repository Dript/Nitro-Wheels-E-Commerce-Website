$(document).ready(function(){
	$('#save_data').click(function(){

		var name=$('#name').val();
		var usrname=$('#usrname').val();
		var email=$('#email').val();
		var contact=$('#contact').val(); 
		var add=$('#address').val();
		var months=$('#months').val();
		var dates=$('#dates').val();
		var years=$('#years').val();
		var status=$('#status').val();
		$.ajax({
			url:'/nitro_wheels/edit_data/',
			type:'POST',
			data:{'name':name,'usrname':usrname,'email':email,'contact':contact,
			'months':months,'dates':dates,'years':years,'address':add,'status':status},
			success:function(response)
			{
				if(response=='success')
				{
					window.location.href='/nitro_wheels/dash/'
				}
			},
			error:function(xhr,textStatus,thrownError)
			{
				alert('error');
			}
		});
	});
})