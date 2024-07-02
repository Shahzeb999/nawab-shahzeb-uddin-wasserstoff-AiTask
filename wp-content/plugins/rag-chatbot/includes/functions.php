<?php

function rag_chatbot_fetch_wordpress_content() {
    $posts = get_posts(array(
        'post_type' => 'post',
        'posts_per_page' => -1,
    ));

    $content = array();
    foreach ($posts as $post) {
        $content[] = array(
            'id' => $post->ID,
            'title' => $post->post_title,
            'content' => $post->post_content,
        );
    }

    return $content;
}

function rag_chatbot_update_embeddings_on_save($post_id) {
    $api_url = get_option('rag_chatbot_api_url');
    if (!$api_url) return;

    $url = $api_url . '/update_embeddings';
    $args = array(
        'body' => json_encode(array('url' => get_permalink($post_id))),
        'headers' => array('Content-Type' => 'application/json'),
    );
    wp_remote_post($url, $args);
}
add_action('save_post', 'rag_chatbot_update_embeddings_on_save');