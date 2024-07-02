<div id="rag-chatbot">
    <form id="rag-chatbot-form">
        <input type="text" id="rag-chatbot-input" placeholder="Ask a question...">
        <button type="submit">Send</button>
    </form>
    <div id="rag-chatbot-response"></div>
</div>
<script>
var rag_chatbot_vars = {
    api_url: '<?php echo esc_js(get_option('rag_chatbot_api_url')); ?>'
};
</script>