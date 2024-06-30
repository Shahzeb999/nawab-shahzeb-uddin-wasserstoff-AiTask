<?php
/**
 * Plugin Name: RAG Chatbot
 * Description: A chatbot plugin using RAG and CoT for WordPress.
 * Version: 1.0
 * Author: Your Name
 */

add_action('rest_api_init', function () {
    register_rest_route('rag-chatbot/v1', '/fetch-content', array(
        'methods' => 'GET',
        'callback' => 'fetch_content',
    ));
    register_rest_route('rag-chatbot/v1', '/update-embeddings', array(
        'methods' => 'POST',
        'callback' => 'update_embeddings',
    ));
});

function fetch_content() {
    // Fetch content logic here
    return new WP_REST_Response(['content' => 'Content fetched'], 200);
}

function update_embeddings(WP_REST_Request $request) {
    $post_id = $request->get_param('post_id');
    $post_content = get_post($post_id)->post_content;

    $response = wp_remote_post('http://your-flask-api-url/update_embeddings', array(
        'method'    => 'POST',
        'body'      => json_encode(array('post_id' => $post_id, 'post_content' => $post_content)),
        'headers'   => array('Content-Type' => 'application/json'),
    ));

    return new WP_REST_Response(json_decode(wp_remote_retrieve_body($response)), wp_remote_retrieve_response_code($response));
}
