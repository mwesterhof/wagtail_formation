$(document).ready(() => {
    function handleFormSubmit(event) {
        const csrftoken = Cookies.get('csrftoken');
        var form = $(this);
        var url = form.attr('action');

        event.stopPropagation();
        event.preventDefault();

        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            headers: {'X-CSRFToken': csrftoken},
            success: function(data) {
                $('form.formation').unbind('submit', handleFormSubmit);
                form.replaceWith(data);
                $('form.formation').on('submit', handleFormSubmit);
            }
        });
    }

    $('form.formation').on('submit', handleFormSubmit);
});
