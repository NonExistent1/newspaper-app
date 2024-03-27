$(document).ready(function(){
    $(".like_button").click(function(event){
        // The work we want to do on click

        // Get required data
        let target = $(event.currentTarget);
        let article_id = target.data('id');
        let article_action = target.data('action');
        let article_like_url = target.data('like-url');
        
        // Get icon and count elements
        let like_icon = target.find('.like_icon');
        let like_count = target.find('.like_count')

        $.ajax({
            url: article_like_url,
            data: {
                article_id: article_id,
                article_action: article_action,
            },
        }).done(function(data) {
            // Do completion work here
            if (data.success) {
                if (article_action === 'like') {
                    //Do like
                    target.removeClass('btn-outline-primary');
                    target.addClass('btn-primary');
                    like_icon.removeClass('bi-hand-thumbs-up');
                    like_icon.addClass('bi-hand-thumbs-up-fill');
                    like_count.html(Number(like_count.html()) + 1);
                    target.data('action', 'unlike')
                
                } else {
                    //Do unlike
                    target.removeClass('btn-primary');
                    target.addClass('btn-outline-primary');
                    like_icon.removeClass('bi-hand-thumbs-up-fill');
                    like_icon.addClass('bi-hand-thumbs-up');
                    like_count.html(Number(like_count.html()) - 1);
                    target.data('action', 'like')
                }
            }
        })
    })
});