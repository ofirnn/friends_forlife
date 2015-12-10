$('#btnClick').on('click',function(){
    $(this).text(function(i, v){
       return v === 'כניסה למערכת' ? 'ביטול' : 'כניסה למערכת'
    })
    
    if($('#1').css('display')!='none'){
    $('#2').show().siblings('div').hide();
    }else if($('#2').css('display')!='none'){
        $('#1').show().siblings('div').hide();
    }
});