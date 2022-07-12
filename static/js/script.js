$('.animated').show(function(){
    var el = $(this);
    var anim = el.data('animation');
    var animDelay = el.data('delay');
    if (animDelay) {

        setTimeout(function(){
            el.addClass( anim + " in" );
            el.removeClass('out');
        }, animDelay);

    }

    else {
        el.addClass( anim + " in" );
        el.removeClass('out');
    }    
},{accY: -150});  

