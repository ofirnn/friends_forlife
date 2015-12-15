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


jQuery(document).ready(function() {
    jQuery('.tabs .tab-links a').on('click', function(e)  {
        var currentAttrValue = jQuery(this).attr('href');
 
        // Show/Hide Tabs
        jQuery('.tabs ' + currentAttrValue).show().siblings().hide();
 
        // Change/remove current tab to active
        jQuery(this).parent('li').addClass('active').siblings().removeClass('active');
 
        e.preventDefault();
    });
});