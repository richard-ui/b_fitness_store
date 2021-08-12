$('.btt-link').click(function(e) { // scroll to top of the page
    window.scrollTo(0,0);
});


$('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    });

// remove item

$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('product_size');
    var url = `/shopping_bag/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'product_size': size};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
});