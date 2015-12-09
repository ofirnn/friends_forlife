$("#myButton").toggle(function(){
    $("#content").slideDown();
    $(this).val("Slide up ↑");
},function(){
    $("#content").slideUp();
    $(this).val("Slide down ↓")
})	