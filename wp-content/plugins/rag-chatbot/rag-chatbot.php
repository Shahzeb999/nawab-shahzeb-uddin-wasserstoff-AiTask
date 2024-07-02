<?php
/**
 * Plugin Name: RAG Chatbot
 * Description: Integrates RAG-based Query Suggestion Chatbot with Chain of Thought
 * Version: 1.0.0
 * Author: Nawab Shahzeb Uddin
 * Text Domain: rag-chatbot
 */

// If this file is called directly, abort.
if (!defined('WPINC')) {
    die;
}

define('RAG_CHATBOT_VERSION', '1.0.0');

// Include the main RAG Chatbot class.
require plugin_dir_path(__FILE__) . 'includes/class-rag-chatbot.php';

/**
 * Begins execution of the plugin.
 */
function run_rag_chatbot() {
    $plugin = new RAG_Chatbot();
    $plugin->run();
}
run_rag_chatbot();