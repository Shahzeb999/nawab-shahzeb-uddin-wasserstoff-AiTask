<?php

class RAG_Chatbot_Settings {

    private $plugin_name;
    private $version;

    public function __construct($plugin_name, $version) {
        $this->plugin_name = $plugin_name;
        $this->version = $version;
    }

    public function add_settings_page() {
        add_options_page(
            'RAG Chatbot Settings',
            'RAG Chatbot',
            'manage_options',
            'rag-chatbot',
            array($this, 'display_settings_page')
        );
    }

    public function display_settings_page() {
        include_once plugin_dir_path(dirname(__FILE__)) . 'admin/partials/settings-page.php';
    }

    public function register_settings() {
        register_setting('rag_chatbot_options', 'rag_chatbot_api_url');
    }
}