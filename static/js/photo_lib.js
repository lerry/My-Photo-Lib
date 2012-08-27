$(function(){
    var win = $(window),
        thumb = $('.thumb_img'),
        replace_src = function(img){
            if(img.attr('src').indexOf('default')>0){
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
