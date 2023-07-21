$(document).ready(() => {
    function handleFormSubmit(event) {
        const csrftoken = Cookies.get('csrftoken');
        var form = $(this);
        var url = form.attr('action');

        event.stopPropagation();
        event.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            type: "POST",
            url: url,
            data: formData,
            headers: {'X-CSRFToken': csrftoken},
            cache: false,
            processData: false,
            contentType: false,
            success: function(data, statusText, response) {
                if(response.getResponseHeader('formationReplace') == 1) {
                    $('form.formation').unbind('submit', handleFormSubmit);
                    form.replaceWith(data);
                    $('form.formation').on('submit', handleFormSubmit);
                }
                else {
                    window.location.href = data;
                }

            }
        });
    }

    $('form.formation').on('submit', handleFormSubmit);
});
