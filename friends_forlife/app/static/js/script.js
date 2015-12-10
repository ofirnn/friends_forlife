$('#btnClick').on('click',function(){
    $(this).text(function(i, v){
       return v === 'כניסה למערכת' ? 'ביטול' : 'כניסה למערכת'
    })
    
    if($('#loginBannerBeforeClick').css('display')!='none'){
    $('#loginBannerAfterClick').show().siblings('div').hide();
    }else if($('#loginBannerAfterClick').css('display')!='none'){
        $('#loginBannerBeforeClick').show().siblings('div').hide();
    }
});