(function($) {
    'use strict';

    $(document).ready(function() {
        $('#rag-chatbot-form').on('submit', function(e) {
            e.preventDefault();
            var query = $('#rag-chatbot-input').val();
            $.ajax({
                url: rag_chatbot_vars.api_url + '/process_query',
                method: 'POST',
                data: JSON.stringify({query: query, previous_context: ''}),
                contentType: 'application/json',
                success: function(response) {
                    $('#rag-chatbot-response').text(response.response);
                },
                error: function(xhr, status, error) {
                    console.error('Error:', error);
                }
            });
        });
    });

})(jQuery);