$(function(){
    var win = $(window),
        thumb = $('.thumb_img'),
        replace_src = function(img){
            if(img.attr('src').indexOf('loading')>0){
               img.attr('src',img.attr('rel'))                               }
        }
    win.scroll(function(){
        thumb.each(function(){
            var self = $(this)
            win.scrollTop()>=self.offset().top-$(win).height() && replace_src(self)
        })
    })
    thumb.each(function(){
        var self = $(this)
        self.offset().top<=win.height() && replace_src(self)
    })
})

$(document).ready(function() {
    $("a.thumbnail").fancybox({
        'overlayShow'   : false,
        'transitionIn'  : 'elastic',
        'transitionOut' : 'elastic'
    });

//    $("a[class=thumbnail]").fancybox({
//        'transitionIn'      : 'none',
//        'transitionOut'     : 'none',
//        'titlePosition'     : 'over',
//        'titleFormat'       : function(title, currentArray, currentIndex, currentOpts) {
//            return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
//        }
//    });
//
}
)
